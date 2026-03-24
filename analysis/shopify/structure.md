参考 [`analysis/html/structure.md`](analysis/html/structure.md) 与 [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 输出 Shopify 侧的模块化设计、框架结构与自定义样式方案，目标是服务 perfectextile 首页的 1:1 视觉复刻与后续可维护开发。

# Shopify 结构设计

## 1. 目标

本文件不再重复分析原站 HTML，也不只描述截图模块，而是把两者合并，落到 Shopify 可执行的主题结构设计上。

目标有 4 个：

1. 把首页拆成适合 Shopify Theme 的 section / block / snippet 体系。
2. 在尽量保持 1:1 外观的前提下，避免把 WordPress 的 DOM 结构原样搬进 Shopify。
3. 让页面具备后续可维护性，尤其是卡片复用、样式复用、资源替换和移动端适配。
4. 为后续实际编码提供清晰的文件结构、组件职责和样式组织方式。

---

## 2. Shopify 设计原则

## 2.1 先还原视觉，再适配 Shopify 数据结构

本项目重点不是完整迁移 WordPress 后台逻辑，而是首页外观复刻。

因此优先级应为：

1. 视觉结构一致
2. 组件拆分合理
3. Shopify 可配置
4. 后台数据通用化

也就是说，不能为了“纯 Shopify 配置化”牺牲首页外观。

## 2.2 先 section 骨架，再 block 细化，再 snippet 抽象

建议实现顺序：

1. 先完成首页 section 骨架
2. 再完成每个 section 内的 block 结构
3. 最后把重复卡片抽成 snippet

这样更符合当前任务目标，也更利于截图逐块比对。

## 2.3 能静态配置的内容优先静态配置

首页很多内容本质上是品牌展示内容，不必一开始强绑定 Shopify 商品或博客对象。

例如：

- 工厂视频卡
- 新疆对比区
- Why Choose Us
- Company History
- Certificate
- 客户背书 CTA

这些内容更适合先用 section settings + blocks 固定配置，等视觉完成后再考虑是否接入动态数据。

## 2.4 Shopify 结构要服务 1:1 复刻，而不是反过来

原站很多区域是 Elementor + 自定义 HTML + 自定义 CSS 混合实现。

在 Shopify 中应该保留：

- 视觉顺序
- 版心宽度
- 卡片布局
- 层叠关系
- 轮播样式
- 按钮样式
- 响应式节奏

但不需要保留：

- WordPress / Elementor 特有 class 命名
- 多余嵌套 DOM
- 插件型结构负担

---

## 3. 推荐的主题文件结构

建议基于 Shopify Dawn 或同类 OS 2.0 主题改造，首页核心结构如下。

## 3.1 Layout 层

### [`layout/theme.liquid`](layout/theme.liquid)
职责：
- 全局 HTML 骨架
- 引入全局字体、CSS、JS
- 渲染 header group、main content、footer group
- 挂载浮动工具入口和全局弹窗容器

### [`config/settings_schema.json`](config/settings_schema.json)
职责：
- 品牌色
- 全局按钮圆角
- 容器宽度
- 全局 section 间距
- Header / Footer 通用设置

---

## 3.2 Section 层

首页建议拆为以下 section：

1. `main-header`
2. `hero-banner`
3. `factory-stats-sites`
4. `xinjiang-comparison`
5. `fabric-category-grid`
6. `finished-bedding-grid`
7. `why-choose-us`
8. `production-process-slider`
9. `testimonials-carousel`
10. `company-history-timeline`
11. `certificates-gallery`
12. `global-customers-cta`
13. `blog-news-grid`
14. `footer-cta-banner`
15. `main-footer`
16. `floating-tools`

其中 [`main-header`](sections/main-header.liquid) 与 [`main-footer`](sections/main-footer.liquid) 可以作为全局 section 使用，不只服务首页。

---

## 3.3 Snippet 层

建议抽出的可复用 snippet：

- `site-logo`
- `header-nav-item`
- `mega-menu-fabric`
- `mega-menu-simple-links`
- `button-primary`
- `button-secondary`
- `card-stat`
- `card-video-site`
- `card-comparison-item`
- `card-fabric-category`
- `card-finished-product`
- `card-feature-icon`
- `card-process-slide`
- `card-testimonial-chat`
- `card-timeline-item`
- `card-certificate`
- `card-blog-post`
- `footer-link-column`
- `floating-action-button`

这些 snippet 的意义不是“为了抽象而抽象”，而是减少重复 DOM 和重复 CSS。

---

## 3.4 Asset 层

建议建立统一样式与脚本分层：

### CSS
- [`assets/base.css`](assets/base.css)：基础重置、字体、按钮、容器、全局变量
- [`assets/components.css`](assets/components.css)：卡片、按钮、徽章、轮播箭头等通用组件样式
- [`assets/sections-home.css`](assets/sections-home.css)：首页 section 样式
- [`assets/sections-header-footer.css`](assets/sections-header-footer.css)：头尾和浮动工具样式

### JS
- [`assets/theme.js`](assets/theme.js)：全局行为
- [`assets/home-sliders.js`](assets/home-sliders.js)：流程轮播、评价轮播、时间线轮播等
- [`assets/header-mega-menu.js`](assets/header-mega-menu.js)：header sticky、桌面 mega menu、移动端菜单切换
- [`assets/floating-tools.js`](assets/floating-tools.js)：语言条、回顶、WhatsApp、聊天浮层的前端行为

---

## 4. 首页 section 设计

以下结构综合了 [`analysis/html/structure.md`](analysis/html/structure.md) 的真实页面顺序与 [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 的视觉模块划分。

## 4.1 [`sections/main-header.liquid`](sections/main-header.liquid)

### 职责
- 渲染顶部导航
- 桌面 Mega Menu
- 移动端抽屉菜单
- 右侧 Get A Quote CTA

### 建议 settings
- `logo_image`
- `logo_width`
- `menu`
- `show_quote_button`
- `quote_button_label`
- `quote_button_link`
- `enable_sticky_header`
- `header_height_desktop`
- `header_height_mobile`

### 建议 blocks
- `mega_menu_fabric`
- `mega_menu_bedding`
- `mega_menu_about`

### 实现建议
- Fabric Mega Menu 需要单独模板化，不建议塞进普通 `linklists`
- Bedding / About 可以用简化版 mega menu
- 移动端不复刻桌面 mega menu 的全部复杂视觉，可保留层级关系但用抽屉式交互实现

---

## 4.2 [`sections/hero-banner.liquid`](sections/hero-banner.liquid)

### 职责
- 实现首页首屏大图/视频 Banner
- 管理标题、卖点、按钮和遮罩

### 建议 settings
- `background_type`（image / video）
- `background_image`
- `background_video_url`
- `overlay_opacity`
- `eyebrow`
- `heading_line_1`
- `heading_line_2`
- `cta_label`
- `cta_link`
- `show_pattern_divider`

### 建议 blocks
- `selling_point`：最多 4~6 条

### 实现建议
- 桌面优先支持视频背景，移动端自动降级为图片
- 标题中的橙色强调行不要硬编码在整段字符串中，最好拆为独立 setting
- 按钮内左侧小 icon 用 CSS / inline SVG 实现，避免依赖外部图标库

---

## 4.3 [`sections/factory-stats-sites.liquid`](sections/factory-stats-sites.liquid)

### 职责
- 上方 4 个数据卡
- 下方工厂展示视频卡组

### 建议 blocks
- `stat_item`
- `site_video_card`

### `stat_item` 字段建议
- `number`
- `suffix`
- `label`

### `site_video_card` 字段建议
- `cover_image`
- `video_url`
- `title`
- `address`
- `location_icon`

### 实现建议
- 数据卡和视频卡虽然同属一个视觉模块，但内部建议拆成两个 wrapper
- 播放按钮统一复用 [`card-video-site`](snippets/card-video-site.liquid) 逻辑
- 若暂不接入真实视频弹层，可先做“点击打开新窗口”方案

---

## 4.4 [`sections/xinjiang-comparison.liquid`](sections/xinjiang-comparison.liquid)

### 职责
- 左侧标题、说明、中国地图热点图
- 右侧多行对比卡片

### 建议 settings
- `section_heading`
- `section_subheading`
- `map_image`
- `left_hotspot_x`
- `left_hotspot_y`
- `right_hotspot_x`
- `right_hotspot_y`

### 建议 blocks
- `comparison_row`

### `comparison_row` 字段建议
- `row_title`
- `traditional_title`
- `traditional_points`
- `xinjiang_title`
- `xinjiang_points`
- `badge_text`

### 实现建议
- 该 section 信息密度高，不建议过度抽象成通用表格组件
- 直接为此区块写定制 DOM 更高效
- `traditional_points` 和 `xinjiang_points` 可用多行文本，前端按换行渲染列表

---

## 4.5 [`sections/fabric-category-grid.liquid`](sections/fabric-category-grid.liquid)

### 职责
- 面料分类入口区
- 8 张分类卡
- 双 CTA 按钮

### 建议 settings
- `heading`
- `subheading`
- `primary_button_label`
- `primary_button_link`
- `secondary_button_label`
- `secondary_button_link`

### 建议 blocks
- `category_card`

### `category_card` 字段建议
- `title`
- `image_main`
- `image_secondary`
- `image_tertiary`
- `image_quaternary`
- `link`

### 实现建议
- 由于原图卡是拼贴式布局，不建议只给一张图
- 建议允许 2~4 张图组合，前端拼出接近原站的 collage 视觉
- 这是后续非常可复用的入口类 section

---

## 4.6 [`sections/finished-bedding-grid.liquid`](sections/finished-bedding-grid.liquid)

### 职责
- 成品床品网格展示
- 6 张产品卡
- 双 CTA 按钮

### 建议 blocks
- `product_card`

### `product_card` 字段建议
- `title`
- `image`
- `link`

### 实现建议
- 该区块视觉比面料分类区更干净，卡片结构应保持极简
- 不建议一开始绑定 Shopify 产品对象，先做静态 block 更容易贴合原站
- 后续如果需要，可增加一个 `product` picker 用于半动态映射

---

## 4.7 [`sections/why-choose-us.liquid`](sections/why-choose-us.liquid)

### 职责
- 背景图 + 遮罩
- 标题和说明
- 4 列图标卖点

### 建议 settings
- `background_image`
- `overlay_opacity`
- `eyebrow`
- `heading`
- `description`

### 建议 blocks
- `feature_item`

### `feature_item` 字段建议
- `icon_svg`
- `title`
- `points`

### 实现建议
- 图标优先使用 inline SVG，保证橙色线性图标风格一致
- `points` 用换行文本输出无序列表
- 桌面 4 列，移动端 1 列或 2 列

---

## 4.8 [`sections/production-process-slider.liquid`](sections/production-process-slider.liquid)

### 职责
- 生产流程图文轮播

### 建议 settings
- `heading`
- `description`
- `slides_per_view_desktop`
- `slides_per_view_mobile`

### 建议 blocks
- `process_slide`

### `process_slide` 字段建议
- `image`
- `title`
- `caption`

### 实现建议
- 优先做自定义轻量轮播，不必急于引入大型第三方 slider 库
- 只要支持：横向滑动、分页点、前后切换，即可满足当前复刻要求
- 样式重点在图片尺寸、标题位置和分页点间距

---

## 4.9 [`sections/testimonials-carousel.liquid`](sections/testimonials-carousel.liquid)

### 职责
- 左侧文案和按钮
- 右侧聊天截图 3D 轮播

### 建议 settings
- `eyebrow`
- `heading`
- `description`
- `button_label`
- `button_link`

### 建议 blocks
- `testimonial_slide`

### `testimonial_slide` 字段建议
- `image`
- `alt_text`
- `quote`
- `customer_name`

### 实现建议
- 视觉核心是“中间大、两侧倾斜”的 3D 卡片布局
- 可以用 CSS `transform` 和 `opacity` 模拟，不一定要复杂 3D 库
- 手机端可降级为普通轮播，桌面端保留立体效果

---

## 4.10 [`sections/company-history-timeline.liquid`](sections/company-history-timeline.liquid)

### 职责
- 左文案介绍
- 右侧时间线节点 + 年份卡片

### 建议 settings
- `heading`
- `description`
- `button_label`
- `button_link`

### 建议 blocks
- `timeline_item`

### `timeline_item` 字段建议
- `year`
- `label`
- `image`
- `title`
- `description`

### 实现建议
- 桌面端保留横向时间线
- 移动端可降级为竖向年表卡片列表
- 时间线节点与下方卡片的对应关系应在 DOM 结构中明确，不建议完全依赖 JS 拼装

---

## 4.11 [`sections/certificates-gallery.liquid`](sections/certificates-gallery.liquid)

### 职责
- 证书图片画廊

### 建议 settings
- `heading`
- `columns_desktop`
- `columns_mobile`

### 建议 blocks
- `certificate_item`

### `certificate_item` 字段建议
- `image`
- `title`
- `link`

### 实现建议
- 优先保证图片清晰度和统一边框感
- 可选 lightbox，但不是首页第一优先级
- 如果图片很多，后续可拓展为可分页 gallery

---

## 4.12 [`sections/global-customers-cta.liquid`](sections/global-customers-cta.liquid)

### 职责
- 背景客户照片拼图
- 中央 CTA 内容层

### 建议 settings
- `heading`
- `description`
- `button_label`
- `button_link`
- `overlay_opacity`

### 建议 blocks
- `background_photo`

### `background_photo` 字段建议
- `image`
- `alt`

### 实现建议
- 背景可用 CSS Grid 形成拼贴矩阵
- 中间叠加一个绝对定位内容层
- 这是 CTA 区，不建议把背景照片做成交互式 gallery

---

## 4.13 [`sections/blog-news-grid.liquid`](sections/blog-news-grid.liquid)

### 职责
- 博客推荐区
- 顶部标题 + View More
- 文章卡片 3 列

### 建议 settings
- `eyebrow`
- `heading`
- `button_label`
- `button_link`
- `source_mode`（manual / blog）
- `blog`

### 建议 blocks
- `article_card`

### `article_card` 字段建议
- `image`
- `date`
- `title`
- `excerpt`
- `link`

### 实现建议
- 初版可以用 manual block，保证和截图完全一致
- 二期可支持自动读取 Shopify blog 文章
- 卡片布局和阴影细节需要与截图严格对齐

---

## 4.14 [`sections/footer-cta-banner.liquid`](sections/footer-cta-banner.liquid)

### 职责
- Footer 前的大图 CTA 横幅

### 建议 settings
- `background_image`
- `overlay_opacity`
- `heading`
- `description`
- `button_label`
- `button_link`

### 实现建议
- 单独 section，不应并入 footer
- 样式上作为页面结束前的最后一次视觉收束和转化引导

---

## 4.15 [`sections/main-footer.liquid`](sections/main-footer.liquid)

### 职责
- 品牌简介
- 社媒图标
- 链接列
- 产品列
- 联系方式列
- 版权信息

### 建议 settings
- `logo_image`
- `brand_description`
- `copyright_text`

### 建议 blocks
- `link_column`
- `product_column`
- `contact_group`
- `social_link`

### 实现建议
- 联系方式信息量较大，建议允许多个 `contact_group`
- Footer 列表不要完全依赖 Shopify 默认 `footer` section 逻辑，建议自定义，以贴近原站企业站排版

---

## 4.16 [`sections/floating-tools.liquid`](sections/floating-tools.liquid)

### 职责
- 语言条
- WhatsApp 按钮
- 聊天按钮
- 回顶 / 辅助按钮

### 建议 settings
- `show_language_bar`
- `language_label`
- `show_whatsapp`
- `whatsapp_link`
- `show_chat_button`
- `chat_link`
- `show_back_to_top`

### 实现建议
- 若第三方聊天系统未接入，可先做静态入口和占位按钮
- 视觉位置要尽量和截图保持一致
- 该 section 可以通过全局渲染，而非只在首页 JSON 模板中出现

---

## 5. 首页 JSON 模板组织方式

建议在 [`templates/index.json`](templates/index.json) 中按以下顺序组织：

1. `main-header`
2. `hero-banner`
3. `factory-stats-sites`
4. `xinjiang-comparison`
5. `fabric-category-grid`
6. `finished-bedding-grid`
7. `why-choose-us`
8. `production-process-slider`
9. `testimonials-carousel`
10. `company-history-timeline`
11. `certificates-gallery`
12. `global-customers-cta`
13. `blog-news-grid`
14. `footer-cta-banner`
15. `main-footer`
16. `floating-tools`

如果主题结构要求 header / footer 走 group，也可以改为：

- Header Group：`main-header`
- Main：第 2 ~ 14 项
- Footer Group：`main-footer`
- Global Fixed Layer：`floating-tools`

---

## 6. Block 与 Snippet 的职责边界

## 6.1 什么适合 block

适合 block 的内容：
- 可重复的内容项
- 需要在主题编辑器中排序
- 每个 item 配置字段差异不大

例如：
- 统计卡
- 工厂卡
- 分类卡
- 产品卡
- 卖点卡
- 流程 slide
- 证书卡
- 文章卡
- 时间线项

## 6.2 什么适合 snippet

适合 snippet 的内容：
- 重复 DOM 结构
- 重复按钮样式
- 重复图标卡结构
- 不一定直接暴露给主题编辑器

例如：
- 按钮组件
- 卡片组件
- Footer 信息列
- 视频封面组件
- 博客卡片组件

## 6.3 什么适合 section 自定义 DOM

适合 section 直接写定制 DOM 的内容：
- Hero Banner
- Xinjiang Comparison
- Testimonials 右侧立体轮播容器
- Company History 时间线整体轨道
- Global Customers CTA 背景拼图层

这些模块结构独特，如果强行过度抽象，反而会增加维护成本。

---

## 7. 自定义样式体系设计

## 7.1 建议建立设计变量

建议在 [`assets/base.css`](assets/base.css) 中定义变量：

```css
:root {
  --pt-color-primary: #ff8c00;
  --pt-color-primary-hover: #e67600;
  --pt-color-text: #000000;
  --pt-color-text-muted: #555555;
  --pt-color-bg: #ffffff;
  --pt-color-bg-soft: #f7f1e7;
  --pt-color-border: #eaeaea;
  --pt-shadow-card: 0 10px 30px rgba(0, 0, 0, 0.08);
  --pt-radius-card: 16px;
  --pt-radius-button: 999px;
  --pt-container: 1200px;
  --pt-section-space-y: 96px;
}
```

这些变量可以稳定支撑整页视觉统一。

## 7.2 样式分层建议

### 基础层
负责：
- `body`
- `img`
- `a`
- 标题字号体系
- 通用按钮
- 容器宽度

### 组件层
负责：
- 卡片阴影
- 轮播箭头
- 分页点
- section 标题头
- 图标样式
- 标签/徽章

### 页面层
负责：
- Hero 特有布局
- 对比区双栏
- 时间线轨道
- 客户照片拼图墙
- Footer 多列布局

这样可以避免所有样式都堆在一个文件中。

## 7.3 不建议完全依赖 Dawn 默认样式

原因：
- 原站视觉与 Dawn 差异较大
- 默认 spacing、按钮、卡片、标题节奏不一致
- 如果不做强定制，很难达到 1:1

因此建议：
- 复用 Dawn 的基础结构与无障碍优势
- 但首页的 section 和组件样式全部自定义覆盖

---

## 8. 响应式策略

## 8.1 关键断点建议

建议至少使用：
- Desktop：`1200px+`
- Tablet：`768px ~ 1199px`
- Mobile：`767px 以下`

同时重点关注原站显著断点：
- `921px` 左右用于 Header 行为切换

## 8.2 模块级响应式调整

### Header
- 桌面：完整导航 + Mega Menu + CTA
- 移动：汉堡菜单 + 折叠子菜单

### Hero
- 桌面：视频背景，高度较大
- 移动：图片背景 + 文案缩小 + 按钮不换行

### Stats / Factory Cards
- 桌面：4 卡横排 + 2 张大媒体卡
- 移动：上下堆叠

### Fabric / Product Grid
- 桌面：4 列 / 3 列
- 平板：2 列
- 手机：1 列或 2 列

### Testimonials
- 桌面：左文右 3D 轮播
- 手机：上下堆叠 + 普通 slider

### Timeline
- 桌面：横向时间线
- 手机：纵向时间卡列表

### Footer
- 桌面：多列
- 手机：折叠式或顺序堆叠

---

## 9. 数据来源建议

## 9.1 第一阶段：手动配置优先

为了先完成高还原复刻，建议首页多数内容采用手动配置：

- 文案手动填入 section settings
- 图片手动上传到 theme editor
- 卡片手动通过 blocks 配置

## 9.2 第二阶段：逐步接入 Shopify 数据

可后续动态化的模块：

- Blog News → Shopify blog
- Finished Bedding → Shopify products / metaobjects
- Footer links → linklist
- Header menu → navigation

## 9.3 不建议优先动态化的模块

- Xinjiang Comparison
- Why Choose Us
- Company History
- Certificates
- Global Customers CTA

这些区域是品牌型内容，手动配置更稳定。

---

## 10. 推荐的开发顺序

建议按“先视觉关键区，再中间重复区，再尾部区”的方式推进。

### 第 1 阶段：全局骨架
1. `main-header`
2. `main-footer`
3. `base.css`
4. 全局按钮、容器、标题系统

### 第 2 阶段：首页核心视觉区
5. `hero-banner`
6. `factory-stats-sites`
7. `xinjiang-comparison`
8. `why-choose-us`

### 第 3 阶段：网格与轮播区
9. `fabric-category-grid`
10. `finished-bedding-grid`
11. `production-process-slider`
12. `testimonials-carousel`
13. `company-history-timeline`
14. `certificates-gallery`
15. `blog-news-grid`

### 第 4 阶段：转化与辅助区
16. `global-customers-cta`
17. `footer-cta-banner`
18. `floating-tools`

### 第 5 阶段：响应式与微调
19. Desktop / Tablet / Mobile 逐屏对比截图
20. 调整留白、字号、圆角、阴影、按钮位置
21. 补充 hover、轮播和交互细节

---

## 11. 最终建议

最适合这次项目的 Shopify 结构不是“最大化后台动态化”，而是：

**以 section 为页面骨架，以 block 为可编辑内容项，以 snippet 为复用卡片，以自定义 CSS 为视觉还原核心。**

也就是说：

- 页面层面：按原站模块顺序拆 section
- 内容层面：按卡片拆 block
- 代码层面：按重复结构抽 snippet
- 样式层面：按首页强定制实现 1:1 视觉复刻

这样既能保持 [`analysis/html/structure.md`](analysis/html/structure.md) 中的真实结构来源，也能吸收 [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 中的视觉模块划分，最终形成适合 Shopify 实际开发的首页蓝图。
