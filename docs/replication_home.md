# perfectextile 首页 Shopify 复刻简化方案

## 1. 目标

本方案只针对 **perfectextile 首页** 做 Shopify 复刻。

目标很明确：

- 只复刻首页内容
- 只强调 **外观完全一致性**
- 不优先追求 WordPress 原有后台逻辑
- 不扩展详情页、博客页、About 页、多语言全站体系
- 用 Shopify CLI + Shopify theme 完成首页可视化复刻

也就是说，这次重点不是“整站重建”，而是：

**把 [`perfectextile 首页`](assets/perfectextile.com/index.html) 做成一个在 Shopify 中视觉尽量 1:1 的首页。**

---

## 2. 复刻范围

只做首页这些内容：

1. Header
2. Hero 首屏
3. 首页分类卡片区
4. 工厂优势 / 对比说明区
5. 视频展示区
6. 产品推荐区
7. 生产流程轮播
8. 客户评价轮播
9. 公司故事 / 时间线
10. 博客推荐区
11. CTA 区
12. Footer

不在本次范围内：

- 产品详情页
- Collection 页
- Blog 内页
- Contact 页深度功能
- 多语言完整切换
- Shopify 后台复杂内容模型

---

## 3. 最适合这次任务的技术策略

因为你要求的是 **首页外观完全一致**，并且希望后续卡片可以复用，所以这次最合适的策略要调整为：

**先一张一张复刻卡片，再把卡片组合成 section，最后再拼成整张首页。**

也就是开发顺序从原来的“先整屏 section”，改成：

- 先拆单卡片
- 再做卡片组
- 再做页面区块
- 最后完成整页组合

这样做的好处：

- 每张卡片能先单独做到 1:1
- 后续别的页面也能复用这些卡片
- 首页组合时更稳定，返工更少
- 视觉校对更容易，一次只比对一个卡片

所以本次首页复刻的核心原则改为：

**优先按卡片颗粒度复刻视觉，再把卡片组装成 Shopify 页面。**

---

## 4. Shopify CLI 实施起点

参考 [`shopify_cli.md`](shopify_cli.md:3)，建议直接这样开始：

```bash
npm install -g @shopify/cli
shopify theme init perfectextile-home --clone-url https://github.com/Shopify/dawn
shopify theme dev
```

作用：

- 安装 Shopify CLI
- 基于 Dawn 创建主题
- 本地实时预览首页复刻效果

---

## 5. 首页结构来源

首页结构主要参考 [`首页源码`](assets/perfectextile.com/index.html)。

从源码可确认以下关键区块：

### 5.1 Header

见 [`header 结构`](assets/perfectextile.com/index.html:447) 与 [`导航结构`](assets/perfectextile.com/index.html:457)。

特点：

- sticky header
- logo + 横向导航
- Mega Menu 下拉
- 移动端折叠菜单

### 5.2 Hero 首屏

见 [`Hero 容器`](assets/perfectextile.com/index.html:936)。

特点：

- 视频背景
- 大标题
- CTA 按钮
- 高视觉冲击力

### 5.3 视频模块

见 [`视频区 1`](assets/perfectextile.com/index.html:1211)、[`视频区 2`](assets/perfectextile.com/index.html:1273)、[`视频区 3`](assets/perfectextile.com/index.html:1317)。

### 5.4 比较/优势说明区

见 [`compare-header`](assets/perfectextile.com/index.html:1391)。

### 5.5 生产流程轮播

见 [`生产流程轮播`](assets/perfectextile.com/index.html:2386)。

### 5.6 客户评价轮播

见 [`客户评价轮播`](assets/perfectextile.com/index.html:2471)。

### 5.7 时间线

见 [`时间线`](assets/perfectextile.com/index.html:2541)。

### 5.8 博客区

见 [`博客卡片`](assets/perfectextile.com/index.html:2663)。

### 5.9 Footer

见 [`Footer`](assets/perfectextile.com/index.html:2828)。

---

## 6. 外观复刻关键设计

如果要做到首页看起来几乎一致，最关键的不是 Liquid，而是下面 4 件事：

## 6.1 颜色完全贴近原站

参考 [`颜色提取结果`](assets/perfectextile.com/extracted_colors.json)。

首页核心颜色建议直接固定：

- 主色：`#FF8C00`
- hover：`#E67600`
- 黑色文字：`#000000`
- 辅助蓝：`#003399`
- 边框灰：`#EAEAEA`
- 浅灰背景：`#F5F5F5`
- 白色背景：`#FFFFFF`

外观一致性上，这些颜色必须优先锁死，不要先做主题色自定义。

## 6.2 字体尽量接近

参考 [`字体提取结果`](assets/perfectextile.com/extracted_fonts.json)。

建议：

- 标题用 `Plus Jakarta Sans`
- 正文用 `Open Sans` 或 `Roboto`
- 少量数字/强调可用 `Akatab`

如果要更像原站，建议直接自托管接近字体。

## 6.3 间距与容器宽度一致

原站首页大量依赖：

- 大块留白
- 卡片间距
- 标题与正文垂直节奏
- 轮播与图片区块的宽度控制

这部分决定“像不像”。

## 6.4 响应式断点尽量贴原站

原站 Astra 关键断点可参考 [`Astra 断点线索`](assets/perfectextile.com/index.html:141)。

建议复刻时至少做：

- Desktop
- Tablet
- Mobile

并重点检查：

- Header 折叠点
- Hero 高度
- 卡片列数变化
- 轮播箭头位置

---

## 7. 首页最简模块拆分

这次只做首页，建议不要拆太细。

最实用的结构不再是“先整块首页 section”，而是“先卡片、再卡片组、再页面”。

## 7.1 第一层：先定义可复刻的单卡片

这一层只解决一个问题：

**每一张卡片本身先做得和原站完全一致。**

建议先抽出这些基础卡片：

### A. `card-image-cta.liquid`

负责：

- 背景图卡片
- 标题
- 按钮/链接
- hover 效果

适用于：

- 首页产品推荐卡
- 分类入口大图卡
- CTA 图卡

### B. `card-icon-feature.liquid`

负责：

- 图标
- 标题
- 描述
- 小型链接

适用于：

- 优势说明卡
- 工厂能力卡
- 图标卖点卡

### C. `card-video-cover.liquid`

负责：

- 视频封面
- 播放按钮
- 标题/说明

适用于：

- 首页视频故事卡
- 工厂视频介绍卡

### D. `card-blog-post.liquid`

负责：

- 文章缩略图
- 标题
- 摘要
- Read more

适用于：

- 首页博客推荐

### E. `card-testimonial.liquid`

负责：

- 客户图片
- 评价内容
- 轮播项样式

适用于：

- 客户评价轮播

### F. `card-timeline-item.liquid`

负责：

- 年份
- 标题
- 描述
- 时间线节点样式

适用于：

- 公司故事 / 时间线

### G. `card-process-slide.liquid`

负责：

- 工艺图
- 标题
- 轮播单项比例

适用于：

- 生产流程轮播

---

## 7.2 第二层：用卡片组成 section

当单卡片都复刻准确后，再组装成 section。

### 7.2.1 `header.liquid`

负责：

- logo
- 一级导航
- Mega Menu
- sticky header
- mobile menu

### 7.2.2 `home-hero.liquid`

负责：

- 视频背景 / 背景图
- 标题
- 文案
- CTA

### 7.2.3 `section-card-grid.liquid`

内部调用：

- [`card-image-cta.liquid`](docs/replication_home.md)
- [`card-icon-feature.liquid`](docs/replication_home.md)

用于：

- fabric 类别区
- bedding 类别区
- 图片卡 / 图标卡区

### 7.2.4 `section-feature-group.liquid`

内部调用：

- [`card-icon-feature.liquid`](docs/replication_home.md)

用于：

- 工厂优势
- compare 区
- 能力说明卡

### 7.2.5 `section-video-story-group.liquid`

内部调用：

- [`card-video-cover.liquid`](docs/replication_home.md)

用于：

- 视频封面
- 播放按钮
- 图文左右排版

### 7.2.6 `section-carousel-group.liquid`

内部调用：

- [`card-process-slide.liquid`](docs/replication_home.md)
- [`card-testimonial.liquid`](docs/replication_home.md)
- 需要时也可调用 [`card-image-cta.liquid`](docs/replication_home.md)

用于：

- 生产流程轮播
- 客户评价轮播
- 推荐图片区

建议做成一个通用轮播 section，通过设置切换样式。

### 7.2.7 `section-timeline.liquid`

内部调用：

- [`card-timeline-item.liquid`](docs/replication_home.md)

用于：

- 品牌历史
- 年份节点
- 文字卡片

### 7.2.8 `section-blog-grid.liquid`

内部调用：

- [`card-blog-post.liquid`](docs/replication_home.md)

用于：

- 首页文章推荐卡片

### 7.2.9 `home-cta-banner.liquid`

负责：

- 最终转化区
- 按钮
- 联系引导

### 7.2.10 `footer.liquid`

负责：

- 页脚导航
- 联系方式
- 社媒

---

## 7.3 第三层：最后再组合成首页

最后一步才是把这些 section 按首页顺序拼起来：

1. Header
2. Hero
3. 分类卡片组
4. 优势卡片组
5. 视频卡片组
6. 流程轮播组
7. 评价轮播组
8. 时间线组
9. 博客组
10. CTA
11. Footer

这样首页的构建逻辑会非常清晰：

- 单卡片准确
- 卡片组稳定
- 页面最终组合自然成立

---

## 8. 最简单、最稳的首页实现方式

如果只求首页外观一致，建议按下面方法做：

## 8.1 内容先写死一部分

比如：

- 首页大标题
- CTA 文案
- 工厂优势文案
- 时间线内容
- 博客区标题

因为目标是首页快速复刻，没必要一开始就做成很复杂的后台可编辑系统。

## 8.2 图片统一先放 Shopify Files

把首页用到的图片统一上传到 Shopify Files，再在 section 中调用。

## 8.3 视频只做前台表现

Hero 视频和内容视频，不需要还原 WordPress 插件逻辑，只要：

- 封面图一致
- 播放逻辑一致
- 尺寸比例一致

即可。

## 8.4 轮播统一用一套 JS

因为原站用了 Swiper 逻辑，首页复刻也建议只保留一套轮播实现。

只需要支持：

- 自动播放
- 左右箭头
- bullets
- 响应式每屏数量变化

---

## 9. 一步一步开发顺序

这是调整后的、最适合首页复刻的顺序：**先卡片，后组合。**

## 第 1 步：起 Dawn 主题

```bash
shopify theme init perfectextile-home --clone-url https://github.com/Shopify/dawn
shopify theme dev
```

## 第 2 步：先做全局样式层

先建立：

- 颜色变量
- 字体变量
- 按钮样式
- 卡片圆角
- 阴影
- container 宽度
- 通用标题样式
- 通用卡片间距

这一步非常关键，因为后面所有卡片都依赖它。

## 第 3 步：先一张一张复刻基础卡片

建议顺序：

1. 图片 CTA 卡
2. 图标优势卡
3. 视频封面卡
4. 博客卡
5. 评价卡
6. 时间线卡
7. 流程轮播卡

每做完一张卡片，就单独对照原站截图或源码检查：

- 尺寸比例
- 字体
- 间距
- 边框/阴影
- hover
- 图片裁切

## 第 4 步：再做 Header 和 Footer

原因：

- 这是首页骨架
- 做完后页面结构会稳定
- 后续组合卡片时更容易观察整体效果

## 第 5 步：做 Hero

优先还原：

- 高度
- 视频背景
- 文案位置
- 按钮样式
- 遮罩层

## 第 6 步：把卡片组合成分类区和优势区

这一步不是新做视觉，而是把前面已经做好的卡片按首页结构排版组合。

重点关注：

- 卡片列数
- 卡片组间距
- 区块标题与卡片组关系
- 桌面/移动端排列

## 第 7 步：把卡片组合成视频区和轮播区

包括：

- 视频故事区
- 流程轮播
- 评价轮播
- 推荐图片区

## 第 8 步：把卡片组合成时间线和博客区

这一步重点是节奏与留白，不是重新设计单卡。

## 第 9 步：最后把所有 section 拼成首页

按首页顺序组合：

- Header
- Hero
- 分类卡片组
- 优势卡片组
- 视频卡片组
- 轮播组
- 时间线组
- 博客组
- CTA
- Footer

## 第 10 步：整页统一微调

包括：

- 按钮色
- 图标
- 区块上下间距
- 轮播箭头
- 卡片阴影
- hover 动效
- 页面节奏一致性

---

## 10. 视觉 1:1 复刻重点检查表

开发完成后，只检查首页这些项：

### Header

- logo 大小是否一致
- 导航字重是否一致
- sticky 后高度是否一致
- 下拉菜单宽度是否一致

### Hero

- 首屏高度是否一致
- 视频位置是否一致
- 标题换行是否一致
- CTA 颜色与圆角是否一致

### 内容区

- section 上下间距是否一致
- 卡片圆角是否一致
- 图片比例是否一致
- 标题字号是否一致
- 文本颜色层级是否一致

### Carousel

- 每屏显示数量是否一致
- 箭头位置是否一致
- pagination 样式是否一致
- 自动滚动节奏是否一致

### Footer

- 列布局是否一致
- 社媒图标风格是否一致
- 留白与分割是否一致

---

## 11. 最务实的简化建议

如果本次只追求“首页看起来一样”，建议直接采用下面策略：

- 首页只做一个模板
- 先不做复杂 Metaobject
- 先不做全站完整 CMS 架构
- 先抽最小可复用卡片
- 一张一张把卡片外观做准
- 再把卡片组合成 section
- 最后把 section 拼成首页
- 先把桌面端做准，再修平板和手机

这样效率最高，也最适合你现在要的工作方式：**先逐卡复刻，再整页组合。**

---

## 12. 最终建议

一句话方案：

**使用 Shopify CLI 基于 Dawn 启动主题，只复刻 [`perfectextile 首页`](assets/perfectextile.com/index.html)，但开发顺序改为先逐张复刻卡片，再把卡片组装成分类区、优势区、视频区、轮播区、时间线区、博客区，最后再组合成完整首页，以这种“卡片优先”的方式完成首页视觉 1:1 还原。**
