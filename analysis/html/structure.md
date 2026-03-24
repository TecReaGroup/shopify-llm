# perfectextile 首页 body 结构详细拆解

本文基于 [`assets/perfectextile.com/index.html`](assets/perfectextile.com/index.html) 中 `<body ...>` 内部真实结构，自上而下整理首页模块、卡片、关键 DOM、关键样式与交互特征，目标是服务 **Shopify 1:1 复刻**，尤其适合“先逐卡复刻，再组合成页面”的开发方式。

---

## 1. 分析范围

首页主内容起点可从 [`<body>`](assets/perfectextile.com/index.html:428) 开始，实际页面骨架从 [`#page`](assets/perfectextile.com/index.html:450) 展开，顺序大致为：

1. 顶部 Header / Mega Menu
2. Hero 视频首屏
3. 数据统计条
4. 工厂视频卡片组
5. Xinjiang 对比说明与热点地图
6. 核心供应能力说明卡
7. Textile 分类推荐卡组
8. Bedding 成品推荐卡组
9. Why choose us 图标优势区
10. Production process 轮播
11. Testimonials 评价轮播
12. Company History 时间线
13. Certificate 证书画廊
14. Ready to choose us 文案 CTA
15. Blog & News 文章卡片
16. 最终 CTA 区
17. Footer
18. 浮动语言切换 / 回到顶部 / WhatsApp / Popup

---

## 2. 全局视觉基调

虽然本文件重点在 body 结构，但首页模块的 1:1 复刻必须先理解全局视觉变量。

### 2.1 全局主色

可从 [`Astra/WooCommerce 内联样式`](assets/perfectextile.com/index.html:77) 和 [`提取颜色`](assets/perfectextile.com/extracted_colors.json) 归纳：

- 品牌主橙：`#FF8C00`
- 深橙 hover：`#E67600`
- 主背景：`#FFFFFF`
- 深文本：`#000000`
- 次文本：`#555555` / `#666666`
- 浅灰背景：`#F3F3F3` / `#F5F5F5`
- 边框灰：`#EAEAEA` / `#EEEEEE`
- 局部蓝色按钮/表单色：`#066AAB`、`#003399`
- WhatsApp 绿：`#25D366`

### 2.2 断点

关键响应式断点可以参考 [`Astra 断点`](assets/perfectextile.com/index.html:141) 与 [`scroll top 样式`](assets/perfectextile.com/index.html:58)：

- `921px` 是明显的 header / layout 切换断点
- 移动端存在独立 DOM 分支，不只是 CSS 折叠

### 2.3 字体风格

参考 [`提取字体`](assets/perfectextile.com/extracted_fonts.json)：

- 页面主要视觉字体倾向 `Plus Jakarta Sans`
- 正文常混用 `Open Sans` / `Roboto`
- 部分 HTML 模块直接强制 `Arial, Helvetica, sans-serif`
- 标题普遍粗体，正文偏中等字重，卡片文案简短直接

---

## 3. body 起始前置元素

在正式视觉内容前，body 内先出现几个非内容型元素：

### 3.1 第三方脚本

- okki analytics：[`window.okkiConfigs`](assets/perfectextile.com/index.html:429)
- GTM noscript iframe：同一位置附近

这类内容 Shopify 复刻时一般不作为 section，而是全局脚本配置。

### 3.2 Skip link

- 跳至内容链接：[`skip-link`](assets/perfectextile.com/index.html:448)

复刻时建议保留，属于可访问性结构。

---

## 4. Header 模块

Header 起点见 [`header`](assets/perfectextile.com/index.html:451)。

## 4.1 Header 容器

外层容器：[`elementor-element-6d2a3bfb`](assets/perfectextile.com/index.html:452)

关键特征：

- `background_background: classic`
- `sticky: top`
- sticky 作用于桌面、平板、移动端
- 是全站统一头部库，不只是首页私有区块

### 复刻要点

- 头部固定吸顶
- 默认白底或近白底
- 高度稳定
- 左 logo，中间主导航，右侧 CTA 按钮

## 4.2 Logo

Logo 位于 [`theme-site-logo`](assets/perfectextile.com/index.html:455)。

图片资源：[`logo img`](assets/perfectextile.com/index.html:457)

特征：

- 宽 380，高 82
- 使用黑白简洁 logo
- 支持 1x / 2x 资源切换

## 4.3 主导航

导航主体在 [`elementor-widget-n-menu`](assets/perfectextile.com/index.html:461)。

一级菜单实际可见节点：

- HOME：[`HOME`](assets/perfectextile.com/index.html:471)
- BEDDING FABRIC：[`BEDDING FABRIC`](assets/perfectextile.com/index.html:477)
- BEDDING：[`BEDDING`](assets/perfectextile.com/index.html:803)
- ABOUT：[`ABOUT`](assets/perfectextile.com/index.html:857)
- WHY CHOOSE：[`WHY CHOOSE`](assets/perfectextile.com/index.html:885)
- BLOG：[`BLOG`](assets/perfectextile.com/index.html:891)
- CONTACT：[`CONTACT`](assets/perfectextile.com/index.html:897)

### 样式/交互特征

- 水平导航
- 二级菜单带上下 caret 图标
- 移动端按钮：[`menu-toggle`](assets/perfectextile.com/index.html:463)
- 桌面下拉是 Mega Menu，不是普通下拉列表

## 4.4 Mega Menu：Bedding Fabric

Mega Menu 开始于 [`e-n-menu-content-2902`](assets/perfectextile.com/index.html:491)。

这个下拉本身就是一个复杂页面区块，包含：

### A. Recent Products 小卡片

标题：[`Recent Products`](assets/perfectextile.com/index.html:499)

两张 CTA 图卡：

- Tufted fabric：[`Tufted fabric`](assets/perfectextile.com/index.html:501)
- waffle fabric：[`waffle fabric`](assets/perfectextile.com/index.html:516)

卡片特征：

- 纯背景图覆盖
- 蒙层 `elementor-cta__bg-overlay`
- 文字叠加在底部/中部
- hover 动效来自 `elementor-animated-content`

### B. 一级分类图标卡 + 子链接列表

第一组：[`microfiber polyester`](assets/perfectextile.com/index.html:533)

子链接：

- white fabric：[`white fabric`](assets/perfectextile.com/index.html:555)
- Dyed Fabric：[`Dyed Fabric`](assets/perfectextile.com/index.html:564)
- Embossed Fabric：[`Embossed Fabric`](assets/perfectextile.com/index.html:573)
- 3D Embossed Fabric：[`3D Embossed Fabric`](assets/perfectextile.com/index.html:582)

第二组：[`printed polyester fabric`](assets/perfectextile.com/index.html:594)

子链接：

- Pigment Printed Fabric：[`Pigment Printed Fabric`](assets/perfectextile.com/index.html:616)
- Nano Printing Fabric：[`Nano Printing Fabric`](assets/perfectextile.com/index.html:625)
- Disperse Printing Fabric：[`Disperse Printing Fabric`](assets/perfectextile.com/index.html:634)
- Digital Printing Fabric：[`Digital Printing Fabric`](assets/perfectextile.com/index.html:643)

第三组：[`SATIN FABRIC`](assets/perfectextile.com/index.html:656)

子链接：

- glossy satin：[`glossy satin`](assets/perfectextile.com/index.html:679)
- matte satin：[`matte satin`](assets/perfectextile.com/index.html:688)

第四组：[`recyled FABRIC`](assets/perfectextile.com/index.html:700)

第五组：[`functional fabric`](assets/perfectextile.com/index.html:719)

子链接：

- waterproof：[`waterproof`](assets/perfectextile.com/index.html:741)
- Antibacterial fabric：[`Antibacterial fabric`](assets/perfectextile.com/index.html:750)
- ultrasonic fabric：[`ultrasonic fabric`](assets/perfectextile.com/index.html:759)
- quilted fabric：[`quilted fabric`](assets/perfectextile.com/index.html:768)

### C. 下拉底部 CTA

- 文案：[`Do you want more products?`](assets/perfectextile.com/index.html:782)
- 按钮：[`Contact Us`](assets/perfectextile.com/index.html:784)
- 装饰图：[`non-woven-fabric-roll`](assets/perfectextile.com/index.html:791)

### Mega Menu 复刻建议

这个区域不建议简单当菜单，而应按“**一个下拉里的小型 landing page**”来复刻。

可拆卡片：

- `card-image-cta`
- `card-icon-category`
- `card-link-list`
- `card-aside-cta`

## 4.5 Mega Menu：Bedding

第二个 mega menu 起点见 [`e-n-menu-content-2903`](assets/perfectextile.com/index.html:817)。

内容相对简单，主要是文字链接块：

- bedding sets：[`bedding sets`](assets/perfectextile.com/index.html:824)
- Duvet covers：[`Duvet covers`](assets/perfectextile.com/index.html:828)
- pillowcase：[`pillowcase`](assets/perfectextile.com/index.html:832)
- Ultrasonic sets：[`Ultrasonic sets`](assets/perfectextile.com/index.html:838)
- comforters：[`comforters`](assets/perfectextile.com/index.html:842)
- Quilts：[`Quilts`](assets/perfectextile.com/index.html:846)

特征：

- 不是图卡，而是竖向文字分类
- 白底 + 简约间距
- hover 重心在文字链接

## 4.6 Mega Menu：About

起点：[`e-n-menu-content-2904`](assets/perfectextile.com/index.html:871)

子链接：

- Company History：[`Company History`](assets/perfectextile.com/index.html:873)
- Global network：[`Global network`](assets/perfectextile.com/index.html:877)

## 4.7 Header 右侧按钮

按钮见 [`Get A Quote`](assets/perfectextile.com/index.html:909)

特征：

- 桌面可见，平板/手机隐藏
- 点击触发 popup 22222
- 是高优先级 CTA，建议在 Shopify header 中保留

---

## 5. Hero 首屏模块

Hero 起点：[`elementor-element-5f19a6e2`](assets/perfectextile.com/index.html:936)

## 5.1 背景

- 背景类型：video
- 视频链接：[`background_video_link`](assets/perfectextile.com/index.html:936)
- 视频容器：[`elementor-background-video-container`](assets/perfectextile.com/index.html:937)

### 视觉特征

- 桌面端视频背景
- 移动端大概率降级为非视频表现
- 文案居中偏左，整体是大面积品牌叙事首屏

## 5.2 Hero 文案结构

主标题：[`h1`](assets/perfectextile.com/index.html:941)

内容为两行：

- `Redefining Polyester: From Fiber to Finish home beddings.`
- `Driving Textile Competitiveness Through Xinjiang’s Energy Edge`

辅助文案：

- 20 年经验：[`manufacturing vendor with over 20year experience`](assets/perfectextile.com/index.html:945)
- 垂直整合：[`vertifical setup...`](assets/perfectextile.com/index.html:947)
- 认证：[`OEKO-TEX 100 , GRS`](assets/perfectextile.com/index.html:949)
- 海外与中国花型设计：[`pattern designers...`](assets/perfectextile.com/index.html:951)

分隔线：[`pattern divider`](assets/perfectextile.com/index.html:953)

主按钮：[`quote now`](assets/perfectextile.com/index.html:959)

### Hero 样式要点

- 标题白色
- 文字层级明确
- 有图案 divider，不是纯直线
- 按钮带左侧 icon：[`fa-angle-double-right`](assets/perfectextile.com/index.html:962)

---

## 6. 首屏后统计条

桌面统计区起点：[`xs_fun_13`](assets/perfectextile.com/index.html:982)

移动统计区起点：[`mobile xs_fun_13`](assets/perfectextile.com/index.html:1102)

### 统计卡 4 张

1. Years experience：[`21`](assets/perfectextile.com/index.html:990)
2. meters annual output：[`80M+`](assets/perfectextile.com/index.html:1017)
3. factory floor space：[`66780m2`](assets/perfectextile.com/index.html:1044)
4. countries ground the world：[`50+`](assets/perfectextile.com/index.html:1072)

### 样式特征

- `elementskit-funfact`
- `style-border-bottom`
- 数字 odometer 动画
- 桌面 4 列
- 移动端改为纵向堆叠独立卡
- 局部竖向分隔线：[`vertical-bar`](assets/perfectextile.com/index.html:1047)

### 复刻建议

这块适合做成统一 `card-stat`，先做一张，再复制 4 次。

---

## 7. 工厂视频卡片组

这一段是首页非常核心的“工厂实力视频卡片组”，从 [`elementor-element-539fdca2`](assets/perfectextile.com/index.html:1206) 开始。

它不是一个单区块，而是多张带错位变换的媒体卡。

## 7.1 视频卡 1：Zhejiang 工厂

视频卡：[`video 1`](assets/perfectextile.com/index.html:1211)

- YouTube：`o7R812yHz-k`
- 封面：[`zhejiang-factory-2.png`](assets/perfectextile.com/index.html:1211)
- 播放按钮在封面中心：[`custom-embed-play`](assets/perfectextile.com/index.html:1214)

附属地址信息卡：[`Factory1...`](assets/perfectextile.com/index.html:1220)

- 图标：地图 pin
- 地址文字：[`Factory1`](assets/perfectextile.com/index.html:1231)

## 7.2 视频卡 2：Workshop / Female textile workers

移动版见 [`video 2 mobile`](assets/perfectextile.com/index.html:1273)

- YouTube：`d6SvWzPXCIY`
- 封面：[`workshop-21.jpg`](assets/perfectextile.com/index.html:1273)

## 7.3 视频卡 3：Xinjiang 工厂

桌面版：[`video 3`](assets/perfectextile.com/index.html:1317)

- YouTube：`TlhDNVHcoPs`
- 封面：[`xinjiang-factory-1.jpg`](assets/perfectextile.com/index.html:1317)

附属地址卡：[`Factory2`](assets/perfectextile.com/index.html:1326)

## 7.4 视频卡 4：通用工厂视频

- 视频：[`dFmlZwbLA3M`](assets/perfectextile.com/index.html:1723)
- 该卡更多承担叙事与品牌氛围作用

### 样式特征

- 大量 `transform translateX / translateY`
- 卡片有交错位移，形成拼贴感
- 视频是封面图 + 点击播放，不是直接加载 iframe
- 附带 icon-box 地址说明
- 部分区域有社媒竖排按钮，但很多桌面版本被隐藏

### 复刻建议

先拆成：

- `card-video-cover`
- `card-address-overlay`

然后再组合成左右交错 section。

---

## 8. Xinjiang 对比说明区

这一段从 [`elementor-element-680d4d8`](assets/perfectextile.com/index.html:1378) 开始，是首页最“自定义 HTML 化”的内容之一。

## 8.1 标题区

标题 HTML：[`compare-header`](assets/perfectextile.com/index.html:1381)

自带内联样式：[`factory-compare style`](assets/perfectextile.com/index.html:1383)

关键样式：

- `max-width: 1200px`
- 标题字号：`34px`
- 高亮文字橙色：`#FF8C00`
- 副标题灰色：`#666`

文案：

- `Beyond Tradition: Why We Choose Xinjiang`
- `A strategic upgrade in energy, supply chain control, and intelligent manufacturing.`

## 8.2 热点地图

地图组件：[`elementskit-hotspot`](assets/perfectextile.com/index.html:1420)

地图图：[`xinjiang.png`](assets/perfectextile.com/index.html:1425)

热点：

- XINJIANG：[`XINJIANG`](assets/perfectextile.com/index.html:1428)
- ZHEJIANG：[`ZHEJIANG`](assets/perfectextile.com/index.html:1443)

视觉特征：

- 热点带 pulse 动画：[`pulse_1 / pulse_2`](assets/perfectextile.com/index.html:1438)
- 地图居中
- 地点标签覆盖在图上

## 8.3 对比表模块

第二段 HTML：[`compare-table`](assets/perfectextile.com/index.html:1463)

这里直接内联了一整套对比表 CSS，是 1:1 复刻时非常关键的样式来源。

### 样式核心

来自 [`内联 style`](assets/perfectextile.com/index.html:1465)：

- 表层背景：`rgba(255, 140, 0, 0.08)`
- 圆角：`16px`
- padding：`30px`
- 头部网格：`grid-template-columns: 1fr 80px 1fr`
- 高亮卡片：橙色渐变 `linear-gradient(135deg, #FF8C00, #ff9f2f)`
- 高亮阴影：`0 14px 40px rgba(255, 140, 0, 0.45)`
- 升级徽章：`STRATEGIC UPGRADE`
- 移动端在 `768px` 以下变单列

### 内容结构

表头：

- Traditional Factory：[`Traditional Factory`](assets/perfectextile.com/index.html:1615)
- Xinjiang Factory：[`Xinjiang Factory`](assets/perfectextile.com/index.html:1617)

5 行对比：

1. Energy Efficiency vs Unmatched Energy Advantage：[`row 1`](assets/perfectextile.com/index.html:1621)
2. Supply Chain Structure vs Fully Vertical Integration：[`row 2`](assets/perfectextile.com/index.html:1633)
3. Logistics & Lead Time vs Gateway to Eurasia：[`row 3`](assets/perfectextile.com/index.html:1647)
4. Traceability & Quality vs End-to-End Control：[`row 4`](assets/perfectextile.com/index.html:1660)
5. Manufacturing Model vs Industry 4.0 Smart Factory：[`row 5`](assets/perfectextile.com/index.html:1673)

### 复刻建议

这个模块最好单独做成 section，不要塞进通用富文本。

---

## 9. 核心供应能力说明区

从 [`elementor-element-f8f2d05`](assets/perfectextile.com/index.html:1691) 附近开始。

主要内容：

- 标题：[`polyester bedsheet fabric supplier`](assets/perfectextile.com/index.html:1695)
- 卖点列表：[`ul list`](assets/perfectextile.com/index.html:1705)
  - 3 Factories
  - 26780㎡
  - 150+ workers
  - 300+ textile equipment
  - 150000000+CNY GMV annual
- 按钮：[`consultation now`](assets/perfectextile.com/index.html:1709)

### 样式特征

- 左文右视频/图片结构
- 标题 + divider + 列表 + 按钮
- 旁边有视频卡，形成信息与媒体并列

---

## 10. Textile 分类推荐区

标题区：[`Choose your competitive bedding Textile now!`](assets/perfectextile.com/index.html:1810)

## 10.1 第一组卡片

4 张图形 CTA 卡：

- microfiber Textile：[`microfiber Textile`](assets/perfectextile.com/index.html:1825)
- recycled textile：[`recycled textile`](assets/perfectextile.com/index.html:1842)
- Satin Textile：[`Satin Textile`](assets/perfectextile.com/index.html:1861)
- functional textile：[`functional textile`](assets/perfectextile.com/index.html:1878)

## 10.2 第二组卡片

4 张新花型/工艺卡：

- seesucker：[`seesucker`](assets/perfectextile.com/index.html:1901)
- waffle Textile：[`waffle Textile`](assets/perfectextile.com/index.html:1918)
- clipped Textile：[`clipped Textile`](assets/perfectextile.com/index.html:1937)
- Tufed Textile：[`Tufed Textile`](assets/perfectextile.com/index.html:1954)

## 10.3 区域底部按钮组

- quote now：[`quote now`](assets/perfectextile.com/index.html:1976)
- request a full catalog：[`request a full catalog`](assets/perfectextile.com/index.html:1990)

### 样式特征

- 全部为 `call-to-action` 背景图卡
- 每张卡以图片为主体，文字很少
- 适合做 2x2 + 2x2 网格
- 按钮区单独一行，靠右/并列

### 复刻建议

这是非常典型的 `card-image-cta` 批量复刻区域。

---

## 11. Bedding 成品推荐区

标题：[`We also offer finished bedding`](assets/perfectextile.com/index.html:2015)

卡片共 6 张：

- Bed Sheet Sets：[`Bed Sheet Sets`](assets/perfectextile.com/index.html:2024)
- Duvet Cover Sets：[`Duvet Cover Sets`](assets/perfectextile.com/index.html:2041)
- Bedspread Sets：[`Bedspread Sets`](assets/perfectextile.com/index.html:2060)
- Quilts Sets：[`Quilts Sets`](assets/perfectextile.com/index.html:2077)
- Comforter Sets：[`Comforter Sets`](assets/perfectextile.com/index.html:2096)
- Ultrasonic Sets：[`Ultrasonic Sets`](assets/perfectextile.com/index.html:2113)

区域底部按钮组：

- quote now：[`quote now`](assets/perfectextile.com/index.html:2136)
- request a full catalog：[`request a full catalog`](assets/perfectextile.com/index.html:2150)

### 样式特征

- 跟 Textile 卡片区是同一视觉语言
- 大图、浅文字、卡片 hover 蒙层
- 适合桌面 3x2 / 平板 2 列 / 手机 1 列

---

## 12. Why choose us 优势区

桌面区起点：[`why choose us desktop`](assets/perfectextile.com/index.html:2160)

移动区起点：[`why choose us mobile`](assets/perfectextile.com/index.html:2270)

### 标题与说明

- 标题：[`Why choose us？`](assets/perfectextile.com/index.html:2169)
- 副标题：[`Competitive pricing...`](assets/perfectextile.com/index.html:2173)

### 4 个优势图标卡

图标：

1. best price：[`best-price-2.png`](assets/perfectextile.com/index.html:2178)
2. quality control：[`quality-control-1.png`](assets/perfectextile.com/index.html:2192)
3. on time：[`on-time-1.png`](assets/perfectextile.com/index.html:2206)
4. customer service：[`customer-service.png`](assets/perfectextile.com/index.html:2220)

对应文本：

1. Competitive price：[`Competitive price`](assets/perfectextile.com/index.html:2229)
2. High quality：[`High quality`](assets/perfectextile.com/index.html:2237)
3. On-time delivery：[`On-time delivery`](assets/perfectextile.com/index.html:2245)
4. Perfect service：[`Perfect service`](assets/perfectextile.com/index.html:2253)

每项都有 3 条 bullet 描述。

### 样式特征

- 图标和文字说明分栏排布
- 列之间有 divider
- 移动版改为图标+文字纵向块
- 这块不是卡片阴影风格，更接近“信息图表式布局”

### 复刻建议

先拆：

- `card-feature-icon`
- `card-feature-text`

再组合成桌面横向布局与移动纵向布局。

---

## 13. Production process 生产流程轮播

区块起点：[`Production process title`](assets/perfectextile.com/index.html:2366)

标题：[`Perfectextile production process`](assets/perfectextile.com/index.html:2374)

描述：[`Discover the craftsmanship...`](assets/perfectextile.com/index.html:2382)

轮播：[`media-carousel`](assets/perfectextile.com/index.html:2386)

### 配置特征

- `slides_per_view: 4`
- `autoplay: yes`
- `autoplay_speed: 5000`
- `space_between: 10px`
- 有 arrows + bullets

### 幻灯片图片

8 张流程图：[`swiper slides`](assets/perfectextile.com/index.html:2389)

图片名包括：

- 27.webp
- 29.webp
- 30.webp
- 32.webp
- 31.webp
- 33.webp
- 34.png
- 35.png

### 样式特征

- 图片直接以背景图方式铺满卡片
- 外层是标准 Swiper
- 左右箭头使用 `eicon-chevron-left/right`

---

## 14. Testimonials 评价轮播

标题区：[`Testimonials`](assets/perfectextile.com/index.html:2455)

副文案：

- `Reviews From Our Clients`：[`Reviews From Our Clients`](assets/perfectextile.com/index.html:2458)
- 介绍文字：[`At perfectextile...`](assets/perfectextile.com/index.html:2460)
- 按钮：[`Write an evaluation`](assets/perfectextile.com/index.html:2462)

轮播：[`coverflow carousel`](assets/perfectextile.com/index.html:2471)

### 配置特征

- `skin: coverflow`
- `autoplay: yes`
- `speed: 500`
- arrows + bullets
- 容器背景使用 gradient

### 评价卡图片

5 张评价图：

- client review-3：[`slide 1`](assets/perfectextile.com/index.html:2474)
- client review-5：[`slide 2`](assets/perfectextile.com/index.html:2480)
- client review-6：[`slide 3`](assets/perfectextile.com/index.html:2486)
- client review-2：[`slide 4`](assets/perfectextile.com/index.html:2492)
- client review-4：[`slide 5`](assets/perfectextile.com/index.html:2498)

### 复刻建议

这里不是传统文字 testimonial，而是“评价截图图片轮播”，复刻重点在：

- coverflow 表现
- 中间项突出
- 卡片圆角与阴影
- 箭头位置与 pagination 样式

---

## 15. Company History 时间线

标题区：[`Company History`](assets/perfectextile.com/index.html:2518)

介绍文案：[`Pengfei was founded...`](assets/perfectextile.com/index.html:2520)

按钮：[`View MORE`](assets/perfectextile.com/index.html:2522)

时间线组件：[`timeline-widget-addon`](assets/perfectextile.com/index.html:2536)

### 结构特征

- 横向时间线
- Swiper 滑动
- 每项包含：年份、大标签、小标签、图片、标题、描述

### 可见节点示例

- 2004 born：[`2004`](assets/perfectextile.com/index.html:2542)
- 2007 develop：同一行延续内容中可见

### 组件特征

- 上下结构：label / icon / arrow / content
- 自带 prev / next 按钮：[`twae-button-prev/next`](assets/perfectextile.com/index.html:2543)
- 有时间线水平线与填充线

### 复刻建议

适合拆成：

- `card-timeline-item`
- `section-timeline-slider`

---

## 16. Certificate 证书画廊

标题：[`CERTIFICATE`](assets/perfectextile.com/index.html:2560)

画廊一：[`gallery 1`](assets/perfectextile.com/index.html:2568)

画廊二：[`gallery 2`](assets/perfectextile.com/index.html:2590)

### 样式特征

- 布局：`justified`
- 理想行高：`430px`
- gap：`10px`
- 点击打开 lightbox
- overlay hover fade-in

### 图片内容

多张 certificate png 图片，采用两组 justified gallery 排列。

### 复刻要点

- 必须控制图片比例与行高，不能直接随意 masonry
- hover 遮罩轻微
- 建议 Shopify 用统一 gallery section 精确控制

---

## 17. Ready to choose us 文案 CTA 区

区块起点：[`Ready to choose us？`](assets/perfectextile.com/index.html:2618)

内容：

- 标题：[`Ready to choose us？`](assets/perfectextile.com/index.html:2620)
- 副标题：[`Customers from all over the world...`](assets/perfectextile.com/index.html:2622)
- 长段落：[`Thank you for your interest...`](assets/perfectextile.com/index.html:2624)
- 按钮：[`get started`](assets/perfectextile.com/index.html:2626)

### 样式特征

- 居中文案 CTA
- 比前面的图卡区更偏内容营销段落
- 按钮仍指向 popup

---

## 18. Blog & News 区

区块起点：[`Blog & News`](assets/perfectextile.com/index.html:2635)

### 标题区

- 主标题：[`Blog & News`](assets/perfectextile.com/index.html:2639)
- 副标题：[`Articles About Perfectextile`](assets/perfectextile.com/index.html:2640)
- 按钮：[`View More`](assets/perfectextile.com/index.html:2644)

### 文章卡 3 张

#### 卡 1

- 标题：[`What Is Geometric Pink 3D Embossed Fabric Bedding`](assets/perfectextile.com/index.html:2684)
- 日期：[`10/02/2026`](assets/perfectextile.com/index.html:2675)
- 摘要：[`Geometric Pink...`](assets/perfectextile.com/index.html:2688)
- 按钮：[`Read more`](assets/perfectextile.com/index.html:2691)

#### 卡 2

- 标题：[`What Makes Polyester Jacquard Fabric Bedding Unique in 2026`](assets/perfectextile.com/index.html:2722)
- 摘要：[`Polyester Jacquard...`](assets/perfectextile.com/index.html:2726)

#### 卡 3

- 标题：[`What Is Polyester Ultrasonic Fabric Bedding and How Is It Made`](assets/perfectextile.com/index.html:2760)
- 摘要：[`Polyester Ultrasonic...`](assets/perfectextile.com/index.html:2764)

### 卡片样式特征

- 上图下文
- 图片宽度充满卡片
- 日期带 calendar icon
- 标题是 `h2.entry-title`
- 底部 `Read more` 按钮
- 桌面 3 列布局

---

## 19. 最终 CTA 区

起点：[`xs_cta_style_22`](assets/perfectextile.com/index.html:2791)

标题：[`Ready to Choose Us? Fabric and bedding`](assets/perfectextile.com/index.html:2793)

描述列表：[`If you are also engaged...`](assets/perfectextile.com/index.html:2794)

按钮：[`quote now`](assets/perfectextile.com/index.html:2802)

### 样式特征

- 居中大标题
- 标题中 `Fabric and bedding` 高亮包裹在 span 中
- 带细长分隔线
- 多行短段落，像招商 CTA
- CTA 直接去 contact-us 页面

---

## 20. Footer 模块

Footer 起点：[`footer`](assets/perfectextile.com/index.html:2828)

## 20.1 左列：Logo + 简介 + 社媒

- logo：[`footer logo`](assets/perfectextile.com/index.html:2832)
- 简介：[`welcome cooperation`](assets/perfectextile.com/index.html:2836)
- 社媒列表：[`social list`](assets/perfectextile.com/index.html:2838)

社媒包含：

- Facebook：[`facebook`](assets/perfectextile.com/index.html:2841)
- LinkedIn：[`linkedin`](assets/perfectextile.com/index.html:2848)
- Instagram：[`instagram`](assets/perfectextile.com/index.html:2855)
- YouTube：[`youtube`](assets/perfectextile.com/index.html:2862)
- TikTok：[`tiktok`](assets/perfectextile.com/index.html:2869)
- Pinterest：[`pinterest`](assets/perfectextile.com/index.html:2876)

## 20.2 Links 列

标题：[`LINKS`](assets/perfectextile.com/index.html:2888)

菜单：[`nav menu`](assets/perfectextile.com/index.html:2892)

内容：

- Home
- About Perfectextile
- Company History
- Global Network
- Why Perfectextile
- Service
- Contact Us

## 20.3 More products 列

标题：[`More products`](assets/perfectextile.com/index.html:2916)

菜单：[`menu-1-8849da0`](assets/perfectextile.com/index.html:2918)

包括：

- All Product
- Printed Polyester Fabric
- 100 White Polyester Fabric
- Bamboo Bed Sheets
- Embossed Polyester Fabric
- Wholesale Satin Bedding
- Ankara Fabric Wholesale

## 20.4 Contact Info 列

标题：[`Contact Info`](assets/perfectextile.com/index.html:2940)

内容：

- 邮箱：[`email icon box`](assets/perfectextile.com/index.html:2943)
- Factory1 地址 + 电话：[`Factory1`](assets/perfectextile.com/index.html:2964)
- Factory2 地址 + 电话：[`Factory2`](assets/perfectextile.com/index.html:2986)
- Warehouse in Thailand：[`Thailand`](assets/perfectextile.com/index.html:3015)
- Vietnam branch office：[`Vietnam`](assets/perfectextile.com/index.html:3037)

## 20.5 底部版权

版权文案：[`Copyright © 2024...`](assets/perfectextile.com/index.html:3065)

### Footer 样式特征

- 多列布局
- 深色/中性色背景趋势
- 标题明确区分各列
- 社媒图标集中在 logo 列
- 信息密度高，接近企业站 footer

---

## 21. body 底部附加浮层与功能模块

这些内容不属于主体 section，但在 1:1 复刻时不能漏。

## 21.1 语言切换悬浮

起点：[`trp-floater-ls`](assets/perfectextile.com/index.html:3075)

支持语言：

- Arabic：[`Arabic`](assets/perfectextile.com/index.html:3084)
- Spanish：[`Spanish`](assets/perfectextile.com/index.html:3087)
- French：[`French`](assets/perfectextile.com/index.html:3090)
- Italian：[`Italian`](assets/perfectextile.com/index.html:3093)
- Portuguese：[`Portuguese`](assets/perfectextile.com/index.html:3096)
- Vietnamese：[`Vietnamese`](assets/perfectextile.com/index.html:3099)
- English 当前语言

特点：

- 右下角悬浮
- dark 风格
- 带国旗图标

## 21.2 回到顶部按钮

- 按钮：[`ast-scroll-top`](assets/perfectextile.com/index.html:3106)
- 样式色：主橙 `#ff8c00`
- 固定右下

## 21.3 WhatsApp 悬浮按钮

起点：[`ht-ctc-chat`](assets/perfectextile.com/index.html:3111)

关键样式：

- `position: fixed; bottom: 150px; right: 30px;`
- 图标 50x50 SVG
- CTA 文案：`WhatsApp us`
- 颜色：绿色 `#25D366`

配置数据：[`ht_ctc_chat_data`](assets/perfectextile.com/index.html:3131)

其中包含：

- 电话：`8613567988730`
- 预填内容：关于 HOME 的咨询

## 21.4 Popup：询盘/目录下载表单

Popup 起点：[`popup 22222`](assets/perfectextile.com/index.html:3132)

结构：

- 顶部横幅图：[`popup banner`](assets/perfectextile.com/index.html:3135)
- 表单组件：[`wpforms`](assets/perfectextile.com/index.html:3137)

### 表单样式变量

局部样式变量见 [`wpforms vars`](assets/perfectextile.com/index.html:3139)

关键值：

- field background：`#FFFFFF`
- field border：`#000000`
- button radius：`21px`
- button background：`#FF8C00`
- button text：`#FFFFFF`
- input height：`31px`
- button height：`48px`
- button font-size：`20px`

### 结论

如果 Shopify 复刻只做首页视觉，也应保留：

- header CTA → 弹窗
- request a full catalog → 弹窗
- get started / quote now 等按钮 → 表单或 contact 页面

---

## 22. 首页卡片/模块复刻优先级建议

如果按照“先卡片，后组合”的方式复刻，建议优先级如下。

### 第一优先级：必须先做的单卡

1. `card-image-cta`
   - 适用：Mega Menu Recent Products、Textile 区、Bedding 区
2. `card-stat`
   - 适用：4 个数据统计 funfact
3. `card-video-cover`
   - 适用：工厂视频卡
4. `card-feature-icon`
   - 适用：Why choose us 图标卡
5. `card-blog-post`
   - 适用：Blog & News
6. `card-process-slide`
   - 适用：Production process 轮播
7. `card-testimonial-image`
   - 适用：Testimonials 图片评价
8. `card-timeline-item`
   - 适用：Company History 时间线

### 第二优先级：中型组合模块

1. `mega-menu-bedding-fabric`
2. `hero-video-banner`
3. `factory-video-cluster`
4. `compare-table-section`
5. `textile-grid-section`
6. `bedding-grid-section`
7. `feature-advantages-section`
8. `certificate-gallery-section`
9. `blog-grid-section`
10. `final-cta-section`

### 第三优先级：全局附加层

1. `footer`
2. `language-switcher-float`
3. `scroll-top`
4. `whatsapp-float`
5. `quote-popup`

---

## 23. 最终复刻结论

从 body 真实结构看，perfectextile 首页并不是“简单几屏 banner + cards”，而是一个 **Elementor 重度拼装、夹杂大量自定义 HTML/CSS、并包含复杂 Mega Menu / 多轮播 / 时间线 / 证书画廊 / popup / 浮层组件** 的企业型营销首页。

对于 Shopify 1:1 复刻，最正确的路径不是直接按 section 粗暴拆，而是：

1. 先按本文把每种卡片识别出来
2. 逐卡把外观做准
3. 再组装成区块
4. 最后按首页顺序拼接

一句话总结：

**首页主体内容确实都在 [`<body>`](assets/perfectextile.com/index.html:428) 内，并且从 [`header`](assets/perfectextile.com/index.html:451) 到 [`footer`](assets/perfectextile.com/index.html:2828) 之间可以清晰拆成可复刻的卡片与模块；要实现 Shopify 1:1，重点是保留 CTA 图卡、视频封面卡、对比表、统计卡、轮播卡、时间线卡、博客卡和浮层交互的真实样式与层级关系。**
