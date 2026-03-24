分析出 home 的所有模块，结构用于设计总体框架，图片主要用于视觉上的 1:1 复刻。

# Home 模块结构分析

## 1. 目的

本文件基于首页截图与页面复刻目标，整理出 home 的完整模块结构。

作用分为两层：

1. 结构层：用于搭建 Shopify 首页总体框架，明确 section 顺序、层级和组件关系。
2. 视觉层：截图主要用于 1:1 复刻时对齐版式、间距、字号、卡片比例、配色和图片裁切方式。

---

## 2. 页面整体结构

首页可以拆成以下模块顺序：

1. Header / 顶部导航
2. Hero 首屏横幅
3. 工厂数据统计 + 双工厂展示
4. 新疆优势对比区
5. 面料分类入口区
6. 成品床品展示区
7. Why Choose Us 卖点区
8. 生产流程轮播区
9. 客户评价区
10. 公司历史时间线区
11. 证书展示区
12. 全球客户背书 CTA 区
13. Blog & News 文章区
14. Footer 顶部 CTA 横幅
15. Footer 页脚信息区
16. 悬浮工具（语言、WhatsApp、聊天）

---

## 3. 模块逐块拆解

## 3.1 Header / 顶部导航

参考截图：[`home-full-page-overview.png`](assets/screenshot/home-full-page-overview.png)、[`home-hero-banner.png`](assets/screenshot/home-hero-banner.png)

### 结构

- 左侧 Logo
- 中间主导航
- 导航包含下拉入口：Bedding Fabric、Bedding、About
- 右侧主 CTA 按钮 Get A Quote
- 整体为白底横向导航栏

### 复刻重点

- 导航高度偏紧凑，偏企业站风格
- Logo 左对齐，导航居中偏右
- CTA 按钮为描边圆角样式
- Header 具有 sticky 观感，滚动时仍固定在顶部

---

## 3.2 Hero 首屏横幅

参考截图：[`home-hero-banner.png`](assets/screenshot/home-hero-banner.png)

### 结构

- 全宽背景媒体区，当前表现为工厂视频/大图背景
- 深色遮罩层
- 主标题
- 橙色强调副标题
- 多条卖点文案列表
- 分隔装饰线
- 主按钮 Quote Now

### 复刻重点

- 首屏高度较高，接近沉浸式 banner
- 标题为页面最强视觉焦点
- 白字 + 橙色强调字形成品牌识别
- 内容整体左对齐，但位于版心内部
- 背景不是普通静态图观感，而是偏视频封面/动态背景

---

## 3.3 工厂数据统计 + 双工厂展示

参考截图：[`home-factory-stats-and-sites.png`](assets/screenshot/home-factory-stats-and-sites.png)

### 结构

- 上部为 4 个数据卡片
  - Years Experience
  - Meters Annual Output
  - Factory Floor Space
  - Countries Ground The World
- 下部为 2 个工厂展示卡
  - 工厂图片
  - 中间播放按钮
  - 下方地址说明

### 复刻重点

- 数据卡片为浅色背景卡片，带阴影和底部橙色短横线
- 四卡横排，强调数字权重
- 下方双工厂卡片视觉尺寸较大
- 视频播放按钮是重要视觉记忆点
- 卡片圆角、阴影、留白都比较明显

---

## 3.4 新疆优势对比区

参考截图：[`home-xinjiang-factory-comparison.png`](assets/screenshot/home-xinjiang-factory-comparison.png)

### 结构

- 左侧：标题 + 简介 + 中国地图示意
- 右侧：对比表格式卡片组
  - Traditional Factory
  - Xinjiang Factory
- 对比维度包含：
  - Energy Efficiency
  - Supply Chain Structure
  - Logistics & Lead Time
  - Traceability & Quality
  - Manufacturing Model

### 复刻重点

- 左右双栏布局
- 右侧每一行都是一组对比卡片
- 橙色卡片代表优势方，白色卡片代表普通方案
- 中间多处出现 VS 强化对比关系
- 此模块是首页中信息密度最高的内容区之一

---

## 3.5 面料分类入口区

参考截图：[`home-bedding-fabric-categories.png`](assets/screenshot/home-bedding-fabric-categories.png)

### 结构

- 区块标题：Choose Your Competitive Bedding Textile Now!
- 8 个分类卡片网格：
  - Microfiber Textile
  - Recycled Textile
  - Satin Textile
  - Functional Textile
  - Seesucker
  - Waffle Textile
  - Clipped Textile
  - Tufed Textile
- 底部双按钮：Quote Now / Request A Full Catalog

### 复刻重点

- 标题居中，下面带橙色横线
- 卡片为统一比例图片卡 + 下方标题
- 采用 4 列网格布局
- 单卡内部是拼图式合成视觉，不是单一纯图
- 是后续 collection/category section 的核心参考模块

---

## 3.6 成品床品展示区

参考截图：[`home-finished-bedding-products.png`](assets/screenshot/home-finished-bedding-products.png)

### 结构

- 标题：We Also Offer Finished Bedding
- 6 个产品卡片：
  - Bed Sheet Sets
  - Bedspread Sets
  - Comforter Sets
  - Duvet Cover Sets
  - Quilts Sets
  - Ultrasonic Sets
- 底部双按钮：Quote Now / Request A Full Catalog

### 复刻重点

- 3 列网格布局
- 卡片更加简洁，以产品抠图为主
- 背景浅色，图片主体占比较大
- 与上一个面料分类区形成“原料/面料”与“成品/套件”两个层级

---

## 3.7 Why Choose Us 卖点区

参考截图：[`home-why-choose-us-benefits.png`](assets/screenshot/home-why-choose-us-benefits.png)

### 结构

- 背景大图（床品生活方式图）
- 居中标题与说明
- 下方 4 个卖点列：
  - Competitive Price
  - High Quality
  - On-Time Delivery
  - Perfect Service
- 每列包含图标、标题、描述列表

### 复刻重点

- 整区有深色遮罩
- 文案居中，卖点四列横排
- 图标采用橙色线性图标风格
- 模块承担品牌说服作用，视觉更像品牌宣言区

---

## 3.8 生产流程轮播区

参考截图：[`home-production-process.png`](assets/screenshot/home-production-process.png)

### 结构

- 标题：Perfectextile Production Process
- 一段说明文案
- 多张流程图片轮播
- 每张卡片包含步骤图和步骤名
  - DTY Process
  - Beam-Warping
  - Water Jet Weaving Machine
  - Lab Preparation Of Dyes
- 下方轮播分页点

### 复刻重点

- 这是典型 carousel section
- 图片卡片尺寸较大，标题在图下方
- 页面中部居中布局，留白明显
- 后续需要支持滑动/切换，而不是静态网格

---

## 3.9 客户评价区

参考截图：[`home-testimonials.png`](assets/screenshot/home-testimonials.png)

### 结构

- 左侧：Testimonials 标题、正文、按钮
- 右侧：手机聊天截图轮播/3D Carousel
- 下方可见时间轴模块的起始部分

### 复刻重点

- 左文右图布局
- 右侧不是普通卡片轮播，而是带透视层叠效果的 carousel
- 按钮为橙色实心按钮
- 此区块重点是“真实聊天截图”带来的信任感

---

## 3.10 公司历史时间线区

参考截图：[`home-company-history.png`](assets/screenshot/home-company-history.png)

### 结构

- 左侧：Company History 标题、长段介绍、View More 按钮
- 右侧上部：时间线年份节点
  - 2004
  - 2007
  - 2012
  - 2016
- 右侧下部：对应年份内容卡片
  - 图片
  - 标题
  - 描述

### 复刻重点

- 左文右时间线的非对称布局
- 时间轴横向展开，节点样式明显
- 卡片为白底内容卡，图文上下排布
- 是品牌故事模块，不仅是普通资讯列表

---

## 3.11 证书展示区

参考截图：[`home-certificates.png`](assets/screenshot/home-certificates.png)

### 结构

- 标题：CERTIFICATE
- 证书图片网格
- 上下两排排列展示多个证书/专利文件

### 复刻重点

- 模块结构简单，但图片展示要求高
- 卡片之间边距统一
- 需要保证证书图片足够清晰，边框感明显
- 适合做纯 gallery/grid section

---

## 3.12 全球客户背书 CTA 区

参考截图：[`home-global-customers-cta.png`](assets/screenshot/home-global-customers-cta.png)

### 结构

- 背景为客户合影拼图墙
- 中央叠加深色遮罩内容层
- 标题：Customers From All Over The World Have Affirmed Us
- 一段说明文案
- 按钮：Get Started

### 复刻重点

- 背景不是单图，而是拼贴式客户照片矩阵
- 前景文案居中覆盖在背景上
- 这是强转化型 CTA 模块
- 需要处理背景层、遮罩层、内容层三层结构

---

## 3.13 Blog & News 文章区

参考截图：[`home-blog-news.png`](assets/screenshot/home-blog-news.png)

### 结构

- 左上标题区：Blog & News / Articles About Perfectextile
- 右上按钮：View More
- 下部 3 张文章卡片
  - 文章封面
  - 日期
  - 标题
  - 摘要
  - Read More

### 复刻重点

- 头部为左标题右按钮布局
- 下方 3 列博客卡片
- 卡片阴影明显，信息层级标准
- 后续适合映射为 blog article card 组件

---

## 3.14 Footer 顶部 CTA 横幅

参考截图：[`home-footer-cta-and-footer.png`](assets/screenshot/home-footer-cta-and-footer.png)

### 结构

- 大幅床品背景图
- 标题：Ready To Choose Us? Fabric And Bedding
- 多行简短说明文案
- 中间按钮：Quote Now

### 复刻重点

- 是 footer 上方独立 CTA，不应直接并入页脚链接区
- 大图背景 + 中央文字覆盖
- 视觉上承担“页面收口前最后一次转化”作用

---

## 3.15 Footer 页脚信息区

参考截图：[`home-footer-cta-and-footer.png`](assets/screenshot/home-footer-cta-and-footer.png)

### 结构

- 左侧品牌简介
- 社媒图标
- Links 列
- More Products 列
- Contact Info 多列地址与联系方式
- 底部版权信息

### 复刻重点

- 多列信息布局
- 联系方式信息量大，需要控制好排版节奏
- Footer 不是极简型，而是企业资料型页脚
- 适合作为独立 footer section + blocks 实现

---

## 3.16 悬浮工具

参考截图：几乎所有截图均可见，例如 [`home-hero-banner.png`](assets/screenshot/home-hero-banner.png)

### 结构

- 右侧悬浮语言切换按钮
- 右下角 WhatsApp 按钮
- 右下角聊天按钮
- 底部语言条 English

### 复刻策略建议

- 若本次目标以首页主体 1:1 为先，可先做视觉占位
- 不必优先实现完整第三方功能
- 但位置、尺寸、悬浮方式建议保留，以保证截图对比一致性

---

## 4. 推荐的总体框架层级

建议把首页按以下层级组织：

### Level 1：页面骨架

- Header
- Main Content
- Footer
- Floating Tools

### Level 2：Main Content 的 section 顺序

1. Hero Banner
2. Factory Stats & Sites
3. Xinjiang Comparison
4. Bedding Fabric Categories
5. Finished Bedding Products
6. Why Choose Us
7. Production Process Slider
8. Testimonials
9. Company History Timeline
10. Certificates Gallery
11. Global Customers CTA
12. Blog News
13. Footer CTA Banner

### Level 3：可复用组件

- 导航项
- CTA 按钮
- 数据统计卡
- 工厂展示卡
- 对比信息卡
- 分类卡片
- 产品卡片
- 图标卖点卡
- 流程轮播卡
- 评价轮播卡
- 时间线卡片
- 证书图片卡
- 博客卡片
- Footer 信息列

---

## 5. 对 1:1 复刻最关键的视觉要点

截图主要用于视觉还原，因此以下内容优先级最高：

### 5.1 布局节奏

- 每个 section 的上下留白
- 标题区与内容区的距离
- 网格列数与卡片间距
- 版心宽度与内容对齐方式

### 5.2 卡片样式

- 圆角大小
- 阴影强度
- 边框有无
- 图片裁切比例
- 文案与按钮在卡片中的位置

### 5.3 品牌视觉

- 白底 + 浅米色背景交替
- 主品牌橙色按钮/强调线/标题强调字
- 深色文字标题 + 清晰层级
- 企业站偏可信赖、偏外贸展示的视觉语气

### 5.4 交互外观

- 轮播分页点
- 箭头位置
- 播放按钮样式
- 悬浮按钮位置
- Header 固定效果

---

## 6. 对后续 Shopify section 设计的建议

如果后续用于 Shopify 复刻，建议直接按下面的 section 思路落地：

- hero-banner
- factory-stats-sites
- xinjiang-comparison
- fabric-category-grid
- finished-bedding-grid
- why-choose-us
- production-process-slider
- testimonials-carousel
- company-history-timeline
- certificates-gallery
- global-customers-cta
- blog-news-grid
- footer-cta-banner
- site-footer

这样结构层和截图模块可以一一对应，后续视觉比对和组件复用都会更稳定。
