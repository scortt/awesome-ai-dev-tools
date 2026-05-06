# Awesome AI Dev Tools

> A curated list of open source software that improves how developers build, test, review, document, and ship software in the AI era.

This list is not a general "awesome open source" directory. It focuses on tools that change the development workflow itself: coding agents, agent runtimes, model context, codebase indexing, AI-assisted review, browser automation, evals, local model infrastructure, and the glue that makes AI useful inside real engineering loops.

## Contents

- [Scope](#scope)
- [Selection Criteria](#selection-criteria)
- [Coding Agents And AI IDEs](#coding-agents-and-ai-ides)
- [Agent Runtimes And Frameworks](#agent-runtimes-and-frameworks)
- [Model Context Protocol](#model-context-protocol)
- [Codebase Search And Indexing](#codebase-search-and-indexing)
- [Review And Change-Inspection UI](#review-and-change-inspection-ui)
- [Browser And UI Automation](#browser-and-ui-automation)
- [Testing, Evals, And Benchmarks](#testing-evals-and-benchmarks)
- [Local Models And Inference](#local-models-and-inference)
- [Audio And Multimodal Workflows](#audio-and-multimodal-workflows)
- [Prompt, Context, And Memory](#prompt-context-and-memory)
- [Docs, Knowledge, And RAG](#docs-knowledge-and-rag)
- [Sandboxes And Secure Execution](#sandboxes-and-secure-execution)
- [Contribution Workflow](#contribution-workflow)

## Scope

Included:

- Open source tools used by developers, agents, or engineering teams.
- Tools that improve AI-assisted implementation, debugging, review, testing, documentation, deployment, or project navigation.
- Infrastructure that makes AI coding agents more reliable: context servers, sandboxes, eval harnesses, browser control, code search, and reproducible environments.

Not included by default:

- Generic libraries that do not directly improve AI-assisted development.
- Closed-source SaaS products without a meaningful open source core.
- One-off prompts with no maintained software around them.
- Model leaderboards that are not tied to developer workflow improvement.

## Selection Criteria

Each entry should answer at least two of these questions:

- Does it shorten a real development loop?
- Does it let an AI agent inspect, change, test, or verify software more safely?
- Does it improve codebase context quality?
- Does it make agent behavior more reproducible or measurable?
- Is it actively usable by maintainers today?

Preferred entry format:

```markdown
- [Project](https://github.com/org/project) - Short, concrete description. `Language` `License`
```

## Coding Agents And AI IDEs

- [OpenAI Codex CLI](https://github.com/openai/codex) - Terminal coding agent for reading, editing, running, and verifying code in a local workspace. `Rust` `Apache-2.0`
- [Claude Code](https://github.com/anthropics/claude-code) - Agentic coding tool that works from the terminal, IDE, and GitHub workflows. `Shell` `License: see repository`
- [Aider](https://github.com/Aider-AI/aider) - AI pair programming in the terminal with strong Git integration and codebase maps. `Python` `Apache-2.0`
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open platform for software development agents with code editing, shell, browser, and workflow automation. `Python` `MIT`
- [Cline](https://github.com/cline/cline) - VS Code coding agent that can edit files, run commands, use browser context, and call MCP tools with user approval. `TypeScript` `Apache-2.0`
- [Continue](https://github.com/continuedev/continue) - Open source AI code assistant for IDEs with model, context, and autocomplete customization. `TypeScript` `Apache-2.0`

## Agent Runtimes And Frameworks

- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for building stateful, controllable agent workflows. `Python` `MIT`
- [AutoGen](https://github.com/microsoft/autogen) - Framework for building multi-agent AI applications and workflows. `Python` `MIT`
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-based AI agents and task workflows. `Python` `MIT`
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Also useful as a reference implementation for practical software-engineering agents. `Python` `MIT`

## Model Context Protocol

- [Model Context Protocol](https://github.com/modelcontextprotocol) - Open protocol and SDK ecosystem for connecting AI applications to tools, data, and context.
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Reference MCP server implementations and pointers to the broader registry. `TypeScript` `Python`
- [FastMCP](https://github.com/jlowin/fastmcp) - Python framework for building MCP servers quickly. `Python` `Apache-2.0`

## Codebase Search And Indexing

- [Sourcegraph Cody](https://github.com/sourcegraph/cody) - AI coding assistant backed by code search and repository context. `TypeScript` `Apache-2.0`
- [Grep App](https://github.com/grep-app/grep) - Fast source-code search service useful for agent and human code navigation. `Go` `MIT`
- [Serena](https://github.com/oraios/serena) - Coding-agent toolkit focused on semantic code retrieval and editing. `Python` `MIT`

## Review And Change-Inspection UI

- [Pierre](https://github.com/pierrecomputer/pierre) - Open source TypeScript monorepo behind AI-friendly code review primitives such as diff rendering and file tree rendering. `TypeScript` `License: see repository`

## Browser And UI Automation

- [Browser Use](https://github.com/browser-use/browser-use) - Makes websites accessible to AI agents and supports browser task automation. `Python` `MIT`
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - MCP server for giving agents structured browser automation through Playwright. `TypeScript` `Apache-2.0`
- [Stagehand](https://github.com/browserbase/stagehand) - AI-friendly browser automation framework built on Playwright. `TypeScript` `MIT`

## Testing, Evals, And Benchmarks

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Benchmark for evaluating software-engineering agents on real GitHub issues. `Python` `MIT`
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Evaluation framework for large language model systems. `Python` `MIT`
- [OpenAI Evals](https://github.com/openai/evals) - Framework and registry for evaluating LLM behavior. `Python` `MIT`
- [promptfoo](https://github.com/promptfoo/promptfoo) - Test and evaluate prompts, models, and LLM applications in CI-style workflows. `TypeScript` `MIT`

## Local Models And Inference

- [Ollama](https://github.com/ollama/ollama) - Run and manage local language models with a simple developer workflow. `Go` `MIT`
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Efficient local inference for LLMs across CPUs and GPUs. `C++` `MIT`
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput LLM serving engine for production and research use. `Python` `Apache-2.0`
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified API gateway and SDK for calling many model providers. `Python` `MIT`

## Audio And Multimodal Workflows

- [Voice Pro](https://github.com/abus-aikorea/voice-pro) - Gradio WebUI for speech recognition, translation, subtitle generation, TTS, voice cloning, and multilingual dubbing workflows. `Python` `GPL-3.0`

## Prompt, Context, And Memory

- [Fabric](https://github.com/danielmiessler/fabric) - Open source framework for reusable AI patterns and prompt workflows. `Go` `MIT`
- [OpenAI Swarm](https://github.com/openai/swarm) - Educational framework for lightweight multi-agent orchestration. `Python` `MIT`
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI agents and assistants. `Python` `Apache-2.0`

## Docs, Knowledge, And RAG

- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for connecting LLM applications to private and domain-specific data. `Python` `MIT`
- [Haystack](https://github.com/deepset-ai/haystack) - Framework for building search, RAG, and agentic knowledge applications. `Python` `Apache-2.0`
- [DocsGPT](https://github.com/arc53/DocsGPT) - Open source assistant for querying documentation and internal knowledge. `Python` `MIT`
- [RaTeX](https://github.com/erweixin/RaTeX) - Pure Rust KaTeX-compatible math renderer for native, web, server-side PNG/SVG/PDF, and AI document workflows. `Rust` `License: see repository`

## Sandboxes And Secure Execution

- [E2B](https://github.com/e2b-dev/E2B) - Secure sandboxes for AI agents and code execution. `TypeScript` `Apache-2.0`
- [Daytona](https://github.com/daytonaio/daytona) - Development environment manager and sandbox infrastructure for AI coding agents. `Go` `AGPL-3.0`
- [Devbox](https://github.com/jetify-com/devbox) - Reproducible development environments powered by Nix. `Go` `Apache-2.0`

## Contribution Workflow

1. Open an issue or pull request with the project link and the category.
2. Explain how it improves AI-era development efficiency.
3. Prefer concrete workflow evidence over marketing language.
4. Keep descriptions short and factual.
5. Avoid star-count-only arguments.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full curation policy.

## License

This list is released under [CC0 1.0](LICENSE). Project names and links belong to their respective owners.
