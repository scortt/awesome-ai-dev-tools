# Awesome AI Dev Tools

> A curated list of open source software that improves how developers build, test, review, document, and ship software in the AI era.

[中文版](README.zh-CN.md)

This list is not a general "awesome open source" directory. It focuses on tools that change the development workflow itself: coding agents, agent runtimes, model context, codebase indexing, AI-assisted review, browser automation, evals, local model infrastructure, and the glue that makes AI useful inside real engineering loops.

## Contents

- [Scope](#scope)
- [Selection Criteria](#selection-criteria)
- [Coding Agents And AI IDEs](#coding-agents-and-ai-ides)
- [Agent Operations And Maintenance](#agent-operations-and-maintenance)
- [Agent Runtimes And Frameworks](#agent-runtimes-and-frameworks)
- [Model Context Protocol](#model-context-protocol)
- [Codebase Search And Indexing](#codebase-search-and-indexing)
- [Review And Change-Inspection UI](#review-and-change-inspection-ui)
- [Design, Prototyping, And Artifacts](#design-prototyping-and-artifacts)
- [3D And Asset Generation](#3d-and-asset-generation)
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
- [OpenManus](https://github.com/FoundationAgents/OpenManus) - Open source general agent project for building and studying autonomous task execution workflows. `Python` `MIT`
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - AI developer agent that plans, implements, and iterates on software projects from natural-language requirements. `Python` `License: see repository`
- [Claude Engineer](https://github.com/Doriandarko/claude-engineer) - CLI and web coding assistant that lets Claude create and use project-specific tools during development sessions. `Python` `License: see repository`
- [Open Interpreter](https://github.com/openinterpreter/open-interpreter) - Natural-language computer interface for running code, using the shell, and operating local workflows. `Python` `AGPL-3.0`
- [AIlice](https://github.com/myshell-ai/AIlice) - General-purpose autonomous agent runtime with shell, browser, and tool-use workflows. `Python` `MIT`

## Agent Operations And Maintenance

- [Keep Codex Fast](https://github.com/vibeforge1111/keep-codex-fast) - Backup-first Codex skill for inspecting, handing off, archiving, and recovering local Codex state without unsafe deletion. `Python` `MIT`
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) - Single-file Claude Code guidance distilled into practical coding-agent behavior rules. `License: see repository`
- [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) - Agent and skill system for coordinating Claude Code across game-development roles and workflows. `Shell` `MIT`
- [Claude HUD](https://github.com/jarrodwatts/claude-hud) - Claude Code plugin for surfacing context usage, tool activity, running agents, and todo progress. `JavaScript` `MIT`
- [Autoresearch](https://github.com/karpathy/autoresearch) - Autonomous research loop for running, judging, and iterating experiments around model-training tasks. `Python` `License: see repository`
- [Claude Autoresearch Skill](https://github.com/uditgoenka/autoresearch) - Claude Code skill for goal-directed modify, verify, keep-or-discard research loops. `JavaScript` `MIT`
- [RTK](https://github.com/rtk-ai/rtk) - CLI proxy that compresses common developer-command output before sending it to LLM workflows. `Rust` `Apache-2.0`
- [Superpowers](https://github.com/obra/superpowers) - Agentic skills framework and software-development methodology for AI-assisted engineering work. `Shell` `MIT`
- [GStack](https://github.com/garrytan/gstack) - Claude Code setup with role-specific tools for design, engineering management, release, docs, and QA. `TypeScript` `MIT`
- [Remodex](https://github.com/Emanuele-web04/remodex) - Remote-control client for operating Codex sessions from macOS. `Swift` `Apache-2.0`
- [Happy](https://github.com/slopus/happy) - Mobile and web client for Codex and Claude Code with realtime voice and encrypted sessions. `TypeScript` `MIT`

## Agent Runtimes And Frameworks

- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for building stateful, controllable agent workflows. `Python` `MIT`
- [AutoGen](https://github.com/microsoft/autogen) - Framework for building multi-agent AI applications and workflows. `Python` `MIT`
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-based AI agents and task workflows. `Python` `MIT`
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Also useful as a reference implementation for practical software-engineering agents. `Python` `MIT`
- [Dify](https://github.com/langgenius/dify) - Platform for building and operating agentic LLM workflows with tools, datasets, and application deployment. `TypeScript` `License: see repository`
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Multi-agent framework that models software-company roles for natural-language programming workflows. `Python` `MIT`
- [Eko](https://github.com/FellouAI/eko) - Agentic workflow framework for turning natural-language tasks into production-oriented automation. `TypeScript` `MIT`
- [n8n](https://github.com/n8n-io/n8n) - Workflow automation platform with native AI nodes for tool orchestration and integration-heavy agent workflows. `TypeScript` `License: see repository`
- [MiniAGI](https://github.com/muellerberndt/mini-agi) - Minimal autonomous agent implementation for experimenting with OpenAI-backed task loops. `Python` `MIT`
- [Zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) - Small autonomous assistant infrastructure for deploying and swapping agent components across environments. `Rust` `Apache-2.0`

## Model Context Protocol

- [Model Context Protocol](https://github.com/modelcontextprotocol) - Open protocol and SDK ecosystem for connecting AI applications to tools, data, and context.
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Reference MCP server implementations and pointers to the broader registry. `TypeScript` `Python`
- [FastMCP](https://github.com/jlowin/fastmcp) - Python framework for building MCP servers quickly. `Python` `Apache-2.0`
- [Unity MCP](https://github.com/CoplayDev/unity-mcp) - MCP bridge that lets AI assistants inspect assets, control scenes, edit scripts, and automate Unity Editor work. `C#` `MIT`
- [TradingView MCP](https://github.com/atilaahmettaner/tradingview-mcp) - MCP server for exposing market screening, technical indicators, and chart context to AI assistants. `Python` `MIT`

## Codebase Search And Indexing

- [Sourcegraph Cody](https://github.com/sourcegraph/cody) - AI coding assistant backed by code search and repository context. `TypeScript` `Apache-2.0`
- [Grep App](https://github.com/grep-app/grep) - Fast source-code search service useful for agent and human code navigation. `Go` `MIT`
- [Serena](https://github.com/oraios/serena) - Coding-agent toolkit focused on semantic code retrieval and editing. `Python` `MIT`
- [Repomix](https://github.com/yamadashy/repomix) - Packs a repository into an AI-friendly file for sharing codebase context with LLMs and coding agents. `TypeScript` `MIT`
- [Devv](https://github.com/devv-ai/devv) - AI-powered developer search engine for finding implementation details, APIs, and engineering references. `License: see repository`
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - Incremental indexing engine for long-horizon agents that need fresh, queryable project context. `Python` `Apache-2.0`

## Review And Change-Inspection UI

- [Pierre](https://github.com/pierrecomputer/pierre) - Open source TypeScript monorepo behind AI-friendly code review primitives such as diff rendering and file tree rendering. `TypeScript` `License: see repository`

## Design, Prototyping, And Artifacts

- [Open Design](https://github.com/nexu-io/open-design) - Local-first design workflow that turns coding-agent CLIs into generators for prototypes, decks, mobile screens, dashboards, media, and exportable artifacts. `TypeScript` `Apache-2.0`
- [Open Slide](https://github.com/1weiho/open-slide) - Agent-native React slide framework with fixed-canvas authoring, comments, present mode, and HTML/PDF export. `TypeScript` `MIT`
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) - Single-binary Office document toolkit that lets AI agents create, inspect, edit, and render Word, Excel, and PowerPoint files without Microsoft Office. `C#` `Apache-2.0`
- [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) - Claude Code and Codex skill for generating single-file horizontal-swipe HTML decks, presentation visuals, and social covers from prompts. `HTML` `MIT`
- [Impeccable](https://github.com/pbakaus/impeccable) - Design language and guidance for improving AI-generated product interfaces. `JavaScript` `Apache-2.0`
- [Awesome Design Skills](https://github.com/bergside/awesome-design-skills) - Curated DESIGN.md and SKILL.md files for design-focused coding agents. `MIT`
- [Awesome Design.md](https://github.com/VoltAgent/awesome-design-md) - Collection of brand design-system files that help coding agents produce matching UI. `MIT`
- [Architecture Diagram Generator](https://github.com/Cocoon-AI/architecture-diagram-generator) - Claude skill for generating standalone HTML and SVG system architecture diagrams. `HTML` `MIT`
- [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) - Web slide framework designed for coding agents that generate frontend-based presentations. `JavaScript` `MIT`
- [Onlook](https://github.com/onlook-dev/onlook) - AI-first visual editor for building, styling, and editing React applications. `TypeScript` `Apache-2.0`
- [OpenUI](https://github.com/wandb/openui) - Live UI generation tool that renders interface descriptions into editable components. `TypeScript` `Apache-2.0`
- [Screenshot to Code](https://github.com/abi/screenshot-to-code) - Converts screenshots into HTML, Tailwind, React, or Vue implementations. `TypeScript` `MIT`
- [Assistant UI](https://github.com/assistant-ui/assistant-ui) - React component library for building AI chat and assistant interfaces. `TypeScript` `MIT`
- [Creative Tim UI](https://github.com/creativetimofficial/ui) - Open source components, blocks, and agents exposed through registry and MCP workflows. `TypeScript` `MIT`

## 3D And Asset Generation

- [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) - Image-to-3D asset generation system with open weights, training code, mesh generation, PBR texture synthesis, Gradio app, and API server. `Python` `License: see repository`
- [3DCellForge](https://github.com/huangserva/3DCellForge) - Browser-based 3D cell generation and exploration studio with React Three Fiber, GLB import/export, and optional Tripo or Hunyuan3D image-to-3D backends. `JavaScript` `MIT`
- [WorldGen](https://github.com/ZiYang-xie/WorldGen) - Text-to-3D scene generation system for creating interactive environments and asset prototypes. `Python` `Apache-2.0`

## Browser And UI Automation

- [Browser Use](https://github.com/browser-use/browser-use) - Makes websites accessible to AI agents and supports browser task automation. `Python` `MIT`
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - MCP server for giving agents structured browser automation through Playwright. `TypeScript` `Apache-2.0`
- [Stagehand](https://github.com/browserbase/stagehand) - AI-friendly browser automation framework built on Playwright. `TypeScript` `MIT`
- [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) - Stealth Chromium build that can be used as a Playwright-compatible browser automation target. `Python` `MIT`
- [Agent Browser](https://github.com/vercel-labs/agent-browser) - Browser automation CLI designed for AI agents. `Rust` `Apache-2.0`
- [Maestro](https://github.com/mobile-dev-inc/Maestro) - Declarative automation framework for mobile and web end-to-end flows. `Kotlin` `Apache-2.0`
- [OpenAI CUA Sample App](https://github.com/openai/openai-cua-sample-app) - Sample application for using computer-using agents across browser and desktop environments. `TypeScript` `MIT`
- [Self Operating Computer](https://github.com/OthersideAI/self-operating-computer) - Multimodal framework for letting AI operate a computer through visual context and actions. `Python` `MIT`

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
- [MLX](https://github.com/ml-explore/mlx) - Array framework for running and experimenting with machine learning workloads on Apple silicon. `C++` `MIT`
- [llm.c](https://github.com/karpathy/llm.c) - Small C and CUDA implementation of LLM training for understanding and modifying model internals. `Cuda` `MIT`
- [llama2.c](https://github.com/karpathy/llama2.c) - Minimal C implementation of Llama 2 inference useful for studying portable local model runtimes. `C` `MIT`
- [tinygrad](https://github.com/tinygrad/tinygrad) - Small neural-network framework and compiler stack for local model experimentation. `Python` `MIT`

## Audio And Multimodal Workflows

- [Voice Pro](https://github.com/abus-aikorea/voice-pro) - Gradio WebUI for speech recognition, translation, subtitle generation, TTS, voice cloning, and multilingual dubbing workflows. `Python` `GPL-3.0`
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - Local C and C++ runtime for Whisper speech recognition. `C++` `MIT`
- [VibeVoice](https://github.com/microsoft/VibeVoice) - Open source voice model project for speech-generation experiments. `Python` `MIT`
- [ChatTTS](https://github.com/2noise/ChatTTS) - Generative speech model for dialogue-style text-to-speech workflows. `Python` `AGPL-3.0`
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - Few-shot voice cloning and text-to-speech toolkit. `Python` `MIT`

## Prompt, Context, And Memory

- [Fabric](https://github.com/danielmiessler/fabric) - Open source framework for reusable AI patterns and prompt workflows. `Go` `MIT`
- [OpenAI Swarm](https://github.com/openai/swarm) - Educational framework for lightweight multi-agent orchestration. `Python` `MIT`
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI agents and assistants. `Python` `Apache-2.0`
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - Maintained guide and reference set for prompt engineering, context engineering, RAG, and agents. `MDX` `MIT`
- [Guidance](https://github.com/guidance-ai/guidance) - Language for controlling LLM generation with structured prompts and programmatic constraints. `Jupyter Notebook` `MIT`
- [GPT Prompt Engineer](https://github.com/mshumer/gpt-prompt-engineer) - Notebook workflow for generating, testing, and ranking prompts against examples. `Jupyter Notebook` `MIT`
- [memU](https://github.com/NevaMind-AI/memU) - Memory layer for long-running proactive agents. `Python` `License: see repository`

## Docs, Knowledge, And RAG

- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for connecting LLM applications to private and domain-specific data. `Python` `MIT`
- [Haystack](https://github.com/deepset-ai/haystack) - Framework for building search, RAG, and agentic knowledge applications. `Python` `Apache-2.0`
- [DocsGPT](https://github.com/arc53/DocsGPT) - Open source assistant for querying documentation and internal knowledge. `Python` `MIT`
- [RaTeX](https://github.com/erweixin/RaTeX) - Pure Rust KaTeX-compatible math renderer for native, web, server-side PNG/SVG/PDF, and AI document workflows. `Rust` `License: see repository`
- [Dataset Viewer](https://github.com/stardustai/dataset-viewer) - Tauri desktop viewer for streaming, searching, and previewing massive datasets from local files, S3, WebDAV, SSH, SMB, and Hugging Face. `TypeScript` `MIT`
- [Docling](https://github.com/docling-project/docling) - Document parsing toolkit for preparing files for generative AI and RAG pipelines. `Python` `MIT`
- [MarkItDown](https://github.com/microsoft/markitdown) - Converts Office files, PDFs, and other documents into Markdown for LLM workflows. `Python` `MIT`
- [Marker](https://github.com/datalab-to/marker) - Converts PDFs to Markdown and JSON for document ingestion pipelines. `Python` `GPL-3.0`
- [Chandra](https://github.com/datalab-to/chandra) - OCR model for extracting complex tables, forms, handwriting, and layout from documents. `Python` `Apache-2.0`
- [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) - PDF parser for creating AI-ready and accessibility-aware document data. `Java` `Apache-2.0`
- [GMFT](https://github.com/conjuncts/gmft) - Lightweight table-extraction library for document ingestion and RAG preprocessing. `Python` `MIT`
- [Zerox](https://github.com/getomni-ai/zerox) - Vision-model based OCR and document extraction toolkit. `TypeScript` `MIT`
- [Firecrawl](https://github.com/firecrawl/firecrawl) - API and service for search, web scraping, crawling, and browser interaction at scale. `TypeScript` `AGPL-3.0`
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM-friendly web crawler and scraper for extracting structured web context. `Python` `Apache-2.0`
- [LLM Scraper](https://github.com/mishushakov/llm-scraper) - TypeScript library for turning webpages into structured data with LLMs. `TypeScript` `MIT`
- [Defuddle](https://github.com/kepano/defuddle) - Extracts the main content of webpages as Markdown for knowledge and agent workflows. `TypeScript` `MIT`
- [FastGPT](https://github.com/labring/FastGPT) - Knowledge-base platform for data processing, RAG retrieval, and visual AI workflow orchestration. `TypeScript` `License: see repository`
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - RAG-based application for chatting with local or private documents. `Python` `Apache-2.0`
- [Onyx](https://github.com/onyx-dot-app/onyx) - Open source AI chat platform with connectors and search across workplace knowledge. `Python` `License: see repository`
- [Quivr](https://github.com/QuivrHQ/quivr) - RAG application framework for integrating files, vector stores, and LLMs into products. `Python` `License: see repository`
- [Ocular](https://github.com/OcularEngineering/ocular) - Search and chat system for organization knowledge using private data. `TypeScript` `License: see repository`
- [Trieve](https://github.com/devflowinc/trieve) - Search, recommendation, RAG, and analytics platform exposed through APIs. `Rust` `MIT`
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) - Agentic data assistant for building AI applications over databases and data workflows. `Python` `MIT`
- [Deep Research](https://github.com/dzhng/deep-research) - Iterative research agent that combines search, scraping, and LLM synthesis. `TypeScript` `MIT`
- [STORM](https://github.com/stanford-oval/storm) - LLM-powered knowledge curation system that researches topics and writes cited reports. `Python` `MIT`
- [FreeAskInternet](https://github.com/nashsu/FreeAskInternet) - Local search aggregator and answer generator that combines multi-engine search with LLM synthesis. `Python` `Apache-2.0`
- [nanoPerplexityAI](https://github.com/Yusuke710/nanoPerplexityAI) - Minimal open source implementation of a Perplexity-style search-answering workflow. `Python` `MIT`
- [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) - AI-assisted PDF translation tool that preserves scientific-paper layout and supports CLI, GUI, MCP, and Docker usage. `Python` `AGPL-3.0`
- [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) - Offline OCR tool for screenshots, images, PDFs, QR codes, and batch document recognition. `Python` `MIT`

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
