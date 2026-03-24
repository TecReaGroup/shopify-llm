#!/usr/bin/env python3
"""Download visual assets from perfectextile.com and extract theme metadata.

Outputs:
- HTML / CSS / JS / images / SVG files under ./assets/perfectextile.com/
- Crawl summary under ./assets/perfectextile.com/manifest.json
- Extracted fonts under ./assets/perfectextile.com/extracted_fonts.json
- Extracted colors under ./assets/perfectextile.com/extracted_colors.json
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import posixpath
import re
import sys
import time
from collections import Counter, deque
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, unquote, urldefrag, urlencode, urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://perfectextile.com/"
DEFAULT_OUTPUT_DIR = Path("assets") / "perfectextile.com"
DEFAULT_MAX_PAGES = 40
DEFAULT_TIMEOUT = 25
DEFAULT_DELAY = 0.2
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)

ASSET_ATTRS = {
    "img": ["src", "data-src", "data-lazy-src", "data-srcset", "srcset"],
    "source": ["src", "srcset", "data-srcset"],
    "script": ["src"],
    "link": ["href"],
    "video": ["src", "poster"],
    "audio": ["src"],
    "image": ["href", "xlink:href"],
    "use": ["href", "xlink:href"],
}

PAGE_EXTENSIONS = {"", ".html", ".htm", ".php", ".asp", ".aspx"}
ASSET_EXTENSIONS = {
    ".css",
    ".js",
    ".mjs",
    ".json",
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
    ".bmp",
    ".ico",
    ".svg",
    ".avif",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".eot",
    ".mp4",
    ".webm",
    ".mp3",
    ".wav",
    ".pdf",
}
EXCLUDED_SCHEMES = ("mailto:", "tel:", "javascript:", "data:", "#")
FONT_IGNORE = {
    "inherit",
    "initial",
    "unset",
    "serif",
    "sans-serif",
    "monospace",
    "system-ui",
    "ui-sans-serif",
    "ui-serif",
    "ui-monospace",
    "emoji",
    "math",
    "fangsong",
    "cursive",
    "fantasy",
}
COLOR_PATTERNS = [
    re.compile(r"#[0-9a-fA-F]{3,8}\b"),
    re.compile(r"rgba?\([^\)]*\)"),
    re.compile(r"hsla?\([^\)]*\)"),
]
FONT_FAMILY_PATTERN = re.compile(r"font-family\s*:\s*([^;}{]+)", re.IGNORECASE)
URL_PATTERN = re.compile(r"url\(([^)]+)\)", re.IGNORECASE)
STYLE_URL_PATTERN = re.compile(r"url\(([^)]+)\)", re.IGNORECASE)
HEX_3 = re.compile(r"^#([0-9a-fA-F]{3})$")
HEX_4 = re.compile(r"^#([0-9a-fA-F]{4})$")
HEX_6 = re.compile(r"^#([0-9a-fA-F]{6})$")
HEX_8 = re.compile(r"^#([0-9a-fA-F]{8})$")
RGB_PATTERN = re.compile(
    r"rgba?\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})(?:\s*,\s*([0-9.]+))?\s*\)",
    re.IGNORECASE,
)
HSL_PATTERN = re.compile(
    r"hsla?\(\s*(-?[0-9.]+)(?:deg)?\s*,\s*([0-9.]+)%\s*,\s*([0-9.]+)%(?:\s*,\s*([0-9.]+))?\s*\)",
    re.IGNORECASE,
)


class SiteArchiver:
    def __init__(
        self,
        base_url: str,
        output_dir: Path,
        max_pages: int = DEFAULT_MAX_PAGES,
        timeout: int = DEFAULT_TIMEOUT,
        delay: float = DEFAULT_DELAY,
    ) -> None:
        self.base_url = ensure_trailing_slash(base_url)
        self.base_parts = urlparse(self.base_url)
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.timeout = timeout
        self.delay = delay

        self.session = requests.Session()
        self.session.trust_env = False
        self.session.proxies.clear()
        self.session.headers.update({"User-Agent": USER_AGENT})

        self.visited_pages: set[str] = set()
        self.downloaded_assets: dict[str, str] = {}
        self.font_counter: Counter[str] = Counter()
        self.color_counter: Counter[str] = Counter()
        self.page_outputs: list[str] = []
        self.asset_outputs: list[str] = []
        self.failures: list[dict[str, str]] = []

    def crawl(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        queue: deque[str] = deque([self.base_url])

        while queue and len(self.visited_pages) < self.max_pages:
            page_url = normalize_url(queue.popleft(), self.base_url)
            if not page_url or page_url in self.visited_pages:
                continue
            if not self.is_same_site(page_url) or not self.is_probable_page(page_url):
                continue

            try:
                response = self.fetch(page_url)
            except requests.RequestException as exc:
                self.record_failure(page_url, exc)
                continue

            content_type = response.headers.get("Content-Type", "")
            if "html" not in content_type and not looks_like_html(response.text):
                saved_path = self.save_response_content(page_url, response)
                self.asset_outputs.append(str(saved_path).replace("\\", "/"))
                continue

            self.visited_pages.add(page_url)
            saved_path = self.save_html(page_url, response.text)
            self.page_outputs.append(str(saved_path).replace("\\", "/"))

            soup = BeautifulSoup(response.text, "html.parser")
            self.extract_fonts_and_colors_from_text(response.text)
            self.extract_fonts_and_colors_from_html(soup)

            for link in self.extract_page_links(soup, page_url):
                if link not in self.visited_pages:
                    queue.append(link)

            for asset_url in self.extract_asset_links(soup, page_url):
                self.download_asset(asset_url)

            time.sleep(self.delay)

        self.write_reports()

    def fetch(self, url: str) -> requests.Response:
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response

    def is_same_site(self, url: str) -> bool:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return False
        return parsed.netloc == self.base_parts.netloc

    def is_probable_page(self, url: str) -> bool:
        path = urlparse(url).path
        suffix = Path(path).suffix.lower()
        return suffix in PAGE_EXTENSIONS

    def extract_page_links(self, soup: BeautifulSoup, page_url: str) -> list[str]:
        links: list[str] = []
        for tag in soup.find_all(["a", "link"]):
            href = tag.get("href")
            rel = [item.lower() for item in tag.get("rel", []) if isinstance(item, str)]
            if not href:
                continue
            if any(href.startswith(prefix) for prefix in EXCLUDED_SCHEMES):
                continue
            absolute = normalize_url(urljoin(page_url, href), self.base_url)
            if not absolute or not self.is_same_site(absolute):
                continue
            if tag.name == "link" and any(item in {"stylesheet", "preload", "icon", "mask-icon", "apple-touch-icon"} for item in rel):
                continue
            if self.is_probable_page(absolute):
                links.append(absolute)
        return dedupe_keep_order(links)

    def extract_asset_links(self, soup: BeautifulSoup, page_url: str) -> list[str]:
        assets: list[str] = []

        for tag_name, attrs in ASSET_ATTRS.items():
            for tag in soup.find_all(tag_name):
                for attr in attrs:
                    value = tag.get(attr)
                    if not value:
                        continue
                    assets.extend(self.parse_url_attribute(value, page_url))

        for tag in soup.find_all(style=True):
            assets.extend(self.parse_css_urls(tag.get("style", ""), page_url))

        for style_tag in soup.find_all("style"):
            css_text = style_tag.string or style_tag.get_text("\n", strip=False)
            self.extract_fonts_and_colors_from_text(css_text)
            assets.extend(self.parse_css_urls(css_text, page_url))

        for meta in soup.find_all("meta"):
            for attr in ("content",):
                value = meta.get(attr)
                if value and any(ext in value.lower() for ext in (".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico")):
                    assets.extend(self.parse_url_attribute(value, page_url))

        return dedupe_keep_order(asset for asset in assets if asset)

    def parse_url_attribute(self, raw_value: str, page_url: str) -> list[str]:
        parts = []
        for chunk in raw_value.split(","):
            candidate = chunk.strip().split(" ")[0].strip("'\"")
            if not candidate or any(candidate.startswith(prefix) for prefix in EXCLUDED_SCHEMES):
                continue
            absolute = normalize_url(urljoin(page_url, candidate), self.base_url)
            if absolute and self.is_same_site(absolute) and self.is_asset_url(absolute):
                parts.append(absolute)
        return parts

    def parse_css_urls(self, css_text: str, page_url: str) -> list[str]:
        assets: list[str] = []
        self.extract_fonts_and_colors_from_text(css_text)
        for match in URL_PATTERN.findall(css_text or ""):
            candidate = match.strip().strip("'\"")
            if not candidate or any(candidate.startswith(prefix) for prefix in EXCLUDED_SCHEMES):
                continue
            absolute = normalize_url(urljoin(page_url, candidate), self.base_url)
            if absolute and self.is_same_site(absolute) and self.is_asset_url(absolute):
                assets.append(absolute)
        return assets

    def is_asset_url(self, url: str) -> bool:
        path = urlparse(url).path.lower()
        suffix = Path(path).suffix.lower()
        if suffix in ASSET_EXTENSIONS:
            return True
        query = parse_qs(urlparse(url).query)
        format_hint = " ".join([" ".join(values) for values in query.values()]).lower()
        return any(ext[1:] in format_hint for ext in ASSET_EXTENSIONS)

    def download_asset(self, asset_url: str) -> None:
        asset_url = normalize_url(asset_url, self.base_url)
        if not asset_url or asset_url in self.downloaded_assets:
            return
        try:
            response = self.fetch(asset_url)
        except requests.RequestException as exc:
            self.record_failure(asset_url, exc)
            return

        saved_path = self.save_response_content(asset_url, response)
        rel_path = str(saved_path).replace("\\", "/")
        self.downloaded_assets[asset_url] = rel_path
        self.asset_outputs.append(rel_path)

        content_type = response.headers.get("Content-Type", "")
        text_like = any(token in content_type for token in ("css", "javascript", "json", "svg", "xml", "text"))
        if text_like:
            text = response.text
            self.extract_fonts_and_colors_from_text(text)
            if "css" in content_type or saved_path.suffix.lower() == ".css":
                for nested in self.parse_css_urls(text, asset_url):
                    self.download_asset(nested)

        time.sleep(self.delay)

    def save_html(self, url: str, text: str) -> Path:
        path = self.url_to_path(url, default_name="index.html", force_html=True)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def save_response_content(self, url: str, response: requests.Response) -> Path:
        content_type = response.headers.get("Content-Type", "")
        path = self.url_to_path(url, content_type=content_type)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)
        return path

    def url_to_path(
        self,
        url: str,
        default_name: str = "index",
        force_html: bool = False,
        content_type: str | None = None,
    ) -> Path:
        parsed = urlparse(url)
        raw_path = unquote(parsed.path or "/")
        safe_path = posixpath.normpath(raw_path)
        if safe_path in {"", "."}:
            safe_path = "/"

        if safe_path.endswith("/") or safe_path == "/":
            file_path = safe_path + default_name
        else:
            file_path = safe_path

        suffix = Path(file_path).suffix
        if force_html and suffix.lower() not in {".html", ".htm"}:
            file_path = file_path.rstrip("/") + "/index.html"
        elif not suffix:
            guessed = guess_extension(content_type)
            if guessed:
                file_path += guessed
            elif not file_path.endswith(default_name):
                file_path += ".bin"

        file_path = sanitize_relative_path(file_path.lstrip("/"))
        if parsed.query:
            query_tag = sanitize_filename(urlencode(sorted(parse_qs(parsed.query, keep_blank_values=True).items()), doseq=True))
            file_path = append_before_suffix(file_path, f"__q_{query_tag}")

        return self.output_dir / file_path

    def extract_fonts_and_colors_from_html(self, soup: BeautifulSoup) -> None:
        for element in soup.find_all(style=True):
            self.extract_fonts_and_colors_from_text(element.get("style", ""))

        for link in soup.find_all("link"):
            href = (link.get("href") or "").lower()
            if "fonts.googleapis.com" in href:
                families = parse_google_font_families(link.get("href", ""))
                for family in families:
                    self.font_counter[family] += 3

    def extract_fonts_and_colors_from_text(self, text: str) -> None:
        if not text:
            return

        for match in FONT_FAMILY_PATTERN.findall(text):
            families = split_font_families(match)
            for family in families:
                if family.lower() not in FONT_IGNORE:
                    self.font_counter[family] += 1

        if "font-family" not in text.lower():
            # Heuristic for CSS custom props like --font-heading: 'Montserrat';
            for token in re.findall(r"['\"]([A-Za-z][A-Za-z0-9\s_-]{1,60})['\"]", text):
                cleaned = normalize_font_name(token)
                if cleaned and cleaned.lower() not in FONT_IGNORE and len(cleaned.split()) <= 4:
                    self.font_counter[cleaned] += 0

        for pattern in COLOR_PATTERNS:
            for color in pattern.findall(text):
                normalized = normalize_color(color)
                if normalized:
                    self.color_counter[normalized] += 1

    def write_reports(self) -> None:
        fonts = [
            {"font": name, "count": count}
            for name, count in self.font_counter.most_common()
            if count > 0
        ]
        colors = [
            {"hex": name, "count": count}
            for name, count in self.color_counter.most_common()
            if count > 0
        ]

        manifest = {
            "base_url": self.base_url,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "pages_downloaded": len(self.page_outputs),
            "assets_downloaded": len(self.asset_outputs),
            "page_files": self.page_outputs,
            "asset_files": self.asset_outputs,
            "fonts_top": fonts[:20],
            "colors_top": colors[:20],
            "failures": self.failures,
        }

        (self.output_dir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (self.output_dir / "extracted_fonts.json").write_text(
            json.dumps(fonts, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (self.output_dir / "extracted_colors.json").write_text(
            json.dumps(colors, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def record_failure(self, url: str, exc: Exception) -> None:
        self.failures.append({"url": url, "error": str(exc)})


def ensure_trailing_slash(url: str) -> str:
    return url if url.endswith("/") else url + "/"


def normalize_url(url: str, base_url: str) -> str:
    if not url:
        return ""
    url, _fragment = urldefrag(url.strip())
    if not url:
        return ""
    parsed = urlparse(urljoin(base_url, url))
    if parsed.scheme not in {"http", "https"}:
        return ""
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    if not path.startswith("/"):
        path = "/" + path
    normalized = parsed._replace(scheme="https", netloc=netloc, path=path)
    return urlunparse(normalized)


def dedupe_keep_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def guess_extension(content_type: str | None) -> str:
    if not content_type:
        return ""
    mime = content_type.split(";", 1)[0].strip().lower()
    if mime == "text/html":
        return ".html"
    if mime == "image/svg+xml":
        return ".svg"
    guessed = mimetypes.guess_extension(mime) or ""
    if guessed == ".jpe":
        return ".jpg"
    return guessed


def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._")
    return cleaned[:120] or "file"


def sanitize_relative_path(path: str) -> str:
    parts = [sanitize_filename(part) for part in path.replace("\\", "/").split("/") if part not in {"", ".", ".."}]
    return "/".join(parts) if parts else "index.html"


def append_before_suffix(path: str, suffix_tag: str) -> str:
    pure = Path(path)
    if pure.suffix:
        return str(pure.with_name(f"{pure.stem}{suffix_tag}{pure.suffix}"))
    return f"{path}{suffix_tag}"


def looks_like_html(text: str) -> bool:
    sample = (text or "").lstrip()[:500].lower()
    return "<html" in sample or "<!doctype html" in sample


def split_font_families(value: str) -> list[str]:
    families = []
    for item in value.split(","):
        normalized = normalize_font_name(item)
        if normalized:
            families.append(normalized)
    return families


def normalize_font_name(value: str) -> str:
    cleaned = value.strip().strip("'\"")
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        return ""
    if re.fullmatch(r"[0-9.]+", cleaned):
        return ""
    return cleaned


def parse_google_font_families(url: str) -> list[str]:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    families: list[str] = []
    for raw in query.get("family", []):
        family = raw.split(":", 1)[0].replace("+", " ")
        normalized = normalize_font_name(family)
        if normalized:
            families.append(normalized)
    return families


def normalize_color(color: str) -> str | None:
    color = color.strip()
    if not color:
        return None

    if HEX_3.match(color):
        triplet = HEX_3.match(color).group(1)
        return "#" + "".join(channel * 2 for channel in triplet).upper()
    if HEX_4.match(color):
        quad = HEX_4.match(color).group(1)
        rgb = "".join(channel * 2 for channel in quad[:3])
        return f"#{rgb.upper()}"
    if HEX_6.match(color):
        return color.upper()
    if HEX_8.match(color):
        return "#" + HEX_8.match(color).group(1)[:6].upper()

    rgb_match = RGB_PATTERN.match(color)
    if rgb_match:
        red, green, blue = [max(0, min(255, int(channel))) for channel in rgb_match.groups()[:3]]
        alpha = rgb_match.group(4)
        if alpha is not None and float(alpha) == 0:
            return None
        return f"#{red:02X}{green:02X}{blue:02X}"

    hsl_match = HSL_PATTERN.match(color)
    if hsl_match:
        hue = float(hsl_match.group(1)) % 360
        sat = max(0.0, min(100.0, float(hsl_match.group(2)))) / 100
        light = max(0.0, min(100.0, float(hsl_match.group(3)))) / 100
        alpha = hsl_match.group(4)
        if alpha is not None and float(alpha) == 0:
            return None
        red, green, blue = hsl_to_rgb(hue, sat, light)
        return f"#{red:02X}{green:02X}{blue:02X}"

    return None


def hsl_to_rgb(hue: float, sat: float, light: float) -> tuple[int, int, int]:
    c = (1 - abs(2 * light - 1)) * sat
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = light - c / 2

    if 0 <= hue < 60:
        r1, g1, b1 = c, x, 0
    elif 60 <= hue < 120:
        r1, g1, b1 = x, c, 0
    elif 120 <= hue < 180:
        r1, g1, b1 = 0, c, x
    elif 180 <= hue < 240:
        r1, g1, b1 = 0, x, c
    elif 240 <= hue < 300:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x

    return (
        round((r1 + m) * 255),
        round((g1 + m) * 255),
        round((b1 + m) * 255),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download perfectextile.com assets and extract design metadata.")
    parser.add_argument("--base-url", default=BASE_URL, help="Base site URL to crawl.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where downloaded files and reports are saved.",
    )
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES, help="Maximum same-domain HTML pages to crawl.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="HTTP request timeout in seconds.")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY, help="Delay between requests in seconds.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    archiver = SiteArchiver(
        base_url=args.base_url,
        output_dir=Path(args.output_dir),
        max_pages=args.max_pages,
        timeout=args.timeout,
        delay=args.delay,
    )
    archiver.crawl()

    summary = {
        "pages_downloaded": len(archiver.page_outputs),
        "assets_downloaded": len(archiver.asset_outputs),
        "top_fonts": archiver.font_counter.most_common(10),
        "top_colors": archiver.color_counter.most_common(10),
        "failures": len(archiver.failures),
        "output_dir": str(Path(args.output_dir).resolve()),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
