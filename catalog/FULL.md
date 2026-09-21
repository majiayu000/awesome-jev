# Jev 资源目录

按类别查找 Jev 相关项目、工具、教程和文章。描述来自收集资料，项目的当前状态以原仓库或网站为准。

[中文首页](../README_zh.md) · [English](../README.md)

## 分类

- [官方资料](#official)
- [SDK 与客户端](#sdks)
- [网关与集成](#integrations)
- [智能体工具](#agents)
- [浏览器与电脑操作](#browser)
- [应用](#apps)
- [游戏与模拟](#games)
- [演示与示例](#demos)
- [评测与研究](#research)
- [资源清单](#lists)
- [文章与讨论](#articles)

<a id="official"></a>

## 官方资料

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| TypeSafe AI | Company homepage, waitlist, and product overview. | [网站](https://typesafe.ai) |
| Documentation | Introduction, primitives, patterns, cookbooks, HTTP API, and SDK references. | [网站](https://docs.typesafe.ai) · [网站](https://docs.typesafe.ai/) |
| Quick start | Shortest path from an API key to a typed decision. | [网站](https://docs.typesafe.ai/introduction/quickstart) |
| Playground | Paste a state, add questions, and see typed answers in the browser. | [网站](https://console.typesafe.ai/playground) |
| HTTP API reference | Request and response contract for POST /v1/systemone. | [网站](https://docs.typesafe.ai/api) |
| Primitives | Choice, Score, and Noul: the three question types and what they return. | [网站](https://docs.typesafe.ai/primitives) |
| Patterns | Speculative fan-out, confidence-gated routing, composite scoring, and intent routing. | [网站](https://docs.typesafe.ai/patterns) |
| Cookbooks | Reproducible recipes: parallel questions, reranking, guardrails, citation checks, extraction, hierarchical classification. | [网站](https://docs.typesafe.ai/cookbooks/parallel_questions) |
| Smart home demo | Official interactive demo of speculative fan-out: many questions in one call, code keeps the relevant answers. | [网站](https://docs.typesafe.ai/demos/smart-home) |
| Workflow evals | Published eval methodology and per-model results for System One workflows. | [网站](https://evals.typesafe.ai) · [网站](https://evals.typesafe.ai/) |
| Jev 1.13 jaggedness | Known failure modes of the current public model, documented by TypeSafe. | [网站](https://docs.typesafe.ai/model-jaggedness/jev-1.13) |
| Introducing System One Models and Jev | Launch post: architecture, RLCD training, pricing, Doom and Wikiracing demos, FAQ. | [网站](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |
| Manifesto | The case for machine-native intelligence built for software, not conversation. | [网站](https://typesafe.ai/manifesto) |
| Discord | Official TypeSafe server. Builder demos live in the Show and Tell channel. | [网站](https://discord.gg/typesafe) |
| @typesafeai on X | Product and research updates. | [网站](https://x.com/typesafeai) |
| TypeSafe agent skills | Official agent skill for Claude Code, Codex, and compatible agents: primitives, patterns, and how to structure evaluations. | [仓库](https://github.com/typesafe-ai/skills) · [网站](https://typesafe.ai) |
| TypeSafe JavaScript SDK | Official TypeScript/JavaScript client with inferred answer types. npm install @typesafe-ai/sdk. | [仓库](https://github.com/typesafe-ai/typesafe-sdk-js) |
| System One adapter (Python) | Official drop-in TypeSafeClient replacement backed by OpenAI, Anthropic, and compatible LLM APIs, for comparing Jev against chat models. | [仓库](https://github.com/typesafe-ai/system-one-adapter-python) |
| TypeSafe Python SDK | Official sync and async Python client. pip install typesafe-sdk. | [仓库](https://github.com/typesafe-ai/typesafe-sdk-python) · [网站](https://docs.typesafe.ai/sdk/python) |
| Jaggedness jev-1.13 | 官方失败模式 — 必读 | [网站](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) |
| typesafe-ai/typesafe-ai.github.io | 原始资料未提供说明。 | [仓库](https://github.com/typesafe-ai/typesafe-ai.github.io) |

<a id="sdks"></a>

## SDK 与客户端

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| advocaat | A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev. | [仓库](https://github.com/pithings/advocaat) |
| typesafe-ai | Typed TypeSafe AI clients for Rust, with async and blocking backends and observable retries. | [仓库](https://github.com/Twister915/typesafe-ai) |
| zod-jev | Zod validates the shape, Jev validates the meaning: semantic checks on request bodies become calibrated probabilities you threshold in code. | [仓库](https://github.com/jomatsu/zod-jev) |
| typesafe-dotnet-sdk | Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI. | [仓库](https://github.com/saibimajdi/typesafeai-dotnet-sdk) · [网站](https://saibimajdi.github.io/typesafeai-dotnet-sdk/) |
| typesafe-sdk (joshmn) | Ruby client for typesafe.ai | [仓库](https://github.com/joshmn/typesafe-sdk) |
| super-jev | A small, extensible decision-to-action harness for TypeSafe Jev | [仓库](https://github.com/Kevthetech143/super-jev) |
| jod | Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers. | [仓库](https://github.com/mateonunez/jod) · [网站](https://npmjs.com/package/@mateonunez/jod) · [文章](https://x.com/mmateonunez/status/2100612699394597125) |
| typesafe-ai-rs | Independent async and blocking Rust SDK for the TypeSafe AI System One API | [仓库](https://github.com/gilljon/typesafe-ai-rs) · [网站](https://docs.rs/typesafe-ai-rs) |
| TypeSafeAI.Net | .NET SDK for the TypeSafe AI platform | [仓库](https://github.com/Hawxy/TypeSafeAI.Net) · [网站](https://docs.typesafe.ai/) |
| typesafe-go (cole-gillespie) | unofficial go SDK for typesafe AI, with typed answers, retries, and context support | [仓库](https://github.com/cole-gillespie/typesafe-go) |
| typesafe-sdk-swift | Swift SDK for TypeSafe AI | [仓库](https://github.com/InsaneArts/typesafe-sdk-swift) |
| typesafe_sdk | An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model. | [仓库](https://github.com/nshkrdotcom/typesafe_sdk) · [文章](https://x.com/elixirforum/status/2100495661942677648) |
| jevgo | Go client for TypeSafe AI's System One API (Jev), with optional Langfuse instrumentation | [仓库](https://github.com/fgn/jevgo) |
| jevclient | Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse. | [仓库](https://github.com/AboveColin/jevclient) · [网站](https://pypi.org/project/jevclient/) |
| jev-go (guillemus) | Unofficial Go SDK for TypeSafe AI's Jev API | [仓库](https://github.com/guillemus/jev-go) |
| jev-go (Gaurav-Gosain) | Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text | [仓库](https://github.com/Gaurav-Gosain/jev-go) |
| typesafe-sdk-rust | Rust SDK for the TypeSafe AI API | [仓库](https://github.com/codeitlikemiley/typesafe-sdk-rust) |
| zio-typesafe-ai | Scala 3 / ZIO client for the System One API: typed end-to-end, several questions per round-trip via NamedTuple. | [仓库](https://github.com/jamesward/zio-typesafe-ai) |
| typesafe-client | Unofficial typed async Rust client for the TypeSafe System One API | [仓库](https://github.com/JedimEmO/typesafe-client) |
| typesafeai-go | Go SDK for TypeSafe AI API https://docs.typesafe.ai/api | [仓库](https://github.com/chez-shanpu/typesafeai-go) |
| kunobi-jev | Rust client for the TypeSafe System One API (Jev) | [仓库](https://github.com/kunobi-ninja/kunobi-jev) |
| tinyjevclient | An integration with jev by typesafe.ai in Rust | [仓库](https://github.com/tinyhumansai/tinyjevclient) |
| decido | Probabilistic decisions for Python. Use Jev or bring your own provider; crawl with Playwright. | [仓库](https://github.com/yairshy/decido) |
| typesafe-sdk (binnash) | PHP & Laravel SDK for TypeSafe AI's JEV Model series | [仓库](https://github.com/binnash/typesafe-sdk) |
| jev | Unofficial Go client for TypeSafe's System One API  and its model, Jev. | [仓库](https://github.com/anilsenay/jev) |
| typesafe-go (zhirschtritt) | Idiomatic Go SDK for the TypeSafe AI API | [仓库](https://github.com/zhirschtritt/typesafe-go) · [网站](https://pkg.go.dev/github.com/zhirschtritt/typesafe-go) |
| typesafe_sdk_ex | Typesafe AI SDK in Elixir using Req | [仓库](https://github.com/vinnie357/typesafe_sdk_ex) |
| typesafe-sdk-php | Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. | [仓库](https://github.com/valksor/typesafe-sdk-php) · [网站](https://packagist.org/packages/valksor/typesafe-sdk-php) |
| typesafe-sdk-go | Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. | [仓库](https://github.com/valksor/typesafe-sdk-go) |
| typesafe_ai (typesend) | Unofficial Elixir SDK for the TypeSafe AI API | [仓库](https://github.com/typesend/typesafe_ai) · [网站](https://typesafe-api.hexdocs.pm/readme.html) |
| typesafe.zig | An idiomatic Zig client for the TypeSafe AI API | [仓库](https://github.com/mattneel/typesafe.zig) |
| typesafe | An idiomatic Elixir client for the TypeSafe AI API | [仓库](https://github.com/mattneel/typesafe) |
| typesafe_ai (hfiguera) | A supervised Mint client for the TypeSafe AI System One API | [仓库](https://github.com/hfiguera/typesafe_ai) |
| s1-rs | Typed System One layer for Rust (Choice/Score/Noul). | [仓库](https://github.com/AbdelStark/s1-rs) |
| typesafe-rs | Latency-first Rust SDK for TypeSafe System One. | [仓库](https://github.com/AbdelStark/typesafe-rs) · [网站](https://docs.rs/typesafe-rs/latest/typesafe_rs/) |
| kitze/skillbox | Self-hosted, versioned skills library for AI agents. MCP, scoped clients, and optional Jev recommendations. | [仓库](https://github.com/kitze/skillbox) |
| gamesonrblx/Jevbridge | ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode. | [仓库](https://github.com/gamesonrblx/Jevbridge) |
| frostney/clean-code-review | Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js. | [仓库](https://github.com/frostney/clean-code-review) · [网站](https://clean-code-review.vercel.app) |
| Olti1947/jev-java | Idiomatic Java SDK for TypeSafe AI Jev System One decision engine | [仓库](https://github.com/Olti1947/jev-java) |
| 2389-research/typesafe-go | A Go client for the TypeSafe System One API — typed judgments and probabilities, zero dependencies outside the standard library. | [仓库](https://github.com/2389-research/typesafe-go) |
| Premo-Cloud/typesafe-sdk-java | Community Java client for the TypeSafe System One API (unofficial) | [仓库](https://github.com/Premo-Cloud/typesafe-sdk-java) · [网站](https://docs.typesafe.ai) |
| yzfly/awesome-jev-zh | Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。 | [仓库](https://github.com/yzfly/awesome-jev-zh) · [网站](https://code.jiangshu.ai/awesome-jev-zh/) |
| latere-ai/typesafe-ai-go-sdk | Go client for the TypeSafe API | [仓库](https://github.com/latere-ai/typesafe-ai-go-sdk) |
| Stumble/jev-go | Community Go SDK for TypeSafe AI Jev / System One | [仓库](https://github.com/Stumble/jev-go) |
| abeldzan/jev-rs | Async-first Rust SDK for the TypeSafe AI API | [仓库](https://github.com/abeldzan/jev-rs) |
| aoprisan/typesafe-ai-rust-sdk | 原始资料未提供说明。 | [仓库](https://github.com/aoprisan/typesafe-ai-rust-sdk) |
| aoprisan/typesafe-ai-scala-sdk | 原始资料未提供说明。 | [仓库](https://github.com/aoprisan/typesafe-ai-scala-sdk) |
| dakdevs/decide-mcp | Configurable decision MCP server with AI SDK, Jev, percentage scores, and bias profile routing | [仓库](https://github.com/dakdevs/decide-mcp) |
| david1gp/jev | Result-based TypeSafe System One client library and jev command-line interface. | [仓库](https://github.com/david1gp/jev) |
| ehmpathy/rhachet-brains-typesafeai | rhachet brain.atom adapter for typesafe.ai classifier models | [仓库](https://github.com/ehmpathy/rhachet-brains-typesafeai) |
| jonesmelton/verdict | ocaml sdk for typesafe.ai's jev model | [仓库](https://github.com/jonesmelton/verdict) |
| kazz187/jev-sdk-go | Go 1.27 client for TypeSafe AI's Jev (System One) API: typed questions, typed answers | [仓库](https://github.com/kazz187/jev-sdk-go) |
| kraayenjon/awesome-jev | A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities. | [仓库](https://github.com/kraayenjon/awesome-jev) · [网站](https://madewithjev.com) |
| lu-zero/systemone | Rust client for the TypeSafe AI systemone API | [仓库](https://github.com/lu-zero/systemone) |
| maddygoround/typesafeai-cli | Give your AI agent a CLI companion who has access to TypeSafe AI's Jev. | [仓库](https://github.com/maddygoround/typesafeai-cli) |
| mhmdkzr/jev | An unofficial Go client for TypeSafe's System One Jev model | [仓库](https://github.com/mhmdkzr/jev) |
| mzainzulifqar/jev-php-sdk | PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13. | [仓库](https://github.com/mzainzulifqar/jev-php-sdk) · [网站](https://packagist.org/packages/mzainzulifqar/jev-php-sdk) |
| Nibir1/typesafe-go | Community-maintained Go SDK for the TypeSafe "System One" API (`Jev`) | [仓库](https://github.com/Nibir1/typesafe-go) |
| nu-sync/effect-evaluation | An Effect-native client for TypeSafe AI System One models (Jev) | [仓库](https://github.com/nu-sync/effect-evaluation) |
| obie/ruby_decision_model | Ruby client for decision models such as Typesafe Jev | [仓库](https://github.com/obie/ruby_decision_model) |
| pierangeloc/zio-typesafe-ai | Simple ZIO based client library for typesafe-ai | [仓库](https://github.com/pierangeloc/zio-typesafe-ai) |
| RadixILS-Dev/typesafe-sdk-go | A typesafe.ai client written in golang | [仓库](https://github.com/RadixILS-Dev/typesafe-sdk-go) |
| sava-software/typesafe-client | Java client for the TypeSafe System One API (Jev): typed questions in, calibrated probabilities out | [仓库](https://github.com/sava-software/typesafe-client) |
| SergeAx/typesafe-sdk-go | TypeSafe.AI Go SDK | [仓库](https://github.com/SergeAx/typesafe-sdk-go) |
| Shubham510/typesafe-go | Unofficial Go SDK for TypeSafe AI's System One API (Jev). | [仓库](https://github.com/Shubham510/typesafe-go) |
| stillroom/agent-workflow-lab | Typed state, explicit transitions, one narrow model judgment, and a human approval gate — a rebuildable agent workflow using and testing Jev. | [仓库](https://github.com/stillroom/agent-workflow-lab) |
| xingwudao/OpenJev | OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI. | [仓库](https://github.com/xingwudao/OpenJev) |

<a id="integrations"></a>

## 网关与集成

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| eve | Vercel's open agent framework, which ships Jev as the default evaluation model in its experimental evaluate path. | [仓库](https://github.com/vercel/eve) · [网站](https://eve.dev) |
| ai-cli | Vercel Labs terminal CLI that can run Jev as the evaluation model for its evaluate command. | [仓库](https://github.com/vercel-labs/ai-cli) · [网站](https://ai-cli.dev) |
| Loki | Self-improving agent harness with an optional TypeSafe Jev companion for typed Choice, Score, and Noul judgments. | [仓库](https://github.com/wundercorp/loki) · [网站](https://loki.computer) · [文章](https://x.com/wundercorp/status/2100619500966056196) |
| neo4jev | Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships | [仓库](https://github.com/jexp/neo4jev) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| ruby_llm-typesafe | TypeSafe structured-output provider for RubyLLM 2 | [仓库](https://github.com/kieranklaassen/ruby_llm-typesafe) |
| HA-Jev | Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity. | [仓库](https://github.com/AboveColin/HA-Jev) |
| typesafe-jev-workflow | Async LangGraph workflow that gets a typed Jev Choice (invoice or general) and routes each inbound email to the matching handler. | [仓库](https://github.com/GiesN/typesafe-jev-workflow) |
| a0-typesafe-ai | TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards. | [仓库](https://github.com/3clyp50/a0-typesafe-ai) |
| typesafe-on-neon | Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing. | [仓库](https://github.com/andrelandgraf/safer-with-jev) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| pg_typesafe | Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification | [仓库](https://github.com/giuliosmall/pg_typesafe) |
| laravel-typesafe-jev | Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes. | [仓库](https://github.com/Butochnikov/laravel-typesafe-jev) |
| typesafe-ai-rails | Community Rails integration on the typesafe-sdk gem: configuration, persisted usage and cost telemetry, and opt-in confidence policies. | [仓库](https://github.com/GenieRobot/typesafe-ai-rails) |
| judging-with-typesafe | Скилл для агентов Letta: суждения по критериям через TypeSafe System One (Jev) | [仓库](https://github.com/carlsonchik/judging-with-typesafe) |
| pydantic-jev-examples | Pydantic AI capabilities made stronger with Jev: small runnable demos, one file each | [仓库](https://github.com/adtyavrdhn/pydantic-jev-examples) |
| typesafe-assist | Home Assistant Assist conversation agent powered by TypeSafe's Jev (System One) model | [仓库](https://github.com/JanOstrowka/typesafe-assist) |
| Jev4Mellea | Jev adapter to Mellea | [仓库](https://github.com/SoundBlaster/Jev4Mellea) |
| n8n-nodes-typesafe-ai | n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities | [仓库](https://github.com/DomMonte/n8n-nodes-typesafe-ai) · [网站](https://docs.typesafe.ai) |
| typesafe-ui | shadcn-style reusable components and blocks for using TypeSafe AI. | [仓库](https://github.com/BunsDev/typesafe-ui) · [网站](https://typesafe-ui.vercel.app) |
| Vercel AI SDK provider | @ai-sdk/typesafe-ai plus experimental_evaluate; use jev-latest as an evaluation model. | [网站](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) · [文章](https://x.com/vercel_dev/status/2100378959653507175) |
| Jev on Vercel AI Gateway | Hosted typesafe-ai/jev for AI SDK evaluate calls, no TypeSafe waitlist required. | [网站](https://vercel.com/ai-gateway/models/jev) · [文章](https://x.com/typesafeai/status/2100376436272173088) |
| agentgateway Jev guardrail example | Jev as an LLM prompt guardrail inside the agentgateway proxy, with tracing and cost tracking. | [文章](https://x.com/agentgateway/status/2100615437973074097) |
| TrainLCD Jev rerank | Pull request adding Jev to station-suggestion reranking in the TrainLCD transit app. | [文章](https://x.com/tinykitten8/status/2100618835443453969) |
| nidhi-singh02/agent-router | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr | [仓库](https://github.com/nidhi-singh02/agent-router) |
| Brainwires/jevwire | Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev) | [仓库](https://github.com/Brainwires/jevwire) |
| docxology/daf-jev | daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill | [仓库](https://github.com/docxology/daf-jev) |
| harshil1712/slidepilot | Voice-driven semantic auto-advance for Slidev, powered by Cloudflare Agents and TypeSafe AI Jev | [仓库](https://github.com/harshil1712/slidepilot) |
| AkashPriyadarshii/jev-seo | 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One | [仓库](https://github.com/AkashPriyadarshii/jev-seo) |
| jerryfane/omp-jev-compaction | Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter | [仓库](https://github.com/jerryfane/omp-jev-compaction) |
| keltokhy/jgrep | grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line. | [仓库](https://github.com/keltokhy/jgrep) |
| lomeshdutta/skill-router | Tell Claude Code which installed skill a session needs, using Jev (TypeSafe AI) for the decision and skills.sh for discovery. | [仓库](https://github.com/lomeshdutta/skill-router) |
| molis-ai/jev-workbench | Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine. | [仓库](https://github.com/molis-ai/jev-workbench) |
| MrJev/awesome-jev | A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.  | [仓库](https://github.com/MrJev/awesome-jev) · [网站](https://mrjev.com) |
| qiz029/dscode | A DeepSeek coding agent harness: persistent shell, Ultra subagents, auto approval, Chrome MCP and session telemetry | [仓库](https://github.com/qiz029/dscode) · [网站](https://www.npmjs.com/package/@toddzheng024/dscode) |
| rajdhakad9826/routeKit | Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage. | [仓库](https://github.com/rajdhakad9826/routeKit) |
| WiktorB2004/llama-index-jev | LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge. | [仓库](https://github.com/WiktorB2004/llama-index-jev) |
| abhishekashokvkumar/jev-mcp-dispatcher | Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence. | [仓库](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher) |
| AkashPriyadarshii/jev-scout | Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring | [仓库](https://github.com/AkashPriyadarshii/jev-scout) |
| BYK/jev-mcp | An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text. | [仓库](https://github.com/BYK/jev-mcp) |
| daftAI2026/awesome-jev | TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai) | [仓库](https://github.com/daftAI2026/awesome-jev) · [网站](https://awesomejev.cc) |
| himomohi/aside-jev | Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime. | [仓库](https://github.com/himomohi/aside-jev) |
| Obrais-cloud/typesafe-mcp | MCP server exposing TypeSafe (Jev/System One) to the fleet: judge, rerank, systemone | [仓库](https://github.com/Obrais-cloud/typesafe-mcp) |
| Ravinder82/jev-flash-router | open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code | [仓库](https://github.com/Ravinder82/jev-flash-router) |
| simota/tenbin | MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score / Noul questions, lint them, measure on labelled data, and put calibrated thresholds in code | [仓库](https://github.com/simota/tenbin) |
| tonyzdev/PiJ | A terminal coding agent with Jev in the loop: skill selection, code ranking, and failure triage. | [仓库](https://github.com/tonyzdev/PiJ) |
| Wang-auspicious/codex-jev-compaction | Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills. | [仓库](https://github.com/Wang-auspicious/codex-jev-compaction) |
| affirmitv/bitrate-advisor | Live-stream encoder settings from telemetry and history: TypeSafe's Jev decision model inside a deterministic safety envelope. Deno, Node, edge runtimes. | [仓库](https://github.com/affirmitv/bitrate-advisor) |
| altregubov/jev-antigravity-mcp | 原始资料未提供说明。 | [仓库](https://github.com/altregubov/jev-antigravity-mcp) |
| alviso/jev-precheck | A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases. | [仓库](https://github.com/alviso/jev-precheck) |
| armsteadj1/vibe-smart-router | A Node-first, policy-bounded payment-context scorer using Jev for held-out feature discovery and per-transaction context. | [仓库](https://github.com/armsteadj1/vibe-smart-router) |
| AStheTECH/mewcp-jev | JEV MCP server by MewCP | [仓库](https://github.com/AStheTECH/mewcp-jev) · [网站](https://mewcp-jev.vercel.app) |
| brnyxx/jev-ra | Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms. | [仓库](https://github.com/brnyxx/jev-ra) · [网站](https://brnyxx.github.io/jev-ra/) |
| carllippert/jev-router | Express with no routes. TypeSafe Jev picks which handler runs. | [仓库](https://github.com/carllippert/jev-router) |
| cbruyndoncx/AskJev-MCP | MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence | [仓库](https://github.com/cbruyndoncx/AskJev-MCP) |
| chungsubeen0/jevmcp | Unofficial MCP for Jev | [仓库](https://github.com/chungsubeen0/jevmcp) |
| danielhirt/jev-lab | Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison | [仓库](https://github.com/danielhirt/jev-lab) |
| david-cermak/jevlike-esp32 | Jevlike edge router on ESP32 | [仓库](https://github.com/david-cermak/jevlike-esp32) |
| denikuchero/jev-chess-lab | Jev chess experiments: independent decisions vs tactical and Stockfish assistance, with full traces and video replays | [仓库](https://github.com/denikuchero/jev-chess-lab) · [网站](https://denikuchero.github.io/jev-chess-lab/) |
| DoGMaTiiC/hermes-jev | Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only. | [仓库](https://github.com/DoGMaTiiC/hermes-jev) |
| duketopceo/jev-compact | Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP | [仓库](https://github.com/duketopceo/jev-compact) |
| fast-facts/jev-mcp | 原始资料未提供说明。 | [仓库](https://github.com/fast-facts/jev-mcp) |
| gorock007/jev-atlas | An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI. | [仓库](https://github.com/gorock007/jev-atlas) · [网站](https://jev-atlas.vercel.app) |
| gzawadzki/jev-usecases | TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage | [仓库](https://github.com/gzawadzki/jev-usecases) |
| hangarbay/jev.mcp | One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text | [仓库](https://github.com/hangarbay/jev.mcp) |
| HiepPP/hiep-paseo-plugin | Local Paseo plugin exposing Jev evaluations through MCP | [仓库](https://github.com/HiepPP/hiep-paseo-plugin) |
| hugo-alves/jev-router-playground | Interactive playground for testing Jev model-routing decisions against OpenRouter models | [仓库](https://github.com/hugo-alves/jev-router-playground) · [网站](https://kvhx37ziab90c.space.minimax.io) |
| islee23520/omo-jevlike-router | Jev-style one-pass skill router for OmO: shrink the skill catalog in your system prompt with one forward pass (frozen Qwen2.5-0.5B + jevlike head, fail-open extension) | [仓库](https://github.com/islee23520/omo-jevlike-router) |
| its-panzer/skilltree | A local-first skill library and visual skill tree, with Jev routing and MCP access. | [仓库](https://github.com/its-panzer/skilltree) |
| jcpsimmons/jev-macos-loop | Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token. | [仓库](https://github.com/jcpsimmons/jev-macos-loop) |
| KrzysztofStaron/jev-experiments | TypeSafe Jev experiments via Vercel AI Gateway: pixel B&W/gray images + long-context relevance filter bench | [仓库](https://github.com/KrzysztofStaron/jev-experiments) |
| maraichr/jev-triage | Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter | [仓库](https://github.com/maraichr/jev-triage) |
| micic-mihajlo/jev-tool-runner | Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks. | [仓库](https://github.com/micic-mihajlo/jev-tool-runner) |
| minhgv/jev-mcp | TypeSafe Jev MCP decision layer for coding agents and CI | [仓库](https://github.com/minhgv/jev-mcp) |
| mpiv-ai/bb-plugin-typesafe-router | Routes a thread's first message to the right harness and model with TypeSafe (Jev), then asks you to confirm. | [仓库](https://github.com/mpiv-ai/bb-plugin-typesafe-router) |
| MSalvalaggio/jev-reflex | Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision). | [仓库](https://github.com/MSalvalaggio/jev-reflex) |
| nekowasabi/jev-routing-go | Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server. | [仓库](https://github.com/nekowasabi/jev-routing-go) |
| nekowasabi/jev-routing-mcp | 原始资料未提供说明。 | [仓库](https://github.com/nekowasabi/jev-routing-mcp) |
| nitinnat/jev-gateway | A small local HTTP service for TypeSafe AI's Jev through Vercel | [仓库](https://github.com/nitinnat/jev-gateway) |
| ohernandezdev/jevmod | Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP. | [仓库](https://github.com/ohernandezdev/jevmod) · [网站](https://jevmod.dev) |
| okooo5km/jev | Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode. | [仓库](https://github.com/okooo5km/jev) · [网站](https://sink.5km.tech/skills) |
| ourines/hermes-jev | Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill | [仓库](https://github.com/ourines/hermes-jev) |
| Perferic/openjev-mcp | Open-source Jev-compatible MCP server for typed decisions (Choice/Score/Noul): local GLiNER backend with a model router, drop-in swappable with the TypeSafe System One API. | [仓库](https://github.com/Perferic/openjev-mcp) |
| Pinutss/jev-mcp-router | Select relevant MCP tools under a context-token budget, without executing them. | [仓库](https://github.com/Pinutss/jev-mcp-router) |
| prasanth263/maza | Local MCP gateway with Jev tool discovery, secure credentials, CLI and dashboard | [仓库](https://github.com/prasanth263/maza) |
| pZacca/askjev | Unofficial MCP server for Jev (Typesafe AI) | [仓库](https://github.com/pZacca/askjev) |
| raj8525/universal-jev | Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents | [仓库](https://github.com/raj8525/universal-jev) |
| rajivkuriakose/typesafe-jev-examples | Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter | [仓库](https://github.com/rajivkuriakose/typesafe-jev-examples) |
| Rawson08/the-llm-dispatcher | An LLM router that uses Jev (TypeSafe System One) to dispatch each request to the cheapest model and lowest reasoning effort that will do the job. OpenAI-compatible proxy, Claude Code and Codex wrappers, TypeScript and C#. | [仓库](https://github.com/Rawson08/the-llm-dispatcher) |
| SadiqOnGithub/jev-lab | Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API | [仓库](https://github.com/SadiqOnGithub/jev-lab) |
| stbenjam/jev-eight-ball | A liquid magic eight ball powered by TypeSafe Jev decisions through OpenRouter | [仓库](https://github.com/stbenjam/jev-eight-ball) |
| stbenjam/jevagotchi | A tiny virtual pet cared for by TypeSafe Jev through OpenRouter | [仓库](https://github.com/stbenjam/jevagotchi) |
| themsquared/jev-benchmark | Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on. | [仓库](https://github.com/themsquared/jev-benchmark) · [网站](https://webofmike.com/jev-benchmark/) |
| Verhex/xerify | Verify before you trust. Cross-provider verification with LLMs and Jev. CLI, library & MCP. | [仓库](https://github.com/Verhex/xerify) · [网站](https://verhex.github.io/xerify/) |
| VinaSundar-Nat/Krypton.Carevo.JMR.MCP | MCP server with tooling for JMR - LIX , JEV and Database tooling | [仓库](https://github.com/VinaSundar-Nat/Krypton.Carevo.JMR.MCP) |
| Xy2002/poker-jev-test-bench | Jev test bench — Texas Hold'em edition: live-fire testing of TypeSafe's Jev evaluation model through a React poker game (Vercel AI Gateway). MIT. | [仓库](https://github.com/Xy2002/poker-jev-test-bench) |

<a id="agents"></a>

## 智能体工具

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| jev.nvim | Neovim plugin that scores functions against a natural-language question and lists results in quickfix. | [仓库](https://github.com/valentynkit/jev.nvim) |
| jev-commit | Git commit-message hook that compares the message with the staged diff and checks for possible credentials. | [仓库](https://github.com/valentynkit/jev-commit) |
| jev-belay | Claude Code Stop hook that checks transcript evidence for unverified completion claims; errors allow the turn to end. | [仓库](https://github.com/valentynkit/jev-belay) |
| foreman | Software Factory Foreman: an agent supervisor that uses Jev decisions to keep coding agents on task. | [仓库](https://github.com/thruwire/foreman) · [文章](https://x.com/JoshARosen/status/2100573432089866717) |
| jev-review (devagrawal09) | A staged code-review workflow and local dashboard built with TypeSafe Jev. | [仓库](https://github.com/devagrawal09/jev-review) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| jev-router (gargpratyush) | Per-turn model routing for Claude Code and Codex; requires Node.js 20.12+, a Jev key, and the corresponding CLI. | [仓库](https://github.com/gargpratyush/jev-router) |
| jev-review (NiazMorshed2007) | Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev. | [仓库](https://github.com/NiazMorshed2007/jev-review) |
| jev-mcp (jkudish) | Proof of concept MCP for Typesafe's new Jev AI model | [仓库](https://github.com/jkudish/jev-mcp) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| pi-warden | Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop | [仓库](https://github.com/DevMortimer/pi-warden) |
| typesafe-mcp | Go CLI and single-binary MCP server exposing TypeSafe judgments to Claude Desktop, Claude Code, and Codex. | [仓库](https://github.com/itsmostafa/typesafe-mcp) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| pi-jev (y0usaf) | TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers | [仓库](https://github.com/y0usaf/pi-jev) |
| ask-jev-skill | Skill for Hermes, and other agents, to ask typesafe's jev | [仓库](https://github.com/shantanugoel/ask-jev-skill) · [文章](https://x.com/KevinMagnan/status/2100587059928764726) |
| jev-codex-router | Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn. | [仓库](https://github.com/0xNatoshi/jev-codex-router) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| winnow | A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context. | [仓库](https://github.com/GhalebDweikat/winnow) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| jev-axi | Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell | [仓库](https://github.com/shiftynick/jev-axi) |
| pi-jev-auto-mode | Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made. | [仓库](https://github.com/jomatsu/pi-jev-auto-mode) |
| jev-mcp (blakestone-x) | MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer | [仓库](https://github.com/blakestone-x/jev-mcp) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| pi-jev-router | Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway | [仓库](https://github.com/mejiasd3v/pi-jev-router) |
| JevLint | Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. | [仓库](https://github.com/huntedman/JevLint) |
| typesafe-skill-router | TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn. | [仓库](https://github.com/DECRUX9812/typesafe-skill-router) |
| jev-agent-skill-router | Typed, confidence-aware agent skill routing with TypeSafe Jev. | [仓库](https://github.com/GodsBoy/jev-agent-skill-router) |
| Jevonian | Local OpenAI/Anthropic/Responses-compatible proxy for coding agents where one Jev call answers both the model route and the thinking level for `jevonian/auto`, after code has filtered candidates by protocol, context window, effort floor, and spent quota windows; a pinned model ID or explicit `jevonian/<route>` skips Jev entirely, and every turn is recorded with the serving model, the reason, real token usage, cache reads, and an estimated cost. | [仓库](https://github.com/xinyao27/jevonian) |
| pi-jev (TheoOliveira) | Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev | [仓库](https://github.com/TheoOliveira/pi-jev) |
| typesafe-cli (geilt) | CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments. | [仓库](https://github.com/geilt/typesafe-cli) |
| diffjury | DiffJury — TypeSafe Jev PR risk router + code review coach | [仓库](https://github.com/raihankhan-rk/diffjury) |
| jev-code | Bounded TypeSafe Jev workflows for coding agents. | [仓库](https://github.com/devagrawal09/jev-code) |
| jevex | Minimal agent loop where Jev directs control flow and a LangChain chat model writes argument values and the final response. | [仓库](https://github.com/jvsteiner/jevex) |
| typesafe-migration-guard | Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model) | [仓库](https://github.com/opaielsheikh/typesafe-migration-guard) |
| typesafe-mod | Claude Code mod that routes decisions to TypeSafe's Jev model: ranks installed skills per prompt, and answers the agent's own this-or-that questions when confident. | [仓库](https://github.com/BeLazy167/typesafe-mod) |
| jev-judgment | Agent Skill: send closed coding-agent judgments to TypeSafe Jev | [仓库](https://github.com/HyunjunJeon/jev-judgment) |
| jev-mcp (rashedInt32) | MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin. | [仓库](https://github.com/rashedInt32/jev-mcp) · [网站](https://www.npmjs.com/package/jev-mcp) |
| jev-shield | Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check. | [仓库](https://github.com/caiovicentino/jev-shield) |
| jcm-router | Local proxy that picks the Claude model and effort per message using TypeSafe Jev. Routes subagents, leaves your cached main chat alone. | [仓库](https://github.com/adarshmishra07/jcm-router) |
| pi-quiet-ask | TypeSafe Jev as the pi coding agent's quiet decision layer | [仓库](https://github.com/HyunjunJeon/pi-quiet-ask) |
| ailerix | Type-safe model router. Jev (System One) banks each request to a typed catalog route. | [仓库](https://github.com/tylerjharden/ailerix) · [网站](https://ailerix.vercel.app) |
| bicameral | Hybrid coding harness: System 2 writes, System 1 (Jev) runs reflexes. | [仓库](https://github.com/AbdelStark/bicameral) |
| jev-system-architect | System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives. | [仓库](https://github.com/samtay32/jev-system-architect) · [文章](https://x.com/Kantorcodes/status/2100607286498488587) |
| jev-mcp (benballintyn) | MCP server giving coding agents typed, calibrated judgments from TypeSafe's Jev model | [仓库](https://github.com/benballintyn/jev-mcp) |
| omp-typesafe | TypeSafe AI (Jev) adversarial reviewer and typesafe_ask tool for the omp coding agent | [仓库](https://github.com/siddicky/omp-typesafe) |
| ask-jev | Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions. | [仓库](https://github.com/omni-/ask-jev) |
| jev-predict-skill | Predict another skill's next closed decision with TypeSafe Jev — without running that skill. | [仓库](https://github.com/DanielKillenberger/jev-predict-skill) |
| Antigravity-mcp-semantic-search-with-TypeSafeAi | Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) powered by TypeSafe System One. | [仓库](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi) |
| jev-guard | Prompt-injection and dangerous-action guard for coding agents (Claude Code, Codex, pi, ACP), powered by Jev | [仓库](https://github.com/leepokai/jev-guard) |
| jev-skillful | Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps. | [仓库](https://github.com/bestagentkits/jev-skillful) |
| jev-router (prismhq) | Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM | [仓库](https://github.com/prismhq/jev-router) |
| jev-mcp (arunav25) | Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy. | [仓库](https://github.com/arunav25/jev-mcp) |
| jev-triage | Uses typeful jev, zero sync to pull and sync large repositories for issue triage | [仓库](https://github.com/cephalization/jev-triage) |
| omp-jevens-classifier | Jev-powered model-judged permission gate for OMP (TypeSafe System One) | [仓库](https://github.com/STRML/omp-jevens-classifier) |
| jev-mcp (burnigtm) | MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client | [仓库](https://github.com/burnigtm/jev-mcp) |
| pi-jev-code | Single-agent Pi coding coprocessor with Jev semantic gates, baseline-to-current diff review, and append-only observability telemetry. | [仓库](https://github.com/KamilPostrozny/pi-jev-code) |
| pi-agent-foreman | Send Pi agents back to work when they stop before the job is done. | [仓库](https://github.com/alexshpunt/pi-agent-foreman) · [网站](https://pi.dev/packages/pi-agent-foreman) |
| check-risk | A CLI and GitHub Action that assesses code-change risk using deterministic rules and TypeSafe Jev, recommending checks and reviewers before merge. | [仓库](https://github.com/moezubair/check-risk) |
| limpet | A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev. | [仓库](https://github.com/noplan-inc/limpet) |
| agent-gate-loop | Reusable GitHub Action: agent fix loop gated by checks, an AI reviewer, and TypeSafe Jev | [仓库](https://github.com/Ripwords/agent-gate-loop) |
| switchboard | Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python. | [仓库](https://github.com/aniruddh-krovvidi/switchboard) |
| frost | A flexible and configurable CLI model router using TypeSafe Jev. | [仓库](https://github.com/marcus/frost) · [网站](https://haplab.com) |
| pi-typesafe-jev | A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions. | [仓库](https://github.com/legacybridge-tech/pi-typesafe-jev) |
| pi-typesafe | Pi coding-agent extension built on the TypeSafe AI System One API (Jev) | [仓库](https://github.com/twilwa/pi-typesafe) |
| jev-review (thiago-ss) | Autonomous Jev pull-request review with typed decisions, calibrated approval gates, and trusted-owner escalation | [仓库](https://github.com/thiago-ss/jev-review) |
| hermes-jev-router | Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending. | [仓库](https://github.com/ussyverse/hermes-jev-router) |
| zcode-jev | Typed judgment layer for coding agents — gates from PRD to ship. Jev-ready, provider-agnostic. | [仓库](https://github.com/Zahrannnn/zcode-jev) |
| jev-builder-loop | Grok skill: Jev as a judgment sensor in a builder-agent loop (priors × probabilities → next act) | [仓库](https://github.com/rainbowpuffpuff/jev-builder-loop) |
| typesafeai-review | Using Typesafe.AI to generate diff reviews. | [仓库](https://github.com/rbalch/typesafeai-review) |
| typesafe-demo-mcp | MCP server exposing TypeSafe System One judgments (noul, choice, score) as agent tools | [仓库](https://github.com/bestagentkits/typesafe-demo-mcp) |
| agent-handoff-gate | Experimental protocol for evidence-aware agent handoffs, with Jev-assisted review before results reach the lead agent. | [仓库](https://github.com/zsoXi/agent-handoff-gate) · [文章](https://x.com/zxdubx/status/2100604919120121960) |
| fabricioctelles/skills | A collection of skills for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusable module that teaches the agent to perform complex tasks with context, structure, and best practices. | [仓库](https://github.com/fabricioctelles/skills) · [网站](https://skilldev.pro) |
| dbreunig/building-with-jev-skill | A skill for writing and improving programs that call Jev, TypeSafe's System One model | [仓库](https://github.com/dbreunig/building-with-jev-skill) |
| superagents-lab/jev-search | Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API. | [仓库](https://github.com/superagents-lab/jev-search) · [网站](https://jev.s1.dev) |
| Dicklesworthstone/skillranker | Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key. | [仓库](https://github.com/Dicklesworthstone/skillranker) |
| supercorp-ai/supercov | Code quality and coverage for coding agents | [仓库](https://github.com/supercorp-ai/supercov) · [网站](https://supercov.com) |
| DanRWilloughby/snifftest | A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. | [仓库](https://github.com/DanRWilloughby/snifftest) · [网站](https://www.npmjs.com/package/snifftest) |
| anpicasso/hermes-jev-approvals | PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only. | [仓库](https://github.com/anpicasso/hermes-jev-approvals) |
| doeixd/jev-pref | Turn your AGENTS.md preferences into a fast, Jev-powered AI linter. | [仓库](https://github.com/doeixd/jev-pref) |
| iamvatsalpatel/tiershift | Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No training data. Policy in plain YAML. TypeScript and Python. | [仓库](https://github.com/iamvatsalpatel/tiershift) |
| MongLong0214/jev-gate | Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary. | [仓库](https://github.com/MongLong0214/jev-gate) |
| ShivamPansuriya/jev-skill-gate | Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session. | [仓库](https://github.com/ShivamPansuriya/jev-skill-gate) · [网站](https://github.com/ShivamPansuriya/jev-skill-gate#does-it-pick-the-right-skills) |
| aegsrl7/jevmap | Map a codebase into units and let Jev (TypeSafe AI) hand an AI coding agent the ten files that matter for a task | [仓库](https://github.com/aegsrl7/jevmap) |
| altryne/jevify | An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments. | [仓库](https://github.com/altryne/jevify) · [网站](https://thursdai.news) |
| buchmark/claude-jev | Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion. | [仓库](https://github.com/buchmark/claude-jev) |
| harrymunro/decision-first | Agent skill that spots bounded-judgment steps, tries a typed decision model (TypeSafe's Jev) first, and documents every attempt | [仓库](https://github.com/harrymunro/decision-first) |
| poponline63/hermes-jev-north-star | Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven. | [仓库](https://github.com/poponline63/hermes-jev-north-star) |
| qkal/Canny | Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Jev advises. Append-only ledger, zero runtime dependencies. | [仓库](https://github.com/qkal/Canny) |
| rthomas24/jev-realtime-trading | Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app. | [仓库](https://github.com/rthomas24/jev-realtime-trading) |
| 24601/Augustus | Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT. | [仓库](https://github.com/24601/Augustus) · [网站](https://github.com/24601/Augustus/blob/main/docs/ecosystem.md) |
| aaravriyer193/OpenSmoke | Find the AI agent runs that broke because their environment did: missing keys, tools, files, permissions, network, or context. Powered by TypeSafe Jev. | [仓库](https://github.com/aaravriyer193/OpenSmoke) |
| AkashPriyadarshii/jev-superpowers | Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions | [仓库](https://github.com/AkashPriyadarshii/jev-superpowers) |
| AlexBabescu/ActionJev | Structured code review for GitHub and Gitea Actions, powered by TypeSafe Jev and written in Rust. | [仓库](https://github.com/AlexBabescu/ActionJev) |
| ArkadyBuryakov/jev-preview | TUI Sandbox for Typesafe Jev API | [仓库](https://github.com/ArkadyBuryakov/jev-preview) |
| BrunooMoniz/polymarket-btc-5m-agent | Agente de trading para o mercado BTC Up/Down de 5 minutos da Polymarket: modelo em código, Jev (TypeSafe System One) como portão, ordens maker, calibração e shadows em paper | [仓库](https://github.com/BrunooMoniz/polymarket-btc-5m-agent) |
| CodeAlive-AI/mastra-jev-moderation | Input moderation for Mastra agents on TypeSafe Jev — one file | [仓库](https://github.com/CodeAlive-AI/mastra-jev-moderation) |
| ddfeyes/jev-mode | I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT. | [仓库](https://github.com/ddfeyes/jev-mode) |
| dsandrade/jevra | An open-source decision layer connecting coding agents with TypeSafe Jev. | [仓库](https://github.com/dsandrade/jevra) |
| Eliran-Turgeman/reaper | Semantic linter for AI coding agents and CI code review. Detects silent failures, weakened tests, scope creep, unnecessary abstractions, and other semantic code smells. | [仓库](https://github.com/Eliran-Turgeman/reaper) |
| eyenpi/actionreflex | A pre-execution gate for AI agent actions, powered by TypeSafe's Jev (System One) model. | [仓库](https://github.com/eyenpi/actionreflex) |
| fabricio852/jevshift | ⚡ Token Saver & Fast Decision Layer for OpenAI Codex — powered by Jev | [仓库](https://github.com/fabricio852/jevshift) |
| getexcited/stepwarden | Every tool call your agent makes, checked before it runs. A Claude Code plugin that uses TypeSafe AI's Jev to verify each pending tool call against the session plan, then allows it, asks you, or blocks it. Proof of concept | [仓库](https://github.com/getexcited/stepwarden) · [网站](https://github.com/getexcited/claude-plugins) |
| ibrahemid/git-jev-stage | Stage the git hunks that match a sentence. Exact patch, preview first, staging only, decided per hunk by Jev. | [仓库](https://github.com/ibrahemid/git-jev-stage) |
| ibrahemid/jevprune | Keeps the lines of a command's output that matter for the task. Exact text, full output recoverable, decided per line by Jev. | [仓库](https://github.com/ibrahemid/jevprune) |
| ivorpad/skillranker | Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key. | [仓库](https://github.com/ivorpad/skillranker) |
| kaustav1996/reflex | A coding agent and personal assistant with System One reflexes (TypeSafe Jev) on top of the Pi coding agent | [仓库](https://github.com/kaustav1996/reflex) |
| kevin9327/jev-harness | JevHarness: TypeSafe Jev agent tool-call gate. execute / confirm / reject in code. | [仓库](https://github.com/kevin9327/jev-harness) |
| knowlet/Decision-Theoretic-Mixture-of-Agents | A fully audited, reproducible decision‑theoretic mixture‑of‑agents framework comparing multiple selector strategies, including OpenJev, with transparent calibration, limitations, and verification artifacts. | [仓库](https://github.com/knowlet/Decision-Theoretic-Mixture-of-Agents) |
| manojlds/jev-review | Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff. | [仓库](https://github.com/manojlds/jev-review) |
| Mentioum/judgement | Agent-friendly Go library and JSON-first CLI for TypeSafe AI's Jev and System One API | [仓库](https://github.com/Mentioum/judgement) |
| milokuo/tagtrim | Tag every line of a command's output, then trim by tag, so your coding agent reads the signal, not the noise. Design stage. | [仓库](https://github.com/milokuo/tagtrim) |
| pistachiopranay/jev-synergy-screening | Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels | [仓库](https://github.com/pistachiopranay/jev-synergy-screening) |
| rashedInt32/jev-gates | Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves. | [仓库](https://github.com/rashedInt32/jev-gates) |
| RiskAverseTech/toolgate | Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Code hook | [仓库](https://github.com/RiskAverseTech/toolgate) |
| rustfuture/reflex-control | Rust policy engine using TypeSafe Jev and deterministic checks to route AI agent decisions. | [仓库](https://github.com/rustfuture/reflex-control) |
| suraj-phanindra/wellposed | Lint your jev requests before they come back confidently wrong. | [仓库](https://github.com/suraj-phanindra/wellposed) |
| Thestral12/pr-sieve | Semantic PR gate: .jev.yml rules as TypeSafe Jev questions. Not a review bot. | [仓库](https://github.com/Thestral12/pr-sieve) |
| wotai-dev/typesafe-jev-tools | A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5. | [仓库](https://github.com/wotai-dev/typesafe-jev-tools) |

<a id="browser"></a>

## 浏览器与电脑操作

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| jev-skip | Browser extension that uses Jev to identify potential sponsor segments from YouTube captions. | [仓库](https://github.com/valentynkit/jev-skip) |
| Jev Ultrafast | Browser Use's ultrafast agent: Jev picks the operation and DOM element in one request; a small LLM only writes text when typing is needed. | [仓库](https://github.com/browser-use/jev-ultrafast) · [网站](https://browser-use.com) · [文章](https://x.com/gregpr07/status/2100411066966749359) |
| typesafe-computer-use | Computer use for about $0.0002 a step: OCR the screen, classify the next action with TypeSafe, click. macOS. | [仓库](https://github.com/awlevin/typesafe-computer-use) · [文章](https://x.com/awlevin/status/2100262612428894676) |
| mobile-jev | Standalone Android agent for Mobilerun where Jev makes every decision, with a live React studio and an Uber demo. | [仓库](https://github.com/droidrun/mobile-jev) |
| unclutter | WXT browser extension: Jev-powered page clutter removal with reusable template rules. | [仓库](https://github.com/kitze/unclutter) · [文章](https://x.com/thekitze/status/2100595129874817340) |
| jev-browser (vlad-terin) | Jev-powered element selection for your agent’s existing computer-use tools | [仓库](https://github.com/vlad-terin/jev-browser) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| jev-browser (Ying-Kai-Liao) | Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server. | [仓库](https://github.com/Ying-Kai-Liao/jev-browser) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| jev-browser (vinilana) | Hybrid browser harness: an LLM turns goals into verifiable subgoals, Jev chooses each action and DOM field, Playwright acts. | [仓库](https://github.com/vinilana/jev-browser) |
| jev-ego | TypeScript browser agent for ego lite: Jev Ultrafast indexed actions, TypeSafe Jev decisions, persistent observe/act CLI. No Chrome or Playwright. | [仓库](https://github.com/romaluev/jev-ego) |
| computer_use | macOS computer use driven by Jev (TypeSafe System One) as the decision maker | [仓库](https://github.com/paulsmith/computer-use-jev) |
| psearch | Parallel web search for terminals and agents, with local Chromium and Jev-guided exploration. | [仓库](https://github.com/komikat/psearch) |
| almond-fastloop | Almond-fastloop: Almond's browser computer-use rig (Chrome DevTools + TypeSafe Jev), and the Browser Use Olympics benchmark it is measured on. | [仓库](https://github.com/eriestra/almond-fastloop) |
| barrunto | A Chrome extension that brings TypeSafe's Jev to X.com to analyze posts as you browse | [仓库](https://github.com/elpumberto/barrunto) |
| jev-browser (tontoko) | One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions. | [仓库](https://github.com/tontoko/jev-browser) |
| otto | Open-source native computer use for macOS and Windows: TypeSafe Jev, local OCR, and selective planning. | [仓库](https://github.com/NobleSpartan6/otto) |
| jev-browse | Drives a real browser with Jev making every decision and Vercel's agent-browser performing every action, with a benchmark. | [仓库](https://github.com/kyrylosyzonenko/jev-browse) |
| sift | Chrome extension that re-ranks Google results with TypeSafe Jev and folds away sales pages and SEO filler. | [仓库](https://github.com/tylergibbs1/sift) |
| jev-mobile | Fast structured Android control loops with TypeSafe Jev and Mobile MCP | [仓库](https://github.com/Friedjof/jev-mobile) |
| browser-use-olympics | Browser Use Olympics by Almond: one prompt, five events, one clock. Plus fast loop, a ~200-line browser computer-use agent (Chrome DevTools + TypeSafe Jev). | [仓库](https://github.com/eriestra/browser-use-olympics) |
| turbo | Jev-powered semantic browser use | [仓库](https://github.com/sightmap/jev-turbo) |
| sloppy-jevs-extension | Open-source Chrome extension that filters AI-generated prose and ads with Jev | [仓库](https://github.com/neddes/sloppy-jevs-extension) |
| jev-browser (MahmoudAdelbghany) | Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included. | [仓库](https://github.com/MahmoudAdelbghany/jev-browser) |
| jev-playwright-mcp | Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent. | [仓库](https://github.com/krw82/jev-playwright-mcp) |
| jev-browser (KesavanKing) | Local browser automation UI that uses TypeSafe Jev to choose bounded page actions and a text model only for field values. | [仓库](https://github.com/KesavanKing/jev-browser) |
| JevTest | Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence. | [仓库](https://github.com/CorieW/JevTest) · [网站](https://jevtest.dev) |
| socai-io/socai | Browser & Computer-Use Agent Optimized for Social Media: Research, Content Extraction, and Agentic Analysis | [仓库](https://github.com/socai-io/socai) · [网站](https://socai.io/) |
| jkudish/jev-browser | Browser use using Typesafe's Jev model | [仓库](https://github.com/jkudish/jev-browser) |
| moritzkremb/jev-voice-browser | Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence. | [仓库](https://github.com/moritzkremb/jev-voice-browser) |
| anandi1989/awesome-jev-usecases | Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results | [仓库](https://github.com/anandi1989/awesome-jev-usecases) · [网站](https://anandi1989.github.io/awesome-jev-usecases/) |
| Heman10x-NGU/Verdict-open-jev | Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground | [仓库](https://github.com/Heman10x-NGU/Verdict-open-jev) |
| vinilana/live-jev | 2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model | [仓库](https://github.com/vinilana/live-jev) |
| mikesmullin/openjev | Local reproduction of AlexWortega/openjev (Qwen3.5-4B NLI cross-encoder playing Doom), plus real-time headed play and a browser front-end | [仓库](https://github.com/mikesmullin/openjev) |
| Nainish-Rai/jev-frontend-qa | Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo. | [仓库](https://github.com/Nainish-Rai/jev-frontend-qa) |
| ranjan2829/AskJev | AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude) | [仓库](https://github.com/ranjan2829/AskJev) · [网站](https://docs.typesafe.ai/introduction) |
| kw2828/OpenJev | Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control | [仓库](https://github.com/kw2828/OpenJev) · [网站](https://kw2828.github.io/OpenJev/) |
| raihankhan-rk/jevarena | JevArena — two Jev agents duel in click-only browser games (Browser Use + TypeSafe Jev) | [仓库](https://github.com/raihankhan-rk/jevarena) |
| AE-AlphaEdge/grokskill-jev | Public Grok skill snapshot around Browser Use Jev Ultrafast | [仓库](https://github.com/AE-AlphaEdge/grokskill-jev) · [网站](https://github.com/browser-use/jev-ultrafast) |
| bramtechs/Focus | Browser extension that blocks distracting websites using TypeSafe: Jev | [仓库](https://github.com/bramtechs/Focus) |
| cartermccann/typesafe-computer-use-hyprland | Hyprland/NixOS fork of typesafe-computer-use — grim + hyprctl + ydotool, TypeSafe Jev decisions | [仓库](https://github.com/cartermccann/typesafe-computer-use-hyprland) |
| CharryLee0426/jev-test | Testing TypeSafe's Jev model on real-time browser games (flappybird.io, play.tetris.com) | [仓库](https://github.com/CharryLee0426/jev-test) |
| juancristobalgd1/jevRemote | Reproducible text-first browser automation experiment with TypeSafe Jev and Playwright. | [仓库](https://github.com/juancristobalgd1/jevRemote) · [网站](https://juancristobalgd1.github.io/jevRemote/) |
| max1874/jev-computer-use | A macOS computer-use agent with a dynamic, indexed action space. No screenshots, no coordinates. A macOS port of browser-use/jev-ultrafast. | [仓库](https://github.com/max1874/jev-computer-use) |
| sandra-arato/icon-matcher-ui | Browser-only UI for icon-matcher — paste a TypeSafe.ai key, match a UI title to an icon live, no backend. | [仓库](https://github.com/sandra-arato/icon-matcher-ui) · [网站](https://icon-matcher-ui.vercel.app) |
| shantanugoel/tetris-ai | Browser Tetris with a first-class AI API: play it with a built-in planning agent, TypeSafe's Jev decision model, or any OpenAI-compatible chat model | [仓库](https://github.com/shantanugoel/tetris-ai) |
| thevibeworks/awesome-typesafe-jev | Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI. | [仓库](https://github.com/thevibeworks/awesome-typesafe-jev) · [网站](https://thevibeworks.github.io/awesome-typesafe-jev/) |
| thevibeworks/pagepilot | An agent in the browser that pays for thinking once: author a deterministic spec (Jev first, LLM on escalation), replay it for 0 tokens. | [仓库](https://github.com/thevibeworks/pagepilot) |
| usingcolor/jev-browser-plugin | Agent plugin: TypeSafe Jev browser automation skills for Grok Bot / Cursor | [仓库](https://github.com/usingcolor/jev-browser-plugin) |
| yatharth1706/jev-automation | Trying automation on web browser via jev from typesafe | [仓库](https://github.com/yatharth1706/jev-automation) |
| yousudip/lizard-agent | A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable. | [仓库](https://github.com/yousudip/lizard-agent) |

<a id="apps"></a>

## 应用

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| jev-trader | One AI trade decision every Monad block. Jev on Kuru MON-USDC. | [仓库](https://github.com/jarrodwatts/jev-trader) · [网站](https://jev-trader.vercel.app/) · [文章](https://x.com/jarrodwatts/status/2100356151468585346) |
| notra | Marketing analytics platform whose feature flag routes brand-visibility classifiers off an LLM and onto Jev boolean decisions. | [仓库](https://github.com/usenotra/notra) · [网站](https://www.usenotra.com/) |
| jevmeter | Put a live Jev (TypeSafe) meter on any video: every sentence scored, rendered as a 16:9 edit | [仓库](https://github.com/ChetasLua/jevmeter) · [文章](https://x.com/chetaslua/status/2100602714204049588) |
| Jev-Moderation-Bot | Real-time Discord moderation bot: Jev evaluates messages and metadata in parallel to catch phishing, spam, and social engineering with a progressive escalation ladder. | [仓库](https://github.com/brainstormity/Jev-Moderation-Bot) |
| commit-miner | Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types. | [仓库](https://github.com/devanshbatham/commit-miner) |
| blink | Codebase search powered by Jev from @typesafe-ai | [仓库](https://github.com/ellipsis-dev/blink) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| ai-elo-ranker | High-speed recursive AI Elo tournament engine powered by Jev and Swiss matchmaking | [仓库](https://github.com/opaielsheikh/ai-elo-ranker) |
| jevlogs | Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. | [仓库](https://github.com/reachjalil/jevlogs) |
| semdecide | Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev. | [仓库](https://github.com/sharziki/semdecide) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| typesafe-cli (y0usaf) | Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose | [仓库](https://github.com/y0usaf/typesafe-cli) |
| jevibe-check | A live tone labeler for Bluesky posts and drafts, using TypeSafe's Jev API. | [仓库](https://github.com/sriganesh/jevibe-check) |
| every | Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev. | [仓库](https://github.com/sufianetaouil/every) |
| commentcop | Put your code comments on trial. Powered by Jev. | [仓库](https://github.com/ntedvs/commentcop) |
| jev-cli | CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out | [仓库](https://github.com/jtsang4/jev-cli) |
| btc-jev-signal | Experimental multi-horizon BTC signal generator using TypeSafe Jev probabilities and Binance market data. | [仓库](https://github.com/WebGrga/btc-jev-signal) |
| JevTicktRouter | A .NET 10 and React 19 application for fast, structured AI-powered ticket triage using TypeSafe Jev. | [仓库](https://github.com/GhrezaKh74/JevTicktRouter) |
| draftpulse | Experimental: live X draft viral scorer powered by TypeSafe Jev | [仓库](https://github.com/pekth/draftpulse) |
| jev-document-classification | JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model. | [仓库](https://github.com/Charlyhno-eng/jev-document-classification) |
| typesafe-jev | Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring. | [仓库](https://github.com/gtaras7/typesafe-jev) |
| typesafe-triage-guard | Three composable judgment pipelines on TypeSafe's Jev: support-ticket triage, observability alert triage, and a deploy-risk gate. | [仓库](https://github.com/shivam2003-dev/typesafe-triage-guard) |
| jevegis | Guardrails for LLM apps in one API call. Prompt injection, jailbreaks, leaks, unsafe content. Built on TypeSafe Jev. MIT. | [仓库](https://github.com/0xArx/jevegis) · [网站](https://jevegis.vercel.app) |
| citation-verifier | Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides. | [仓库](https://github.com/MarissaFamularo/citation-verifier) · [网站](https://verify.papertrellis.com) |
| jev-rerank | Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0. | [仓库](https://github.com/hev/reranker) |
| emoji-jev | Emoji autocomplete at the speed of typing. TypeSafe AI Jev on a Whop-hosted TanStack Start app. | [仓库](https://github.com/colinmcdermott/emoji-jev) |
| jev-resume-analyzer | CV diagnostics and job alignment with TypeSafe Jev, React and FastAPI | [仓库](https://github.com/awun8191/jev-resume-analyzer) |
| jev-audio-beeper | Low-latency audio censorship POC using Jev typed decisions and ffmpeg. | [仓库](https://github.com/santos-sanz/jev-audio-beeper) |
| scam-shield | Scam text message filter powered by TypeSafe's Jev model | [仓库](https://github.com/ShupingR/scam-shield) · [网站](https://scam-shield-seven-ecru.vercel.app) |
| typesafe-comment | Small Python package that uses typesafe.ai to evaluate code comments on certain heuristics | [仓库](https://github.com/Hexdigest123/typesafe-comment) |
| transcript-scorecard | ACME live support-call scoring demo with TypeSafe AI, Effect, SQLite, React, Vite, and Turborepo | [仓库](https://github.com/brandonbryant12/transcript-scorecard) |
| mimicry | Rewrite AI drafts in your own voice with a bounded TypeSafe feedback loop. | [仓库](https://github.com/jxucoder/mimicry) |
| s1s | System One Search: navigate and trace code with TypeSafe judgments and repository evidence | [仓库](https://github.com/cpaczek/s1s) · [网站](https://s1s.iar.dev) |
| pkg-gate | Pre-install security gate for npm lifecycle scripts using TypeSafe System One. | [仓库](https://github.com/hemanth/pkg-gate) · [网站](https://hemanth.github.io/pkg-gate/) |
| Jev Classifier | Local Telegram channel JSON analyzer for intent, quality, sentiment, and speaker tone. | [网站](https://jevclassifier.vercel.app) · [文章](https://x.com/DagmawiBabi/status/2100618066459553796) |
| dmx.to | X client with Jev smart rules that filter the timeline by usefulness, type, and topic. | [网站](https://dmx.to) · [文章](https://x.com/thekitze/status/2100570975175877106) |
| TheoLeeCJ/SemIf | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. | [仓库](https://github.com/TheoLeeCJ/SemIf) · [网站](https://openjev.com) |
| realZachi/pg-jev | Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev. | [仓库](https://github.com/realZachi/pg-jev) · [网站](https://pgjev.com) |
| ekzhang/openjev-sglang | Jev-compatible API endpoint based on open models (prefill-only) | [仓库](https://github.com/ekzhang/openjev-sglang) · [网站](https://ekzhang--openjev-sglang-openjev.us-west.modal.direct) |
| realZachi/typesafe-adblock | 🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker. | [仓库](https://github.com/realZachi/typesafe-adblock) |
| mrnugget/jev-shell-history | Fish-style zsh history autosuggestions ranked by Jev (TypeSafe) | [仓库](https://github.com/mrnugget/jev-shell-history) |
| razorback16/openjev | Open, Jev-compatible System One decision server on DiffusionGemma | [仓库](https://github.com/razorback16/openjev) · [网站](https://codiv.ai) |
| RafalWilinski/vibecheck | Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post | [仓库](https://github.com/RafalWilinski/vibecheck) |
| dannote/jev | TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer | [仓库](https://github.com/dannote/jev) |
| compozy/yoshi | Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy | [仓库](https://github.com/compozy/yoshi) |
| zadescoxp/Jev-Trades | Trading bot with the all new TypeSafe AI's first system one model named as Jev | [仓库](https://github.com/zadescoxp/Jev-Trades) · [网站](https://jevtrades.zadescoxp.com) |
| stephanj/parallelConstraintDecoding | Parallel Constraint Decoding using Java and Llama.cpp compared to Python 🔥 | [仓库](https://github.com/stephanj/parallelConstraintDecoding) |
| AlbionaHoti/refgarden | A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked collections. | [仓库](https://github.com/AlbionaHoti/refgarden) |
| komorra/Eugeniusz | Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine. | [仓库](https://github.com/komorra/Eugeniusz) |
| manifoldor/xtags | 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。 | [仓库](https://github.com/manifoldor/xtags) |
| scale-venture-partners/riff | A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model | [仓库](https://github.com/scale-venture-partners/riff) |
| arielweinberger/jev-autopilot | This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01. | [仓库](https://github.com/arielweinberger/jev-autopilot) |
| keeltrace/hermes-jev | Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev. | [仓库](https://github.com/keeltrace/hermes-jev) |
| unicodeveloper/jevocks | Everyday Stocks Status with Jev | [仓库](https://github.com/unicodeveloper/jevocks) · [网站](https://jevinik.up.railway.app) |
| DECRUX9812/openjev | Open, local, zero-cost reimplementation of the Jev decision layer for job postings | [仓库](https://github.com/DECRUX9812/openjev) |
| djangobeatty/textured | Textured — Sounds of words. A musical toy from Fluxus. | [仓库](https://github.com/djangobeatty/textured) · [网站](https://textured.fyi/) |
| EugeneBoondock/jevsql | SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by meaning — batched, cached and cost-guarded. | [仓库](https://github.com/EugeneBoondock/jevsql) |
| luantak/is-malicious | A codebase scanner that helps you to not run malicous code | [仓库](https://github.com/luantak/is-malicious) |
| maker-KK/todo-jev | ⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One) | [仓库](https://github.com/maker-KK/todo-jev) |
| reachjalil/jev-tree | Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. | [仓库](https://github.com/reachjalil/jev-tree) · [网站](https://reachjalil.github.io/jev-tree/) |
| reycn/smart-switch | Reimagined window switcher for macOS using frontier artificial intelligence. Predicted by TypeSafe's Jev model | [仓库](https://github.com/reycn/smart-switch) |
| tumf/jev-cli | Small dependency-free CLI for TypeSafe Jev | [仓库](https://github.com/tumf/jev-cli) · [网站](https://docs.typesafe.ai/introduction) |
| vmendes90/jev-shield | Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev | [仓库](https://github.com/vmendes90/jev-shield) |
| wfzyx/von | The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev. | [仓库](https://github.com/wfzyx/von) |
| anxkhn/JevPlaysPokemon | Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM. | [仓库](https://github.com/anxkhn/JevPlaysPokemon) |
| erhanmeydan/jev2048 | TypeSafe'in Jev karar modeli gerçek bir online 2048 sitesinde oynuyor — hamle başına tek API çağrısı, tek anahtar. | [仓库](https://github.com/erhanmeydan/jev2048) |
| fernandoviac/judged | Focused terminal interface for typed judgments from TypeSafe System One. | [仓库](https://github.com/fernandoviac/judged) |
| franknoh/OpenJev | 原始资料未提供说明。 | [仓库](https://github.com/franknoh/OpenJev) |
| keltokhy/jlink | Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, cite it. Python, CLI, Stata and R. | [仓库](https://github.com/keltokhy/jlink) |
| kitze/pagegrade | Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev. | [仓库](https://github.com/kitze/pagegrade) |
| Nasrallah-AL/jev-cli | Command-line tool for TypeSafe's Jev AI model | [仓库](https://github.com/Nasrallah-AL/jev-cli) · [网站](https://jevcli.vectorz.app/) |
| qddegtya/qualm | Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it. | [仓库](https://github.com/qddegtya/qualm) · [网站](https://github.com/qddegtya/qualm#readme) |
| Red5d/jev-cvss | Fast CVSS scoring from vulnerability descriptions using Typesafe Jev | [仓库](https://github.com/Red5d/jev-cvss) |
| soderlind/ai-provider-for-jev | Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul). | [仓库](https://github.com/soderlind/ai-provider-for-jev) |
| solhosty/last-train-jev | A small detective escape room built with TypeSafe Jev, React, and Express. | [仓库](https://github.com/solhosty/last-train-jev) |
| StefanoITA/ts-jev-cost-calculator | Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe. | [仓库](https://github.com/StefanoITA/ts-jev-cost-calculator) |
| youshinh/md-memo | A zero-latency, local-first Markdown scratchpad with offline AI (Ollama/vLLM) and autonomous IME control. Built with Go and OS-native webviews. | [仓库](https://github.com/youshinh/md-memo) · [网站](https://youshinh.github.io/md-memo/) |
| 0xnairb/jevpot | AI-powered jackpot number predictor and intelligence oracle built with TypeSafe System One (Jev) | [仓库](https://github.com/0xnairb/jevpot) |
| 0xSarnavo/potpie-doc-parser | Ask the Potpie docs a question, get the exact paragraph that answers it. Extractive search powered by Jev (TypeSafe System One) — no LLM, no embeddings, nothing generated. | [仓库](https://github.com/0xSarnavo/potpie-doc-parser) |
| afanjul/jev-llm | Fake autoregressive language model powered by TypeSafe Jev | [仓库](https://github.com/afanjul/jev-llm) |
| AkashPriyadarshii/jev-git | Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev | [仓库](https://github.com/AkashPriyadarshii/jev-git) · [网站](https://typesafe.ai) |
| allay-team/openjev | 原始资料未提供说明。 | [仓库](https://github.com/allay-team/openjev) |
| amithkk/jev-experiments | Experiments with Typesafe's Jev | [仓库](https://github.com/amithkk/jev-experiments) |
| aoi-yoneda/haikyuBattleJev | Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風 | [仓库](https://github.com/aoi-yoneda/haikyuBattleJev) |
| Ayush0054/metis | Metis: automatic GitHub issue triage powered by TypeSafe AI Jev. A reusable GitHub Action. | [仓库](https://github.com/Ayush0054/metis) |
| BradMyrick/Jev-Rug-Checker | a multi-chain EVM token screener built on Jev by @TypeSafe AI | [仓库](https://github.com/BradMyrick/Jev-Rug-Checker) |
| chrisXchen/typesafe-cookie-consent | Chrome extension that reads every cookie banner and popup like a person and clicks the honest button. Judged by TypeSafe's Jev. BYOK, no backend. | [仓库](https://github.com/chrisXchen/typesafe-cookie-consent) |
| derinworks/penr-oz-jev-syslog-analyzer | An asyncio daemon that tails journald or syslog and asks Jev, for each event, which subsystem it belongs to, how severe it is, and whether it's noise. Plain code then ignores the event, alerts on it, or escalates it to a human when confidence is low. | [仓库](https://github.com/derinworks/penr-oz-jev-syslog-analyzer) |
| distributedlabs/magic-8-ball | A TypeSafe Jev-powered Magic 8 Ball | [仓库](https://github.com/distributedlabs/magic-8-ball) |
| djascorp/jev-trade | Trading project using JEV by TypeSafe AI | [仓库](https://github.com/djascorp/jev-trade) |
| edsonayllon/jev-prototype | Feed triage prototype: TypeSafe Jev judgments tag posts by type, sentiment, and attention | [仓库](https://github.com/edsonayllon/jev-prototype) |
| EdytaKucharska/ticket-quest | Playful ticket triage that shows how TypeSafe Jev's typed, probability-backed decisions compare with prompting an LLM. Cost of Delay ranking, certainty-gated routing, bring-your-own-key LLM race. | [仓库](https://github.com/EdytaKucharska/ticket-quest) · [网站](https://ticket-quest-three.vercel.app) |
| farukkavlak/vocabboost | Look up a word from the subtitles and see what it means in that line, without leaving the video. | [仓库](https://github.com/farukkavlak/vocabboost) |
| gpazo/jev-vphone-cli | Jev from Typesafe.ai + vphone-cli | [仓库](https://github.com/gpazo/jev-vphone-cli) |
| gzd2032/typesafe-ai-test | a test repo for typesafe.ai | [仓库](https://github.com/gzd2032/typesafe-ai-test) |
| hasura/jev-test-datasets | Public repo containing generated synthetic data to test jev from typesafe | [仓库](https://github.com/hasura/jev-test-datasets) |
| hide-G/magi-system-on-jev | MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question. | [仓库](https://github.com/hide-G/magi-system-on-jev) |
| jagenaujagenau/ground-truth | Ground News style bias check for the article in your current tab. | [仓库](https://github.com/jagenaujagenau/ground-truth) · [网站](https://groundtruth.click/) |
| jdhornsby/typesafe-jev | 原始资料未提供说明。 | [仓库](https://github.com/jdhornsby/typesafe-jev) |
| jflam/jev1 | Jev (TypeSafe System One) proof of concept: smart-home assistant demo | [仓库](https://github.com/jflam/jev1) |
| joshbla/jev-plays-2048 | A visible 2048 experiment powered by TypeSafe | [仓库](https://github.com/joshbla/jev-plays-2048) |
| juanegido/jev-pr-judge | Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action | [仓库](https://github.com/juanegido/jev-pr-judge) · [网站](https://jev-pr-judge.vercel.app) |
| jujumilk3/jev-calibration-audit | Independent API-only calibration audit of TypeSafe AI's Jev decision model | [仓库](https://github.com/jujumilk3/jev-calibration-audit) |
| JustinRoderick/jev-test | Testing typesafe.ai new model Jev | [仓库](https://github.com/JustinRoderick/jev-test) |
| kaijia323/dsh-plugin-jev | TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness | [仓库](https://github.com/kaijia323/dsh-plugin-jev) |
| kamesan1577/re-heitan | X（旧Twitter）のタイムラインから誹謗中傷を取り除く Chrome 拡張。判定を TypeSafe の System One モデル Jev で行う。 | [仓库](https://github.com/kamesan1577/re-heitan) |
| kenhuangus/jev-usecases | Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic | [仓库](https://github.com/kenhuangus/jev-usecases) |
| kevin9327/jev-code | JevCode: TypeSafe Jev diff merge gate. merge / comment / block in code. | [仓库](https://github.com/kevin9327/jev-code) |
| kspviswa/chakravyuha-jev | Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step. | [仓库](https://github.com/kspviswa/chakravyuha-jev) |
| kylemclaren/jevql | Semantic SQL for vanilla Postgres. Powered by Jev | [仓库](https://github.com/kylemclaren/jevql) · [网站](https://jevql.fly.dev/) |
| lainollll/lm-studio-typesafe-chat | Tkinter chat and live visual narration with LM Studio, TypeSafe Jev, and Chatterbox TTS | [仓库](https://github.com/lainollll/lm-studio-typesafe-chat) |
| lautaroalejo02/TypeSafe-Test-Project | This is just for testing TypeSafe AI | [仓库](https://github.com/lautaroalejo02/TypeSafe-Test-Project) · [网站](https://jev-pilot-proxy.vercel.app) |
| lhotwll217/jev-cli | JSON-in, typed-decisions-out CLI for the TypeSafe System One API | [仓库](https://github.com/lhotwll217/jev-cli) |
| LingXuanYin/jev-chat | Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。 | [仓库](https://github.com/LingXuanYin/jev-chat) · [网站](https://cohub.live/ncyg191125/jev-chat/w/jev-chat) |
| linw1995/dify-plugin-typesafe-ai | 原始资料未提供说明。 | [仓库](https://github.com/linw1995/dify-plugin-typesafe-ai) |
| m0rphtail/triagedy | Alert triage as a UNIX filter: JSONL security alerts in, typed decisions out. Runs on TypeSafe Jev or a local model; policy routing stays in code. | [仓库](https://github.com/m0rphtail/triagedy) |
| mahan-ym/cleaner | An experiment with JEV from typesafe.ai to clean up my useless data. | [仓库](https://github.com/mahan-ym/cleaner) |
| makefinks/jev-feed-filter | Smart, dynamic AI filtering for X and YouTube feeds using Jev | [仓库](https://github.com/makefinks/jev-feed-filter) |
| marcelomar21/demo-tetris-jev | Tetris arcade jogado pelo Jev da TypeSafe AI, com decisões em JSON, antecipação de jogadas e custo por partida. | [仓库](https://github.com/marcelomar21/demo-tetris-jev) |
| markfive-proto/typesafe-vs-deepseek | TypeSafe (Jev) vs DeepSeek-flash: side-by-side speed/token/cost/accuracy comparison across invoice extraction, email classification, and reranking | [仓库](https://github.com/markfive-proto/typesafe-vs-deepseek) · [网站](https://typesafe-vs-deepseek.vercel.app) |
| markmdev/hundred-faces | A wall of a hundred invented people who react while you type, on TypeSafe AI's Jev | [仓库](https://github.com/markmdev/hundred-faces) |
| mattn/sqlite3-jev | SQLite extension that calls TypeSafe Jev (or tensai serve) from SQL | [仓库](https://github.com/mattn/sqlite3-jev) |
| MichitoSugawara/jev-lint | Semantic lint CLI powered by TypeSafe Jev | [仓库](https://github.com/MichitoSugawara/jev-lint) |
| miounet11/jevcode | JevCode — Jev (TypeSafe System One) 技术解决方案与最佳实践 · https://www.jevcode.ai | [仓库](https://github.com/miounet11/jevcode) · [网站](https://www.jevcode.ai) |
| model-clis/jev | Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out | [仓库](https://github.com/model-clis/jev) |
| n3ndor/n8n-nodes-typesafe-jev | n8n community node for TypeSafe Jev structured AI decisions | [仓库](https://github.com/n3ndor/n8n-nodes-typesafe-jev) |
| nardinmarcus/pi-jev-typesafe | TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps | [仓库](https://github.com/nardinmarcus/pi-jev-typesafe) |
| noetion/dsh-jev | DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers. | [仓库](https://github.com/noetion/dsh-jev) |
| nsillik/jevvin-off | Prototyping against TypeSafe's Jev System One API: a one-ticket quickstart and a Bluesky Jetstream firehose demo. | [仓库](https://github.com/nsillik/jevvin-off) |
| Obrais-cloud/ticket-rerank | FastAPI service that reranks support tickets by urgency using TypeSafe (Jev / System One) | [仓库](https://github.com/Obrais-cloud/ticket-rerank) |
| Obrais-cloud/typesafe-translate | Escribe lenguaje natural y un LLM local lo compila a variables de TypeSafe (state + questions) y las ejecuta (Jev / System One) | [仓库](https://github.com/Obrais-cloud/typesafe-translate) |
| oceanByte/tsai-cli | Unofficial CLI for the TypeSafe AI System One API. | [仓库](https://github.com/oceanByte/tsai-cli) |
| ojusave/beat-jev | A penalty shootout powered by Render Workflows, TypeSafe Jev, and Render Postgres. Python and TypeScript examples. | [仓库](https://github.com/ojusave/beat-jev) |
| Olli0103/openclaw-typesafe-ai | Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation. | [仓库](https://github.com/Olli0103/openclaw-typesafe-ai) |
| ozzy2438/apply-os | Apply OS — Personal career decision engine powered by TypeSafe AI (Jev). Ranks job postings, drafts applications, and automates the pipeline with typed, calibrated decisions. Agency-ready build spec included. | [仓库](https://github.com/ozzy2438/apply-os) |
| ozzy2438/personal-decision-inbox | Agency-ready build prompt for a Personal Decision Inbox powered by TypeSafe AI (Jev). Full end-to-end spec: architecture, UI, integrations, deployment. | [仓库](https://github.com/ozzy2438/personal-decision-inbox) |
| phuthuycoding/jev-audit | AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy. | [仓库](https://github.com/phuthuycoding/jev-audit) |
| Pimmetjeoss/tribe-crm-jev | TypeSafe Jev-powered lead intake and live CRM judgment demo for Tribe CRM | [仓库](https://github.com/Pimmetjeoss/tribe-crm-jev) |
| piyush-infocusp/openjev | 原始资料未提供说明。 | [仓库](https://github.com/piyush-infocusp/openjev) |
| piyush97/focus-tube | Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model | [仓库](https://github.com/piyush97/focus-tube) |
| RajKKapadia/youtube-typesafe-ai-demo | 原始资料未提供说明。 | [仓库](https://github.com/RajKKapadia/youtube-typesafe-ai-demo) |
| recodelabs/duckdb-jev | Natural-language WHERE clauses for DuckDB, powered by TypeSafe's Jev | [仓库](https://github.com/recodelabs/duckdb-jev) |
| robzolkos/omarchy-issue-classifier | Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each. | [仓库](https://github.com/robzolkos/omarchy-issue-classifier) |
| rolottr/x-jev-classifier | Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev from Typesafe | [仓库](https://github.com/rolottr/x-jev-classifier) |
| sandra-arato/icon-matcher | Match a UI section title to a Hugeicons icon using TypeSafe.ai's Choice primitive — no lexical/keyword search. | [仓库](https://github.com/sandra-arato/icon-matcher) |
| Senzo41/typesafe-ai-usecases | 原始资料未提供说明。 | [仓库](https://github.com/Senzo41/typesafe-ai-usecases) |
| shishiv/pi-jeev | A bounded TypeSafe Jev decision tool for Pi | [仓库](https://github.com/shishiv/pi-jeev) |
| shunta-furukawa/jev-tick-lab | A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis. | [仓库](https://github.com/shunta-furukawa/jev-tick-lab) |
| sio-funmatsu/fmjev | 原始资料未提供说明。 | [仓库](https://github.com/sio-funmatsu/fmjev) |
| spivi/cloudforge-jev | Sidecar: grade a cloudforge student writeup with TypeSafe Jev. Not part of the OSS product. | [仓库](https://github.com/spivi/cloudforge-jev) |
| Spykoninho/trading-bot-jev | Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news | [仓库](https://github.com/Spykoninho/trading-bot-jev) |
| sueszli/qwen27b-jev | multiple-choice questions for Qwen3.8-27B, read from logits | [仓库](https://github.com/sueszli/qwen27b-jev) |
| sxoni/typesafe-ai-clone | 原始资料未提供说明。 | [仓库](https://github.com/sxoni/typesafe-ai-clone) |
| Tatuck/jev-boe-demo | Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE). | [仓库](https://github.com/Tatuck/jev-boe-demo) · [网站](https://tatuck.github.io/jev-boe-demo/) |
| Tepes99/openjev-lite | My take on the latest hype with comparisons to cheaper traditional options for this kind of task. Quick poc vibed with my local ai rig | [仓库](https://github.com/Tepes99/openjev-lite) |
| TKY-27/JevSlop | Jevによるnote記事のAI Slop判定サイト | [仓库](https://github.com/TKY-27/JevSlop) · [网站](https://jevslop.pages.dev/) |
| ufec/jev-block-android-ad | JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through. | [仓库](https://github.com/ufec/jev-block-android-ad) |
| vishivishvish/jev-typesafeai | 原始资料未提供说明。 | [仓库](https://github.com/vishivishvish/jev-typesafeai) |
| vkpdeveloper/mrsecret | Mr. Secret — blurs secrets & PII on any page using TypeSafe AI Jev | [仓库](https://github.com/vkpdeveloper/mrsecret) |
| willprout/magic-8-ball | A beautifully minimal Magic 8 Ball powered by Jev from TypeSafe. Twenty classic answers, one fast AI judgment. | [仓库](https://github.com/willprout/magic-8-ball) |
| ximhear/jev-kr-name-age | 이름으로 나이대를 맞히는 React 웹 (TypeSafe Jev) | [仓库](https://github.com/ximhear/jev-kr-name-age) |
| zsoXi/FeedGate | Precision-first Chrome feed filter (v2.1.0) using TypeSafe Jev judgments: promotional posts are kept unless independently strong spam or ad evidence appears. Reversible cosmetic filtering, zero runtime dependencies. | [仓库](https://github.com/zsoXi/FeedGate) |

<a id="games"></a>

## 游戏与模拟

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| jev-plays-pokemon-red | PyBoy game agent where code handles routing and arithmetic and Jev selects among actions at decision points. | [仓库](https://github.com/valentynkit/jev-plays-pokemon-red) |
| typesafe-mario | A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state. | [仓库](https://github.com/fhshaik/typesafe-mario) |
| jev-drone | Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz | [仓库](https://github.com/RomanSlack/jev-drone) |
| typesafe-snake | Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code | [仓库](https://github.com/sorrycc/typesafe-snake) |
| tsai-sc | TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities. | [仓库](https://github.com/phyous/tsai-sc) |
| mario-jev | Python prototype that plays NES Super Mario Bros. from structured RAM observations, with Jev answering focused movement and jump questions. | [仓库](https://github.com/shantanugoel/mario-jev) |
| OneVOneJev | 1v1 Jev quickscope arena — Three.js + TypeSafe System One | [仓库](https://github.com/emrickgarrett/OneVOneJev) |
| heist-one | Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world. | [仓库](https://github.com/AbdelStark/heist-one) |
| rubikjev | Challenge the Jev's intelligence in Rubik Cube puzzles | [仓库](https://github.com/0xtrou/rubikjev) · [网站](https://rubikjev.solo.engineer) |
| jev-doom-agent | A browser-native Doom agent experiment with structured spatial state, composable AI controls, live decision telemetry, and a Chocolate Doom WebAssembly runtime. | [仓库](https://github.com/lukaske/jev-doom-agent) |
| tsai-civ2 | TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-game harness. | [仓库](https://github.com/phyous/tsai-civ2) |
| casse-brique-typesafe | A Next.js brick breaker whose paddle is controlled in real time by TypeSafe AI's Jev model. Built with Claude Code. | [仓库](https://github.com/Para-FR/casse-brique-typesafe) |
| pong-jev | TypeSafe's Jev plays Atari Pong. One typed Choice question per frame, no coordinates sent to the model. | [仓库](https://github.com/safzanpirani/pong-jev) |
| cyber-breach-jev | Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model | [仓库](https://github.com/rchovatiya88/cyber-breach-jev) |
| Agent-JEV-Tetris | using the new model JEV to play the game tetris | [仓库](https://github.com/Yasserbhb/Agent-JEV-Tetris) |
| last-exit | A cyberpunk border encounter powered by TypeSafe Jev. Bluff the guard. Inspect the receipts. | [仓库](https://github.com/0x963D/last-exit) · [网站](https://gate.fade.tools) |
| beatjev | Browser game: try to beat Jev at spotting a spam message. | [仓库](https://github.com/lambertsj/beatjev) · [网站](https://beatjev2it.jlamberts86.workers.dev) · [文章](https://x.com/j_lamberts/status/2100592556081832131) |
| pdoom-protocol | USER + JEV: P(DOOM) PROTOCOL — co-op platform shooter where TypeSafe Jev plays alongside you | [仓库](https://github.com/onionminionops-beep/pdoom-protocol) |
| jev-games | Visual Jev lab for multiple games and emulator platforms | [仓库](https://github.com/shantanugoel/jev-games) |
| jev.mods | Minecraft mod where Jev tries to finish the game from scratch without a scripted route. | [仓库](https://github.com/Hardel-DW/jev.mods) |
| jev-play-ping-pong | Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence. | [仓库](https://github.com/Icohen007/jev-play-ping-pong) · [网站](https://indispensable-lingonberry-hot.julius.site/) |
| jev-gomoku | MoonBit client for Jev plus a Jev-vs-Jev gomoku match, with timing logs. | [仓库](https://github.com/mizchi/jev-gomoku) |
| typesafe-3d-chess | 3D chess powered by TypeSafe AI (Jev). AI vs AI by default, or play either side. Multiple difficulty levels. | [仓库](https://github.com/malDuffin/typesafe-3d-chess) |
| jev2048 | Let Jev (TypeSafeAI) solve 2048 | [仓库](https://github.com/KyleKreuter/jev2048) |
| river-oaks | NPCs of River Oaks Houston, Texas using Jev to power NPCs | [仓库](https://github.com/BunsDev/river-oaks) |
| hundred | 100 AI NPCs live in a tiny town. Jev chooses the next action; the world writes the story. | [仓库](https://github.com/jammaru/jev-lab) |
| snake-jev | Snake controlled by parallel Jev assessments, with one API call per game tick. | [仓库](https://github.com/siroccomask/snake-jev) |
| jev-askable-arm | Zero-shot English goals on a sim Franka. Jev chains hardcoded primitives. | [仓库](https://github.com/TarunTomar122/jev-askable-arm) |
| typesafe-chess | Chess where both players are TypeSafe's Jev model: every move is a typed Choice decision | [仓库](https://github.com/TholeG/typesafe-chess) |
| jev-snake | An experimental Snake environment where the game engine owns deterministic rules and TypeSafe AI's Jev makes the movement decision from structured state on every tick. | [仓库](https://github.com/iammusham/jev-snake) |
| jev-tetris | A visual TypeSafe demo where Jev chooses verified Tetris placements. | [仓库](https://github.com/MachineLearning-Nerd/jev-tetris) |
| ps2-ai-agent | Autonomous PlayStation 2 AI Agent with real-time visual telemetry HUD powered by TypeSafe Jev System One | [仓库](https://github.com/opaielsheikh/ps2-ai-agent) |
| jev-bfs | Wikipedia link races with direct Jev ranking and a live terminal display. | [仓库](https://github.com/komikat/jev-bfs) |
| shady-town | Shady Town: social-deduction party game for the living room TV, moderated by TypeSafe Jev | [仓库](https://github.com/tpaulshippy/shady-town) |
| roverlab | A 3D planetary rover sandbox for experimenting with autonomous decisions using TypeSafe AI. | [仓库](https://github.com/juancamiloqhz/roverlab) |
| river-run-typesafe | River shooter game in Python, inspired by Atari's River Raid, played by a TypeSafe AI pilot | [仓库](https://github.com/ashaazami/river-run-typesafe) |
| typesafe-minecraft-demo | A Minecraft Java player controlled by TypeSafe AI, with live decisions, Canadian flag building, and a side-by-side dashboard. | [仓库](https://github.com/ellistev/typesafe-minecraft-demo) |
| terrarium | A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world. | [仓库](https://github.com/TheGali/terrarium) |
| siege | SIEGE: 200 people vs one agent. A typed action gate (TypeSafe System One) that learns from every breach, evaluated by W&B Weave, hardened by a defender loop. Built at CoreWeave Hacks: Agent Loops 2026. | [仓库](https://github.com/vnmoorthy/siege) · [网站](https://vnmoorthy.github.io/siege/) |
| jev-t-rex-runner | Chrome dino game played by Typesafe AI Jev model | [仓库](https://github.com/joshlarsen/jev-t-rex-runner) · [网站](https://devfolioco.github.io/t-rex-runner-game/) |
| Jev Driving Lab | Interactive experiments from support routing to a 3D driving simulation: structured sensor state in, typed steer, brake, and overtake decisions out. | [仓库](https://github.com/kavehmz/typesafe-playground) · [文章](https://x.com/kavehmz/status/2100616111771238881) |
| Jev Tetris | Jev picks rotation and column from holes, stack height, and bumpiness. | [网站](https://jev-omega.vercel.app) |
| Jev Pac-Man | The maze as JSON; Jev picks the turn at each junction in real time. | [网站](https://jev-pacman.ephraimduncan.com) |
| Hollow Creek | Village NPCs that judge you each tick, deciding what to do and how they feel, instead of chatting. | [网站](https://hollow-creek-sigma.vercel.app) |
| Jev Arcade | Krunker-style 1v1 FPS where Jev decides move, aim, ADS, fire, and jump at about 9 Hz. | [网站](https://jev-arcade.vercel.app/duel) · [文章](https://x.com/Neel490/status/2100618722318688753) |
| Game Plan | Small game that tests how Jev handles unknown input. | [网站](https://game-plan.adriaansendennis.workers.dev/play) · [文章](https://x.com/DennisAdriaans/status/2100616874719347136) |
| Jev board games | Playable board games driven by Jev decisions. | [网站](https://jevboardgames.everpaper.app/) · [文章](https://x.com/MarcoIannello/status/2100622449268191524) |
| chess-jev | 3D chess where Jev plays both sides, or you jump in. | [网站](https://chess-jev.loomens.com) · [文章](https://x.com/BuildWithKhalil/status/2100364868733812987) |
| inanna-malick/jev-dsl | Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels | [仓库](https://github.com/inanna-malick/jev-dsl) |
| joelhooks/pi-fast-jev-compaction | Pi extension: verbatim context compaction with TypeSafe Jev decisions | [仓库](https://github.com/joelhooks/pi-fast-jev-compaction) |
| kevinpita/pi-jev-context | Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history. | [仓库](https://github.com/kevinpita/pi-jev-context) |
| leonaaardob/fast-dev-compaction | Codex plugin: verbatim Jev-guided context restoration around session compaction. Port of tamaratran/fast-jev-compaction to Codex lifecycle hooks. | [仓库](https://github.com/leonaaardob/fast-dev-compaction) |
| nickthompson480/typesafe-ai-playground | Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI. | [仓库](https://github.com/nickthompson480/typesafe-ai-playground) |
| Nyarlathoteppppp/pi-heed | Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev. | [仓库](https://github.com/Nyarlathoteppppp/pi-heed) |
| 4esv/jev-mario | TypeSafe Jev plays Super Mario Bros from a text description of emulator RAM | [仓库](https://github.com/4esv/jev-mario) |
| QuentinDanblon/pi-fast-jev-compaction | Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim. | [仓库](https://github.com/QuentinDanblon/pi-fast-jev-compaction) |
| Query-farm/vgi-typesafe | A VGI worker exposing TypeSafe System One questions (choice, noul, score) to DuckDB/SQL as LATERAL-joinable table functions | [仓库](https://github.com/Query-farm/vgi-typesafe) · [网站](https://query.farm/vgi/) |
| tyleree/jevbot | Options trading bot (backtest + Alpaca paper only) with TypeSafe Jev as the decision core | [仓库](https://github.com/tyleree/jevbot) |
| Wang-auspicious/pi-jev-compaction | Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully. | [仓库](https://github.com/Wang-auspicious/pi-jev-compaction) |
| aieo-product/jev-gamebenchmark | Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs | [仓库](https://github.com/aieo-product/jev-gamebenchmark) |
| bahramzada/jev-taxi-dispatch | Real-vaxt taksi dispetçerlik simulyasiyası — TypeSafe JEV (System One) modeli ilə | [仓库](https://github.com/bahramzada/jev-taxi-dispatch) |
| cassiomc1/fast-jev-compaction-alt | Continuous, verbatim context compaction for LLM agents using TypeSafe's Jev model. | [仓库](https://github.com/cassiomc1/fast-jev-compaction-alt) |
| clankagent/pi-jev | Jev-powered semantic process conditions and skill suggestions for Pi | [仓库](https://github.com/clankagent/pi-jev) |
| felixfisher/pi-jev-compaction | Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction | [仓库](https://github.com/felixfisher/pi-jev-compaction) |
| filippos95/cybercab-jev | Three.js robotaxi game where TypeSafe's Jev model makes the driving decisions | [仓库](https://github.com/filippos95/cybercab-jev) |
| furedea/reflex-state | Jev-powered execution state for Pi coding agents. Track changes, checks, and blockers outside the main LLM, with evidence-backed updates and replay. Inspired by SKILL.state. | [仓库](https://github.com/furedea/reflex-state) |
| jason-allen-oneal/openclaw-plugin-typesafe-ai | TypeSafe AI (Jev System One) plugin for OpenClaw - sub-100ms group triage, tool safety guardrails, compaction curation, and model routing | [仓库](https://github.com/jason-allen-oneal/openclaw-plugin-typesafe-ai) |
| kxzk/typesafe-jev-drone-demo | Three.js drone simulator with a Python backend and live TypeSafe Jev navigation | [仓库](https://github.com/kxzk/typesafe-jev-drone-demo) |
| luiginotmario/postgres-Jev | Natural-language PostgreSQL predicates with TypeSafe Jev. A simple search playground with randomly generated databases. | [仓库](https://github.com/luiginotmario/postgres-Jev) · [网站](https://postgres-jev.vercel.app) |
| Maverick-Ansh/intentions_emergent | Latent reasoning for user-intent decomposition: does more continuous-space compute produce better goal extraction? With JEV (TypeSafe System One) as the calibrated decision layer. | [仓库](https://github.com/Maverick-Ansh/intentions_emergent) |
| milanboers/jev-plays-pokemon | Playing Pokemon Red using TypeSafe Jev | [仓库](https://github.com/milanboers/jev-plays-pokemon) |
| nourhelmi/pi-jev-compaction | Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals without rerunning commands. | [仓库](https://github.com/nourhelmi/pi-jev-compaction) |
| Nyarlathoteppppp/pi-jev-context | Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks. | [仓库](https://github.com/Nyarlathoteppppp/pi-jev-context) |
| skcache/jevtrafficsim | TypeSafe AI's first model Jev takes on an entire city's traffic | [仓库](https://github.com/skcache/jevtrafficsim) |

<a id="demos"></a>

## 演示与示例

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| killmyidea | Describe your startup idea. Jev decides: kill it, fix it or ship it. | [仓库](https://github.com/monteduro/killmyidea) · [网站](https://killmyidea.stemonte.io) |
| jev-me | A grill-me style interrogation of your idea, with Jev doing the grilling. | [仓库](https://github.com/jon-devlapaz/jev-me) |
| typesafe-ai-playground (BunsDev) | Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI. | [仓库](https://github.com/BunsDev/typesafe-ai-playground) · [网站](https://jev.works) |
| jev-system-one | A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports | [仓库](https://github.com/haseeb-heaven/jev-system-one) |
| Should AI Kill Us All? | Live verdict page: feeds Jev the day’s Florida Man, odd-news, politics and world headlines and asks all three primitives whether AI should kill us all, refreshed every ten minutes. | [仓库](https://github.com/hellogumbo/should-ai-kill-us-all) · [网站](https://shouldaikillusall.com) |
| jev-playground (Little-Planet-Labs) | A small Next.js app for experimenting with TypeSafe AI's Jev model (System One) | [仓库](https://github.com/Little-Planet-Labs/jev-playground) · [网站](https://jev-playground-zeta.vercel.app) |
| clarity-judge | Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence. | [仓库](https://github.com/BunsDev/clarity-judge) · [网站](https://judge.jev.works) |
| gpt-vs-jev | Compare GPT generated language with JEV structured Noul decisions on the same input. | [仓库](https://github.com/TanayPadar/gpt-vs-jev) · [网站](https://gptvsjev.vercel.app) · [文章](https://x.com/nerdytanay/status/2100465397267144815) |
| harden-jev-decides | JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board. | [仓库](https://github.com/tylerjharden/harden-jev-decides) |
| typesafe-ai-playground (markjaquith) | A playground for experiments around Jev, TypeSafe's System One model. | [仓库](https://github.com/markjaquith/typesafe-ai-playground) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| got-jev | Jev (TypeSafe AI) PoC through Game of Thrones | [仓库](https://github.com/phureewat29/got-jev) · [网站](https://jev.phureewat.com) |
| toolgate | Agent tool/MCP call gate — allow / ask_human / deny via TypeSafe Jev | [仓库](https://github.com/ndolinschi/toolgate) · [网站](https://toolgate.vercel.app) |
| guard-jev | Comment-moderation playground: paste a comment, Jev decides what to do with it. | [仓库](https://github.com/NorbertBodziony/guard-jev) · [网站](https://guard-jev.vercel.app) |
| typesafe-arena | A playground for TypeSafeAI's Jev Model | [仓库](https://github.com/DeepBlueDynamics/typesafe-arena) |
| Instinct | Instinct: describe a case in free text and Jev picks the UI from a fixed catalog without generating a line of code or copy. | [仓库](https://github.com/joevidev/ui-generator-instinct-jev) · [网站](https://ui-generator-instinct-jev.vercel.app) |
| jev-should-i-apply | Typesafe/Jev public X demo | [仓库](https://github.com/cardotrejos/jev-should-i-apply) |
| jev-user-jury | Typesafe/Jev public X demo | [仓库](https://github.com/cardotrejos/jev-user-jury) |
| jev-ad-preflight | Typesafe/Jev public X demo | [仓库](https://github.com/cardotrejos/jev-ad-preflight) |
| jev-dev | 同じ発言を jev と LLM の両方に判定させ、感情の変動値のズレと応答速度を1画面で見比べるデモ（affectus + Vercel AI Gateway） | [仓库](https://github.com/n-yokomachi/jev-dev) |
| Jev Gamecast | Jev Gamecast: replay-first React app that asks Jev typed questions about live sports data. | [仓库](https://github.com/narulaskaran/jev-data-questions) · [网站](https://jev-gamecast.vercel.app) |
| jev-paper-judge | Feedback on your paper in seconds. | [仓库](https://github.com/JacobLinCool/jev-paper-judge) · [网站](https://jev-paper-judge.jacob.workers.dev) |
| human-compiler | A compiler for human language. Paste text, get diagnostics. Measured by TypeSafe Jev. | [仓库](https://github.com/asfarsadewa/human-compiler) · [网站](https://human-compiler.asfarlab.fun) |
| Search-Function-Test | A test project based on Jev AI, the goal is to build a search function for a blog/article website that has 100s of articles to search from, So the user can actually use the search as chat to question anything and find related answers/articles | [仓库](https://github.com/Shifros/Search-Function-Test) · [网站](https://search-function-test.vercel.app) |
| jev-bun1 | TypeSafe の Jev を TypeScript SDK で使ってみる最初の 1 歩 | [仓库](https://github.com/heiwa4126/jev-bun1) |
| jevplay | TypeSafe Jev playground — custom Choice/Score/Noul builder with live distributions | [仓库](https://github.com/ndolinschi/jevplay) · [网站](https://jevplay.vercel.app) |
| mcpmatch | Match user goals to MCP catalog (two-stage) via TypeSafe Jev | [仓库](https://github.com/ndolinschi/mcpmatch) · [网站](https://mcpmatch.vercel.app) |
| spendbrake | Agent budget brake — continue / downgrade_model / stop via TypeSafe Jev | [仓库](https://github.com/ndolinschi/spendbrake) · [网站](https://spendbrake.vercel.app) |
| harnessjudge | Judge agent steps — ok / retry / escalate / stop via TypeSafe Jev | [仓库](https://github.com/ndolinschi/harnessjudge) · [网站](https://harnessjudge.vercel.app) |
| swarmrouter | Route tasks to research/code/browser/support/writer agents via TypeSafe Jev | [仓库](https://github.com/ndolinschi/swarmrouter) · [网站](https://swarmrouter.vercel.app) |
| jev-playground (wustep) | Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI. | [仓库](https://github.com/wustep/jev-playground) · [网站](https://jev-playground.vercel.app) |
| hiresignal | HireSignal — resume first-pass fit+interview via TypeSafe Jev | [仓库](https://github.com/ndolinschi/hiresignal) · [网站](https://hiresignal-opal.vercel.app) |
| trustgate | TrustGate — indie media T&S gate via TypeSafe Jev | [仓库](https://github.com/ndolinschi/trustgate) · [网站](https://trustgate-mu.vercel.app) |
| lanebreak | LaneBreak — support ticket priority+routing via TypeSafe Jev | [仓库](https://github.com/ndolinschi/lanebreak) · [网站](https://lanebreak.vercel.app) |
| cartshield | CartShield — SMB checkout fraud disposition via TypeSafe Jev | [仓库](https://github.com/ndolinschi/cartshield) · [网站](https://cartshield.vercel.app) |
| pulselane | PulseLane — clinic triage decisions via TypeSafe Jev | [仓库](https://github.com/ndolinschi/pulselane) · [网站](https://pulselane-topaz.vercel.app) |
| jev-demos | Demos to test the effectiveness of TypeSafe's "Jev" System One Model | [仓库](https://github.com/Bud-ro/jev-demos) |
| Job Risk Analyzer | Job Risk Analyzer: CLI and REST API that uses Jev to score an occupation's exposure to AI-driven layoffs and its resilience. | [仓库](https://github.com/WeSecureYou/Jev-test) · [网站](https://jev-test.vercel.app) |
| jev-board-lab | Interactive explorer and Jev question workspace for Jev Board datasets. | [仓库](https://github.com/WebGrga/jev-board-lab) |
| extremely-specific-council | Twelve members. Zero qualifications. A playful TypeSafe AI council with animated votes, inspectable decisions, and shareable verdicts. | [仓库](https://github.com/cbetz/extremely-specific-council) · [网站](https://extremely-specific-council-five.vercel.app) |
| Probably | Probably: live BTC, ETH, and XRP prices with a shared TypeSafe buy-or-wait demonstration. No trades placed. | [仓库](https://github.com/JordiParraCrespo/typesafe-ai-trading-showcase) · [网站](https://typesafe-ai-trading-showcase.vercel.app) |
| typesafe-image-diffusion | Diffusion-style pixel art out of a classifier: 256 parallel per-pixel Jev questions plus refinement passes. | [仓库](https://github.com/Wizhill05/typesafe-image-diffusion) · [文章](https://x.com/just_aryansingh/status/2100617080395710748) |
| Yes / No | Free, no-signup Noul demo. Ask a question, get yes, no, or maybe, with web search when needed. | [网站](https://yesno.coderai.dev) |
| TypeSafe Typewriter | Val Town demo where 16 typed judgments update live as you type. | [网站](https://typesafe-demo.val.run/) · [文章](https://x.com/stevekrouse/status/2100287368221659289) |
| Crowdcheck | Test a post against 10,000 synthetic personas before you publish it. | [网站](https://crowdcheck-ai.vercel.app/) |
| Jev mood demo | Talk nicely or nastily over time; structured state tracks the mood. | [网站](https://jev-demo.vercel.app) |
| Jev Room | One sentence becomes six room settings. Jev chooses, the app renders. | [网站](https://jev-room.moe136231.chatgpt.site) |

<a id="research"></a>

## 评测与研究

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| openjev (TheoLeeCJ) | Can we run something like Jev on a 3090 at home? | [仓库](https://github.com/TheoLeeCJ/openjev) · [网站](https://openjev.com) · [文章](https://x.com/hhkkmon/status/2100443314957038010) |
| jevlike | Train a small model that chooses among a changing list of text options, one probability per option in a single pass. Includes Doom, chess, and Wikispeedia demos. | [仓库](https://github.com/vinnylarouge/jevlike) · [文章](https://x.com/hhkkmon/status/2100443314957038010) |
| jev-eval-agent | Personal-assistant agent built on Vercel's eve with 100 mocked tools, measuring how many steps it takes when Jev picks the tool versus the LLM. | [仓库](https://github.com/vinilana/jev-eval-agent) |
| typesafe-ai-benchmark | This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev. | [仓库](https://github.com/iammrduncan/typesafe-ai-benchmark) · [网站](https://hackersintheloop.org/) · [文章](https://x.com/iamMrDuncan/status/2100467548298899918) |
| open-jev (daseinlabs) | One-pass option scoring with a local Gemma 3 4B on Apple silicon via MLX, inspired by jevlike, with a Doom demo. | [仓库](https://github.com/daseinlabs/open-jev) |
| jevmlx | Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass. | [仓库](https://github.com/bnsd55/jevmlx) · [文章](https://x.com/beni_il_/status/2100617387116568956) · [网站](https://github.com/bnsd55/jevmlx#readme) |
| jev-on-a-laptop | Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo. | [仓库](https://github.com/rorshopping/jev-on-a-laptop) · [文章](https://x.com/hhkkmon/status/2100443314957038010) |
| open-jev (JoshuaSP) | Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results | [仓库](https://github.com/JoshuaSP/open-jev) |
| jevbetter | A stronger one-pass scorer over a variable list of text options: hashed n-gram encoder, rival-aware attention, gated head, temperature scaling, benchmarked against jevlike. | [仓库](https://github.com/olanotolu/jevbetter) |
| decider | One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B | [仓库](https://github.com/Mapika/decider) |
| TypeAR | Type-safe one-decision-per-token decoding engine for autoregressive LLMs, inspired by Jev. | [仓库](https://github.com/zmtomorrow/TypeAR) · [文章](https://x.com/MingtianZhang/status/2100579236960682120) |
| openvons | openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド | [仓库](https://github.com/genai-craft/openvons) · [网站](https://genai-craft.com) |
| jev-benchmarks | Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks. | [仓库](https://github.com/AbdelStark/jev-benchmarks) |
| LegalForecastBench | LegalForecast-MTD benchmark alpha and official evaluation workflows | [仓库](https://github.com/johnhughes3/LegalForecastBench) |
| jev-lm | A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval | [仓库](https://github.com/y0usaf/jev-lm) |
| jev-korean-benchmark | Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence | [仓库](https://github.com/mahlernim/jev-korean-benchmark) · [网站](https://ahn-lab.org/jev-korean-benchmark/) |
| jevfire | JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks. | [仓库](https://github.com/kikoncuo/jevfire) · [网站](https://kikoncuo.github.io/jevfire/) · [网站](https://kikoncuo.github.io/jevfire/learn.html) |
| openjev (zhihz) | Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev. | [仓库](https://github.com/zhihz/openjev) |
| system-one-open | Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal) | [仓库](https://github.com/mithalouni/system-one-open) |
| jev-behavior-study | Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification. | [仓库](https://github.com/RINNECODER/jev-behavior-study) |
| jev-chat | A chatbot from typed Jev decisions: hierarchical speculative decoding over System One probabilities. | [仓库](https://github.com/adhyaay-karnwal/jev-chat) |
| jev_stock | An experimental JEV-powered framework for forecasting short-term stock price direction from structured market data. | [仓库](https://github.com/sosopop/jev_stock) |
| jev-for-engineers | Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies. | [仓库](https://github.com/Foadsf/jev-for-engineers) |
| trade-jev | Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data | [仓库](https://github.com/justinhe16/trade-jev) |
| jev-benchmark | Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs | [仓库](https://github.com/wondertwins/jev-benchmark) |
| calibre | Calibration and confidence-based routing measured on Banking77: 80.2% accuracy at $0.103 per 500 decisions | [仓库](https://github.com/FirasSX914/Janus) |
| jevgpt | A chatbot built on a model that cannot generate text (TypeSafe AI's Jev, driven autoregressively) | [仓库](https://github.com/Bewinxed/jevgpt) |
| system-one | Batched single-token choice inference for open language models, compatible with TypeSafe | [仓库](https://github.com/sgoedecke/system-one) |
| jev-little-airways | A show-and-tell capability study for Jev, TypeSafe's System One decision model. | [仓库](https://github.com/lbotinelly/jev-little-airways) |
| kyotsu-ai-bench | AI benchmark on Japan's 2026 Common Test: Jev vs luna-none vs luna-low (static dashboard) | [仓库](https://github.com/shibadogcap/kyotsu-ai-bench) |
| decisionbridge | A Jev-inspired decision interface for existing LLMs. Explicit choices, scores, calibration, and review thresholds. | [仓库](https://github.com/grishahq/decisionbridge) |
| padflow-jev-evals | Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev. | [仓库](https://github.com/zsavage8/padflow-jev-evals) |
| mcts-agent | Discriminative Monte Carlo Tree Search using TypeSafe Jev System One Primitives and Gemini | [仓库](https://github.com/lhemerly/mcts-agent) |
| jev-rerank-bench | Can a decision model beat dedicated rerankers? TypeSafe Jev vs Cohere Rerank 4 vs ZeroEntropy zerank-2 vs a chat-model baseline: 14 datasets, every raw API response, bootstrap ranges on every gap. | [仓库](https://github.com/anessbelbati/jev-rerank-bench) |
| jev-sec-bench | Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go | [仓库](https://github.com/Gaurav-Gosain/jev-sec-bench) · [文章](https://x.com/_GauravGosain/status/2100111398277959715) |
| jev-agent-failure-benchmark | Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset). | [仓库](https://github.com/TokenTrim/jev-agent-failure-benchmark) |
| qwen-rlcd | Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B | [仓库](https://github.com/shamazharikh/qwen-rlcd) |
| RISC-jeV | I tortured Jev into being a RISC-V CPU. | [仓库](https://github.com/i2cjak/RISC-jeV) |
| jev-synergy-screening | Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels | [仓库](https://github.com/PistachioAIHQ/jev-synergy-screening) |
| jev-freeform | An observable raw-character chat experiment powered entirely by TypeSafe Jev Choice | [仓库](https://github.com/kesku/jev-freeform) |
| jev-playground (hegargarcia) | Benchmarks Jev against other evaluation models in games with explicit states, legal actions, and measurable outcomes. | [仓库](https://github.com/hegargarcia/jev-playground) |
| jev-as-a-judge | Using Jev as an evaluator. | [仓库](https://github.com/danielgshea/jev-as-a-judge) |
| jev-report | 发明 RLHF 的人，这次做了个不会说话的模型：Jev 独立研究报告。52 页 PDF + 50 条中文实测复现包 + 143 条可回溯数据表 | [仓库](https://github.com/HackSing/jev-report) |
| jev-research-eval | Reproducible Jev Ultrafast research-browser eval harness + field note (QC’d cases, suite runner, report generator). Not investment advice. | [仓库](https://github.com/jgridifier/jev-research-eval) |
| jev-exploration | Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code | [仓库](https://github.com/SamuelSacco/jev-exploration) |
| jev-secret-detection | Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets | [仓库](https://github.com/teyhouse/jev-secret-detection) · [文章](https://x.com/Teyhouse/status/2100555273718907064) |
| jev-phishing-bench | Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark. | [仓库](https://github.com/anisselbd/jev-phishing-bench) |
| system-one-gemma | Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev. | [仓库](https://github.com/akash-kamat/system-one-gemma) |
| jev-routing-experiment | Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena | [仓库](https://github.com/TokenTrim/jev-routing-experiment) |
| jev-jp-address | Jev (TypeSafe) 性能評価プロジェクト — 日本郵便 KEN_ALL をマスタに、AI SDK 経由の Jev が住所のあいまい一致にどこまで使えるかを検証 | [仓库](https://github.com/smasato/jev-jp-address) |
| openjev-experiments | Openjev experiments | [仓库](https://github.com/zefir1990/openjev-experiments) · [网站](https://demensdeum.com) |
| shade-arena-jev-monitor | Evaluating TypeSafe's Jev as a fast monitor and action gate for agent sabotage in SHADE-Arena, compared with Gemini 2.5 Flash/Pro. | [仓库](https://github.com/nican2018/shade-arena-jev-monitor) |
| thaiexam-jev-charts | Charts: TypeSafe Jev evaluated on Thai standardized exams vs 110 other models | [仓库](https://github.com/vehas/thaiexam-jev-charts) |
| jev-column-race | Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper | [仓库](https://github.com/goodrahstar/jev-column-race) · [网站](https://jev-column-race.vercel.app) |
| jev-trace-classifier | Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next | [仓库](https://github.com/sypherin/jev-trace-classifier) |
| jev-shadcn-lint-eval | A small second eval for shadcn-ui/lint that uses TypeSafe's Jev to judge the linter's own output. | [仓库](https://github.com/blas0/jev-shadcn-lint-eval) |
| jev-deferred-crispification | Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1). | [仓库](https://github.com/dnakhoa/jev-deferred-crispification) |
| jev-finance-benchmark | typesafe.ai model jev finance benchmark | [仓库](https://github.com/hifizz/jev-finance-benchmark) |
| jev-pick-and-place-study | A small reproducible MuJoCo pilot comparing Jev, Claude Haiku, and reactive rules for pick-and-place. | [仓库](https://github.com/tryaksh/jev-pick-and-place-study) |
| jev-spam-eval | Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines | [仓库](https://github.com/bitnovus/jev-spam-eval) |
| jev-anotacao-sentencas | Jev (TypeSafe) vs. Gemini 3.8 Flash vs. GPT-5.6 Luna na anotação estruturada de sentenças do TJSP: qualidade, tempo e custo | [仓库](https://github.com/lab-dados/jev-anotacao-sentencas) · [网站](https://lab-dados.github.io/jev-anotacao-sentencas/) |
| jev-lab | TypeScript experiments, evaluations, and latency benchmarks for TypeSafe's Jev model | [仓库](https://github.com/Menny1337/jev-lab) |
| jev-headline-bench | Can Jev pick the winner of a real headline A/B test? 64.5% across 10,984 Upworthy randomized experiments, 74.7% when the difference was decisive. | [仓库](https://github.com/Gaurav-Gosain/jev-headline-bench) |
| jev-alpha-bench | Does Jev predict stock returns from news? It reads the news well; there is no tradeable alpha. Three arms separate reading from recall. | [仓库](https://github.com/Gaurav-Gosain/jev-alpha-bench) |
| FinancialPredictionJev | Using Jev to test how well it predicts financial markets(just like most llms as of september 2026, it doesnt do that good) | [仓库](https://github.com/thodoh1/FinancialPredictionJev) |
| Typesafe_chess_eval | An evaluation of typesafe AI chess. As it turns out, the AI isn't doing really well even though chess is not a particularly open-ended game. Still, it's only a prototype and this probably wasn't optimzied for games. | [仓库](https://github.com/AliceRoselia/Typesafe_chess_eval) |
| typesafe-oracles | Evaluating TypeSafe's System One primitives (Choice/Score/Noul) — where a typed oracle beats an LLM call | [仓库](https://github.com/trophee-bot/typesafe-oracles) |
| system-one-adapter-rust | Rust port of TypeSafe system-one-adapter (LLM-backed system_one evaluations) | [仓库](https://github.com/codeitlikemiley/system-one-adapter-rust) |
| PocketJev | On-device iPhone visual decision tool using MLX and Qwen3-VL direct option logits. | [仓库](https://github.com/NullPo-jp/PocketJev) |
| misereru-slide-jev | Ongoing Japanese research deck on Jev and System One models, maintained as Markdown slides. | [仓库](https://github.com/myokoym/misereru-slide-jev) · [网站](https://myokoym.github.io/misereru-slide-jev/) |
| Parallel Constrained Decoding (Qwen2.5-1B-RLCD) | Hugging Face Space exploring open-source parallel constrained decoding as an alternative to Jev. | [网站](https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding) |
| carlaiau/jev-reranking | Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model | [仓库](https://github.com/carlaiau/jev-reranking) |
| OmniJev/awesome-jev | Papers, open reproductions and independent evaluations behind System One models and Jev. | [仓库](https://github.com/OmniJev/awesome-jev) · [网站](https://omnijev.github.io/awesome-jev/) |
| abhixhek/jevcal | Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher. | [仓库](https://github.com/abhixhek/jevcal) |
| zhuyansen/jev-search-rerank-eval | Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured. | [仓库](https://github.com/zhuyansen/jev-search-rerank-eval) |
| AntonioCoppe/jev-harness | Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job. | [仓库](https://github.com/AntonioCoppe/jev-harness) |
| 0xnairb/research_desk | TypeSafe Jev demonstration for new analyzation — experimenting with Jev for fast analysis of news and tickers | [仓库](https://github.com/0xnairb/research_desk) |
| AkashPriyadarshii/jev-curate | High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul). | [仓库](https://github.com/AkashPriyadarshii/jev-curate) · [网站](https://crates.io/crates/jev-curate) |
| AnshChoudhary/typesafe-ai-firewall | Shadow-mode validation harness for a pre-execution firewall on AI agent tool calls (TypeSafe/Jev). Real run, findings in report.md. | [仓库](https://github.com/AnshChoudhary/typesafe-ai-firewall) |
| dayhaysoos/jevals | Local evaluation workbench for TypeSafe Jev | [仓库](https://github.com/dayhaysoos/jevals) |
| hamakyo/jev-starter | Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps. | [仓库](https://github.com/hamakyo/jev-starter) |
| memovai/openevals | Affordable platform for parallel agent evals and observability. Powered by JEV. | [仓库](https://github.com/memovai/openevals) |
| rongxinzy/LightJev | Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo. | [仓库](https://github.com/rongxinzy/LightJev) |
| 24601/rh-guard | Reward-hack radar for coding agents: structural denies + TypeSafe Jev System One sidecar for Claude Code & Cursor hooks | [仓库](https://github.com/24601/rh-guard) |
| 4esv/jev-eval | Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost | [仓库](https://github.com/4esv/jev-eval) |
| AIPI-mvoronovych/JEVBenchmark-Contradiction-Detection | Checking JEV's Contradiction detection (Model by TypeSafe.AI) | [仓库](https://github.com/AIPI-mvoronovych/JEVBenchmark-Contradiction-Detection) |
| alex-sun-kuo/jev-consumer-research | Consumer research explorations using TypeSafe's Jev | [仓库](https://github.com/alex-sun-kuo/jev-consumer-research) |
| avshalomd/longjev | Long inputs for TypeSafe AI's Jev decision model. An experiment, published with its evals. | [仓库](https://github.com/avshalomd/longjev) |
| BrendanH18/jev-lab | Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do | [仓库](https://github.com/BrendanH18/jev-lab) |
| choxos/jev-reviewer | Ask a trial report and its supplements for systematic review data by voice, text or a questions file. Jev (TypeSafe System One) points at the lines; every answer is a verbatim quote with its file and page. PDF, Word and text files; CSV export. | [仓库](https://github.com/choxos/jev-reviewer) · [网站](https://jevreviewer.xera.ac) |
| cmartinez9/jev-judge-bench | Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and agreement with human labels. | [仓库](https://github.com/cmartinez9/jev-judge-bench) |
| DECRUX9812/openjev-lm | open-Jev LM arm: Qwen2.5-0.5B + LoRA reproducing a hosted decision model's judgment at 92.9% on hand-labelled gold - trained overnight on a 6-vCPU CPU-only host, $0/call. Paper, corpora, harnesses, receipts. | [仓库](https://github.com/DECRUX9812/openjev-lm) |
| eggmasonvalue/jev-takes-mauboussin | Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test | [仓库](https://github.com/eggmasonvalue/jev-takes-mauboussin) |
| FFatTiger/new-api-plugin-typesafe | TypeSafe AI System One (Jev) task plugin for QuantumNous/new-api — native /v1/systemone, synchronous evaluation, token billing | [仓库](https://github.com/FFatTiger/new-api-plugin-typesafe) |
| heaven-hm/jev-system-one | A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports | [仓库](https://github.com/heaven-hm/jev-system-one) |
| Jabbslad/pi-jev-tools | TypeSafe ranking, classification, retrieval and structured-decision tools for Pi coding agents | [仓库](https://github.com/Jabbslad/pi-jev-tools) |
| javiergradiche/ruby_llm-providers-typesafe | TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking. | [仓库](https://github.com/javiergradiche/ruby_llm-providers-typesafe) · [网站](https://rubygems.org/gems/ruby_llm-providers-typesafe) |
| jeiel85/jevscope | Local-first visual decision debugger and regression testbench for TypeSafe AI Jev | [仓库](https://github.com/jeiel85/jevscope) · [网站](https://jeiel85.github.io/jevscope/) |
| jmanhype/jev-dspy-lab | Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows | [仓库](https://github.com/jmanhype/jev-dspy-lab) |
| misaalya/snbt-jev-bench |  Jev on Indonesia's SNBT 2025 university entrance test: 159 questions, seven subtests, audited answer keys. | [仓库](https://github.com/misaalya/snbt-jev-bench) |
| ndolinschi/jev-wave | TypeSafe Jev research + 5 product specs | [仓库](https://github.com/ndolinschi/jev-wave) |
| NicolasMontone/jev-evals | Rubric-based eval harness cheap enough to run on every PR, powered by typesafe-ai/jev | [仓库](https://github.com/NicolasMontone/jev-evals) |
| robipop22/Jev-is-odd | Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks. | [仓库](https://github.com/robipop22/Jev-is-odd) |
| samoweb3/jev-x-posts | Sortable 48-hour X post report for Jev, TypeSafe AI and Diogo Almeida, with Jev sentiment labels | [仓库](https://github.com/samoweb3/jev-x-posts) |
| TyrellD1/typesafe-ai_smoke-test | Smoke test: route prompts to a work or life database with TypeSafe AI (Jev), 30-case eval | [仓库](https://github.com/TyrellD1/typesafe-ai_smoke-test) |

<a id="lists"></a>

## 资源清单

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| awesome-typesafe | Curated list of official resources and community projects for TypeSafe, System One models, and Jev, with a GitHub Pages site. | [仓库](https://github.com/AbdelStark/awesome-typesafe) · [网站](https://abdelstark.github.io/awesome-typesafe/) |
| awesome-jev (yibie) | A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions. | [仓库](https://github.com/yibie/awesome-jev) |
| awesome-jev (AnotiaWang) | A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources. | [仓库](https://github.com/AnotiaWang/awesome-jev) · [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| Anil-matcha/awesome-jev-by-typesafe | Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software. | [仓库](https://github.com/Anil-matcha/awesome-jev-by-typesafe) · [网站](https://typesafe.ai/) |
| cobanov/awesome-jev | A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions. | [仓库](https://github.com/cobanov/awesome-jev) |
| fatwang2/awesome-jev | A source-backed Jev project directory with a reusable Jev-only GitHub review workflow. | [仓库](https://github.com/fatwang2/awesome-jev) |
| hellogumbo/awesome-jev | A community directory of projects built on Jev, TypeSafe AI's System One model. | [仓库](https://github.com/hellogumbo/awesome-jev) · [网站](https://awesomejev.com) |
| logicrw/awesome-jev-projects | Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync | [仓库](https://github.com/logicrw/awesome-jev-projects) · [网站](https://logicrw.github.io/awesome-jev-projects/) |
| SeeAPI/awesome-jev-use-cases | Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI. | [仓库](https://github.com/SeeAPI/awesome-jev-use-cases) · [网站](https://www.seeapi.com/) |
| aliaihub/awesome-jev-usecases | Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced. | [仓库](https://github.com/aliaihub/awesome-jev-usecases) |
| fatwang2/jev-review-action | Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model. | [仓库](https://github.com/fatwang2/jev-review-action) |
| ozers/jevsome-projects | Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily. | [仓库](https://github.com/ozers/jevsome-projects) · [网站](https://jevsome.ozersubasi.com) |
| rhc98/awesome-jev | Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself. | [仓库](https://github.com/rhc98/awesome-jev) · [网站](https://awesome-jev.xyz) |
| sontakey/awesome-jev | Unofficial list of insanely useful TypeSafe AI Jev / System One projects | [仓库](https://github.com/sontakey/awesome-jev) |
| JohnDotOwl/awesome-jev | A curated list of projects built on Jev, TypeSafe AI's System One model. | [仓库](https://github.com/JohnDotOwl/awesome-jev) |
| Awesome Jev | Community-maintained bilingual directory of Jev / TypeSafe System One projects, SDKs, tutorials, and evaluations. | [仓库](https://github.com/majiayu000/awesome-jev) |
| thevibeworks/jevgate | Which shell commands may your coding agent run without asking? An allowlist proves what it can; Jev, a no-text model, judges only the rest. Claude Code hook + CLI, measured. | [仓库](https://github.com/thevibeworks/jevgate) |
| wh000wh000/awesome-jev-live | Evidence-graded index of the Jev / TypeSafe System One ecosystem. Rebuilt every 2 hours in 20 languages. | [仓库](https://github.com/wh000wh000/awesome-jev-live) |
| yangzhou-chaofan/awesome-jev-prompt | latest top 100 showcases for jev (keep updating) from x / github / latest sources | [仓库](https://github.com/yangzhou-chaofan/awesome-jev-prompt) |

<a id="articles"></a>

## 文章与讨论

| 项目或资源 | 说明 | 链接 |
| --- | --- | --- |
| Hacker News launch thread | 1,800-point thread debating whether typed decisions replace LLM calls for classification, routing, and scoring. | [文章](https://news.ycombinator.com/item?id=49717558) |
| AINews: Jev, a System One Model that only decides | Latent Space's launch-day roundup: over 100x faster and 200x cheaper than small frontier LLMs. | [文章](https://www.latent.space/p/ainews-jev-a-system-one-model-that) |
| TypeSafe AI debuts model for machines that plays Doom | The Register on the launch, the Doom demo, and the $40M seed round. | [文章](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) |
| Jev: System One models explained | The Neuron's explainer on AI decisions without a chatbot. | [文章](https://www.theneuron.ai/explainer-articles/typesafe-jev-system-one-models-explained/) |
| Mini-Vibe Check: Jev judged everything I have written in 0.7 seconds | Every's Mike Taylor runs his whole archive through Jev. | [文章](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) |
| Jev: The Language Model That Will Not Talk | Anthony Maio's essay on what a model that cannot generate text is for. | [文章](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) |
| TypeSafe Jev: the first decision-only model class | Release-week technical roundup: API, evals, adapter, and skill. | [文章](https://www.developersdigest.tech/blog/typesafe-jev-system-one-models-release-guide-2026) |
| He says he co-invented ChatGPT. His new AI will not write a word | dev.to walkthrough of the Vercel AI SDK evaluate integration. | [文章](https://dev.to/gabrielanhaia/he-says-he-co-invented-chatgpt-his-new-ai-jev-wont-write-a-word-e3c) |
| Typed decisions, not chat | Independent walkthrough separating TypeSafe's published claims from public evidence. | [文章](https://warmersun.com/jev/) |
| What is Jev? | Short practical intro with a Python ticket-triage example. | [文章](https://mohammedshehu.com/jev-typesafe-ai/) |
| AI that does not talk | Practical guide: playground, Python and JS SDKs, raw HTTP, and the agent skill. | [文章](https://ziplyne.agency/blog/ai-that-doesnt-talk-typesafe-jev-guide) |
| Jev vs Mistral and Gemini for event validation | Head-to-head test at validating local event listings, with cost and latency. | [文章](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) |
| TypeSafeのJevを正しく驚く | Japanese walkthrough of what Jev is and is not. | [文章](https://zenn.dev/nwn/articles/824026c76116e0) |
| jev 同士に五目並べで対戦させた | Jev vs Jev gomoku with source and timing logs. | [文章](https://zenn.dev/mizchi/articles/jev-plays-gomoku) |
| Launch thread by Diogo Almeida | TypeSafe's founder on why RLCD-trained decision models are a shorter path to value than chat models. | [文章](https://x.com/CompleteSkeptic/status/2099925682726002904) |
| Computer use built on Jev | Aaron Levin: 155x cheaper than Opus 5, about 20x faster, and it generalizes across operating systems. | [文章](https://x.com/awlevin/status/2100262612428894676) |
| Browser Use + Jev | Gregor Zunic's flight-search demo with a dynamic DOM action space. | [文章](https://x.com/gregpr07/status/2100411066966749359) |
| Jev Typewriter launch | Steve Krouse's playable 16-judgment demo and video. | [文章](https://x.com/stevekrouse/status/2100287368221659289) |
| Model router built with Jev | Ephraim Duncan's demo where Jev decides which model should serve a request. | [文章](https://x.com/ephraimduncan/status/2100454070536351824) |
| Jev vs Qwen on Cerebras | Video comparison against a structured-output LLM baseline. | [文章](https://x.com/iamMrDuncan/status/2100467548298899918) |
| Internal classifier field note | Matched-precision comparison against a private fine-tuned classifier. | [文章](https://x.com/identityTorn/status/2100475121324728615) |
| Jev as an agent safety monitor | Test report using Jev to check each agent action first: most attacks caught, almost no false blocks. | [文章](https://x.com/isNickMa/status/2100566407524344225) |
| Hide posts on X with natural language | Marcel Pociot's browser extension that collapses posts based on a Jev judgment. | [文章](https://x.com/marcelpociot/status/2100520134481735729) |
| Jev plays Minecraft (r/accelerate) | Work-in-progress demo of Jev driving Minecraft, including fleeing zombies at night. | [文章](https://reddit.com/r/accelerate/comments/1whk9oy/new_typesafe_ai_jev_model_playing_minecraft_wip/) |
| Vercel fx: Jev as a command safety reviewer | Guillermo Rauch: Jev reviews every fx command, faster and more accurate than a chat model. | [文章](https://x.com/rauchg/status/2100307962262872105) |
| Stagehand + Jev browser use | Observe the accessibility tree, Jev chooses the next action, Stagehand executes. | [文章](https://x.com/kylejeong/status/2100622054945095934) |
| OpenCode browser use powered by Jev | Preview of fast browser use with Jev and OpenCode's browser CLI. | [文章](https://x.com/thdxr/status/2100288951978164647) |
| Ground Truth news-framing extension | Browser extension that classifies an article's framing, type, topic, and loaded language with Jev. | [文章](https://x.com/jagenaujagenau/status/2100622352333574460) |
| Jev in a Grammarly-style Mac app | Desktop writing app using Jev for fast structured writing judgments. | [文章](https://x.com/nielsmouthaan/status/2100543809465577665) |
| Kalshi prediction-market bot | Jev trades 15-minute and 1-hour BTC, ETH, and SOL markets on Kalshi. | [文章](https://x.com/stablebun/status/2100614911898390589) |
| Model router CLI | Task plus subscription list in, Jev picks which model or agent should handle it. | [文章](https://x.com/nidhisinghattri/status/2100617830890885415) |
| Support ticket classifier | Jev labels category, urgency, and human-versus-auto handling for support tickets. | [文章](https://x.com/ifahimreza/status/2100616988746023102) |
| ConsoleChaosRacing driven by Jev | Racing UI wired to Jev driving decisions. | [文章](https://x.com/Maoku/status/2100611986358927627) |
| skillbox + Jev skill routing | MCP skill router where Jev picks the relevant skills instead of a long agent search. | [文章](https://x.com/thekitze/status/2100556122570792999) |
| jev-rabbit PR review bot | Work-in-progress PR reviewer with plain-English Jev rules. | [文章](https://x.com/thekitze/status/2100616530275029139) |
| AIAvatarKit turn-end gate | Voice-dialog turn-end detection using Jev scores after speech. | [文章](https://x.com/uezochan/status/2100608556823388486) |
| Early Jev tools roundup | Thread cataloguing the first wave of Jev tools: MCP servers, routers, reviewers, and browser agents. | [文章](https://x.com/0xLogicrw/status/2100478725393686556) |
| Jev: System One models explained (DataCamp) | Third-party write-up of the System One primitives, pricing, and vendor workflow evals. | [文章](https://www.datacamp.com/blog/system-one-models-jev) |
| DuckDB Jev classifier | DuckDB extension that classifies rows in CSV, Parquet, or DuckDB tables with Jev, about 10 seconds per 1,000 rows. | [文章](https://x.com/hamiltonulmer/status/2100370557405667768) |
| Hook panel A/B tester | Near-real-time scoring of TikTok and Instagram hooks against about 100 personas. | [文章](https://x.com/Vybhav/status/2100609472750047263) |
| Jev gomoku harness | Local tactics shrink 225 moves to about 40 candidates, then Jev picks among tiered options. | [文章](https://x.com/VacekvVita/status/2100609341145465325) |
| ViZDoom Jev agent | Two decision channels on ViZDoom, navigation at 5 Hz and combat at 12 Hz, with an 18-kill test run. | [文章](https://x.com/kmad/status/2100339921714323624) |
| StarCraft Brood War WASM MCP demo | Brood War in WASM exposed as an MCP server, with Jev playing and still losing to a Zerg rush. | [文章](https://x.com/literallydenis/status/2100622868878868603) |
| Spanish AEPD corpus test | Jev versus a hand-built regex on 544 public data-protection resolutions: 98.2% agreement for about five cents. | [文章](https://x.com/juanmacias/status/2100463494629925048) |
| Tabletop MMORPG action mapper | Eval of Jev turning free-text player intent into typed server actions: 96% agreement, 317 ms median. | [文章](https://x.com/Jon_iy/status/2100397782322364792) |
| Jev in 34 seconds | Short video explainer of how Jev's typed-decision loop works. | [文章](https://x.com/dwhitedesign/status/2100368024649769384) |
| agentjournal ledger tests | 25,174 Jev calls for $1.43 across template-trap, multi-dimension, and real-ledger account-coding tasks. | [文章](https://x.com/agent_journal/status/2100611808545632758) |
| Wiki-link clicker demo | Page-level demo where Jev picks which candidate link to click toward a goal. | [文章](https://x.com/mark1nhu/status/2100620075090792490) |

[资料来源与维护](SOURCE.md)
