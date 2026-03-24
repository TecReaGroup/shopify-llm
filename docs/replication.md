# perfectextile Shopify 1:1 模块化复刻方案

## 1. 目标定义

目标不是“做一个类似站”，而是基于现有抓取资产，对 [`perfectextile.com 首页结构`](assets/perfectextile.com/index.html) 与核心详情页结构做 **Shopify Online Store 2.0 的模块化 1:1 复刻**：

- 页面视觉尽量一致：版式、留白、字体、主色、卡片、轮播、按钮、响应式断点。
- 信息架构一致：头部导航、Mega Menu、首页内容顺序、产品详情页信息区块、FAQ、相关产品、页脚。
- 功能行为一致：轮播、视频、粘性头部、语言切换占位、询盘 CTA、表单弹层替代方案。
- 实现方式可维护：每个视觉区块都拆成独立 Shopify section / snippet / block，而不是把整页写死。

不建议直接把 WordPress / Elementor HTML 原样塞入 Shopify。正确方案是：**抽象模块 → 建 Shopify section schema → 用 theme settings 驱动内容 → 对特殊交互用少量 JS 复刻。**

---

## 2. 已知站点特征拆解

从 [`首页源码`](assets/perfectextile.com/index.html)、[`详情页源码`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html)、[`颜色提取`](assets/perfectextile.com/extracted_colors.json)、[`字体提取`](assets/perfectextile.com/extracted_fonts.json)、[`CLI 说明`](shopify_cli.md) 可归纳出以下关键点：

### 2.1 技术来源特征

原站主要来自 WordPress + Astra + Elementor / Elementor Pro 生态：

- Astra 主题基础布局与全局变量
- Elementor 容器式页面搭建
- Mega Menu / Carousel / Accordion / Popup / Form 等插件能力
- 多语言来自 TranslatePress
- 局部 WhatsApp 悬浮沟通

对应到 Shopify 时，不能复制插件体系，只能复刻 **结果层**：

- 布局结果
- CSS 视觉结果
- JS 交互结果
- CMS 编辑体验

### 2.2 颜色系统

从 [`颜色提取结果`](assets/perfectextile.com/extracted_colors.json) 看，主色非常明确：

- 主背景：`#FFFFFF`
- 主品牌橙：`#FF8C00`
- 深橙 hover / active：`#E67600`
- 主文本黑：`#000000`
- 深蓝辅助：`#003399`
- 灰色体系：`#333333`、`#EEEEEE`、`#EAEAEA`、`#F5F5F5`

建议在 Shopify 中建立 design tokens：

- `--pt-color-primary: #FF8C00`
- `--pt-color-primary-hover: #E67600`
- `--pt-color-text: #000000`
- `--pt-color-heading: #111111`
- `--pt-color-muted: #666666`
- `--pt-color-border: #EAEAEA`
- `--pt-color-surface: #F5F5F5`
- `--pt-color-accent-blue: #003399`

### 2.3 字体系统

从 [`字体提取结果`](assets/perfectextile.com/extracted_fonts.json) 看，实际站点混用了很多字体，但核心优先级明显是：

- `Plus Jakarta Sans`
- `Akatab`
- `Montserrat`
- `Roboto` / `Open Sans`

Shopify 复刻时不要继续混乱，建议收敛为：

- Heading：`Plus Jakarta Sans`
- Body：`Open Sans` 或 `Roboto`
- 特殊强调/数字：可局部使用 `Akatab`

这样既接近原站，又利于统一维护。

### 2.4 页面结构特征

首页可抽象为：

1. Sticky Header + Mega Menu
2. Hero（视频背景 / 大标题 / CTA）
3. Fabric 分类入口
4. Bedding 分类入口
5. 工厂优势 / 对比说明区
6. 视频内容区
7. 数据 / 能力 / 工厂卖点区
8. 产品卡片轮播 / 分类推荐
9. 生产流程轮播
10. 客户评价轮播
11. 公司故事 / 时间线
12. 博客内容区
13. CTA + 联系引导
14. Footer

详情页可抽象为：

1. Header
2. 产品图库 / 轮播
3. 标题 + 面包屑 + 概述 + CTA
4. 规格表
5. 细节图集
6. 卖点图标区
7. 生产流程轮播
8. FAQ Accordion
9. 可持续说明
10. Related Products
11. Blog 推荐
12. 最终 CTA
13. Footer

---

## 3. Shopify 技术路线

## 3.1 主题基础选择

建议直接基于 Dawn 初始化，但只保留其 Shopify 标准能力，样式与区块重写：

参考 [`shopify cli 初始化命令`](shopify_cli.md:3)。

推荐流程：

```bash
npm install -g @shopify/cli
shopify theme init perfectextile-theme --clone-url https://github.com/Shopify/dawn
```

原因：

- Dawn 原生支持 OS 2.0 section everywhere
- schema、blocks、presets 结构标准
- 产品页、集合页、文章页模板基础已齐全
- 后续更容易维护与二次扩展

## 3.2 架构原则

核心原则：**“一屏一 section，可复用片段进 snippet，可配置内容进 settings/block。”**

建议模块层级：

- `layout`：头部、页脚、全局 token、容器宽度、栅格
- `sections`：每一屏独立 section
- `snippets`：卡片、按钮、图标项、轮播项、语言切换、breadcrumbs
- `templates`：首页、产品页、页面模板、博客模板
- `assets`：主题 CSS / JS，仅存复刻所需

## 3.3 复刻方式选择

### A. 能直接用 Shopify 原生数据的，优先数据驱动

例如：

- 产品标题、描述、图库、变体
- 博客文章
- 导航菜单
- Metaobject 驱动 FAQ / 时间线 / 工厂能力

### B. 原站是 Elementor 拼装内容的，改为 section schema 驱动

例如：

- 首页 Hero
- 工厂优势区
- 对比区
- 视频区
- CTA 区

### C. 复杂重复内容，改为 Metaobject 管理

例如：

- 工厂实力卡片
- 时间线
- FAQ
- 国家/语言入口
- 首页推荐产品组

---

## 4. 模块化复刻蓝图

下面是建议的 Shopify 模块切分。每个模块都对应一个 section，必要时附带 snippet。

## 4.1 Header / Mega Menu

原站头部特征见 [`首页头部结构`](assets/perfectextile.com/index.html:447) 与 [`菜单结构`](assets/perfectextile.com/index.html:457)。

### 目标复刻点

- 顶部透明/白底切换
- sticky header
- 一级导航横排
- 二级大菜单 Mega Menu
- 移动端抽屉菜单
- logo 左、菜单中/右、CTA 右侧

### Shopify 实现

- 使用 `header` section 重写
- 一级导航来自 Shopify Navigation
- Mega Menu 使用 menu handle + block 配置图片卡片、子分类列
- 移动端用 drawer + accordion

### 推荐拆分

- `sections/header.liquid`
- `snippets/site-logo.liquid`
- `snippets/mega-menu-panel.liquid`
- `snippets/mobile-nav-panel.liquid`

### 必要技术

- CSS sticky + backdrop
- JS 控制 hover / click 展开
- Shopify `linklists` / menu
- 为 Mega Menu 提供 block 配置：标题、图片、按钮、子链接组

---

## 4.2 Hero Section

原站首页 Hero 有视频背景和强视觉 CTA，见 [`首页 Hero 容器`](assets/perfectextile.com/index.html:936)。

### 目标复刻点

- 视频背景或静态背景图
- 左侧标题、描述、按钮
- 可能叠加统计、信誉信息或辅助文案
- 桌面端大留白，移动端裁切优化

### Shopify 实现

- 自定义 `hero-video.liquid`
- 支持 YouTube / MP4 / fallback image
- 支持 overlay、heading、subheading、2 个按钮
- 支持 desktop/mobile 独立高度

### 必要技术

- CSS `object-fit: cover`
- 自定义 overlay
- 懒加载视频与移动端降级

---

## 4.3 分类入口 / 产品导航区

原站首页用了大量分类卡、图标卡、CTA 卡。可抽象为多个通用 section。

### 建议拆成 3 类 section

1. `category-feature-grid`
   - 图标 + 标题 + 子链接
2. `image-cta-cards`
   - 背景图卡片 + 标题 + 链接
3. `product-family-grid`
   - 系列产品入口网格

### 对应原站内容

- Fabric 分类卡
- Bedding 分类卡
- New Product / Tufted / Waffle 等引导卡

### Shopify 实现

全部由 blocks 驱动：

- 图标
- 标题
- 描述
- 链接
- 子项列表
- 背景图片

---

## 4.4 工厂优势 / 比较区 / 价值主张区

原站有大量“为什么选择我们”“对比传统方案”“工厂优势”的内容块，部分直接写在 HTML 中，如 [`compare-header`](assets/perfectextile.com/index.html:1391)。

### 建议拆分

- `comparison-section`
- `feature-icon-grid`
- `stat-highlight-grid`
- `factory-capability-section`

### 内容结构

每块支持：

- 小标题
- 主标题
- 描述
- 左右两列对比项
- 优势卡片（图标 / 数字 / 文案）

### 必要技术

- CSS grid / flex
- 移动端卡片纵向堆叠
- 数字区可选简单 count-up，但不必强依赖第三方库

---

## 4.5 视频内容区

原站首页有多处视频卡，见 [`首页视频模块`](assets/perfectextile.com/index.html:1211)、[`首页视频模块 2`](assets/perfectextile.com/index.html:1273)、[`首页视频模块 3`](assets/perfectextile.com/index.html:1317)。

### 实现建议

做一个通用 section：`media-story-section`

支持：

- 左文右视频 / 左视频右文
- 视频封面图
- 点击后打开原位 iframe / modal
- 支持多 block 形成多段故事

### 技术建议

- 优先封面图 + 延迟加载 iframe
- 避免首页直接加载多个 YouTube iframe
- modal 可简单自写，不依赖 app

---

## 4.6 产品推荐 / 生产流程 / 客户评价轮播

原站大量使用 Swiper，见 [`首页生产流程轮播`](assets/perfectextile.com/index.html:2386)、[`首页评价轮播`](assets/perfectextile.com/index.html:2471)、[`详情页流程轮播`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:1360)。

### Shopify 轮播策略

可选两种：

1. 原生滚动 + scroll snap
2. 引入轻量级 slider JS

如果要尽量 1:1，建议用轻量 slider，自定义样式复刻 Elementor 的：

- 左右箭头
- bullets
- autoplay
- coverflow / carousel / slideshow 三种变体

### 推荐 section

- `media-carousel`
- `testimonial-carousel`
- `process-carousel`
- `related-products-carousel`

### 数据来源

- 图片轮播：section block
- 评价轮播：Metaobject `testimonial`
- Related products：产品集合或 metafield 引用

---

## 4.7 时间线 / 品牌故事

原站有时间线，见 [`首页时间线`](assets/perfectextile.com/index.html:2541)。

### Shopify 实现建议

做 `brand-timeline.liquid`，数据来自 Metaobject：

字段建议：

- year
- label
- title
- description
- image

### 好处

- 后续维护历史节点非常方便
- 可同时输出首页时间线与 About 页面时间线

---

## 4.8 博客推荐区

原站首页与详情页都有 blog 推荐卡片，见 [`首页博客卡片`](assets/perfectextile.com/index.html:2663) 与 [`详情页博客卡片`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:1674)。

### Shopify 实现建议

- 使用 Shopify Blog / Article 原生内容
- section 支持：
  - 选择 blog
  - 选择显示数量
  - 是否显示摘要
  - 按时间倒序

### 推荐 section

- `blog-post-grid`
- `article-related-posts`

---

## 4.9 CTA / 表单 / 询盘体系

原站有多个 CTA 和弹层表单，见 [`详情页目录下载表单`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:2203)，以及 WhatsApp 浮动入口 [`聊天入口`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:2138)。

### Shopify 复刻建议

不要照搬 WordPress 表单插件逻辑，建议换成 Shopify 可维护体系：

#### 基础版

- Contact form section
- CTA 跳转 `/pages/contact`
- 悬浮 WhatsApp 按钮

#### 进阶版

- 弹层表单 section/snippet
- 表单字段映射到 Shopify 联系邮件
- Catalog Download 改成：提交后跳转文件 URL 或自动邮件发送

### 推荐模块

- `contact-cta-banner`
- `catalog-download-form`
- `floating-whatsapp`

---

## 4.10 Footer

原站 Footer 结构见 [`首页页脚`](assets/perfectextile.com/index.html:2828)。

### 复刻点

- Logo + 简介
- 公司导航
- 产品导航
- 社媒图标
- 联系信息
- 多列布局

### Shopify 实现

- `footer.liquid`
- 多 menu block
- 社媒用 theme settings
- 联系方式支持 richtext

---

## 5. 产品详情页 1:1 复刻方案

详情页是复刻重点，因为 perfectextile 大量流量可能来自长尾 SEO 页面。

## 5.1 Shopify 数据模型映射

将原 WordPress 产品/内容页映射到 Shopify Product + Metafield：

### Shopify Product 核心字段

- Title
- Description
- Media
- Collections
- SEO title / description

### Metafields 建议

- `custom.short_intro`
- `custom.spec_table`
- `custom.process_images`
- `custom.feature_icons`
- `custom.faq_items`
- `custom.sustainability_content`
- `custom.related_products_manual`
- `custom.catalog_file`
- `custom.video_url`

这样可以让一个统一的产品模板，承载大多数 fabric 页面。

## 5.2 详情页模板建议

使用一个主模板：

- `templates/product.perfectextile.json`

模板 section 顺序建议：

1. Header
2. Product gallery hero
3. Product intro + CTA
4. Specification table
5. Detail image grid
6. Feature icon grid
7. Process carousel
8. FAQ accordion
9. Sustainability section
10. Related products
11. Related blog posts
12. Final CTA
13. Footer

## 5.3 FAQ 模块

原站 FAQ 结构见 [`详情页手风琴`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:1433)。

Shopify 方案：

- section block 或 Metaobject 驱动
- 保证支持 schema.org FAQ 输出
- 默认全部折叠，单项展开

## 5.4 规格表模块

原站详情页含表格型规格内容，见 [`详情页规格区`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:1027)。

Shopify 方案：

- 若规格字段固定，使用 metafields
- 若规格字段经常变化，使用 Metaobject `spec_row`
- section 输出 table，并做移动端横向滚动

---

## 6. 多语言复刻策略

原站存在多语言入口，见 [`首页 hreflang`](assets/perfectextile.com/index.html:258) 与 [`详情页语言切换`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html:2091)。

### Shopify 推荐方案

如果目标是完整复刻多语言，必须使用 Shopify Markets + Translate & Adapt 或配套翻译方案。

### 实施建议

#### 第 1 阶段

先完成英文主站 1:1 复刻。

#### 第 2 阶段

接入多语言：

- EN
- ES
- FR
- IT
- PT
- VI
- AR

### 注意点

- URL 路由由 Shopify Markets 管理
- menu、产品标题、描述、博客、页面模板都需要翻译
- SEO title / meta description 单独翻译
- 若短期只需视觉复刻，可先做语言切换 UI 占位，不立即接完整翻译

---

## 7. SEO 1:1 复刻策略

perfectextile 明显是 SEO 驱动型 B2B 内容站，因此 Shopify 复刻不能只做首页。

## 7.1 必做项

- 保留页面语义层级：`h1`、`h2`、`h3`
- 每个产品页自定义 meta title / description
- FAQ 输出结构化数据
- Breadcrumb 输出结构化数据
- Blog / Article 模板完整化
- 图片 alt 文本补齐

## 7.2 URL 迁移策略

如果后续真要从原域迁移到 Shopify，需要做 301 mapping。但如果只是“复刻一个 Shopify 版本”，当前先把 URL 结构设计清楚：

- 产品页 slug 对齐现有爆款落地页 slug
- 页面页模板承接 About / Contact / Global Network 等栏目
- Blog 保持主题分类与文章结构

---

## 8. 样式系统设计

## 8.1 全局设计 Token

建议先建立统一 token，再做 section：

- 颜色 token
- 字体 token
- 圆角 token
- 间距 token
- 阴影 token
- 容器宽度 token
- 响应式断点 token

### 响应式断点建议

参考原站 Astra 断点，可采用：

- Desktop: `>= 1200px`
- Laptop: `992px - 1199px`
- Tablet: `768px - 991px`
- Mobile: `< 768px`

原站还明显使用了 `921px` 作为一类关键断点，见 [`Astra 配置`](assets/perfectextile.com/index.html:141)。Shopify 复刻时建议保留兼容：

- 主断点可设 `990px`
- 对特定 header/menu 行为可单独参考 `921px`

## 8.2 字体落地策略

如果 Shopify 字体库没有完全对应，可采用：

- 优先 Shopify 内置字体近似替代
- 若必须 1:1，使用本地字体 / 自托管字体

现有字体资产可参考 [`Astra 本地字体 CSS`](assets/perfectextile.com/wp-content/astra-local-fonts/astra-local-fonts__q_ver_4.12.5.css)。

## 8.3 样式文件组织建议

建议拆为：

- `base.css`：reset / typography / tokens / utilities
- `theme.css`：全局布局
- `section-*.css`：复杂 section 单独维护
- `component-*.css`：按钮、卡片、轮播、accordion

不要把整个站都塞进一个巨大 CSS 文件。

---

## 9. Shopify CLI 一步一步实现流程

下面给出实操顺序，适合从 0 到 1 搭建。

## 第 1 步：初始化主题

```bash
npm install -g @shopify/cli
shopify theme init perfectextile-theme --clone-url https://github.com/Shopify/dawn
```

目标：拿到一个标准 OS 2.0 主题骨架。

## 第 2 步：启动本地开发

```bash
shopify theme dev
```

目标：边开发边预览，避免反复上传。

## 第 3 步：建立复刻资产清单

从现有抓取数据整理：

- 首页所有区块顺序
- 所有 CTA 文案
- 所有主图 / 卡片图 / 视频封面
- 所有产品详情页模块类型
- 所有 FAQ / 表格 / 流程图

建议先做一个 mapping 表：

- WordPress 区块 → Shopify section
- 原始文案 → Shopify 数据字段
- 原图片 URL → Shopify Files / Product media / Metaobject image

## 第 4 步：先做全局基础层

先完成：

- design tokens
- typography
- button system
- card system
- spacing system
- container/grid system

理由：后面的 section 都依赖它。

## 第 5 步：先做 Header + Footer

原因：

- 这是全站骨架
- 所有页面都依赖
- 先把 sticky、mega menu、移动端导航打通

## 第 6 步：复刻首页首屏到尾屏

推荐顺序：

1. Hero
2. 分类入口区
3. 优势区
4. 视频区
5. 产品推荐区
6. 流程轮播
7. 评价轮播
8. 时间线
9. Blog 推荐
10. 最终 CTA

注意：每完成一个 section，都要先抽象成可配置模块，不要为了快写死内容。

## 第 7 步：建立产品模板

先做一个主力详情页模板，以 [`nano printing fabric`](assets/perfectextile.com/nano-printing-fabric-manufacture/index.html) 为样板最合适，因为它模块齐全：

- 图库
- 简介
- CTA
- 规格表
- 图文区
- 优势图标
- 流程轮播
- FAQ
- 相关文章
- 最终表单

## 第 8 步：设计 Metaobject / Metafield 体系

优先建立：

- FAQ
- Testimonial
- Timeline Event
- Factory Feature
- Product Spec Row
- CTA Item

这样后续批量复刻页面会快很多。

## 第 9 步：批量迁移内容

迁移顺序建议：

1. 首页
2. 3~5 个核心产品详情页
3. About / Contact / Company History
4. Blog 文章
5. 其他长尾详情页

## 第 10 步：做响应式微调

重点检查：

- 头部导航断点
- Hero 文案换行
- 卡片网格塌陷
- 轮播箭头位置
- 表格横向滚动
- FAQ 点击区域
- Footer 多列折叠

## 第 11 步：做性能优化

重点：

- 图片转 WebP / AVIF
- 首页视频延迟加载
- 非首屏轮播延迟初始化
- 避免巨量未使用 JS
- 字体数量控制

## 第 12 步：上线前校验

检查清单：

- 首页视觉对比
- 产品页视觉对比
- CTA 链接
- 询盘表单提交
- 404 / 301 逻辑
- SEO meta
- FAQ schema
- 多语言切换
- 移动端菜单

---

## 10. 推荐的 Shopify 模板与模块清单

下面是建议至少实现的模块清单。

### 全局

- Header
- Footer
- Announcement bar
- Floating WhatsApp
- Breadcrumbs
- Modal

### 首页 sections

- Hero video banner
- Category feature grid
- Image CTA cards
- Factory comparison section
- Media story split section
- Capability stats grid
- Product family carousel
- Process carousel
- Testimonial carousel
- Brand timeline
- Blog post grid
- Final CTA banner

### 产品页 sections

- Product media hero
- Product intro summary
- Specification table
- Feature icon grid
- Detail image gallery
- Process carousel
- FAQ accordion
- Sustainability content
- Related products
- Related articles
- Catalog download CTA/form

### 页面模板 sections

- Rich text hero
- Multi-column story
- Team/company timeline
- Global map/network block
- Contact info + form

---

## 11. 数据组织建议

## 11.1 什么放 Theme Settings

适合全局统一配置的：

- 品牌色
- 按钮样式
- Logo
- 社媒链接
- WhatsApp 号码
- 全局 CTA 文案

## 11.2 什么放 Section Settings

适合页面级编辑的：

- 标题
- 描述
- 背景图
- 按钮文案
- 排版方向
- 卡片数量

## 11.3 什么放 Metaobject

适合大量重复结构化内容的：

- FAQ
- Testimonials
- Timeline
- Feature items
- Spec rows
- Region/language items

## 11.4 什么放 Product Metafield

适合单产品专属信息的：

- 规格表
- 专属视频
- 下载目录
- 专属 FAQ
- 关联产品

---

## 12. 关键难点与解决方案

## 难点 1：WordPress Elementor 是自由布局，Shopify 是 schema 驱动

### 解决

不要复制 DOM，改为抽象 section。先保留视觉，再重组结构。

## 难点 2：Mega Menu 很复杂

### 解决 1

用 header block + menu handle + promo card 组合实现，不追求与 Elementor DOM 一致，追求视觉与交互一致。

## 难点 3：大量详情页内容差异化明显

### 解决 2

统一主模板 + metafield/metaobject 扩展，控制 80% 页面复用同一模板。

## 难点 4：多语言与 SEO 页面量大

### 解决 3

先英文主站，后多语言；先高流量页，后长尾页。

## 难点 5：轮播、弹层、视频较多

### 解决 4

统一 JS 组件层，不要每个 section 各写一套脚本。

---

## 13. 最实用的开发顺序

如果希望最高效，按下面顺序执行：

1. 初始化 Dawn 主题
2. 建立全局 token / 基础样式
3. 做 Header / Footer
4. 做 Hero
5. 做首页分类与卡片区
6. 做通用轮播组件
7. 做首页流程/评价/推荐区
8. 做 CTA / 表单 / WhatsApp
9. 做产品详情页模板
10. 接入 metafields / metaobjects
11. 迁移首批内容
12. 做多语言和 SEO 精修

这个顺序最稳，返工最少。

---

## 14. 最终落地建议

如果目标是“完全复刻 + 后续长期维护”，最佳做法不是追求 WordPress 的源码一致，而是：

- **视觉 1:1**
- **信息架构 1:1**
- **交互体验 1:1**
- **Shopify 实现方式模块化、可配置、可批量扩展**

一句话总结：

**先用 Shopify CLI 基于 Dawn 起主题，再把 perfectextile 拆成 Header / Hero / 分类卡 / 优势区 / 视频区 / 轮播区 / 时间线 / CTA / Footer / 产品模板等标准 section，用 metafield 和 metaobject 管理差异内容，先复刻英文主站，再扩展多语言与 SEO 页面。**
