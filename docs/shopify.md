# shopify

Shopify 1:1 复刻 [perfectextile](https://perfectextile.com/)的主页，只需要主页：

用 Sections + Liquid 重建布局（Hero、产品 Collection 网格、FAQ 用 Metafields）。
产品页改成“批发询价”模式（禁用购物车，用 apps 如 “Wholesale” 或 “Request a Quote” 替换为弹出表单）。
导入产品为 Draft，MOQ/规格用 Custom Fields。

第一阶段：资源提取与架构分析（AI 辅助）

在写代码之前，先把原站的“骨架”和“皮肉”扒下来。

1. 提取视觉资产 (Assets)：
  在 ./lib 下编写 python 脚本一键下载 `perfectextile.com` 的所有 html css js, 图片、Logo、Icon（SVG 格式）。插件查出它使用的主要字体（如 Roboto, Montserrat 等），以及提取主色调（Hex 颜色代码）。
1. 分析网页结构 (AI 辅助)：
   使用 Prompt：
     > *"这是一个纺织品 B2B 网站的截图。请帮我将这个页面自上而下拆解为 Shopify 的 Section 模块，列出每个模块需要哪些自定义字段（如：图片、标题、富文本、按钮链接），以 JSON 结构输出。"*

---

## AI 辅助 1:1 代码复刻（核心实操）

### 1. 基础全局样式替换 (Base CSS)

严格注意设计规范，和卡片复用性

打开 `assets/base.css`。生成全局 CSS 变量。

**提示词：**
> *"修改当前的 CSS 变量，将主色调改为 `[填入原站色号]`，背景色改为 `[原站背景色]`，字体改为 `[原站字体]`。"*

### 2. 自定义 Section 模块复刻（以“首页轮播图/Hero”为例）

Shopify 的核心是 `Section`（模块）。为了日后能随便换素材，必须写成动态 Schema [1]。

在 `sections` 文件夹下新建一个文件 `custom-hero.liquid`。

**Cursor 截图提问玩法：**
原站 Hero 区域的截图于 hero.png，Prompt：
> *"请用 Shopify Liquid 和 Tailwind CSS（或普通 CSS）完美复刻这个模块。要求：
>
> 1. 视觉 1:1 还原截图。
> 2. 必须包含 Shopify schema，使得背景图片、大标题、副标题和按钮链接都可以在 Shopify 后台自定义。

#### 3. 逐个击破其他页面

重复上述操作，将原站的“产品分类展示（Collection）”、“关于我们（About Us）”、“特色面料网格（Feature Grid）”逐个截图给 Cursor，生成对应的 `.liquid` 文件。

---
