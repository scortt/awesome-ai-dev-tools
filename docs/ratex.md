# RaTeX：面向原生、多端和服务端的纯 Rust 数学公式渲染器

RaTeX 是一个用 Rust 编写的 LaTeX 数学渲染引擎，目标是兼容 KaTeX 语法，同时摆脱 JavaScript、WebView 和 DOM 的依赖。它把 LaTeX 数学表达式解析成 Rust 核心里的 display list，再输出到 iOS、Android、Flutter、React Native、Web、PNG、SVG、PDF 等不同目标。

它适合放进 AI 时代开发效率工具库里的“Docs, Knowledge, And RAG”分类。原因是：AI 文档、科研助手、教育工具、论文阅读器、知识库和多端笔记应用都经常需要稳定渲染数学公式。传统方案在 Web 上很好，但到了移动端、服务端、离线环境或 CI 生成图片/PDF 时，经常要引入 WebView、headless Chrome 或 JS runtime。RaTeX 的切入点正是把公式渲染变成一个可移植的原生 Rust 能力。

## 它解决什么问题

数学公式渲染在 AI 应用里会越来越常见：

- AI 生成论文摘要、讲义、解题步骤，需要展示 LaTeX 公式。
- RAG 系统索引数学、物理、化学文档，需要把公式输出成图片、SVG 或 PDF。
- 教育类 App 需要在 iOS、Android、Flutter、React Native 上原生渲染公式。
- 服务端需要批量把公式转成 PNG/SVG/PDF，用于报告、题库、卡片或文档导出。
- 离线工具不能依赖 WebView、远程字体或浏览器运行时。

KaTeX 和 MathJax 在 Web 场景成熟，但在非 Web 场景常常需要包一层浏览器环境。RaTeX 的目标是用一个 Rust core 覆盖这些场景。

## 核心能力

### KaTeX 兼容的数学语法

RaTeX README 中说明它覆盖约 99% 的 KaTeX 数学语法，支持 fractions、radicals、integrals、matrices、environments、stretchy delimiters 等常见公式结构。

对 AI 文档工具来说，这意味着大多数由模型生成的 LaTeX 数学表达式可以直接渲染，而不必为每个平台维护不同的公式渲染方案。

### 化学和物理单位

RaTeX 支持 `mhchem` 风格的 `\ce` 和 `\pu`：

- `\ce` 可用于化学方程式；
- `\pu` 可用于符合 IUPAC 风格的数值和单位表达。

这让它不仅适合数学，也适合科学教育、化学文档、物理单位表达和 STEM 知识库。

### 多平台输出

项目 README 列出的目标平台包括：

- iOS：XCFramework + Swift / CoreGraphics
- Android：JNI + Kotlin + Canvas / AAR
- Flutter：Dart FFI + `CustomPainter`
- React Native：Native module + C ABI
- Web：WASM + Canvas 2D + `<ratex-formula>` Web Component
- Server / CI：PNG rasterizer
- SVG：自包含 vector SVG
- PDF：嵌入 KaTeX fonts 的 vector PDF

这对 AI 产品很重要，因为同一个知识内容可能要在网页、移动端、离线文档、服务端导出里同时出现。RaTeX 试图让这些渲染结果来自同一个核心。

### Rust core 和 display list 架构

RaTeX 的核心流程大致是：

1. LaTeX string 输入；
2. lexer 生成 token stream；
3. parser 生成 AST；
4. layout 生成 layout box；
5. 输出 display list；
6. 不同平台把 display list 渲染成 Canvas、PNG、SVG 或 PDF。

这个架构的价值是把“公式理解”和“平台绘制”拆开。对需要多端一致输出的应用来说，这比在每个平台分别适配 JS/DOM 或 WebView 更可控。

## 为什么它属于这个 awesome 项目

AI 时代的开发效率不只包括代码生成，也包括知识生产和技术文档生产。很多 AI 应用会生成包含公式的内容，但公式渲染一旦进入移动端、服务端、离线或导出场景，就会变成工程负担。

RaTeX 属于这个项目，是因为它可以成为这些工作流的基础设施：

- AI 教育产品：把模型生成的解题步骤稳定渲染到移动端。
- AI 科研助手：把论文中的公式转成统一显示层。
- RAG / 文档系统：把公式内容渲染成可索引、可导出、可预览的资产。
- 报告生成：服务端批量生成数学公式 PNG、SVG 或 PDF。
- 跨平台笔记：同一套 LaTeX 输入在 Web、iOS、Android 中保持一致。

它不是 coding agent，但它明显服务于 AI 时代的知识工作和开发者工具。

## 使用边界和注意事项

RaTeX 的边界也要写清楚：

- 如果你的项目只运行在 Web 上，KaTeX 仍然是成熟且高性能的默认选择。
- RaTeX 的重点不是在 Web 场景击败 KaTeX，而是把 KaTeX-compatible 渲染带到原生、多端和服务端。
- README 标注语法覆盖接近 KaTeX，但不是 100% 完全等价。
- 许可证需要以仓库实际 LICENSE 为准，awesome 条目里先写 `License: see repository`。
- 对于中文、emoji、韩文等 KaTeX 字体外字符，项目通过系统 Unicode 字体发现和 fallback 处理，服务端/CI 环境最好显式配置字体。

## 适合谁使用

- 构建 AI 教育、数学、物理、化学工具的开发者。
- 需要在移动端原生渲染 LaTeX 公式的 App。
- 需要服务端批量生成公式 PNG、SVG、PDF 的文档系统。
- 需要把 AI 生成的公式内容嵌入报告、课件、题库或知识库的团队。
- 希望避免 WebView/headless Chrome 依赖的跨平台开发者。

## 项目信息

- GitHub: https://github.com/erweixin/RaTeX
- Live demo: https://erweixin.github.io/RaTeX/
- 技术栈: Rust, WASM, C ABI, Swift/Kotlin/Flutter glue layers
- 输出目标: iOS, Android, Flutter, React Native, Web, PNG, SVG, PDF
- 当前 GitHub 页面显示约 940 stars，主仓库公开。

## 推荐 awesome 条目

```markdown
- [RaTeX](https://github.com/erweixin/RaTeX) - Pure Rust KaTeX-compatible math renderer for native, web, server-side PNG/SVG/PDF, and AI document workflows. `Rust` `License: see repository`
```
