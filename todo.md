# todo

目前只考虑主页的复刻

1. 模块化（会复用）：注意到原站的设计语言和模块划分，尽量抽象成可复用的 Shopify Section 模块。
2. 动态 Schema：每个 Section 模块都要写成动态 Schema 的形式，方便在 Shopify 后台自定义内容。

3. 分析 html，图片，总结出各个模块，再转成 Shopify Section 模块，写成动态 Schema 的形式。
4. 逐个模块复刻，先从视觉上 1:1 还原，再把内容写成动态 Schema 的形式。

基于 shopify 的 structure.md 开始重构代码,注意一个一个模块去复刻，为了一比一还原，可以回去分析截图或者html，以及对应的文档，生成 prompt.md
只需要复刻主页内容，图片什么的，直接使用 <https://perfectextile.com/> 的资源就行了，注意分析原站的设计语言和模块划分，尽量抽象成可复用的 Shopify Section 模块。每个 Section 模块都要写成动态 Schema 的形式，方便在 Shopify 后台自定义内容。严格注意设计规范，和卡片复用性。prompt 直接一次性的完整prompt，让它一步一步来，而不是各个prompt

像素级映射 逐段对照原站真实 DOM 深度还原 并且添加 js
