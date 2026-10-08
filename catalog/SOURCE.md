# 资料来源与维护

[FULL.md](FULL.md) 按类别展示收集的资源。同一个仓库或主要链接只展示一次，并保留收集记录中附带的网站和文章链接。不同地址可能仍指向同一项目，发现后可继续整理。

## 数据来源

- [entries.json](entries.json) 保存早期目录数据，初始描述和元数据来自 [hellogumbo/awesome-jev 的 data/projects.json](https://github.com/hellogumbo/awesome-jev/blob/main/data/projects.json)，记录日期为 2026-09-18。该数据也用于 [awesomejev.com](https://awesomejev.com/)。
- [`docs/data/entries.json`](../docs/data/entries.json) 保存原仓库的 GitHub 采集与补充数据。日期和原始采集文件的限制见[仓库来源说明](../SOURCE.md)。[GITHUB.md](GITHUB.md) 保留其可读记录，便于追溯。

原始 JSON 数据保留用于核对历史来源，不作为当前网页的展示数据，也不代表当前分类与核验状态。当前资源入口统一为 [FULL.md](FULL.md)。网页的资源目录由 [生成脚本](../scripts/build_site.py) 从 `FULL.md` 生成，中文用途说明复用 [README_zh.md](../README_zh.md)。

网页首页的精选卡片在生成脚本的 `TEMPLATE` 中人工维护，不会随目录条目或中文 README 自动更新。精选项目的接入条件与带日期的核对范围见[核对记录](../guides/featured-review.md)。

## 维护

新增或更新资源时，修改 `FULL.md` 中相应条目，保留名称、用途和原始链接。无需与外部目录保持相同内容或更新节奏。原始采集文件记录历史状态，不要求与编辑后的目录完全一致。

修改 `FULL.md` 或 `README_zh.md` 后，在仓库根目录运行 `python3 scripts/build_site.py`，同时提交生成的首页、`docs/categories/` 分类页与 `docs/sitemap.xml`；用 `python3 scripts/build_site.py --check` 检查是否同步。完整流程见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

链接失效时标注状态或更新地址。精简首页时仍保留完整目录中的收集记录。
