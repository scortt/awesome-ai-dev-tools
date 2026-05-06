# Pierre：给 AI 编程工具准备的代码审查 UI 基础设施

Pierre 不是一个传统意义上的“通用开源软件”，更像是一组面向下一代开发工具的前端基础组件。它的主仓库 `pierrecomputer/pierre` 是一个 TypeScript monorepo，当前公开展示的核心项目包括 Diffs 和 Trees：前者用于渲染代码 diff，后者用于渲染文件树。

这类工具值得放进 AI 时代的开发效率工具库，是因为 AI 编程的主要瓶颈已经不只是“生成代码”，而是让开发者快速理解、审查、选择、接受或拒绝 AI 生成的变更。Diff 视图、文件树、行级评论、局部接受/拒绝、冲突处理、生成快照对比，这些都是 AI coding workflow 的基础界面能力。

## 它解决什么问题

AI coding agent 每次修改代码，本质上都会产生一组变更。开发者需要回答几个问题：

- 改了哪些文件？
- 每个文件改了哪些行？
- 这些改动是否合理？
- 哪些改动可以接受，哪些需要回滚？
- 如果 AI 给出多个版本，如何比较它们？
- 如果有 merge conflict，如何把当前版本、传入版本或二者结合起来？

Pierre 的价值就在这里。它不是替你写代码，而是提供“看懂 AI 写了什么”的 UI 层。

## 核心项目

### `@pierre/diffs`

`@pierre/diffs` 是一个开源 diff 和代码渲染库。官方介绍里强调它基于 Shiki 做语法高亮和主题系统，支持高度自定义。

对 AI 开发工具来说，它特别有用的能力包括：

- 统一视图和左右分栏视图两种 diff layout。
- 支持 Shiki 主题，能跟编辑器、代码审查工具或产品自身主题融合。
- 支持 classic diff 标记、整行背景、竖条等多种变更样式。
- 支持 word/character 级别的 inline change highlight。
- 支持隐藏行号、换行、字体和行高定制。
- 支持自定义 hunk separator 和文件头。
- 支持 merge conflict resolution UI，可以选择 current、incoming 或 both。
- 支持 comments 和 annotations，可用于行级评论、CI 结果、AI 解释或审查建议。
- 支持 accept/reject changes，这一点非常适合 Cursor、Claude Code、Codex 类工具的“局部采纳”交互。
- 支持 line selection 和 token hover。
- 除了 Git patch，也可以直接对比任意两个文件，适合比较 AI 生成的多个快照。

这意味着它不只是一个“把 diff 画出来”的组件，而是可以作为 AI 代码审查界面的底座。

### `@pierre/trees`

`@pierre/trees` 是一个文件树渲染库。官方介绍强调它面向性能和灵活性，适合渲染大型项目结构。

对 AI coding 产品来说，文件树同样是关键组件，因为 agent 的工作范围、变更范围和上下文边界都要通过文件树呈现。它提供的能力包括：

- 空目录链 flatten，让深层项目结构更紧凑。
- Git status 标记，能显示 modified、added、deleted、renamed、untracked、ignored 等状态。
- 自定义 context menu，可接入新建文件、重命名、删除等产品操作。
- drag and drop 文件移动。
- 搜索与过滤文件名。
- 内置 virtualization，大量文件展开时仍然保持性能。
- 键盘导航、ARIA roles、focus 管理等可访问性支持。
- 内置文件图标集，也支持自定义 icon sprite。
- 支持 Shiki themes 和 CSS variables。
- 支持 compact/default/relaxed 等密度设置。

如果要做一个 AI IDE、agent dashboard、代码审查面板、生成结果预览器，文件树和 diff 视图通常是最基础的两块 UI。

## 为什么它属于这个 awesome 项目

Pierre 很适合收进这个项目的第一个工具，因为它代表的是 AI 时代开源软件的新方向：不是“通用软件工具”，而是面向 AI-assisted development workflow 的底层构件。

过去的开发工具库常常收录编辑器、数据库、框架、CLI。AI 时代更需要收录的是这些东西：

- agent 如何展示它将要修改的文件；
- 人如何审查 agent 的 diff；
- 如何接受、拒绝、评论某一段 AI 生成的代码；
- 如何比较不同生成版本；
- 如何让代码界面在大型仓库里仍然快速、可访问、可嵌入。

Pierre 正好落在这个位置。它不替代 coding agent，但它能让 coding agent 的输出更容易被人类理解和控制。

## 适合谁使用

- 正在构建 AI IDE 或 coding agent UI 的团队。
- 想给内部 AI 代码生成工具加上 diff review 面板的团队。
- 需要渲染大型代码变更、review annotation、CI annotation 的工程工具。
- 需要在网页里展示 repo 文件树、Git 状态和代码变更的产品。

## 使用判断

如果你的产品只是偶尔展示一小段文本 diff，Pierre 可能偏重。但如果你的产品要承载真实开发工作流，例如 AI 修改多文件、用户逐段审查、局部接受或拒绝、展示文件树和 Git 状态，那么 Pierre 的抽象就很有价值。

## 项目信息

- GitHub: https://github.com/pierrecomputer/pierre
- 官网: https://pierre.computer
- Diffs: https://diffs.com
- Trees: https://trees.software
- 技术栈: TypeScript, React, Bun, Shiki
- 当前 GitHub 页面显示主仓库为公开仓库，约 3.5k stars，主语言 TypeScript。

## 推荐 awesome 条目

```markdown
- [Pierre](https://github.com/pierrecomputer/pierre) - Open source TypeScript monorepo behind AI-friendly code review primitives such as diff rendering and file tree rendering. `TypeScript` `License: see repository`
```
