"""Render the complete Markdown catalog as a searchable, crawlable static page."""
import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://majiayu000.github.io/awesome-jev/'
REPO = 'https://github.com/majiayu000/awesome-jev/blob/main/'

def build():
    cards, categories = [], {}
    category_id = category = ''
    for line in (ROOT / 'catalog/FULL.md').read_text().splitlines():
        if match := re.fullmatch(r'<a id="([^"]+)"></a>', line):
            category_id = match[1]
        elif line.startswith('## ') and category_id:
            category = line[3:]
            categories[category_id] = category
        elif line.startswith('| ') and category_id:
            fields = [field.strip() for field in line.strip('|').split('|')]
            if fields[0] in ('项目或资源', '---'):
                continue
            if len(fields) != 3:
                raise ValueError(f'Unexpected catalog row: {line}')
            name, description, raw_links = fields
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', raw_links)
            if not links:
                raise ValueError(f'Missing resource link: {name}')
            for _, url in links:
                parsed = urlsplit(url)
                if parsed.scheme not in ('https', 'http') or not parsed.netloc or parsed.username or parsed.password:
                    raise ValueError(f'Invalid resource URL: {url}')
            link_html = ' · '.join(f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>' for label, url in links)
            domain = urlsplit(links[0][1]).hostname
            cards.append(f'<article class="card" data-category="{html.escape(category_id, quote=True)}"><div class="resource-body"><div class="resource-heading"><span class="resource-initial" aria-hidden="true">{html.escape(name[:1].upper())}</span><span class="category">{html.escape(category)}</span></div><h3><a href="{html.escape(links[0][1], quote=True)}">{html.escape(name)}</a></h3><p>{html.escape(description)}</p></div><div class="resource-footer"><span class="resource-domain">{html.escape(domain)}</span><div class="resource-links">{link_html}</div></div></article>')
    if not cards:
        raise ValueError('The catalog is empty')
    options = ''.join(f'<option value="{key}">{html.escape(value)}</option>' for key, value in categories.items())
    buttons = ''.join(f'<button type="button" data-category="{key}" aria-pressed="false">{html.escape(value)}</button>' for key, value in categories.items())
    return TEMPLATE.replace('__CATEGORY_OPTIONS__', options).replace('__CATEGORY_BUTTONS__', buttons).replace('__RESOURCE_CARDS__', ''.join(cards))

TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f3f0e9">
<title>Awesome Jev — 开源项目、工具与实践</title>
<meta name="description" content="查找 Jev / TypeSafe System One 的开源项目、SDK、浏览器自动化、教程与评测。从入门精选到完整资源目录，按用途探索。">
<link rel="canonical" href="https://majiayu000.github.io/awesome-jev/">
<meta property="og:type" content="website"><meta property="og:site_name" content="Awesome Jev"><meta property="og:title" content="Awesome Jev — 开源项目、工具与实践">
<meta property="og:description" content="从一次判断，到一个项目。探索 Jev 的 SDK、开源工具、教程与评测。"><meta property="og:url" content="https://majiayu000.github.io/awesome-jev/">
<meta property="og:image" content="https://majiayu000.github.io/awesome-jev/social-preview.png"><meta property="og:image:width" content="1280"><meta property="og:image:height" content="640"><meta property="og:image:alt" content="Awesome Jev 项目目录与路径选择概念插画">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Awesome Jev"><meta name="twitter:description" content="Jev projects, SDKs, tutorials and evaluations."><meta name="twitter:image" content="https://majiayu000.github.io/awesome-jev/social-preview.png">
<link rel="stylesheet" href="css/style.css"><script src="js/app.js" defer></script>
</head>
<body>
<a class="skip" href="#resources">跳至资源目录</a>
<header class="site-header shell"><a class="brand" href="./" aria-label="Awesome Jev 首页"><span class="brand-mark" aria-hidden="true">j/</span><span>awesome jev<small>A COMMUNITY FIELD GUIDE</small></span></a><nav aria-label="主导航"><a href="#featured">精选</a><a href="#resources">目录</a><a href="#learn">入门</a><a href="https://github.com/majiayu000/awesome-jev/blob/main/README.md" lang="en">EN</a></nav><a class="github-link" href="https://github.com/majiayu000/awesome-jev">GitHub <span>↗</span></a></header>
<main>
<section class="hero shell" aria-labelledby="hero-title">
<div class="hero-copy"><p class="eyebrow"><span class="live-dot"></span> THE JEV EXPLORER</p><h1 id="hero-title">从一次判断，<br>到一个<span>项目。</span></h1><p class="hero-description">Jev 的开源项目、SDK、教程与评测。<br>发现一个思路，找到工具，开始动手。</p><form id="hero-search" class="hero-search" role="search" hidden><label class="sr-only" for="hero-q">搜索 Jev 项目与资源</label><span aria-hidden="true">⌕</span><input id="hero-q" type="search" placeholder="搜索工具、SDK 或使用场景…" autocomplete="off"><button type="submit" aria-label="搜索资源">→</button></form><div class="hero-actions"><a class="button primary" href="#resources">探索资源目录 <span>↗</span></a><a class="text-link" href="#learn">第一次了解 Jev？ <span>→</span></a></div><div class="hero-footnote"><span class="asterisk" aria-hidden="true">✳</span><p>围绕 TypeSafe System One 整理<br><span>社区维护 · 中英文入门</span></p></div></div>
<figure class="hero-art"><img src="assets/decision-paths.webp" alt="象牙色分岔轨道与橙色路径组成的决策装置概念插画" width="1672" height="941" fetchpriority="high"><figcaption><span>STUDY 01 / POSSIBLE PATHS</span><span>每一次选择，都通向新的可能 ↗</span></figcaption><div class="art-label" aria-hidden="true"><span>DECISION<br>IN MOTION</span><b>01—</b></div></figure>
</section>
<section class="topic-strip shell" aria-label="按用途探索"><a href="#resources" data-category-link="sdks"><span>01 / INTEGRATE</span><strong>接入 Jev <i>↗</i></strong><p>SDK、客户端与集成</p></a><a href="#resources" data-category-link="agents"><span>02 / AUTOMATE</span><strong>构建智能体 <i>↗</i></strong><p>路由、代码审查与工具调用</p></a><a href="#resources" data-category-link="browser"><span>03 / INTERACT</span><strong>操作浏览器 <i>↗</i></strong><p>浏览器与电脑操作项目</p></a><a href="#resources" data-category-link="research"><span>04 / EVALUATE</span><strong>理解能力边界 <i>↗</i></strong><p>评测、对比与开源实现</p></a></section>
<section id="featured" class="featured shell" aria-labelledby="featured-title"><div class="section-heading"><div><p class="eyebrow">A FEW PLACES TO BEGIN</p><h2 id="featured-title">先看这几个。</h2></div><a class="text-link" href="https://github.com/majiayu000/awesome-jev/blob/main/README_zh.md">查看全部入门精选 ↗</a></div>
<div class="featured-grid">
<article class="feature-card sdk-card"><div class="feature-visual" aria-hidden="true"><span class="code-tag">&lt;/&gt;</span><span class="visual-caption">THE BUILDING BLOCKS</span><span class="visual-index">01</span></div><div class="feature-body"><p class="eyebrow">OFFICIAL / SDK</p><h3>从官方客户端开始</h3><p>使用 JavaScript、TypeScript 或 Python，把 Jev 接入自己的程序。</p><div class="feature-links"><a href="https://github.com/typesafe-ai/typesafe-sdk-js">JavaScript ↗</a><a href="https://github.com/typesafe-ai/typesafe-sdk-python">Python ↗</a></div></div></article>
<article class="feature-card browser-card"><div class="feature-visual" aria-hidden="true"><span class="browser-glyph"><i></i><i></i><i></i><b>↗</b></span><span class="visual-caption">FROM CHOICE TO ACTION</span><span class="visual-index">02</span></div><div class="feature-body"><p class="eyebrow">BROWSER / AUTOMATION</p><h3>browser-use / jev-ultrafast</h3><p>由 Jev 选择浏览器操作与 DOM 元素，语言模型负责生成输入文字。</p><div class="feature-links"><a href="https://github.com/browser-use/jev-ultrafast">探索项目 ↗</a></div></div></article>
<article class="feature-card router-card"><div class="feature-visual" aria-hidden="true"><span class="route-glyph"><i></i><i></i><i></i></span><span class="visual-caption">FIND THE RIGHT ROUTE</span><span class="visual-index">03</span></div><div class="feature-body"><p class="eyebrow">AGENTS / ROUTING</p><h3>jev-router</h3><p>为 Claude Code 的任务选择模型，参考如何把判断用于实际工作流。</p><div class="feature-links"><a href="https://github.com/gargpratyush/jev-router">探索项目 ↗</a></div></div></article>
</div></section>
<section id="resources" class="catalog-section" aria-labelledby="catalog-title"><div class="shell"><div class="section-heading"><div><p class="eyebrow">THE RESOURCE INDEX</p><h2 id="catalog-title">找到你需要的下一步。</h2></div><p class="section-caption">项目、工具、教程与文章<br>原始链接，按用途整理。</p></div>
<div class="catalog-main"><div id="filters" class="catalog-controls" hidden><label class="search-label" for="q"><span class="sr-only">搜索资源</span><span class="search-symbol" aria-hidden="true">⌕</span><input id="q" type="search" placeholder="搜索名称、用途或链接…" autocomplete="off"><kbd aria-hidden="true">/</kbd></label><label class="mobile-category" for="category"><span class="sr-only">分类</span><select id="category"><option value="">全部分类</option>__CATEGORY_OPTIONS__</select></label><button id="reset" class="reset" type="button">重置 ↺</button></div><div class="catalog-status"><p id="status" role="status" aria-live="polite">全部资源</p><div class="view-switch" id="view-switch" role="group" aria-label="目录显示方式" hidden><button type="button" data-view="grid" aria-pressed="true">▦ 卡片</button><button type="button" data-view="list" aria-pressed="false">☰ 列表</button></div></div><div class="category-buttons" id="category-buttons" role="group" aria-label="按类别筛选" hidden><button type="button" data-category="" aria-pressed="true">全部分类</button>__CATEGORY_BUTTONS__</div>
<noscript><p>下方可直接阅读全部资源。启用 JavaScript 后可搜索、分类和翻页。</p></noscript><div id="grid" class="resource-list" data-view="grid">__RESOURCE_CARDS__</div><div id="empty" class="empty-state" hidden><span aria-hidden="true">∅</span><h3>暂时没有找到。</h3><p>试试项目英文名、相关用途，或重置筛选。</p><button type="button" id="empty-reset">重新浏览全部资源 ↗</button></div><nav id="pagination" class="pagination" aria-label="资源分页" hidden><button type="button" id="page-prev">← 上一页</button><span id="page-status" aria-live="polite"></span><button type="button" id="page-next">下一页 →</button></nav><p class="catalog-footnote">描述保留收集时的语言，当前状态以项目说明为准。<a href="https://github.com/majiayu000/awesome-jev/blob/main/catalog/FULL.md">在 GitHub 阅读完整目录 ↗</a></p></div></div></section>
<section id="learn" class="learning shell" aria-labelledby="learn-title"><figure class="learning-art"><img src="assets/evaluation-study.webp" alt="金属平衡杆、陶瓷阶梯与琥珀色校准块组成的评估概念插画" width="1672" height="941" loading="lazy"><figcaption>STUDY 02 / MEASURE, THEN DECIDE</figcaption></figure><div class="learning-copy"><p class="eyebrow">UNDERSTAND BEFORE YOU BUILD</p><h2 id="learn-title">先动手，<br>也要看清边界。</h2><p>Jev 可以选择选项、打分和判断条件。输出格式正确，并不意味着判断一定正确。</p><div class="reading-list"><a href="https://docs.typesafe.ai/"><span>01</span><div><h3>认识 Jev</h3><p>官方文档、接口说明与快速入门</p></div><b>↗</b></a><a href="https://github.com/majiayu000/awesome-jev/blob/main/examples/README.md"><span>02</span><div><h3>试一个实际用途</h3><p>运行离线工单示例，再按需接入 API</p></div><b>↗</b></a><a href="https://github.com/majiayu000/awesome-jev/blob/main/taxonomy/critique-limits.md"><span>03</span><div><h3>记录结果，也记录错误</h3><p>能力局限、评测方法与使用注意事项</p></div><b>↗</b></a></div></div></section>
<section class="contribute shell"><span class="contribute-symbol" aria-hidden="true">✳</span><div><p class="eyebrow">A COLLECTION GROWS BY SHARING</p><h2>发现了值得一试的项目？</h2><p>补充链接、修正描述，或分享一次有记录的使用经验。</p></div><a class="button primary" href="https://github.com/majiayu000/awesome-jev/blob/main/CONTRIBUTING.md">参与整理 <span>↗</span></a></section>
</main>
<footer class="site-footer"><div class="shell footer-top"><a class="footer-wordmark" href="#">awesome jev<span>↗</span></a><p>为好奇心找到一个起点。<br><span>A field guide to Jev & System One.</span></p></div><div class="shell footer-bottom"><p>社区维护，与 TypeSafe 无隶属关系。<br>收录不代表已验证安全性、准确率或生产可用性。</p><nav aria-label="页脚导航"><a href="https://github.com/majiayu000/awesome-jev/blob/main/SOURCE.md">资料来源</a><a href="https://github.com/majiayu000/awesome-jev/blob/main/updates/README.md">社区动态</a><a href="https://github.com/majiayu000/awesome-jev/blob/main/LICENSE">许可</a><a href="#">返回顶部 ↑</a></nav></div></footer>
</body></html>
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the published HTML is stale')
    args = parser.parse_args()
    output = ROOT / 'docs/index.html'
    rendered = build()
    if args.check:
        if not output.exists() or output.read_text() != rendered:
            raise SystemExit('Website is stale. Run python3 scripts/build_site.py and commit docs/index.html.')
        print('Website matches catalog/FULL.md.')
    else:
        output.write_text(rendered)
        print('Generated docs/index.html from catalog/FULL.md.')
