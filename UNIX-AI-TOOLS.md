# Classic Unix Tools For AI-Era Development

> Small, composable tools that make AI coding agents, MCP servers, backtest pipelines, and multi-language engineering workflows cheaper, safer, and easier to operate.

This page collects classic Unix-style tools that are especially useful when an AI agent needs to inspect files, reduce context, transform structured data, queue long jobs, manage configuration, monitor services, or bridge local and remote systems.

## Priority Map

### Tier 1: put into the active toolchain

- `cdb` / `tinycdb` - Fast read-heavy key-value stores for structured agent memory, file summaries, symbol maps, and deterministic lookup tables.
- `jq` - JSON filtering and transformation. Use it to reduce API responses, logs, and backtest outputs before sending anything to an LLM.
- `make` - Cross-language workflow orchestration. Treat `Makefile` targets as executable SOPs for coding agents.
- LSP servers - Code intelligence for agents: definitions, references, types, diagnostics, and refactor safety.

### Tier 2: recommended for agent and MCP environments

- `nq` - Minimal command-line task queue for long-running jobs such as backtests, report generation, data downloads, embeddings, and batch scans.
- `sponge` - Safe in-place file updates from `moreutils`; prevents accidentally overwriting a file while reading from it.
- `envdir` - Directory-based environment variables; one file per secret or setting. Useful when many MCP servers and providers need separate credentials.
- `socat` - Network glue for bridging TCP, Unix sockets, serial ports, stdio-style services, and local debugging endpoints.

### Tier 3: useful when the workflow needs them

- `jc` - Converts command output such as `ps`, `df`, `dig`, and `ifconfig` into JSON so agents can inspect system state through `jq`.
- `nc` / `netcat` - Lightweight network probe for testing ports, sockets, and simple protocol interactions.
- `entr` - Runs commands when watched files change. Useful for edit-test loops and local development automation.

### Tier 4: keep in the toolbox

- `gron` - Flattens JSON into line-oriented assignments, making `grep` and `diff` useful for large nested JSON files.
- `fswatch` - Cross-platform file-change watcher, especially useful on macOS for upload folders and file-driven pipelines.
- `inotifywait` - Linux file-change watcher for event-driven server workflows.

### Tier 5: understand the idea, use modern replacements when appropriate

- `ts` from `moreutils` - Adds timestamps to each output line. Useful for ad-hoc logs.
- `chronic` from `moreutils` - Suppresses successful command output and only shows output on failure.
- `redo` - Simpler rebuild tool inspired by `make`; useful to understand, but less common than `make` in agent workflows.
- `multilog` - Classic log rotation tool; useful conceptually, but often replaced by journald, Docker logs, Loki, or application logging.
- `daemontools`, `runit`, `s6` - Service supervision systems. The idea matters; many modern deployments use `systemd`, Docker Compose, or Kubernetes instead.
- `tcpserver` / `ucspi-tcp` - Classic Unix network service wrappers; mostly useful as design references today.
- `netpipes` - Old network pipe toolkit; useful historically, usually replaced by `socat`, SSH, or modern proxies.

## Tool Notes

### cdb / tinycdb

Use for deterministic, read-heavy lookup tables. Good examples:

- file path -> summary
- symbol -> metadata
- strategy id -> parameters
- prompt id -> canonical instruction
- task id -> status

Do not use cdb for semantic memory. Pair it with embeddings or a vector store when the agent needs fuzzy recall.

### jq

Use before calling the model whenever the input is JSON.

Examples:

```bash
jq 'keys' result.json
jq '.trades[-20:]' backtest.json
jq '{summary, metrics, recent_trades: .trades[-20:]}' backtest.json
```

Agent rule:

```text
Do not paste large raw JSON into the model if the required fields can be extracted with jq.
```

### jo

Generates JSON from shell arguments.

```bash
jo symbol=AAPL price=200 qty=10
```

Useful for small shell scripts and API calls, but less important when the project already uses Python, Rust, or TypeScript for JSON generation.

### jc

Converts many plain-text command outputs into JSON.

```bash
ps aux | jc --ps | jq '.[] | {user, pid, cpu_percent, mem_percent, command}'
df -h | jc --df | jq '.[] | {filesystem, size, used, available, capacity}'
dig example.com | jc --dig | jq '.answer'
```

Best for server inspection, debugging, and agent-operated ops workflows.

### gron

Flattens JSON for line-oriented diffing.

```bash
gron config.old.json > old.txt
gron config.new.json > new.txt
diff old.txt new.txt
```

Useful when a backtest result changed and the first question is: what parameter changed?

### moreutils: sponge, ts, chronic

`sponge` is the most important one for agent workflows.

Bad:

```bash
jq '.risk = 1.0' config.json > config.json
```

Good:

```bash
jq '.risk = 1.0' config.json | sponge config.json
```

`ts` is useful for quick logging:

```bash
make backtest | ts >> logs/backtest.log
```

`chronic` is useful for scheduled jobs that should stay silent unless they fail:

```bash
chronic make nightly-backtest
```

### make

Use `make` as a cross-language workflow layer, not just as a compiler helper.

Example:

```make
.PHONY: test backtest report index

test:
	cargo test

backtest:
	cargo run --release -- backtest

report:
	python scripts/build_report.py

index:
	python scripts/build_index.py
```

Agent rule:

```text
Prefer Makefile targets over inventing ad-hoc command sequences.
```

### nq and task-spooler

Use a queue for expensive jobs.

```bash
nq make backtest
nq make report
nq python scripts/build_index.py
```

`nq` is minimal. `task-spooler` is more featureful. Start with `nq` unless the project needs queue inspection, concurrency control, or job management.

### entr, inotifywait, fswatch

Use these for file-driven loops.

Development watch loop:

```bash
ls src/*.rs tests/*.rs | entr make test
```

Mac upload-folder workflow:

```bash
fswatch uploads/ | while read file; do make process-upload; done
```

Linux upload-folder workflow:

```bash
inotifywait -m uploads/
```

### envdir

Use directory-based configuration when there are many providers, MCP servers, or per-agent credentials.

```text
env/
├── OPENAI_API_KEY
├── DATABENTO_KEY
├── GITHUB_TOKEN
├── CAD_MCP_URL
└── TRADING_MCP_URL
```

Run:

```bash
envdir env make backtest
```

Agent rule:

```text
Prefer changing one environment-variable file over rewriting a large .env file when envdir is used.
```

### multilog, runit, s6, daemontools

These are classic service-operation tools. The important concept is service supervision:

```text
start service -> monitor process -> restart on crash -> collect logs
```

For modern AI and MCP deployments, common replacements are:

- `systemd` for Linux hosts
- Docker Compose for small service groups
- Kubernetes for large deployments
- Loki / journald / application-native tracing for logs

### nc and socat

`nc` is for probing:

```bash
nc -vz localhost 3000
```

`socat` is for bridging:

```bash
socat TCP-LISTEN:9000,fork TCP:127.0.0.1:8000
```

`socat` is especially useful around MCP, local API gateways, Unix sockets, temporary TCP exposure, and protocol mismatch debugging.

### Plan 9 ideas: 9P, plumber, sam, acme

These are mostly design references rather than daily tools.

- `9P` - Treat local and remote resources as file-like interfaces.
- `plumber` - Message router between programs; conceptually similar to tool routing or agent routing.
- `sam` - Structural editing ideas that anticipate modern AST-based tools, tree-sitter, ast-grep, and LSP-based refactors.
- `acme` - Text as UI; a useful mental model for commandable agent workspaces.

## LSP Servers For AI Coding Agents

Language servers are not classic Unix tools, but they should be part of the same AI development environment.

Recommended defaults:

- Rust: `rust-analyzer`
- TypeScript / JavaScript: `typescript-language-server`
- Python: `pyright`
- C / C++: `clangd`
- Go: `gopls`

Agent rule:

```text
Before large refactors, prefer LSP-backed definitions, references, diagnostics, and type information over guessing from raw text.
```

## Suggested AGENTS.md Snippet

```md
## Tooling Discipline

- `jq`, `make`, `nq`, `moreutils`, and `socat` may be available in this environment.
- Prefer `Makefile` targets over manually inventing command sequences.
- Use `jq` to inspect, filter, and reduce JSON before analysis.
- Use `jc` for plain-text command output when structured system inspection is needed.
- Use `nq` for long-running or resource-heavy tasks such as backtests, report generation, data downloads, embeddings, and batch scans.
- Use `sponge` when transforming a file and writing back to the same file.
- Prefer `envdir`-style one-file-per-variable configuration when managing many MCP or provider credentials.
- Use `socat` for temporary socket/TCP bridging and local service debugging.
- Do not paste large raw JSON, logs, or command output into the model unless explicitly necessary.

## Code Intelligence

- Language servers should be available for supported project languages.
- Prefer LSP-based code navigation and diagnostics before guessing from raw text.
- Rust projects should use `rust-analyzer`.
- TypeScript projects should use `typescript-language-server`.
- Python projects should use `pyright`.
- C/C++ projects should use `clangd`.
```
