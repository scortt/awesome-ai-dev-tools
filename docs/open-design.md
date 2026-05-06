# Open Design：把本地 coding agent 变成设计产物生成器

Open Design 是一个 local-first 的开源设计工作流工具，目标是成为 Claude Design 的开放替代品。它本身不绑定一个固定模型或固定 agent，而是自动检测本机 `PATH` 上已有的 coding-agent CLI，例如 Claude Code、Codex CLI、Cursor Agent、Gemini CLI、OpenCode、Qwen、GitHub Copilot CLI 等，然后把这些 agent 接入一套技能驱动的设计生成流程。

它适合放进 AI 时代开发效率工具库里的“Design, Prototyping, And Artifacts”分类。原因是它解决的不是传统 UI 组件库问题，而是让 AI agent 直接产出可预览、可导出、可继续编辑的设计资产：Web 原型、移动端界面、dashboard、landing page、slides、图片、视频和 motion graphics。

## 它解决什么问题

AI coding agent 已经能写代码，但从“用户一句话”到“可交付设计产物”中间还有很多步骤：

- 先问清楚使用场景、受众、语气、品牌背景；
- 选择视觉方向，而不是让模型自由发挥；
- 套用可复用的 design system；
- 生成真实项目文件，而不是只输出一段 HTML；
- 在沙盒 iframe 中预览结果；
- 支持 HTML、PDF、PPTX、MP4、ZIP、Markdown 等格式导出；
- 允许用户在生成过程中看到 todo、工具调用和进度，并中途打断或修正。

Open Design 的价值是把这些步骤组织成一个本地可运行的设计生产闭环。

## 核心能力

### 使用本机已有 coding agent

Open Design README 中说明，它会自动检测本机 `PATH` 上的多个 coding-agent CLI。它不是再造一个 agent，而是把已有 agent 变成设计引擎。

这对开发者很实用：如果你已经在用 Codex、Claude Code、Cursor Agent 或 Gemini CLI，就不需要为设计工作流再迁移到一个封闭平台。Open Design 扮演的是本地 daemon、Web UI、prompt stack、skills 和 artifact runtime 的协调层。

### Local-first 和 BYOK

项目强调 local-first、web-deployable、BYOK。README 里还提到没有 CLI 时，可以通过 OpenAI-compatible BYOK proxy 走同一条 chat/artifact loop。

这个设计很符合 AI 开发工具的长期方向：模型、agent、API key、运行位置都可以替换，而不是被锁进某一个云端产品。

### Skills 和 Design Systems

Open Design 内置大量 skills 和 design systems。README 中列出 prototype mode 和 deck mode 的技能，例如：

- web prototype
- SaaS landing
- dashboard
- mobile app
- gamified app
- social carousel
- magazine poster
- wireframe sketch
- PM spec
- engineering runbook
- finance report
- HR onboarding
- invoice
- kanban board
- weekly update deck

它还内置大量品牌级 design systems，让生成结果更像“有设计约束的产物”，而不是普通 LLM 生成的随机风格页面。

### Discovery Form 和 Direction Picker

Open Design 的一个重要点是：在 agent 开始写设计之前，先通过交互表单锁定需求，包括 surface、audience、tone、brand context、scale 等。没有品牌方向时，还可以让用户从多个 curated visual directions 中选择，例如 editorial、minimal、soft、tech utility、brutalist 等方向。

这对 AI 设计很关键。很多 AI 页面失败，不是因为模型不会写 CSS，而是因为需求没有被结构化，视觉方向没有被约束。Open Design 把这个过程前置。

### Sandboxed Preview 和 Export

生成结果以 `<artifact>` 的形式在 sandboxed iframe 中预览，并可导出为 HTML、PDF、PPTX、ZIP、Markdown、MP4 等格式。这让它不只是“聊天里给一段代码”，而是更接近一个设计 artifact 工作台。

### 本地项目和持久化

README 提到它使用本地 daemon 在项目文件夹中运行 agent，并把项目、conversation、messages、tabs、saved templates 等保存到 SQLite。换句话说，生成结果不是一次性的聊天消息，而是一个可以重新打开、继续编辑的项目。

## 为什么它属于这个 awesome 项目

这个 awesome 项目的主题是“AI 时代提高开发效率的开源软件”。Open Design 很符合这个边界，因为它把 AI agent 从代码编辑扩展到了设计交付：

- 产品经理可以生成 PM spec、wireframe、deck；
- 开发者可以快速做 dashboard、landing、mobile app 原型；
- 创作者可以生成 poster、social carousel、motion frames；
- 团队可以把 design system 和 skill prompt 固化成可重复工作流；
- 本地 agent 可以直接读写项目文件，而不是只在云端生成静态截图。

它不是传统 Figma 插件，也不是单纯模板库。它更像“agent-native design IDE”的开源实现。

## 使用边界和注意事项

Open Design 的能力很强，但也有边界：

- 它依赖本机 agent CLI 或 BYOK API，实际质量会受所选模型和 agent 能力影响。
- 设计系统和 skills 很多，维护时要注意版本和 prompt 行为漂移。
- 它适合生成原型和 artifacts，不等同于成熟产品的完整设计评审流程。
- 如果团队已经有严格 Figma 流程，它更适合作为前期探索和快速产物生成，而不是直接替代设计源文件。
- 项目当前 GitHub 页面显示 Star 数很高、issue/PR 也较多，说明活跃度高，但也意味着变动可能快，实际集成前应锁版本。

## 适合谁使用

- 想用 Codex、Claude Code、Cursor、Gemini 等 agent 快速生成设计原型的开发者。
- 需要从一句话生成 landing page、dashboard、mobile screen、deck 的团队。
- 想把内部 design system 和 prompt workflow 固化成可重复流程的产品团队。
- 需要本地预览、导出 HTML/PDF/PPTX/MP4 的创作者或创业团队。
- 想研究 Claude Design 类 artifact-first 工作流的开源实现者。

## 项目信息

- GitHub: https://github.com/nexu-io/open-design
- 官网: https://open-design.ai
- 技术栈: TypeScript, web app, local daemon, SQLite, Electron optional
- License: Apache-2.0
- 当前 GitHub 页面显示约 28.6k stars，主仓库公开。

## 推荐 awesome 条目

```markdown
- [Open Design](https://github.com/nexu-io/open-design) - Local-first design workflow that turns coding-agent CLIs into generators for prototypes, decks, mobile screens, dashboards, media, and exportable artifacts. `TypeScript` `Apache-2.0`
```
