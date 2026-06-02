# Awesome AI Dev Tools 中文版

> 一个面向 AI 时代开发者的开源工具清单，关注如何更高效地构建、测试、审查、文档化和交付软件。

[English](README.md)

这不是一个泛泛的“开源项目大全”。这个清单只收录会改变开发工作流本身的工具：代码智能体、智能体运行时、模型上下文、代码库索引、AI 辅助审查、浏览器自动化、评测、本地模型基础设施，以及让 AI 真正进入工程闭环的胶水工具。

## 目录

- [范围](#范围)
- [筛选标准](#筛选标准)
- [代码智能体与 AI IDE](#代码智能体与-ai-ide)
- [智能体运维与维护](#智能体运维与维护)
- [智能体运行时与框架](#智能体运行时与框架)
- [Model Context Protocol](#model-context-protocol)
- [代码库搜索与索引](#代码库搜索与索引)
- [开发者 CLI 与终端工具](#开发者-cli-与终端工具)
- [代码审查与变更查看 UI](#代码审查与变更查看-ui)
- [设计、原型与产物](#设计原型与产物)
- [3D 与资产生成](#3d-与资产生成)
- [浏览器与 UI 自动化](#浏览器与-ui-自动化)
- [测试、评测与基准](#测试评测与基准)
- [本地模型与推理](#本地模型与推理)
- [音频与多模态工作流](#音频与多模态工作流)
- [提示词、上下文与记忆](#提示词上下文与记忆)
- [文档、知识与 RAG](#文档知识与-rag)
- [沙箱与安全执行](#沙箱与安全执行)
- [贡献流程](#贡献流程)

## 范围

收录：

- 开发者、智能体或工程团队会使用的开源工具。
- 能改善 AI 辅助实现、调试、审查、测试、文档、部署或项目导航的工具。
- 能让 AI coding agent 更可靠的基础设施：上下文服务器、沙箱、评测框架、浏览器控制、代码搜索和可复现环境。

默认不收录：

- 不能直接改善 AI 辅助开发的通用库。
- 没有实质开源核心的闭源 SaaS。
- 没有维护软件形态的一次性提示词。
- 与开发工作流无关的模型排行榜。

## 筛选标准

每个条目至少应该回答下面两个问题：

- 它是否缩短了真实开发闭环？
- 它是否让 AI agent 更安全地检查、修改、测试或验证软件？
- 它是否改善了代码库上下文质量？
- 它是否让智能体行为更可复现或可衡量？
- 它是否已经能被维护者实际使用？

推荐条目格式：

```markdown
- [Project](https://github.com/org/project) - 简短、具体的说明。`Language` `License`
```

## 代码智能体与 AI IDE

- [OpenAI Codex CLI](https://github.com/openai/codex) - 终端代码智能体，可在本地工作区阅读、编辑、运行并验证代码。`Rust` `Apache-2.0`
- [Claude Code](https://github.com/anthropics/claude-code) - 面向终端、IDE 和 GitHub 工作流的 agentic coding 工具。`Shell` `License: see repository`
- [Aider](https://github.com/Aider-AI/aider) - 终端 AI 结对编程工具，具备强 Git 集成和代码库地图能力。`Python` `Apache-2.0`
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 软件开发智能体开放平台，支持代码编辑、Shell、浏览器和工作流自动化。`Python` `MIT`
- [Cline](https://github.com/cline/cline) - VS Code coding agent，可编辑文件、运行命令、使用浏览器上下文，并经用户批准调用 MCP 工具。`TypeScript` `Apache-2.0`
- [Continue](https://github.com/continuedev/continue) - 开源 AI 代码助手，支持 IDE 内的模型、上下文和自动补全定制。`TypeScript` `Apache-2.0`
- [OpenManus](https://github.com/FoundationAgents/OpenManus) - 开源通用智能体项目，用于构建和研究自主任务执行工作流。`Python` `MIT`
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - AI developer agent，可根据自然语言需求规划、实现并迭代软件项目。`Python` `License: see repository`
- [Claude Engineer](https://github.com/Doriandarko/claude-engineer) - CLI 与 Web 代码助手，让 Claude 在开发会话中创建和使用项目专用工具。`Python` `License: see repository`
- [Open Interpreter](https://github.com/openinterpreter/open-interpreter) - 面向计算机的自然语言接口，可运行代码、使用 Shell 并操作本地工作流。`Python` `AGPL-3.0`
- [AIlice](https://github.com/myshell-ai/AIlice) - 通用自主智能体运行时，支持 Shell、浏览器和工具调用工作流。`Python` `MIT`

## 智能体运维与维护

- [Keep Codex Fast](https://github.com/vibeforge1111/keep-codex-fast) - 备份优先的 Codex skill，用于检查、交接、归档和恢复本地 Codex 状态，避免不安全删除。`Python` `MIT`
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) - 单文件 Claude Code 指南，把实用的 coding-agent 行为规则沉淀为 CLAUDE.md。`License: see repository`
- [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) - 面向游戏开发角色和流程的 Claude Code 智能体与 skill 协作系统。`Shell` `MIT`
- [Claude HUD](https://github.com/jarrodwatts/claude-hud) - Claude Code 插件，用于显示上下文使用量、工具活动、运行中的智能体和 todo 进度。`JavaScript` `MIT`
- [Autoresearch](https://github.com/karpathy/autoresearch) - 自主研究循环，用于围绕模型训练任务运行、评判和迭代实验。`Python` `License: see repository`
- [Claude Autoresearch Skill](https://github.com/uditgoenka/autoresearch) - Claude Code skill，用于目标驱动的修改、验证、保留或丢弃研究循环。`JavaScript` `MIT`
- [RTK](https://github.com/rtk-ai/rtk) - CLI 代理，可在把常见开发命令输出发送给 LLM 前进行压缩。`Rust` `Apache-2.0`
- [Superpowers](https://github.com/obra/superpowers) - 面向 AI 辅助工程工作的 agentic skills 框架和软件开发方法论。`Shell` `MIT`
- [GStack](https://github.com/garrytan/gstack) - Claude Code 配置集，提供设计、工程管理、发布、文档和 QA 等角色工具。`TypeScript` `MIT`
- [Remodex](https://github.com/Emanuele-web04/remodex) - 用于从 macOS 远程控制 Codex 会话的客户端。`Swift` `Apache-2.0`
- [Happy](https://github.com/slopus/happy) - Codex 和 Claude Code 的移动端与 Web 客户端，支持实时语音和加密会话。`TypeScript` `MIT`

## 智能体运行时与框架

- [LangGraph](https://github.com/langchain-ai/langgraph) - 用于构建有状态、可控智能体工作流的框架。`Python` `MIT`
- [AutoGen](https://github.com/microsoft/autogen) - 用于构建多智能体 AI 应用和工作流的框架。`Python` `MIT`
- [CrewAI](https://github.com/crewAIInc/crewAI) - 用于编排基于角色的 AI agent 和任务工作流的框架。`Python` `MIT`
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 也可作为实践型软件工程智能体的参考实现。`Python` `MIT`
- [Dify](https://github.com/langgenius/dify) - 用于构建和运营 agentic LLM 工作流的平台，支持工具、数据集和应用部署。`TypeScript` `License: see repository`
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - 多智能体框架，用软件公司角色来组织自然语言编程工作流。`Python` `MIT`
- [Eko](https://github.com/FellouAI/eko) - Agentic workflow 框架，把自然语言任务转为偏生产化的自动化流程。`TypeScript` `MIT`
- [n8n](https://github.com/n8n-io/n8n) - 工作流自动化平台，带原生 AI 节点，适合工具编排和集成密集型 agent workflow。`TypeScript` `License: see repository`
- [MiniAGI](https://github.com/muellerberndt/mini-agi) - 最小自主智能体实现，适合实验 OpenAI 驱动的任务循环。`Python` `MIT`
- [Zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) - 小型自主助手基础设施，用于跨环境部署和替换智能体组件。`Rust` `Apache-2.0`

## Model Context Protocol

- [Model Context Protocol](https://github.com/modelcontextprotocol) - 连接 AI 应用与工具、数据、上下文的开放协议和 SDK 生态。
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - MCP server 参考实现，以及指向更广泛注册表的入口。`TypeScript` `Python`
- [FastMCP](https://github.com/jlowin/fastmcp) - 用于快速构建 MCP server 的 Python 框架。`Python` `Apache-2.0`
- [Unity MCP](https://github.com/CoplayDev/unity-mcp) - MCP 桥接器，让 AI assistant 能检查资产、控制场景、编辑脚本并自动化 Unity Editor 工作。`C#` `MIT`
- [TradingView MCP](https://github.com/atilaahmettaner/tradingview-mcp) - MCP server，把市场筛选、技术指标和图表上下文暴露给 AI assistant。`Python` `MIT`

## 代码库搜索与索引

- [Sourcegraph Cody](https://github.com/sourcegraph/cody) - 基于代码搜索和仓库上下文的 AI 代码助手。`TypeScript` `Apache-2.0`
- [Grep App](https://github.com/grep-app/grep) - 快速源码搜索服务，适合智能体和人工进行代码导航。`Go` `MIT`
- [Serena](https://github.com/oraios/serena) - 面向 coding agent 的工具包，专注语义代码检索和编辑。`Python` `MIT`
- [Repomix](https://github.com/yamadashy/repomix) - 把整个仓库打包成 AI 友好的文件，用于向 LLM 和 coding agent 提供代码库上下文。`TypeScript` `MIT`
- [Devv](https://github.com/devv-ai/devv) - 面向开发者的 AI 搜索引擎，用于查找实现细节、API 和工程参考。`License: see repository`
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - 面向长周期智能体的增量索引引擎，让项目上下文保持新鲜且可查询。`Python` `Apache-2.0`

## 开发者 CLI 与终端工具

- [Doxx](https://github.com/bgreenwell/doxx) - 终端工具，可在不打开 Microsoft Office 的情况下安全检查 `.docx` 文档内容。`Rust` `MIT`
- [Mole](https://github.com/tw93/Mole) - macOS 终端工具，用于清理、卸载、分析、优化和监控系统。`Shell` `MIT`
- [tproxy](https://github.com/kevwan/tproxy) - 用于代理和分析 TCP 连接的 CLI 调试工具。`Go` `MIT`
- [Piku](https://github.com/piku/piku) - 极简自托管 PaaS，可通过 `git push` 把应用部署到自己的服务器。`Python` `MIT`
- [VizTracer](https://github.com/gaogaotiantian/viztracer) - Python 追踪和性能分析工具，可记录执行过程并渲染交互式 trace。`Python` `Apache-2.0`
- [kitty](https://github.com/kovidgoyal/kitty) - 快速、可脚本化、基于 GPU 的终端模拟器，适合本地开发工作流。`Python` `GPL-3.0`
- [OpenAI Proxy](https://github.com/egoist/openai-proxy) - Edge proxy，可通过 Cloudflare Workers 或 Vercel Edge 转发 OpenAI API 调用。`TypeScript` `License: see repository`

## 代码审查与变更查看 UI

- [Pierre](https://github.com/pierrecomputer/pierre) - 开源 TypeScript monorepo，提供适合 AI 的代码审查基础组件，如 diff 渲染和文件树渲染。`TypeScript` `License: see repository`

## 设计、原型与产物

- [Open Design](https://github.com/nexu-io/open-design) - 本地优先设计工作流，把 coding-agent CLI 变成原型、幻灯片、移动界面、dashboard、媒体和可导出产物生成器。`TypeScript` `Apache-2.0`
- [Open Slide](https://github.com/1weiho/open-slide) - Agent-native React 幻灯片框架，支持固定画布、评论、演示模式和 HTML/PDF 导出。`TypeScript` `MIT`
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) - 单二进制 Office 文档工具，让 AI agent 无需 Microsoft Office 也能创建、检查、编辑和渲染 Word、Excel、PowerPoint。`C#` `Apache-2.0`
- [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) - Claude Code 和 Codex skill，用于从提示词生成单文件横滑 HTML 幻灯片、演示视觉和社交封面。`HTML` `MIT`
- [Impeccable](https://github.com/pbakaus/impeccable) - 设计语言和指南，用于改善 AI 生成的产品界面。`JavaScript` `Apache-2.0`
- [Awesome Design Skills](https://github.com/bergside/awesome-design-skills) - 面向设计型 coding agent 的 DESIGN.md 和 SKILL.md 文件合集。`MIT`
- [Awesome Design.md](https://github.com/VoltAgent/awesome-design-md) - 品牌设计系统文件集合，帮助 coding agent 生成匹配品牌的 UI。`MIT`
- [Architecture Diagram Generator](https://github.com/Cocoon-AI/architecture-diagram-generator) - Claude skill，用于生成独立 HTML 和 SVG 系统架构图。`HTML` `MIT`
- [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) - 面向 coding agent 的 Web 幻灯片框架，用前端方式生成演示文稿。`JavaScript` `MIT`
- [Onlook](https://github.com/onlook-dev/onlook) - AI-first 可视化编辑器，用于构建、样式化和编辑 React 应用。`TypeScript` `Apache-2.0`
- [OpenUI](https://github.com/wandb/openui) - 实时 UI 生成工具，可把界面描述渲染为可编辑组件。`TypeScript` `Apache-2.0`
- [Screenshot to Code](https://github.com/abi/screenshot-to-code) - 把截图转换成 HTML、Tailwind、React 或 Vue 实现。`TypeScript` `MIT`
- [Assistant UI](https://github.com/assistant-ui/assistant-ui) - 用于构建 AI chat 和 assistant 界面的 React 组件库。`TypeScript` `MIT`
- [Creative Tim UI](https://github.com/creativetimofficial/ui) - 开源组件、区块和 agent，通过 registry 与 MCP workflow 暴露给开发工具。`TypeScript` `MIT`

## 3D 与资产生成

- [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) - 图像到 3D 资产生成系统，提供开放权重、训练代码、网格生成、PBR 纹理合成、Gradio app 和 API server。`Python` `License: see repository`
- [3DCellForge](https://github.com/huangserva/3DCellForge) - 浏览器 3D 细胞生成和探索工作室，支持 React Three Fiber、GLB 导入导出，以及可选 Tripo 或 Hunyuan3D 图像到 3D 后端。`JavaScript` `MIT`
- [WorldGen](https://github.com/ZiYang-xie/WorldGen) - 文本到 3D 场景生成系统，用于创建交互式环境和资产原型。`Python` `Apache-2.0`

## 浏览器与 UI 自动化

- [Browser Use](https://github.com/browser-use/browser-use) - 让网站可被 AI agent 操作，并支持浏览器任务自动化。`Python` `MIT`
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 通过 Playwright 给 agent 提供结构化浏览器自动化能力的 MCP server。`TypeScript` `Apache-2.0`
- [Stagehand](https://github.com/browserbase/stagehand) - 基于 Playwright 的 AI 友好浏览器自动化框架。`TypeScript` `MIT`
- [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) - Stealth Chromium 构建，可作为 Playwright 兼容的浏览器自动化目标。`Python` `MIT`
- [Agent Browser](https://github.com/vercel-labs/agent-browser) - 为 AI agent 设计的浏览器自动化 CLI。`Rust` `Apache-2.0`
- [Maestro](https://github.com/mobile-dev-inc/Maestro) - 面向移动端和 Web 端到端流程的声明式自动化框架。`Kotlin` `Apache-2.0`
- [OpenAI CUA Sample App](https://github.com/openai/openai-cua-sample-app) - 使用 computer-using agent 操作浏览器和桌面环境的示例应用。`TypeScript` `MIT`
- [Self Operating Computer](https://github.com/OthersideAI/self-operating-computer) - 多模态框架，让 AI 通过视觉上下文和动作操作计算机。`Python` `MIT`
- [KasmVNC](https://github.com/kasmtech/KasmVNC) - 可通过 Web 访问的 VNC server 和 client，用于安全远程桌面环境。`C++` `GPL-2.0`

## 测试、评测与基准

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - 用真实 GitHub issue 评测软件工程智能体的 benchmark。`Python` `MIT`
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - 大语言模型系统评测框架。`Python` `MIT`
- [OpenAI Evals](https://github.com/openai/evals) - 用于评估 LLM 行为的框架和注册表。`Python` `MIT`
- [promptfoo](https://github.com/promptfoo/promptfoo) - 以 CI 风格测试和评估提示词、模型与 LLM 应用。`TypeScript` `MIT`

## 本地模型与推理

- [Ollama](https://github.com/ollama/ollama) - 用简单的开发者工作流运行和管理本地语言模型。`Go` `MIT`
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - 面向 CPU 和 GPU 的高效本地 LLM 推理。`C++` `MIT`
- [vLLM](https://github.com/vllm-project/vllm) - 面向生产和研究的高吞吐 LLM serving engine。`Python` `Apache-2.0`
- [LiteLLM](https://github.com/BerriAI/litellm) - 统一 API gateway 和 SDK，用于调用多种模型提供商。`Python` `MIT`
- [MLX](https://github.com/ml-explore/mlx) - 面向 Apple silicon 的数组框架，用于运行和实验机器学习工作负载。`C++` `MIT`
- [llm.c](https://github.com/karpathy/llm.c) - 小型 C/CUDA LLM 训练实现，用于理解和修改模型内部机制。`Cuda` `MIT`
- [llama2.c](https://github.com/karpathy/llama2.c) - 极简 C 版 Llama 2 推理实现，适合研究可移植本地模型运行时。`C` `MIT`
- [tinygrad](https://github.com/tinygrad/tinygrad) - 小型神经网络框架和编译器栈，用于本地模型实验。`Python` `MIT`

## 音频与多模态工作流

- [Voice Pro](https://github.com/abus-aikorea/voice-pro) - Gradio WebUI，支持语音识别、翻译、字幕生成、TTS、声音克隆和多语言配音工作流。`Python` `GPL-3.0`
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - Whisper 语音识别的本地 C/C++ 运行时。`C++` `MIT`
- [VibeVoice](https://github.com/microsoft/VibeVoice) - 开源语音模型项目，用于语音生成实验。`Python` `MIT`
- [ChatTTS](https://github.com/2noise/ChatTTS) - 面向对话式 TTS 工作流的生成式语音模型。`Python` `AGPL-3.0`
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - Few-shot 声音克隆和文本转语音工具包。`Python` `MIT`

## 提示词、上下文与记忆

- [Fabric](https://github.com/danielmiessler/fabric) - 可复用 AI patterns 和提示词工作流的开源框架。`Go` `MIT`
- [OpenAI Swarm](https://github.com/openai/swarm) - 轻量多智能体编排的教育型框架。`Python` `MIT`
- [Mem0](https://github.com/mem0ai/mem0) - 面向 AI agent 和 assistant 的记忆层。`Python` `Apache-2.0`
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - 持续维护的提示词工程、上下文工程、RAG 和 agent 指南与参考资料。`MDX` `MIT`
- [Guidance](https://github.com/guidance-ai/guidance) - 用结构化提示词和程序化约束控制 LLM 生成的语言。`Jupyter Notebook` `MIT`
- [GPT Prompt Engineer](https://github.com/mshumer/gpt-prompt-engineer) - 用示例生成、测试和排序提示词的 notebook 工作流。`Jupyter Notebook` `MIT`
- [memU](https://github.com/NevaMind-AI/memU) - 面向长期运行主动智能体的记忆层。`Python` `License: see repository`

## 文档、知识与 RAG

- [LlamaIndex](https://github.com/run-llama/llama_index) - 把 LLM 应用连接到私有和领域数据的数据框架。`Python` `MIT`
- [Haystack](https://github.com/deepset-ai/haystack) - 用于构建搜索、RAG 和 agentic knowledge 应用的框架。`Python` `Apache-2.0`
- [DocsGPT](https://github.com/arc53/DocsGPT) - 用于查询文档和内部知识的开源 assistant。`Python` `MIT`
- [RaTeX](https://github.com/erweixin/RaTeX) - 纯 Rust KaTeX 兼容数学渲染器，支持原生、Web、服务端 PNG/SVG/PDF 和 AI 文档工作流。`Rust` `License: see repository`
- [Dataset Viewer](https://github.com/stardustai/dataset-viewer) - Tauri 桌面查看器，可从本地文件、S3、WebDAV、SSH、SMB 和 Hugging Face 流式搜索和预览大规模数据集。`TypeScript` `MIT`
- [Docling](https://github.com/docling-project/docling) - 文档解析工具包，用于把文件准备成适合生成式 AI 和 RAG pipeline 的数据。`Python` `MIT`
- [MarkItDown](https://github.com/microsoft/markitdown) - 把 Office 文件、PDF 和其他文档转换成 Markdown，供 LLM 工作流使用。`Python` `MIT`
- [Marker](https://github.com/datalab-to/marker) - 把 PDF 快速转换为 Markdown 和 JSON，用于文档摄取 pipeline。`Python` `GPL-3.0`
- [Chandra](https://github.com/datalab-to/chandra) - OCR 模型，可从复杂表格、表单、手写内容和版面中抽取信息。`Python` `Apache-2.0`
- [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) - PDF parser，用于生成 AI-ready 和可访问性友好的文档数据。`Java` `Apache-2.0`
- [GMFT](https://github.com/conjuncts/gmft) - 轻量表格抽取库，用于文档摄取和 RAG 预处理。`Python` `MIT`
- [Zerox](https://github.com/getomni-ai/zerox) - 基于视觉模型的 OCR 和文档抽取工具包。`TypeScript` `MIT`
- [Firecrawl](https://github.com/firecrawl/firecrawl) - 面向大规模搜索、网页抓取、爬取和浏览器交互的 API 与服务。`TypeScript` `AGPL-3.0`
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM 友好的网页爬虫和抓取工具，用于抽取结构化网页上下文。`Python` `Apache-2.0`
- [LLM Scraper](https://github.com/mishushakov/llm-scraper) - TypeScript 库，用 LLM 把网页转换成结构化数据。`TypeScript` `MIT`
- [Defuddle](https://github.com/kepano/defuddle) - 把网页主体内容提取为 Markdown，供知识库和 agent workflow 使用。`TypeScript` `MIT`
- [FastGPT](https://github.com/labring/FastGPT) - 知识库平台，支持数据处理、RAG 检索和可视化 AI workflow 编排。`TypeScript` `License: see repository`
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - 基于 RAG 的应用，用于和本地或私有文档对话。`Python` `Apache-2.0`
- [Onyx](https://github.com/onyx-dot-app/onyx) - 开源 AI chat 平台，通过连接器和搜索访问工作场景知识。`Python` `License: see repository`
- [Quivr](https://github.com/QuivrHQ/quivr) - RAG 应用框架，用于把文件、向量库和 LLM 集成进产品。`Python` `License: see repository`
- [Ocular](https://github.com/OcularEngineering/ocular) - 面向组织私有数据的搜索和聊天系统。`TypeScript` `License: see repository`
- [Trieve](https://github.com/devflowinc/trieve) - 通过 API 暴露搜索、推荐、RAG 和分析能力的平台。`Rust` `MIT`
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) - Agentic data assistant，用于在数据库和数据工作流之上构建 AI 应用。`Python` `MIT`
- [Deep Research](https://github.com/dzhng/deep-research) - 迭代式研究 agent，组合搜索、网页抓取和 LLM 综合。`TypeScript` `MIT`
- [STORM](https://github.com/stanford-oval/storm) - LLM 驱动的知识整理系统，可研究主题并生成带引用的报告。`Python` `MIT`
- [FreeAskInternet](https://github.com/nashsu/FreeAskInternet) - 本地搜索聚合与答案生成器，把多搜索引擎结果和 LLM 综合结合起来。`Python` `Apache-2.0`
- [nanoPerplexityAI](https://github.com/Yusuke710/nanoPerplexityAI) - Perplexity 风格搜索问答工作流的极简开源实现。`Python` `MIT`
- [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) - AI 辅助 PDF 翻译工具，保留科学论文版式，并支持 CLI、GUI、MCP 和 Docker。`Python` `AGPL-3.0`
- [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) - 离线 OCR 工具，支持截图、图片、PDF、二维码和批量文档识别。`Python` `MIT`

## 沙箱与安全执行

- [E2B](https://github.com/e2b-dev/E2B) - 面向 AI agent 和代码执行的安全沙箱。`TypeScript` `Apache-2.0`
- [Daytona](https://github.com/daytonaio/daytona) - 开发环境管理器和面向 AI coding agent 的沙箱基础设施。`Go` `AGPL-3.0`
- [Devbox](https://github.com/jetify-com/devbox) - 基于 Nix 的可复现开发环境。`Go` `Apache-2.0`

## 贡献流程

1. 提 issue 或 pull request，说明项目链接和分类。
2. 解释它如何提升 AI 时代的软件开发效率。
3. 优先提供具体工作流证据，而不是营销话术。
4. 描述保持简短、事实化。
5. 不要只因为 star 数高就添加项目。

完整收录策略见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本清单使用 [CC0 1.0](LICENSE) 发布。项目名称和链接归各自所有者所有。
