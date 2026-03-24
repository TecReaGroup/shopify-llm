请作为一名资深 Shopify Theme 工程师，基于 [`docs/shopify.md`](docs/shopify.md)、[`analysis/html/structure.md`](analysis/html/structure.md)、[`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 和 [`analysis/shopify/structure.md`](analysis/shopify/structure.md)，对 [`https://perfectextile.com/`](https://perfectextile.com/) 的**主页内容**进行 Shopify 1:1 复刻规划与逐步实现。

注意，这是一份**一次性完整 Prompt**，用于驱动你从分析到实现按步骤推进，不是拆分成多个零散 prompt。你必须严格按照下面的流程执行。

---

# 任务目标

只复刻 [`https://perfectextile.com/`](https://perfectextile.com/) 的**首页内容**，不处理整站其他页面。

你的目标不是简单“做一个相似页面”，而是：

1. 尽量 1:1 还原原站首页的视觉风格、模块顺序、卡片结构、间距节奏、交互外观。
2. 充分分析原站的**设计语言**、**模块划分**、**可复用卡片模式**。
3. 尽量将页面抽象为**可复用的 Shopify Section 模块**与可复用 Snippet。
4. 每个 Section 都必须写成**动态 Schema** 的形式，便于在 Shopify 后台自定义内容。
5. 资源层面优先直接使用原站 [`https://perfectextile.com/`](https://perfectextile.com/) 的图片、视频、Logo、图标等现有资源，不需要另做一套新素材。
6. 严格注意设计规范、样式一致性和卡片复用性。

---

# 最高优先级

执行过程中，优先级必须严格如下：

1. **首页视觉 1:1 还原**
2. **模块拆分合理**
3. **Shopify section/schema 可配置**
4. **卡片与代码复用性**
5. **后续维护性**

也就是说：

- 不要为了“写得更抽象”而牺牲视觉一致性
- 不要为了“后台更灵活”而破坏原站版式
- 不要为了“图省事”直接套 Dawn 默认模块替代复杂结构

---

# 资源使用要求

你在复刻首页时，图片、视频、Logo、图标等资源，**直接优先使用原站资源**，无需重新设计素材。

也就是说：

- 可以直接引用 [`https://perfectextile.com/`](https://perfectextile.com/) 的现有资源地址
- 也可以优先使用本地已分析或已下载的资源线索，例如 [`assets/perfectextile.com`](assets/perfectextile.com)、[`assets/screenshot`](assets/screenshot)
- 截图主要用于视觉比对和 1:1 校准，不是要重新绘制素材

如果某一处资源找不到，就回到原站 HTML 或截图继续分析，不要随便替换成风格不一致的占位图。

---

# 必须参考的资料

开始任何实现之前，必须综合阅读和使用以下资料：

- [`docs/shopify.md`](docs/shopify.md)
- [`analysis/html/structure.md`](analysis/html/structure.md)
- [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md)
- [`analysis/shopify/structure.md`](analysis/shopify/structure.md)
- 截图目录 [`assets/screenshot`](assets/screenshot)
- 原站资源与页面线索 [`assets/perfectextile.com/index.html`](assets/perfectextile.com/index.html)

你不能跳过分析阶段直接编码。

---

# 对原站的理解要求

在正式改代码前，你必须先总结原站首页的以下内容，并以此指导实现：

## 1. 设计语言

你必须识别并贯穿实现：

- 主品牌橙色的使用方式
- 白底 / 浅米色背景的交替节奏
- 企业型外贸网站的视觉气质
- 标题与正文的层级关系
- 按钮的圆角、描边、实心与 hover 规律
- 卡片的阴影、边框、圆角和留白
- 模块间的大块留白节奏
- 网格与轮播的统一风格

## 2. 模块划分

你必须把首页拆解为合理的 Shopify 首页模块，而不是照搬 WordPress DOM。

至少应识别出以下首页内容层级：

1. Header
2. Hero Banner
3. Factory Stats & Sites
4. Xinjiang Comparison
5. Fabric Category Grid
6. Finished Bedding Grid
7. Why Choose Us
8. Production Process Slider
9. Testimonials Carousel
10. Company History Timeline
11. Certificates Gallery
12. Global Customers CTA
13. Blog News Grid
14. Footer CTA Banner
15. Main Footer
16. Floating Tools

## 3. 可复用卡片模式

你必须分析哪些内容应该抽象成复用卡片，例如：

- 统计卡
- 视频封面卡
- 对比信息卡
- 分类卡片
- 产品卡片
- 图标卖点卡
- 流程轮播卡
- 评价卡
- 时间线卡
- 证书卡
- 博客卡
- Footer 信息列

并优先让这些结构具备 Snippet 复用潜力。

---

# 总体实现原则

## 1. 只复刻首页内容

不要扩展到：

- 产品详情页
- collection 页
- about 内页
- 博客内页
- 联系页深度功能
- 全站多语言系统

## 2. 逐步推进，但这份 Prompt 是完整总控 Prompt

虽然这是一份一次性的完整 Prompt，但实际执行时你必须**一步一步来**。

这意味着：

- 先做分析与计划
- 再做全局基础层
- 再按首页模块顺序逐个复刻
- 每完成一个模块后再进入下一个
- 不要一口气无分析地同时重写所有 section

## 3. 每个 Section 都必须支持动态 Schema

每个 Shopify Section 都必须：

- 有明确的 `settings`
- 有必要时支持 `blocks`
- 字段语义清晰
- 能在 Shopify 后台自定义标题、图片、按钮、列表项等内容

禁止把首页所有内容硬编码在 Liquid 模板里。

## 4. 优先 section + snippet 架构

你需要把首页设计成：

- section 负责页面模块骨架
- block 负责可编辑重复项
- snippet 负责可复用卡片结构
- CSS 负责还原视觉
- 必要的 JS 负责轮播、菜单、悬浮工具等交互

## 5. 严格注意设计规范与卡片复用性

实现中必须保持：

- 统一命名
- 统一间距系统
- 统一按钮规范
- 统一卡片规范
- 统一圆角和阴影系统
- 统一标题样式与正文节奏
- 相似结构优先复用，不重复造轮子

---

# 推荐的 Shopify 结构目标

你最终的首页应该优先向以下结构靠拢：

## Section 级别

建议包含但不限于：

- [`sections/main-header.liquid`](sections/main-header.liquid)
- [`sections/hero-banner.liquid`](sections/hero-banner.liquid)
- [`sections/factory-stats-sites.liquid`](sections/factory-stats-sites.liquid)
- [`sections/xinjiang-comparison.liquid`](sections/xinjiang-comparison.liquid)
- [`sections/fabric-category-grid.liquid`](sections/fabric-category-grid.liquid)
- [`sections/finished-bedding-grid.liquid`](sections/finished-bedding-grid.liquid)
- [`sections/why-choose-us.liquid`](sections/why-choose-us.liquid)
- [`sections/production-process-slider.liquid`](sections/production-process-slider.liquid)
- [`sections/testimonials-carousel.liquid`](sections/testimonials-carousel.liquid)
- [`sections/company-history-timeline.liquid`](sections/company-history-timeline.liquid)
- [`sections/certificates-gallery.liquid`](sections/certificates-gallery.liquid)
- [`sections/global-customers-cta.liquid`](sections/global-customers-cta.liquid)
- [`sections/blog-news-grid.liquid`](sections/blog-news-grid.liquid)
- [`sections/footer-cta-banner.liquid`](sections/footer-cta-banner.liquid)
- [`sections/main-footer.liquid`](sections/main-footer.liquid)
- [`sections/floating-tools.liquid`](sections/floating-tools.liquid)

## Snippet 级别

建议优先抽象的复用组件：

- [`snippets/button-primary.liquid`](snippets/button-primary.liquid)
- [`snippets/button-secondary.liquid`](snippets/button-secondary.liquid)
- [`snippets/card-stat.liquid`](snippets/card-stat.liquid)
- [`snippets/card-video-site.liquid`](snippets/card-video-site.liquid)
- [`snippets/card-comparison-item.liquid`](snippets/card-comparison-item.liquid)
- [`snippets/card-fabric-category.liquid`](snippets/card-fabric-category.liquid)
- [`snippets/card-finished-product.liquid`](snippets/card-finished-product.liquid)
- [`snippets/card-feature-icon.liquid`](snippets/card-feature-icon.liquid)
- [`snippets/card-process-slide.liquid`](snippets/card-process-slide.liquid)
- [`snippets/card-testimonial-chat.liquid`](snippets/card-testimonial-chat.liquid)
- [`snippets/card-timeline-item.liquid`](snippets/card-timeline-item.liquid)
- [`snippets/card-certificate.liquid`](snippets/card-certificate.liquid)
- [`snippets/card-blog-post.liquid`](snippets/card-blog-post.liquid)
- [`snippets/footer-link-column.liquid`](snippets/footer-link-column.liquid)

如果某个 snippet 暂时没有必要抽离，可以延后，但要先评估复用价值。

---

# 样式与脚本规范

## CSS 组织建议

优先按以下方式组织：

- [`assets/base.css`](assets/base.css)：全局变量、字体、基础元素、容器、按钮基础规范
- [`assets/components.css`](assets/components.css)：通用卡片、按钮、网格、图标卡、分页点等组件样式
- [`assets/sections-home.css`](assets/sections-home.css)：首页各模块专属样式
- [`assets/sections-header-footer.css`](assets/sections-header-footer.css)：Header / Footer / Floating Tools 样式

## CSS 实现要求

你必须：

- 优先建立统一 CSS 变量系统
- 保持颜色、阴影、圆角、section 间距的一致性
- 不要大量依赖内联样式
- 不要把所有样式堆在单一文件
- 不要照搬 WordPress / Elementor class 名

## JS 使用原则

只在必要时添加 JS，例如：

- Header sticky
- 移动端菜单
- Mega Menu 交互
- 轮播
- 浮动工具
- 视频播放按钮

如果纯 CSS 可以实现，就优先纯 CSS。
不要轻易引入大体积第三方库。

---

# 响应式要求

实现时至少覆盖：

- Desktop
- Tablet
- Mobile

重点检查：

- Header 折叠逻辑
- Hero 高度变化
- 分类卡 / 产品卡的列数变化
- 轮播在小屏下的退化方式
- 时间线在移动端的改造方式
- Footer 多列在移动端的堆叠方式

移动端允许在结构上做合理降级，但不能破坏整体设计语言。

---

# 必须遵守的执行流程

你必须严格按以下步骤推进，不允许跳步：

## Step 1：先分析，不写代码

先输出以下分析内容：

1. 基于 [`analysis/html/structure.md`](analysis/html/structure.md) 总结原站首页真实结构顺序
2. 基于 [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 总结首页视觉模块顺序与设计语言
3. 基于 [`analysis/shopify/structure.md`](analysis/shopify/structure.md) 输出 Shopify 侧的 section / block / snippet 设计方案
4. 总结哪些部分必须高定制，哪些部分适合抽成复用卡片
5. 给出建议的首页开发顺序

这一阶段只做分析与计划，不修改代码。

## Step 2：建立全局基础层

在进入首页 section 之前，先处理：

1. 全局颜色变量
2. 字体策略
3. 容器宽度
4. section 间距体系
5. 全局按钮系统
6. 通用卡片系统

确保后续每个 section 都可以在统一设计规范下实现。

## Step 3：按首页顺序逐个复刻 Section

必须按首页顺序，一个模块一个模块推进，推荐顺序如下：

1. Header
2. Hero Banner
3. Factory Stats & Sites
4. Xinjiang Comparison
5. Fabric Category Grid
6. Finished Bedding Grid
7. Why Choose Us
8. Production Process Slider
9. Testimonials Carousel
10. Company History Timeline
11. Certificates Gallery
12. Global Customers CTA
13. Blog News Grid
14. Footer CTA Banner
15. Main Footer
16. Floating Tools

## Step 4：每复刻一个模块前都要先重新分析

每开始一个新 section 时，你都必须重新做以下动作：

1. 回看 [`analysis/shopify/structure.md`](analysis/shopify/structure.md) 中该模块对应 section 的职责、建议 settings、建议 blocks
2. 回看 [`analysis/html/structure.md`](analysis/html/structure.md) 中原站该模块的真实结构、关键 DOM 和交互线索
3. 回看 [`analysis/screenshot/structure.md`](analysis/screenshot/structure.md) 中该模块的视觉重点
4. 对照该模块对应截图，确认：
   - 版式
   - 留白
   - 图片比例
   - 圆角
   - 阴影
   - 标题层级
   - 按钮位置
   - 桌面/移动端趋势

然后再编码。

## Step 5：每个模块都要输出完整说明

每完成一个模块，都必须说明：

1. 当前完成的是哪个 section
2. 修改了哪些文件
3. 为什么这样拆 section / snippet / schema
4. 与原站截图和 HTML 对齐的依据是什么
5. 当前模块后续还可以如何微调

---

# 每个模块的最低实现要求

在复刻每个首页 Section 时，必须同时满足以下标准：

1. 有独立明确的 Shopify Section 文件
2. 有完整动态 Schema
3. 重复项优先用 blocks
4. 可复用结构优先评估是否抽 snippet
5. 桌面端视觉尽量贴近截图
6. 移动端具备基础适配
7. 不要影响尚未处理的其他模块
8. 能直接接入原站资源进行展示

---

# 对动态 Schema 的要求

每个 Section 都必须思考并尽量支持以下可配置项：

- 标题
- 副标题
- 富文本描述
- 按钮文字与链接
- 图片
- 视频链接
- 列表项
- 卡片项
- 背景图
- 遮罩透明度
- 排序可控的 blocks

字段命名必须语义化，禁止使用：

- `text1`
- `text2`
- `img1`
- `item1`

你应该使用更清晰的命名，例如：

- `section_heading`
- `section_description`
- `primary_button_label`
- `primary_button_link`
- `background_image`
- `video_url`
- `feature_title`
- `feature_points`

---

# 对可复用性的要求

你必须主动识别页面中的重复结构，并尽量抽成可复用组件。

但要注意：

- 复用是为了减少重复和统一样式
- 不是为了过度抽象
- 如果某个模块高度定制，就优先保证该模块本身的 1:1 视觉，而不是强行通用化

也就是说：

- 普通卡片可复用
- 超高定制模块可以局部专用 DOM
- 但按钮、卡片壳、标题头、CTA 形式仍应尽量统一

---

# 明确禁止事项

你在执行过程中，禁止做以下事情：

1. 把任务扩展成整站重构
2. 未分析文档和截图就直接生成代码
3. 一上来同时粗暴改写多个 section
4. 为了省事直接照搬 WordPress / Elementor DOM
5. 用与原站完全不一致的占位图或风格替代资源
6. 不写动态 Schema，直接把内容写死
7. 过度依赖 Dawn 默认 section 样式
8. 过度引入第三方 JS 库
9. 破坏统一设计规范和卡片复用策略
10. 忽略移动端基础适配

---

# 最终输出方式要求

你在执行这份 Prompt 时，必须按阶段输出，而不是一口气只给最终代码。

推荐输出节奏：

1. 先给首页总体分析与 Shopify 结构计划
2. 再给全局基础层方案
3. 然后每次只处理一个 section：
   - 先分析
   - 再实现
   - 再总结
4. 按顺序持续推进直到首页完成

也就是说，这是一份**完整总控 Prompt**，但你执行时必须**逐模块、逐阶段**推进。

---

# 最终执行指令

现在开始执行：

**请严格基于 [`docs/shopify.md`](docs/shopify.md)、[`analysis/html/structure.md`](analysis/html/structure.md)、[`analysis/screenshot/structure.md`](analysis/screenshot/structure.md)、[`analysis/shopify/structure.md`](analysis/shopify/structure.md)，只针对 [`https://perfectextile.com/`](https://perfectextile.com/) 的首页内容，先完成分析与结构计划，再建立全局基础层，然后按首页顺序一步一步复刻为可复用、可配置、支持动态 Schema 的 Shopify Section 模块。图片、视频、Logo、图标等资源优先直接使用原站资源。全程严格遵守设计规范、模块划分与卡片复用性要求，并以 1:1 视觉还原为最高优先级。**
