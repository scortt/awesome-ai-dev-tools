# AI Agent 的 Unix 风格工具链

> 这是一组在 Unix / Plan 9 时代就存在或延续下来的小工具。到了 AI Agent、MCP、本地自动化和长任务工作流时代，它们重新变得很有价值。

这个文件关注的不是“大框架”，而是让 agent 更省 token、更安全地改文件、更可靠地跑任务、更容易管理配置、更方便桥接网络服务的胶水工具。

## 优先级地图

### 核心工作流工具

- [cdb](https://cr.yp.to/cdb.html) - Constant Database，极快的只读 key-value 数据库，适合结构化 agent 记忆、符号索引和本地元数据缓存。`C` `Public domain`
- [tinycdb](https://www.corpit.ru/mjt/tinycdb.html) - cdb 的小型实用实现，适合在本地 agent 系统中落地 cdb 风格索引。`C` `Public domain`
- [jq](https://github.com/jqlang/jq) - 命令行 JSON 处理器，用于在把 JSON 送给 LLM 前做提取、过滤、验证和压缩。`C` `MIT`
- [GNU Make](https://www.gnu.org/software/make/) - 跨语言构建与工作流编排工具；对 agent 来说，`make test`、`make backtest`、`make report` 就是可执行 SOP。`C` `GPL-3.0`
- Language Server - LSP server 给 coding agent 提供语义导航、诊断、定义、引用和类型信息，避免只靠裸文本猜测。
  - [rust-analyzer](https://github.com/rust-lang/rust-analyzer) - Rust 语言服务器。`Rust` `Apache-2.0 OR MIT`
  - [clangd](https://github.com/llvm/llvm-project/tree/main/clang-tools-extra/clangd) - C/C++ 语言服务器，基于 Clang/LLVM。`C++` `Apache-2.0 WITH LLVM-exception`
  - [Pyright](https://github.com/microsoft/pyright) - Python 静态类型检查器和语言服务器。`TypeScript` `MIT`
  - [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server) - TypeScript / JavaScript 的 LSP server。`TypeScript` `MIT`

### 推荐进入本地 agent 环境的工具

- [nq](https://github.com/leahneukirchen/nq) - 极简命令行任务队列，适合排队运行回测、数据下载、embedding、索引生成和报告生成。`C` `Public domain`
- [moreutils](https://joeyh.name/code/moreutils/) - 一组 Unix 小工具；对 agent 来说，最重要的是安全改文件和改善日志。`Various` `GPL-2.0`
  - `sponge` - 先读完全部输入再写输出，避免 agent 执行 `cmd file > file` 把文件写坏。
  - `ts` - 给每行输出加时间戳，不改程序代码也能看日志耗时。
  - `chronic` - 成功时静默，失败时输出，适合定时任务。
  - `pee`、`vipe`、`vidir` - 其他管道和编辑辅助工具，知道即可。
- [envdir](https://cr.yp.to/daemontools/envdir.html) - 用目录管理环境变量；一个文件对应一个变量，适合大量 MCP 凭证和模型 provider 配置。`C` `Public domain`
- [socat](http://www.dest-unreach.org/socat/) - 网络世界的管道工具，可桥接 TCP、Unix socket、PTY、串口等端点，适合 MCP transport、端口转发和本地服务调试。`C` `GPL-2.0`

### 结构化文本和 token 压缩工具

- [GNU recutils](https://www.gnu.org/software/recutils/) - 纯文本记录数据库，适合人类可编辑的结构化记忆和轻量目录。`C` `GPL-3.0`
- [jo](https://github.com/jpmens/jo) - 从 shell 参数生成 JSON，减少脚本里手写 JSON 的转义错误。`C` `GPL-2.0`
- [jc](https://github.com/kellyjonbrazil/jc) - 把 `ps`、`df`、`dig`、`netstat` 等命令输出转换成 JSON，再交给 `jq` 或 LLM 处理。`Python` `MIT`
- [gron](https://github.com/tomnomnom/gron) - 把 JSON 拍平成可 grep、可 diff 的赋值行，适合比较大型配置和回测结果。`Go` `MIT`

### 工作流和文件触发工具

- [redo](https://github.com/apenwarr/redo) - 受 redo 思想启发的构建系统；可作为 Make 的简洁替代思路了解，但 agent 生态里 Make 更通用。`Python` `Apache-2.0`
- [Task Spooler](https://viric.name/soft/ts/) - 功能更完整的本地任务队列，和 `nq` 同赛道，但队列查看与控制更强。`C` `GPL-2.0`
- [entr](https://github.com/eradman/entr) - 文件变化时自动执行命令，适合 watch-mode 测试和 agent 的改代码-跑测试循环。`C` `ISC`
- [inotify-tools](https://github.com/inotify-tools/inotify-tools) - Linux 文件事件工具集，包括 `inotifywait`，适合上传目录和事件驱动 pipeline。`C` `GPL-2.0`
- [fswatch](https://github.com/emcrisostomo/fswatch) - 跨平台文件变化监听工具，在 macOS 上尤其有用。`C++` `GPL-3.0`

### 日志和服务监督

- [multilog](https://cr.yp.to/daemontools/multilog.html) - daemontools 里的日志读取和轮转工具，适合理解长期 agent 日志管理。`C` `Public domain`
- [daemontools](https://cr.yp.to/daemontools.html) - 经典服务监督工具；现在多被 systemd 和容器替代，但思想很重要。`C` `Public domain`
- [runit](http://smarden.org/runit/) - 简单的 Unix 服务监督器，可用于理解常驻 MCP 和 agent 服务的守护方式。`C` `BSD-style`
- [s6](https://skarnet.org/software/s6/) - 更现代、更强的进程监督套件，支持服务树、ready 通知和可靠守护进程。`C` `ISC`
- [systemd](https://github.com/systemd/systemd) - 当前 Linux 主流服务管理器，适合部署长期运行的本地 agent、MCP server 和 API gateway。`C` `LGPL-2.1`
- [Docker Compose](https://github.com/docker/compose) - 多服务本地编排工具，适合同时管理多个 MCP server、gateway、数据库和 agent 进程。`Go` `Apache-2.0`

### 网络胶水和调试

- [netcat-openbsd](https://salsa.debian.org/debian/netcat-openbsd) - 简单 TCP/UDP 调试工具，用于检查端口、发送原始请求和测试服务。`C` `BSD-style`
- [tcpserver / ucspi-tcp](https://cr.yp.to/ucspi-tcp.html) - djb 生态里的小型 TCP server/client 工具，适合理解“把程序变成网络服务”的 Unix 思路。`C` `Public domain`
- [netpipes](https://web.purplefrog.com/~thoth/netpipes/) - 较老的网络管道工具集，今天更多是历史和思想价值。`C` `License: see project`

### Plan 9 和结构化编辑思想

- [Plan 9 from User Space](https://github.com/9fans/plan9port) - 把 Plan 9 的 `acme`、`sam`、`plumber` 等工具移植到 Unix-like 系统；适合理解文件化远程资源和文本即界面的思想。`C` `MIT`
- [plumber](https://9fans.github.io/plan9port/man/man4/plumber.html) - Plan 9 的消息路由系统，可以在程序之间传递文本、文件位置、URL 和命令；概念上接近现代 agent router 和 tool dispatch。`C` `MIT`
- [sam](https://9fans.github.io/plan9port/man/man1/sam.html) - 结构化文本编辑器，带命令语言和正则编辑能力，对代码感知编辑思想很有启发。`C` `MIT`
- [acme](https://9fans.github.io/plan9port/man/man1/acme.html) - Plan 9 编辑器和 shell 环境，把文本作为 UI；和今天 agent-native 文本界面有相似思想。`C` `MIT`
- [9P](https://9fans.github.io/plan9port/man/man3/intro.html) - Plan 9 文件协议；适合理解如何用统一接口暴露远程工具、资源和服务。

## 建议写进 AGENTS.md 的规则

```md
## Local tool discipline

- Prefer Makefile targets over ad-hoc command sequences when a workflow exists.
- Use `jq` to inspect, filter, and reduce JSON before asking the model to reason over it.
- Use `jc` to convert plain-text command output into JSON before filtering with `jq`.
- Use `nq` for long-running or resource-heavy jobs such as backtests, downloads, embedding/index generation, batch scans, and report generation.
- Use `sponge` when transforming a file and writing back to the same file.
- Prefer envdir-style secrets for many MCP credentials and API provider settings: one file per environment variable.
- Prefer language-server diagnostics, definitions, references, and type information before guessing from raw text.
- Use `socat` or `nc` for local network debugging and temporary protocol/port bridges.
```

## AI 时代实用优先级

1. `cdb` / `tinycdb`：结构化记忆和本地索引。
2. `jq`：JSON token 压缩。
3. `make`：跨语言可执行工作流。
4. LSP server：语义代码理解。
5. `nq`：长任务排队。
6. `sponge`：安全原地改文件。
7. `envdir`：大量 MCP/API 密钥管理。
8. `socat`：协议和端口桥接。
9. `jc`：命令输出转 JSON。
10. `entr` / `fswatch` / `inotifywait`：需要时做文件触发循环。
