# 首页精选核对记录 / Featured project review

[中文首页](../README_zh.md) · [English](../README.md)

核对日期：2026-09-20。范围是网站首页三张精选卡片所链接的四个仓库。项目链接固定到本次读取的提交；归档状态与推送日期来自 GitHub API。

| 项目与原始文档 | 仓库状态 | 接入条件 | Jev 的作用 | 本次实际检查 |
| --- | --- | --- | --- | --- |
| [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js/blob/66880ccded6cb642dc1809620c2b108c33730214/README.md) | 未归档、未禁用；最后推送 2026-09-15 | Node.js 20+；`npm install @typesafe-ai/sdk`；真实调用需要 `TYPESAFE_API_KEY`。 | JavaScript / TypeScript 程序向 Jev 发送状态与问题，读取结构化答案。 | 在临时目录安装 0.6.0 并成功导入；Node.js 22.15.0，安装禁用生命周期脚本。 |
| [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python/blob/2ce5c65f13646cab6e6f782328194c9d85f3300a/README.md) | 未归档、未禁用；最后推送 2026-09-18 | Python 3.10+；`pip install typesafe-sdk` 或 `uv add typesafe-sdk`；真实调用需要 `TYPESAFE_API_KEY`。 | Python 程序调用 Jev，读取 Choice、Score 和 Noul 结果。 | 在独立虚拟环境安装 0.7.0 并成功导入；Python 3.14.7。 |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/README.md) | 未归档、未禁用；最后推送 2026-09-18 | Python 3.12+、uv、Chrome、Browser Harness、TypeSafe 密钥与文字模型密钥；作者提供 `uv sync` 接入步骤。 | Jev 选择浏览器操作与 DOM 元素，文字模型只在需要输入文字时参与。 | 已核对 README 和依赖声明；未运行安装、连接浏览器或复现演示。 |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/README.md) | 未归档、未禁用；最后推送 2026-09-19 | Node.js 20.12+；`npm install -g jev-router`；Jev 密钥与已登录的 Claude Code 或 Codex CLI。 | 在新的用户轮次选择模型，实际执行交给对应编程 CLI。 | 在临时目录安装 0.3.0，禁用生命周期脚本；未启动路由命令或修改 CLI 配置。 |

安装与导入通过仅说明本次环境中的包可用。没有调用真实 Jev API，没有复现作者的准确率、成本或速度，没有验证生产环境兼容性。密钥、服务额度与 CLI 登录需要使用者自行准备。

## English

Checked on 2026-09-20: all four repositories linked by the homepage feature cards were public, unarchived and enabled. Links above point to the reviewed README commits. The JavaScript SDK 0.6.0 and Python SDK 0.7.0 installed and imported in isolated environments; jev-router 0.3.0 installed with npm lifecycle scripts disabled. Browser automation was reviewed from its README and dependency declaration only. No live API calls, browser-control sessions, routing sessions or performance reproductions were performed. The router now documents both Claude Code and Codex support.
