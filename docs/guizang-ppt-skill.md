# Guizang PPT Skill：让 Agent 生成杂志风网页 PPT 和封面

Guizang PPT Skill 是一个面向 Claude Code、Codex 等 agent 环境的开源 skill。它把提示词转成横向翻页的单文件 HTML deck，也可以生成 PPT 配图和多平台封面。

它适合放进这个 awesome 项目的 “Design, Prototyping, And Artifacts” 分类。原因是它不是传统 PPT 模板库，而是一套给 coding agent 使用的结构化设计工作流：agent 根据需求澄清、版式规则、主题系统、图片槽位和检查清单，生成可以直接在浏览器打开的演示文件。

## 它解决什么问题

很多 AI 生成 PPT 的问题不是“不会写页面”，而是缺少约束。模型容易临时发明版式、堆满文字、图片比例失控、封面和正文风格断裂，最后得到的是能看但很难用于真实分享的页面。

Guizang PPT Skill 把这个流程拆成更稳定的步骤：

1. 先选择视觉系统；
2. 用 6 问清单澄清受众、时长、素材、图片、主题色和硬约束；
3. 从固定模板和版式骨架中选择页面结构；
4. 生成横向左右翻页的单文件 HTML deck；
5. 可选生成配图、封面、分享卡等素材；
6. 用检查清单和脚本自检排版问题。

对 AI-assisted development 来说，它的价值在于把“让 agent 做 PPT”从一次性提示词变成可重复执行的 artifact 生产流程。

## 核心能力

### 单文件 HTML 横向 deck

生成结果是可以直接用浏览器打开的单文件 HTML，不需要构建、不需要服务器。交互上支持键盘左右翻页、滚轮、触屏滑动、底部圆点和 ESC 索引。

这类输出很适合开发者快速做内部分享、产品发布、demo day、私享会材料，或者把文章和方法论转成演讲 deck。

### 两套视觉系统

Guizang PPT Skill 内置两套视觉方向：

- Style A：电子杂志 × 电子墨水，偏叙事、观点、个人风格表达；
- Style B：瑞士国际主义，偏事实、产品、分析和方法论表达。

Style A 提供封面、章节、数据大字报、图文、图片网格、pipeline、对比等布局。Style B 更严格，提供 22 种锁定版式、16 列网格、直角色块、发丝线、无阴影、无渐变、无圆角，并通过校验器约束输出。

这种“先限定设计语言，再让 agent 填内容”的方式，比完全自由生成更适合稳定交付。

### Agent 配图和封面工作流

项目把配图也纳入流程。它支持在 Codex 环境中询问用户是否需要配图，再按页面比例生成纪实照片、信息图、流程图、系统关系图、UI 情景图或数据图表。

它也可以基于文章或 PPT 核心观点生成多平台封面，例如公众号 21:9 头图、公众号 1:1 分享卡、小红书 3:4 封面和视频号横版封面。

关键点是：图片被当作 PPT 素材，而不是一张自带标题、页脚和装饰边框的“假 PPT 截图”。这能减少 AI 生成素材和真实版式之间的冲突。

### 检查清单和版式校验

Skill 目录里包含 `references/checklist.md`，把常见问题按 P0 到 P3 分级。瑞士风还提供 `scripts/validate-swiss-deck.mjs`，用于检查居中标题、实验版式、SVG 内写字、图片脱离槽位等问题。

这让它从“审美提示词”变成更接近工程化的生成系统：模板、规则、脚本和人工预览共同约束结果。

## 为什么适合 AI 开发效率工具库

这个 awesome 项目关注的是 AI 时代提高开发效率的开源软件。Guizang PPT Skill 的价值在于，它把 agent 的能力从代码编辑扩展到了设计产物生产。

典型使用场景包括：

- 把文章、提纲或产品想法转成演讲 deck；
- 为发布会、内部分享、demo day 快速生成网页 PPT；
- 用固定版式系统约束 AI 输出，减少返工；
- 让 Codex/Claude Code 生成配图、封面和分享卡；
- 把 PPT 交付物保持为可读、可改、可预览的 HTML 文件。

它和 Open Slide、Open Design 属于相邻方向，但更偏“skill + 模板 + 检查清单”的 agent 工作流，而不是完整产品平台或 React slide 框架。

## 边界和注意点

Guizang PPT Skill 更适合风格明确、叙事强、视觉表达重要的分享材料，不适合所有 PPT 场景。

使用时需要注意：

- 不适合大段表格数据或高密度培训课件；
- 静态 HTML 不适合多人协作编辑；
- Style B 强依赖固定版式，不能随意发明页面结构；
- 配图生成仍需要人工确认语义、版权和比例；
- 最终交付前要用浏览器预览和检查清单逐页过一遍。

## 适合谁

- 经常用 Claude Code、Codex 或 Cursor 做内容产物的开发者；
- 需要快速生成演讲 deck 的产品、工程和独立开发者；
- 想把长文或方法论变成网页 PPT 的内容创作者；
- 需要公众号头图、分享卡、小红书封面的个人品牌或小团队；
- 想研究 AI agent 如何稳定生成设计 artifact 的工具开发者。

## 项目信息

- GitHub: https://github.com/op7418/guizang-ppt-skill
- 类型: Claude Code / Codex skill
- 输出: single-file HTML deck, PPT visuals, social covers
- 主要语言: HTML
- License: MIT

## Awesome 列表条目

```markdown
- [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) - Claude Code and Codex skill for generating single-file horizontal-swipe HTML decks, presentation visuals, and social covers from prompts. `HTML` `MIT`
```
