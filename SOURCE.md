# 资料来源

Awesome Jev 是人工整理的资源清单。README 提供入门与精选项目，分类文档补充相关资料。这里的推荐不代表项目已经通过测试。

## 来源与维护

优先引用官方文档、GitHub 仓库、作者文章和原始评测。其他目录可用于发现资料，具体介绍应指向原项目。新增或更正条目直接修改相应 Markdown，流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

现有分类与研究材料主要整理于 2026-09-17 至 2026-09-19。整理日期不等于逐项测试日期。API、价格、开放范围与项目维护状态可能变化，使用时应查看原始来源。

- [TypeSafe 文档](https://docs.typesafe.ai/)与[发布文章](https://typesafe.ai/blog/introducing-system-one-models-and-jev)提供官方说明。
- [awesomejev.com](https://awesomejev.com/)、[hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev)、[AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe)、[yibie/awesome-jev](https://github.com/yibie/awesome-jev)和[AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev)曾用于发现项目。
- [research/](research/00-overview.md)保留早期调研来源和当时的记录，不是当前 API 文档，也不表示本仓库独立复现了其中结果。

首页和分类页不再维护重复的星数排名。研究笔记中的历史星数保留原日期与来源，不作为当前排名。

## 当前网页的来源

网页的资源目录由 [scripts/build_site.py](scripts/build_site.py) 从 [catalog/FULL.md](catalog/FULL.md) 生成，中文用途说明复用 [README_zh.md](README_zh.md)。生成结果包括 `docs/index.html`、`docs/categories/` 分类页与 `docs/sitemap.xml`；更新与同步检查方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

网页首页的精选卡片在生成脚本的 `TEMPLATE` 中人工维护，不会随目录条目或中文 README 自动更新。精选项目的接入条件与带日期的核对范围见[核对记录](guides/featured-review.md)；网站的其他来源说明见 [docs/SOURCE.md](docs/SOURCE.md)。

## 网页数据的历史来源

`docs/data/entries.json` 是一份独立的历史快照，未与当前 Markdown 同步，也不再作为当前网页的展示数据。

旧版来源说明称，该数据由 GitHub API 采集结果与当时的 README 精选表合并。它引用的 `/workspace/uploads/discovered_repos.json` 原始文件没有随仓库提交，这份历史快照的采集和生成脚本也未提交。因此，目前不能仅凭仓库重做该数据集，也不能据此宣称每条数据已经得到独立核实。

历史快照中仍有旧版标签与推荐字段，它们不作为当前资源清单的收录标准，也不代表当前分类与核验状态。

[完整资源目录](catalog/FULL.md) 汇总收集的项目、文档与文章。原始数据保留以便追溯，来源和维护方式见[目录说明](catalog/SOURCE.md)。

## 名称

仓库使用 `awesome-jev`，标题使用 **Awesome Jev**，遵循常见的 `awesome-主题` 命名方式。命名参考 [Awesome 清单规范](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md)，不表示已被该目录收录。
