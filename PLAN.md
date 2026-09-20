# Awesome Jev 维护计划

本计划按当前仓库和维护者要求更新。项目是 Jev / TypeSafe System One 的双语资源清单，使用普通的项目分类与用途说明。完整目录持续保留；首页精选只是阅读入口。

## 本次范围

- 改善 GitHub 的项目说明、主题词和双语首页导航。
- 补充接入路线、使用注意事项和贡献检查命令。
- 添加轻量 CI，检查本地链接、中英文资源链接及目录数据。
- 保留已有项目、来源记录和完整目录。
- 本次同时修改网站并启用 GitHub Pages（维护者已确认）。

旧计划中的旧仓库名、“可信地图”、信任等级、Must-30 固定名额、删除目录建议和自动周更承诺不再采用。收录项目时直接写用途、来源、测试条件与尚未确认的部分。

## 首页与发现

- [x] 统一名称为 Awesome Jev，使用当前仓库地址。
- [x] 英文和中文首页介绍 Jev、SDK、教程与评测。
- [x] 添加阅读路线，连接入门、SDK、使用方法、完整目录和社区动态。
- [x] 保留官方文档、模型限制、发布介绍和试用控制台四个入门入口。
- [x] 首页说明格式正确与判断正确的区别，并补充使用注意事项。
- [x] 添加 CI 状态入口；状态以实际运行结果为准。
- [x] 网站分享图片使用首页截图，已配置 Open Graph 与 Twitter 图片链接。
- [x] GitHub 仓库单独的 Social preview 图片已上传并在设置页确认显示。

About 使用清晰的一句话介绍，并明确中英双语。Topics 围绕 Jev、TypeSafe、System One、智能体和浏览器自动化；不堆砌无关热词。未发布网站时不填写不存在的 Homepage。

## 内容与贡献

- [x] 中英文首页保持同一组资源链接。
- [x] 完整收集内容保留在 `catalog/`，来源见 [SOURCE.md](SOURCE.md)。
- [x] SDK 分类直接连接完整 SDK 目录。
- [x] 贡献说明要求原始链接、用途和性能主张的测试条件。
- [x] 更新说明提供每期写作要点，并按真实日期维护索引。

有实际变化再发布社区动态，不预写未来新闻，不自动对外发帖。模型版本、接口、价格和作者实验结果需要在更新时重新核实；CI 不替代内容审阅。暂时无法访问的资源先检查或标注，不自动删除。

## 自动检查

本地运行：

```sh
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -v
git diff --check
```

GitHub Actions 在提交到 main 和打开或更新 PR 时执行。检查维护文档的相对链接和标题锚点、两种语言首页的外部链接一致性、资源 JSON 是否可读取。历史研究笔记不纳入文档链接检查。CI 另外检查生成的网站是否与完整目录一致；网站原始 JSON 只读检查格式。

外部链接仍由贡献者打开核实。HTTP 限流、登录要求或临时故障不能直接作为删除资源的理由。

## 后续工作

- [x] 网页复用 38 条精选资源的中文用途说明，支持多关键词、大小写与全角字符搜索。
- [x] 搜索、分类、页码和显示方式写入网址，可复制分享，并在刷新和前进后退时恢复。
- [x] 生成 11 个独立分类页，提供分类介绍、原始资源、导航、独立 canonical 与 sitemap 条目。
- [x] 2026-09-20 核对首页四个精选仓库的状态和接入条件，实际安装两个 SDK 与路由包；范围和未验证事项见[核对记录](guides/featured-review.md)。
- [x] [PR #1](https://github.com/majiayu000/awesome-jev/pull/1) 的五个项目已核对原始 README，并纳入双语首页与完整目录；未复现作者的性能结果。
- [x] [PR #2](https://github.com/majiayu000/awesome-jev/pull/2) 已审查，保留双语入门、工单示例与离线测试、资源推荐表单。旧网站和 README 精选数据生成器由当前完整目录网站替代；独立候选采集工具不纳入本次维护范围。
- [x] 网站统一名称并从完整目录生成可直接阅读的 HTML，提供搜索和分类筛选。
- [x] 补充标题、描述、canonical、社交分享元数据与 sitemap。
- [x] GitHub Pages 已发布，线上搜索、移动端及无 JavaScript 阅读验证通过。
- [x] 完整目录中的仓库自身条目已更新为 Awesome Jev，清除旧名称与旧定位。
- [x] 网站已融合工具目录的搜索、分类和卡片／列表浏览方式，并保留原有配色与插画。
- [x] Spellbook Illustrated Gallery 模板已移除固定图片与整站示例，改为生图、整页设计及六类扩展方向的指导；[PR #205](https://github.com/majiayu000/spellbook/pull/205) 已合并。
- [x] 2026-09-20 已通过 Google Search Console 的 HTML 标记验证，资源范围为 `https://majiayu000.github.io/awesome-jev/`；验证标记保留在网站生成器中。
- [x] 已提交 `sitemap.xml`，Search Console 确认提交成功；首页“请求编入索引”也成功，已进入优先抓取队列。
- [ ] 等待 Google 后续抓取与收录。2026-09-20 检查时首页尚未收录，sitemap 显示“无法抓取”；线上 sitemap 返回 HTTP 200 且 XML 可解析，尚不能确认 Google 抓取失败的原因。提交成功不代表已收录，后续需在 Search Console 复查处理状态。

参考仓库：[awesome-grok-bot](https://github.com/majiayu000/awesome-grok-bot)。参考其清楚的入口和自动检查，不照搬面向不同数据的复杂校验规则。

## 2026-09-20 追加

- [x] 新增 [guides/gotchas.md](guides/gotchas.md) 与首页「踩坑」入口。
- [x] 新增 [updates/2026-09-20.md](updates/2026-09-20.md) 记录清单/站点自身进展与精选核对。

