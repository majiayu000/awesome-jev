# Contributing to Awesome Jev

欢迎补充有明确用途的 Jev 项目、教程和评测，也欢迎纠正错误信息。

## 收录要求

- 提供可公开访问的项目或文章链接。
- 用一句话说明它解决什么问题，以及 Jev 在其中做什么。
- 优先链接项目源码、官方文档、作者文章或原始测试结果。
- 性能、成本和准确率数字要附测试条件与来源。未亲自复现时，写明“作者报告”或“厂商公布”。
- 示例和实验可以收录，但不要称为生产可用；已失效、归档或停止维护的项目不放在首页推荐中。

无需填写一套标签，也不按星数、浏览量或固定名额收录。

## 修改哪里

| 内容 | 文件 |
| --- | --- |
| 首页精选 | 同时修改 `README.md` 和 `README_zh.md`，保持项目与含义一致 |
| 完整收集记录 | `catalog/`，按该目录 README 说明维护来源数据与可读清单 |
| 分类补充 | `taxonomy/` 中对应的文档，在 `SUMMARY.md` 查看分类 |
| 使用方法 | `patterns/` 中对应的文档 |
| 某个时间段的动态 | `updates/`，注明日期并更新索引 |
| 来源与整理方式 | `SOURCE.md` |

一个项目只在最相关的分类中写完整介绍，其他位置按需要链接过去。首页可以保留一句简短推荐。首页精选不等于收集总量；精简首页时保留完整目录中的记录。链接失效时标注状态或更新地址，不要静默删除历史收集内容。

## 如何描述证据

来源、文章类型和验证程度分别写清楚即可，不需要“可信”等级。

- 官方文档说明产品接口；厂商性能主张仍需查看测试方法。
- 第三方解读属于文章，不能仅凭作者独立就称为独立评测。
- 评测应能找到任务、数据或样本、方法、对照和结果；本仓库未复现的结果要明确归因给原作者。
- 一次演示只能说明该次运行。开源兼容实现也不等于官方模型、训练方法或权重。
- 尚未确认的资料保留在研究笔记中，不作为已验证结论推荐。

## 提交前检查

打开新增链接，检查本地相对链接，核对中英文首页的一致性，并运行 `python3 scripts/check_repository.py` 与 `git diff --check`。自动检查会核对中英文首页的外部链接、维护文档的相对链接和目录 JSON 格式；外部网站是否可达仍需人工确认。不要为了文档修改引入构建系统或测试框架。

网页目录由 `catalog/FULL.md` 生成。修改完整目录后运行 `python3 scripts/build_site.py`，同时提交 `docs/index.html`；用 `python3 scripts/build_site.py --check` 检查是否同步。`docs/data/entries.json` 保留历史收集记录，不再作为网页展示数据。

修改示例后运行 `python3 -m unittest discover -s examples -v`，默认测试不调用真实 API。

## English summary

Provide a public link and a plain-language description of the use case. Attribute claims to their sources, distinguish commentary from experiments, and state when results have not been reproduced here. Keep both READMEs aligned. Use the category pages for additional resources and the dated updates for news. After editing `catalog/FULL.md`, run `python3 scripts/build_site.py` and commit the generated `docs/index.html` too.
