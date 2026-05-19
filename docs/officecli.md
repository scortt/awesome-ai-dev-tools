# OfficeCLI：给 AI Agent 使用的 Office 文档命令行工具

OfficeCLI 是一个开源的 Office 文档 CLI，目标是让 AI agent 可以直接创建、读取、修改和渲染 Word、Excel、PowerPoint 文件。它以单文件 binary 形式分发，不要求本机安装 Microsoft Office，也不需要用户自己拼接多套 Python 或 Office SDK。

它适合放进这个 awesome 项目的 “Design, Prototyping, And Artifacts” 分类。原因是它处理的是真实交付物，而不是纯文本草稿：agent 可以通过命令行生成 `.docx`、`.xlsx`、`.pptx`，再把文档渲染成 HTML 或 PNG，用视觉反馈继续修正。

## 它解决什么问题

AI agent 生成 Office 文件时经常卡在两个地方：

1. 文件格式复杂，Word、Excel、PowerPoint 各自需要不同库和对象模型；
2. 生成后缺少可视化反馈，agent 很难知道标题是否溢出、图表是否遮挡、页面是否真的可读。

OfficeCLI 把这些能力收敛成一组命令。agent 可以用 `create` 新建文件，用 `add`、`set`、`remove` 修改元素，用 `view` 和 `get --json` 读取结构，再用 `view html`、`view screenshot` 或 `watch` 做预览。

对 AI-assisted development 来说，它的价值不只是“能生成 Office 文件”，而是把 Office 文档纳入了 agent 可执行、可检查、可迭代的工程循环。

## 核心能力

### Word、Excel、PowerPoint 三类格式

OfficeCLI 覆盖 `.docx`、`.xlsx`、`.pptx` 三类常见办公文件。它支持创建、读取、修改和生成内容，README 中也列出了对段落、表格、样式、图片、公式、图表、数据验证、透视表、幻灯片、形状、动画、主题等对象的支持。

这让 agent 可以把报告、表格、演示稿当成结构化文档，而不是只能输出 Markdown 或 HTML。

### Agent-friendly 结构读取

OfficeCLI 可以把文档结构以 outline 或 JSON 形式暴露出来。例如 agent 可以定位到 `/slide[1]/shape[1]`，读取元素属性，再针对具体对象修改文本、颜色、位置或尺寸。

这种路径式操作对 agent 很重要：它比“重新生成整份文件”更稳，也更适合增量修复。

### 内置渲染和预览闭环

项目内置文档渲染能力，可以把 Office 文件渲染为 HTML 或 PNG，也可以通过 `officecli watch` 启动本地实时预览。每次 `add`、`set` 或 `remove` 后，浏览器预览会更新。

这解决了 Office 自动化中很关键的一步：agent 不只写文件，还能看见自己生成的结果。对于 PPT 和复杂表格，这个反馈环节比单纯检查 XML 或 JSON 更接近真实交付。

### 单 binary 分发

OfficeCLI 以单文件 binary 发布，官方安装脚本会下载对应平台版本。README 说明 .NET runtime 被打包进去，用户不需要单独管理运行时。

这种部署方式适合 agent 环境、CI、服务器和容器，因为它减少了 Office、COM、LibreOffice、Python 包版本等外部依赖。

### Agent skill 集成

项目提供给 AI agent 使用的 skill 文件。安装流程会把 OfficeCLI 的使用方式暴露给 Claude Code、Codex、Cursor 等环境，让 agent 知道如何调用命令、读取文档、修改内容和做预览。

这使它更像一个 agent 工具层，而不是只面向人类的 Office 转换命令。

## 为什么适合 AI 开发效率工具库

这个 awesome 项目关注的是能改善 AI 时代开发工作流的开源工具。OfficeCLI 的位置很明确：它把传统办公文档变成 agent 可以操作的 artifact。

典型使用场景包括：

- 根据产品需求、数据库查询或实验结果生成报告；
- 批量修改 Word 文档样式、页眉页脚、表格和图片；
- 让 agent 生成 PowerPoint 初稿，再通过截图或 HTML 预览修正；
- 从 Excel 中读取结构化数据、公式、图表和透视表；
- 在 CI 或服务器上生成可交付的 Office 文件，而不依赖桌面 Office。

它和 Open Slide、Guizang PPT Skill 处在相邻方向。Open Slide 更偏 slides-as-code，Guizang PPT Skill 更偏网页 PPT 和封面工作流；OfficeCLI 则直接面向真实 Office 文件格式。

## 边界和注意点

OfficeCLI 适合让 agent 自动化 Office 文档，但不等于完整替代人类办公软件。

使用时需要注意：

- 复杂企业模板、品牌母版和精细排版仍需要人工验收；
- 自动生成的图表、动画、页眉页脚、公式和表格要用预览或截图检查；
- 文档内容来自模型时，事实准确性和版权仍要单独审查；
- 自动更新和 agent skill 安装会改动用户环境，团队环境中应固定版本和安装路径；
- 对要求严格兼容 Microsoft Office 的交付物，应在最终 Office 软件中打开验收一次。

## 适合谁

- 经常让 Codex、Claude Code、Cursor 等 agent 生成办公文档的开发者；
- 需要批量生成报告、演示稿、表格和数据交付物的工程团队；
- 想把 Office 文档生成接入 CI、脚本或后端任务的人；
- 需要让 agent 读取和修复 `.docx`、`.xlsx`、`.pptx` 的用户；
- 想研究 AI agent 如何稳定产出非代码 artifact 的工具开发者。

## 项目信息

- GitHub: https://github.com/iOfficeAI/OfficeCLI
- 官网: https://officecli.ai
- 类型: Office document CLI for AI agents
- 支持格式: Word `.docx`, Excel `.xlsx`, PowerPoint `.pptx`
- 主要语言: C#
- License: Apache-2.0
- 安装命令: `curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash`

## 推荐 awesome 条目

```markdown
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) - Single-binary Office document toolkit that lets AI agents create, inspect, edit, and render Word, Excel, and PowerPoint files without Microsoft Office. `C#` `Apache-2.0`
```
