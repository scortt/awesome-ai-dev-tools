# Keep Codex Fast：让长期使用后的 Codex 本地状态保持轻快、可恢复

Keep Codex Fast 是一个面向 Codex 的 maintenance skill。它解决的不是模型能力问题，而是长期使用 Codex 之后，本地状态、历史会话、日志、worktree、终端进程和项目引用逐渐变重的问题。

它适合放进 AI 时代开发效率工具库里的“Agent Operations And Maintenance”分类。随着 coding agent 变成日常开发工具，真正影响效率的不只是 agent 会不会写代码，还包括它的本地状态是否可控、历史是否能交接、旧会话是否能安全归档、日志和 worktree 是否拖慢工作区。

## 它解决什么问题

长期使用 Codex 之后，经常会出现这些情况：

- 很多长聊天一直留在 active 状态；
- 经常 resume 旧线程，导致上下文越来越重；
- 同时跨多个 repo 工作；
- 有多个终端、dev server、worktree 和日志文件；
- 想清理但担心误删上下文、历史和还没交接的工作。

Keep Codex Fast 的核心规则是：先做 handoff，再归档；先备份，再 apply；默认只报告，不直接修改。

## 核心能力

### Report-first，默认不改状态

README 明确说明，默认情况下这个 skill 只做报告，不会写文件、创建备份、移动目录或修改本地 Codex 状态，除非用户明确要求。

这点很重要。任何清理 agent 本地状态的工具如果默认会动文件，都有风险。Keep Codex Fast 把检查和执行分开，让用户先看到哪里变重，再决定是否处理。

### Handoffs First

项目强调在归档旧 active chats 之前，要先创建 handoff 文档。handoff 会记录：

- 当前目标；
- 已完成事项；
- 触碰过的文件；
- 已跑过的命令和检查；
- 已知错误或未解决问题；
- 后续 3-7 个具体步骤；
- 可以粘贴到新 Codex 线程里的 reactivation prompt。

这正好符合 coding agent 长期协作的真实需求：旧聊天负责执行，handoff 文档负责连续性，新聊天负责速度。

### Archive，不是 Delete

Keep Codex Fast 的安全边界是 archive 而不是永久删除。README 中说明它可以处理旧的非 pinned active sessions、stale worktrees、较大的 `logs_2.sqlite*`、失效的 `config.toml` project references，以及 Windows extended path mismatch 等本地状态问题。

但它不会永久删除 chats、logs 或 worktrees，而是先写 backup/restore artifacts，再移动到 archive 位置。

### Backup-first Apply

项目提供了几种脚本模式：

- report-only；
- details；
- backup-only；
- apply；
- wait for Codex exit before applying。

这让它既可以作为 Codex skill 被自然语言调用，也可以由高级用户直接跑脚本。它还提醒用户：如果 Codex 正在运行，不要直接 mutate local state，应先关闭 Codex。

### Recurring Reminder，而不是自动清理

README 对定期维护的态度很保守：可以创建 weekly 或 biweekly reminder，但提醒不应该自动 archive、move、prune、rotate、normalize、delete 或 mutate。原因很现实：自动任务不知道用户是否已经为重要会话创建 handoff。

这个设计比“定时清理一切”更适合开发工作站。

## 为什么它属于这个 awesome 项目

这个 awesome 项目收的是 AI 时代提高开发效率的开源软件。Keep Codex Fast 的价值在于，它把 coding agent 的“运行卫生”变成一个可重复、可审计、可恢复的流程。

AI coding agent 会越来越像长期运行的开发环境，而不是一次性聊天窗口。长期使用后，性能和上下文管理会成为真实问题：

- 哪些会话还需要保留？
- 哪些旧线程应该转成 handoff？
- 哪些 worktree 已经过期？
- 哪些日志和本地数据库拖慢体验？
- 清理前有没有备份和恢复路径？

Keep Codex Fast 不提升模型智商，但能提升 agent 工作站的可维护性。这是 AI 开发效率工具中很容易被忽略的一层。

## 使用边界和注意事项

这个工具的边界必须明确：

- 它是 Codex-specific skill，不是通用系统清理工具。
- 它适合本地 Codex 状态维护，不应该被当成随意删除缓存的脚本。
- 真正 apply 前应该先确认重要会话已有 handoff，或明确不需要 handoff。
- 如果 Codex 正在运行，应该先退出 Codex，再做变更。
- backup 文件可能包含本地 Codex 元数据，不应直接公开分享。
- 自动化只能提醒，不应该自动执行 destructive 或 state-mutating maintenance。

## 适合谁使用

- 重度使用 Codex、经常多 repo 多线程开发的人。
- 经常 resume 旧会话，感觉 Codex 本地状态变重的用户。
- 需要把旧 agent 会话转成可继续交接文档的开发者。
- 想安全归档旧 chats、worktrees、logs，而不是直接删除的人。
- 想建立 weekly/biweekly Codex maintenance reminder 的用户。

## 项目信息

- GitHub: https://github.com/vibeforge1111/keep-codex-fast
- 技术栈: Python, Codex Skill
- License: MIT
- 当前 GitHub 页面显示约 763 stars，主仓库公开。

## 推荐 awesome 条目

```markdown
- [Keep Codex Fast](https://github.com/vibeforge1111/keep-codex-fast) - Backup-first Codex skill for inspecting, handing off, archiving, and recovering local Codex state without unsafe deletion. `Python` `MIT`
```
