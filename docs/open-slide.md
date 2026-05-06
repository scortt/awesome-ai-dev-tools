# Open Slide：专为 coding agent 设计的 React 幻灯片框架

Open Slide 是一个面向 agent 的幻灯片框架。它的核心判断很直接：slides are visual code，而 coding agent 很擅长写代码。所以它不是让用户在传统 PPT 编辑器里拖拽元素，而是让 agent 根据自然语言生成 React 组件形式的 slide，再由 open-slide 负责画布、缩放、导航、热更新、演示模式和导出。

它适合放进 AI 时代开发效率工具库的“Design, Prototyping, And Artifacts”分类。和 Open Design 相比，Open Slide 更垂直：它专注让 AI agent 生成、修改、预览、演示和导出 slide deck。

## 它解决什么问题

做演示文稿通常有两个痛点：

- 内容和结构需要 AI 帮忙快速起草；
- 视觉布局又需要足够稳定，不能只是聊天窗口里生成一堆 Markdown。

Open Slide 的做法是把每一页 slide 当成任意 React component，但固定渲染到 1920 × 1080 canvas。这样 agent 可以写它熟悉的 React/TypeScript/CSS，而框架负责把结果变成可播放、可导出、可部署的 deck。

对开发者来说，这比让 AI 直接生成 PPTX 更容易调试，也比 Markdown slide 框架更自由。

## 核心能力

### Agent-native authoring

Open Slide 可以和 Claude Code、Codex、Cursor 等 coding agent 一起工作。README 中提到它的 scaffolder 内置 skills：

- `/create-slide`：端到端起草 deck，会先问 topic/aesthetic、page count、text density、motion vs static 等问题，再规划结构并写页面。
- `/slide-authoring`：技术参考，告诉 agent 1920 × 1080 canvas、字号体系、颜色和布局规则。

这让它不是“用户自己写 React slide”，而是把 agent 写 slide 的上下文、规则和项目结构提前准备好。

### 1920 × 1080 固定画布

每页 slide 都渲染到固定 1920 × 1080 canvas。这个约束对 AI 很重要：如果不固定画布，模型很容易生成尺寸漂移、布局不稳定或演示时比例错乱的页面。

固定画布让 agent 可以围绕明确尺寸做布局，也让导出 PDF/HTML 时更可控。

### In-browser inspector 和评论闭环

Open Slide 的一个实用功能是浏览器内 inspector。用户可以点击 dev server 中的任意元素并附加评论，例如“make this red”“shrink the headline”。这些评论会保存为源码里的 `@slide-comment` markers。之后运行 `/apply-comments`，agent 会应用所有 pending edits 并清理 markers。

这个流程很像把设计评审变成 agent 可执行的代码修改任务：

1. 预览 deck；
2. 点击元素写评论；
3. agent 读取评论并修改源码；
4. 再次预览。

### Assets manager 和 logo 搜索

Open Slide 提供每个 deck 的 assets panel，用于管理图片、视频和字体。它还集成了 svgl logo catalogue，方便搜索并放入品牌 SVG logo。

这对做 pitch deck、产品介绍、公司内部分享很有用，因为 slide 往往需要大量品牌资产和图片，而不是纯文字。

### Professional present mode

Open Slide 提供 fullscreen playback、键盘导航，以及 presenter mode：当前/下一页预览、speaker notes 和 timer。它不是只面向浏览器预览，而是考虑了真实演示场景。

### HTML 和 PDF 导出

项目支持把 deck 导出为自包含静态 HTML 或 print-ready PDF。这让 deck 可以不用服务器就分享，也可以部署到 Vercel、Cloudflare Pages、Netlify 等静态托管平台。

## 为什么它属于这个 awesome 项目

这个项目收录的是“AI 时代提高开发效率的开源软件”。Open Slide 很符合这个边界，因为它把演示文稿从传统 GUI 编辑转成了 agent-friendly code workflow：

- 自然语言 brief 进入 agent；
- agent 生成 React slide；
- 框架提供固定画布和演示 runtime；
- 用户通过浏览器 inspector 做评论；
- agent 应用评论回源码；
- 最后导出 HTML/PDF 或静态部署。

这套流程让 slide deck 变成可以被 AI 读写、测试、重构和版本管理的代码资产。对开发者、创业团队、技术布道、产品 demo、内部汇报来说，这比传统 PPT 更适合和 coding agent 协作。

## 使用边界和注意事项

Open Slide 的边界也要清楚：

- 它适合 agent 生成 React-based slides，不是传统 PPT 编辑器的完全替代品。
- 如果团队必须交付复杂 PPTX 母版和企业模板，可能还需要额外转换或人工整理。
- 它要求用户接受“slides as code”的工作方式，适合开发者和技术团队。
- 生成质量仍取决于所用 coding agent 对布局、视觉层级和内容结构的理解。
- 它目前的导出重点是静态 HTML 和 PDF，而不是直接完整替代 PowerPoint 编辑生态。

## 适合谁使用

- 经常做技术分享、产品 demo、投资人 pitch deck 的开发者。
- 想用 Codex、Claude Code、Cursor 等 agent 快速起草 deck 的团队。
- 需要把 slides 纳入 Git、代码审查和静态部署流程的人。
- 想让 AI 根据浏览器评论自动修改 slide 源码的用户。
- 想把演示文稿当成 React artifact 管理的产品/工程团队。

## 项目信息

- GitHub: https://github.com/1weiho/open-slide
- 官网: https://open-slide.dev
- 技术栈: TypeScript, React, Vite, pnpm, Turbo
- License: MIT
- 初始化命令: `npx @open-slide/cli init my-slide`
- 当前 GitHub 页面显示约 1.5k stars，主仓库公开。

## 推荐 awesome 条目

```markdown
- [Open Slide](https://github.com/1weiho/open-slide) - Agent-native React slide framework with fixed-canvas authoring, comments, present mode, and HTML/PDF export. `TypeScript` `MIT`
```
