# Unix-Style Tools For AI Agents

> Classic Unix and Plan 9 inspired tools that become more valuable when coding agents, MCP servers, local workflows, and long-running automation need reliable glue.

This document focuses on small tools that help agents reduce token usage, inspect local systems, queue work, manage configuration, bridge network protocols, and operate codebases more safely.

## Priority Map

### Core agent workflow tools

- [cdb](https://cr.yp.to/cdb.html) - Constant database format for extremely fast read-only key-value lookup; useful for structured agent memory, symbol indexes, and local metadata caches. `C` `Public domain`
- [tinycdb](https://www.corpit.ru/mjt/tinycdb.html) - Compact implementation of cdb tools and library; a practical way to use cdb-style indexes in local agent systems. `C` `Public domain`
- [jq](https://github.com/jqlang/jq) - Command-line JSON processor for extracting, filtering, validating, and reducing JSON before sending context to an LLM. `C` `MIT`
- [GNU Make](https://www.gnu.org/software/make/) - Cross-language build and workflow orchestrator; useful as an executable SOP for agents through targets such as `make test`, `make backtest`, and `make report`. `C` `GPL-3.0`
- Language servers - LSP servers give coding agents semantic navigation, diagnostics, definitions, references, and type information instead of raw text guessing.
  - [rust-analyzer](https://github.com/rust-lang/rust-analyzer) - Rust language server for semantic code intelligence. `Rust` `Apache-2.0 OR MIT`
  - [clangd](https://github.com/llvm/llvm-project/tree/main/clang-tools-extra/clangd) - C/C++ language server backed by Clang and LLVM. `C++` `Apache-2.0 WITH LLVM-exception`
  - [Pyright](https://github.com/microsoft/pyright) - Python static type checker and language server. `TypeScript` `MIT`
  - [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server) - LSP wrapper for TypeScript and JavaScript projects. `TypeScript` `MIT`

### Recommended local agent environment tools

- [nq](https://github.com/leahneukirchen/nq) - Minimal command-line job queue for long-running backtests, data downloads, embedding jobs, indexing, and report generation. `C` `Public domain`
- [moreutils](https://joeyh.name/code/moreutils/) - Collection of small Unix utilities; especially useful for agent-safe file rewrites and readable logs. `Various` `GPL-2.0`
  - `sponge` - Read all input before writing output; prevents agents from corrupting files with `cmd file > file` patterns.
  - `ts` - Prefix output lines with timestamps for quick log timing without changing application code.
  - `chronic` - Suppress successful command output and only show logs on failure, useful for scheduled jobs.
  - `pee`, `vipe`, `vidir` - Additional pipeline and editing helpers worth knowing.
- [envdir](https://cr.yp.to/daemontools/envdir.html) - Directory-based environment-variable management; one file per variable, useful for many MCP credentials and provider settings. `C` `Public domain`
- [socat](http://www.dest-unreach.org/socat/) - Multipurpose relay for TCP, Unix sockets, PTYs, serial ports, and other endpoints; useful for bridging local services, MCP transports, and debugging network glue. `C` `GPL-2.0`

### Structured text and token-reduction helpers

- [GNU recutils](https://www.gnu.org/software/recutils/) - Plain-text record database for human-editable structured memory and lightweight local catalogs. `C` `GPL-3.0`
- [jo](https://github.com/jpmens/jo) - Small utility for generating JSON from shell arguments; reduces fragile hand-written JSON in scripts. `C` `GPL-2.0`
- [jc](https://github.com/kellyjonbrazil/jc) - Converts common command output such as `ps`, `df`, `dig`, and `netstat` into JSON for `jq` and LLM workflows. `Python` `MIT`
- [gron](https://github.com/tomnomnom/gron) - Flattens JSON into greppable assignment lines; useful for diffing huge config or backtest JSON files. `Go` `MIT`

### Workflow and file-trigger tools

- [redo](https://github.com/apenwarr/redo) - Simple build system inspired by redo; useful to understand as a cleaner alternative to Make, though Make remains more common for agents. `Python` `Apache-2.0`
- [Task Spooler](https://viric.name/soft/ts/) - Feature-rich local job queue; similar to `nq` but with more queue inspection and control. `C` `GPL-2.0`
- [entr](https://github.com/eradman/entr) - Run commands when watched files change; useful for watch-mode testing and agent edit-test loops. `C` `ISC`
- [inotify-tools](https://github.com/inotify-tools/inotify-tools) - Linux file-event tools including `inotifywait`; useful for upload directories and event-driven pipelines. `C` `GPL-2.0`
- [fswatch](https://github.com/emcrisostomo/fswatch) - Cross-platform file change monitor, especially practical on macOS where Linux inotify is unavailable. `C++` `GPL-3.0`

### Logging and service supervision

- [multilog](https://cr.yp.to/daemontools/multilog.html) - Log reader and rotator from daemontools; useful as a small conceptual model for long-running agent logs. `C` `Public domain`
- [daemontools](https://cr.yp.to/daemontools.html) - Classic service supervision toolkit; mostly superseded by systemd and containers, but important historically. `C` `Public domain`
- [runit](http://smarden.org/runit/) - Simple Unix service supervisor; useful conceptually for always-on MCP and agent services. `C` `BSD-style`
- [s6](https://skarnet.org/software/s6/) - Modern supervision suite for service trees, process readiness, and reliable daemons. `C` `ISC`
- [systemd](https://github.com/systemd/systemd) - Current mainstream Linux service manager for long-running local agents, MCP servers, and API gateways. `C` `LGPL-2.1`
- [Docker Compose](https://github.com/docker/compose) - Practical service orchestration for multiple local MCP servers, gateways, databases, and agent processes. `Go` `Apache-2.0`

### Network glue and debugging

- [netcat-openbsd](https://salsa.debian.org/debian/netcat-openbsd) - Simple TCP/UDP debugging tool for checking ports, sending raw requests, and testing services. `C` `BSD-style`
- [tcpserver / ucspi-tcp](https://cr.yp.to/ucspi-tcp.html) - Small TCP server/client tools from the djb ecosystem; useful historically and conceptually for turning programs into network services. `C` `Public domain`
- [netpipes](https://web.purplefrog.com/~thoth/netpipes/) - Older collection of network pipeline tools; mostly historical, but aligned with Unix network-glue thinking. `C` `License: see project`

### Plan 9 and structural editing ideas

- [Plan 9 from User Space](https://github.com/9fans/plan9port) - Ports Plan 9 tools such as `acme`, `sam`, and `plumber` to Unix-like systems; useful for understanding file-oriented distributed tools and text-as-interface workflows. `C` `MIT`
- [plumber](https://9fans.github.io/plan9port/man/man4/plumber.html) - Plan 9 message-routing system that lets programs hand off text, file locations, URLs, and commands; conceptually close to modern agent routers and tool dispatch. `C` `MIT`
- [sam](https://9fans.github.io/plan9port/man/man1/sam.html) - Structural text editor with command language and regular-expression editing; historically important for thinking about code-aware editing. `C` `MIT`
- [acme](https://9fans.github.io/plan9port/man/man1/acme.html) - Plan 9 editor and shell environment where text acts as UI; relevant to agent-native text interfaces. `C` `MIT`
- [9P](https://9fans.github.io/plan9port/man/man3/intro.html) - Plan 9 file protocol; conceptually useful for thinking about exposing remote tools, resources, and services through uniform interfaces.

## Suggested AGENTS.md Rules

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

## Practical Priority For AI-Era Development

1. `cdb` / `tinycdb` for structured memory and local indexes.
2. `jq` for JSON token reduction.
3. `make` for cross-language executable workflows.
4. LSP servers for semantic code intelligence.
5. `nq` for queueing long-running jobs.
6. `sponge` for safe in-place file rewrites.
7. `envdir` for many MCP/API secrets.
8. `socat` for protocol and port bridging.
9. `jc` for turning command output into JSON.
10. `entr` / `fswatch` / `inotifywait` for file-triggered loops when needed.
