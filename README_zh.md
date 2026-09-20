# Awesome Jev

[![Checks](https://github.com/majiayu000/awesome-jev/actions/workflows/checks.yml/badge.svg)](https://github.com/majiayu000/awesome-jev/actions/workflows/checks.yml)

Jev（TypeSafe System One）的开源项目、SDK、教程和评测精选，帮助你寻找接入方式与参考实现。

[在线目录](https://majiayu000.github.io/awesome-jev/) · [English](README.md) · [收录与贡献说明](CONTRIBUTING.md) · [资料来源](SOURCE.md)

本清单由社区维护，与 TypeSafe 无隶属关系。收录表示值得参考，不代表已通过安全、准确率或生产可用性验证。

**[完整资源目录](catalog/FULL.md)** · 按类别浏览项目、工具、教程和文章。

## 从这里开始

[阅读双语入门教程](guides/start.md#中文) · [运行离线工单示例](examples/README.md#中文)

1. 第一次了解 Jev，先看下方的官方文档和发布介绍，了解它能处理哪些判断。
2. 准备接入项目，选择对应语言的 [SDK](taxonomy/sdks.md)，再按[路由](patterns/routing.md)或[结果检查](patterns/verification.md)的步骤试用。
3. 寻找参考项目，浏览下方精选或[完整目录](catalog/FULL.md)；查看近期变化可读[社区动态](updates/README.md)。

## 目录

- [入门](#入门)
- [SDK 与接入](#sdk-与接入)
- [智能体工具](#智能体工具)
- [浏览器自动化](#浏览器自动化)
- [应用与游戏](#应用与游戏)
- [评测与开源实现](#评测与开源实现)
- [文章与中文资源](#文章与中文资源)
- [使用前注意](#使用前注意)
- [踩坑与边界](#踩坑与边界)
- [更多资料](#更多资料)

## 入门

Jev 用于选择选项、打分和判断条件，结果可供程序继续处理。输出符合规定格式，并不意味着判断一定正确。

- [官方文档](https://docs.typesafe.ai/) - API 说明、快速入门与使用示例。
- [模型能力局限](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) - Jev 1.13 的已知限制与使用注意事项。
- [发布介绍](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - TypeSafe 对 Jev 及其适用场景的介绍。
- [在线试用](https://console.typesafe.ai/) - TypeSafe 提供的 API 试用控制台。

## SDK 与接入

- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - 官方 JavaScript 与 TypeScript 客户端，用于调用 Jev API；需要 Node.js 20+ 和 TypeSafe 密钥。
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - 官方 Python 客户端，用于调用 Jev API；需要 Python 3.10+ 和 TypeSafe 密钥。
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) - 通过相同的决策接口比较 Jev 与语言模型。
- [TypeSafe skills](https://github.com/typesafe-ai/skills) - 帮助编程智能体使用 Jev 的官方说明。
- [Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - 网关模型页面，当前接入方式与价格以服务商说明为准。
- [Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) - Cloudflare 的模型接入文档。
- [vercel/eve](https://github.com/vercel/eve) - 包含 Jev 评估功能的智能体框架，Jev 只是其中一部分。
- [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) - 包含 Jev 评估功能的命令行工具。

## 智能体工具

- [jev-router](https://github.com/gargpratyush/jev-router) - 为 Claude Code 和 Codex 的任务选择模型；需要 Node.js 20.12+、Jev 密钥和已登录的对应 CLI。
- [jev-review — devagrawal09](https://github.com/devagrawal09/jev-review) - 带看板的代码审查流程。
- [jev-review — NiazMorshed2007](https://github.com/NiazMorshed2007/jev-review) - 通过 MCP 插件进行本地代码审查。
- [foreman](https://github.com/thruwire/foreman) - 使用 Jev 检查编程智能体的工作。
- [jev-mcp](https://github.com/jkudish/jev-mcp) - 通过 MCP 工具提供 Jev 检查与查找功能。
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code 的 Stop 钩子，结合会话证据检查未经验证的完成声明；发生错误时放行。
- [jev-commit](https://github.com/valentynkit/jev-commit) - Git 提交信息钩子，检查提交说明与暂存改动是否一致，并检查可能的凭据。
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim 插件，根据自然语言问题对函数评分，并在 quickfix 中展示结果。

## 浏览器自动化

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - 浏览器自动化工具，由 Jev 选择操作与 DOM 元素，由语言模型生成输入文字；需要 Python 3.12+、Chrome、Jev 与文字模型服务。
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - 利用 OCR 识别的文字帮助 Jev 选择电脑操作。

## 应用与游戏

- [notra](https://github.com/usenotra/notra) - 包含基于 Jev 的功能开关路由。
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - 在每个 Monad 区块请求一次判断的交易实验，收录不代表其能够盈利。
- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) - 使用模拟器结构化状态的游戏智能体。
- [jev-skip](https://github.com/valentynkit/jev-skip) - 浏览器扩展，使用 Jev 从 YouTube 字幕中识别可能的赞助片段。
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - PyBoy 游戏智能体，由代码处理路线和计算，Jev 在决策点选择操作。
- [jev-drone](https://github.com/RomanSlack/jev-drone) - 在 MuJoCo 中使用 Jev 的无人机模拟实验。

## 评测与开源实现

- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) - 重排序评测，使用其结论前需查看数据集与测试方法。
- [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) - 钓鱼内容分类对比，包含 Jev 表现不及对照模型的结果。
- [Janus](https://github.com/FirasSX914/Janus) - 在自己的数据上测量置信度阈值，再据此在大小模型之间路由。
- [jevlike](https://github.com/vinnylarouge/jevlike) - 开源选项评分实现，不是 TypeSafe 的模型权重。
- [OpenJev / SemIf](https://github.com/TheoLeeCJ/SemIf) - 受 Jev 启发的独立实现，不是官方模型。
- [TypeSafe 工作流评测](https://evals.typesafe.ai/) - 厂商发布的评测，需查看参考答案与对照方法。

## 文章与中文资源

- [Every / Mike Taylor](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) - 小样本使用评测，不能作为通用准确率保证。
- [OrcaRouter 中文介绍](https://www.orcarouter.ai/zh-CN/blog/jev-typesafe-system-one-what-we-know) - 介绍产品与已有公开材料。
- [宝玉的中文解读](https://x.com/dotey/status/2100109937237987823) - 解释 Jev 的用途，属于第三方解读，不是独立评测。
- [jev-report](https://github.com/HackSing/jev-report) - 中文报告与复现材料；2026-09-19 已确认仓库存在，本清单未复现其中结果。

## 使用前注意

- 输出格式正确，不代表判断正确；先用你自己的样本验证。
- 一个请求含多个意图时，分别判断，避免用一个类别概括所有需求。
- 精确计算和日期运算交给代码处理。
- 置信度阈值需要在实际数据上测量，不能直接照搬示例。
- 对比速度、成本和准确率时，记录模型版本、输入、测试条件和失败结果。
- 模型参与工具调用时，在程序中限制权限，并为不确定的结果保留人工处理路径。

更多说明见[能力局限](taxonomy/critique-limits.md)和[评测方法](taxonomy/benchmarks-replicas.md)。以上是使用建议，本仓库未独立复现所有收录项目。


## 踩坑与边界

精选几条最容易误读的公开事实；完整列表与英文对照见 [guides/gotchas.md](guides/gotchas.md)。

- 格式正确不等于判断正确；先看官方 [模型能力局限](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。
- 演示「赢过一次」不等于可复现（例：[Pac-Man 后续](https://x.com/ephraimduncan/status/2100554620254752981)）。
- 小样本速度/成本文章不能外推成通用准确率（例：[Every 实验](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds)）。
- 开源复刻不是官方权重；负结果（如 [phishing-bench](https://github.com/anisselbd/jev-phishing-bench)）同样收录。
- 首页精选卡片的核对范围见 [guides/featured-review.md](guides/featured-review.md)：安装通过 ≠ 生产验收。

## 更多资料

- [按资源类别查找](SUMMARY.md)。
- [使用方法](SUMMARY.md#使用方法)。
- [能力局限与评测注意事项](taxonomy/critique-limits.md)。
- [踩坑与边界](guides/gotchas.md)。
- [社区动态](updates/README.md)。
- [历史研究笔记](research/00-overview.md)。

## 参与贡献

欢迎补充项目、更正描述和提交失败案例，请先阅读[贡献说明](CONTRIBUTING.md)。
