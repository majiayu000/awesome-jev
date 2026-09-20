"""Render the complete Markdown catalog as a searchable, crawlable static page."""
import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://majiayu000.github.io/awesome-jev/'
REPO = 'https://github.com/majiayu000/awesome-jev/blob/main/'

CATEGORY_INTROS = {
    'official': '从官方文档、快速入门、API 说明和模型局限开始了解 Jev。',
    'sdks': '查找 JavaScript、TypeScript、Python 等语言的 SDK 和客户端，选择适合项目的接入方式。',
    'integrations': '浏览模型网关、框架适配器和服务集成，了解 Jev 如何进入现有技术栈。',
    'agents': '查找模型路由、代码审查、工单分类与智能体检查工具，了解判断结果如何进入工作流。',
    'browser': '浏览网页自动化、DOM 操作、OCR 与电脑控制项目，比较它们的输入和执行方式。',
    'apps': '探索搜索、内容处理、个人工具等应用，查看 Jev 在实际产品中承担的任务。',
    'games': '浏览游戏智能体、模拟环境和交互实验，观察结构化状态如何用于动作选择。',
    'demos': '从演示、教程和小型示例入手，了解输入、问题、模型结果和程序处理的完整过程。',
    'research': '查找评测、开源实现和研究资料；比较结果时注意数据、模型版本与测试条件。',
    'lists': '探索其他社区清单和资料目录，寻找更多 Jev 与 TypeSafe System One 的相关资源。',
    'articles': '阅读发布介绍、技术文章与社区讨论；作者经验与性能主张需要结合原始材料判断。',
}


def build():
    cards, categories = [], {}
    # Reuse maintained Chinese descriptions instead of a second translation database.
    chinese = {
        url.rstrip('/'): description
        for url, description in re.findall(
            r'^- \[[^\]]+\]\((https://[^)]+)\) - (.+)$',
            (ROOT / 'README_zh.md').read_text(), re.MULTILINE)
    }
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
            translated = next((chinese[url.rstrip('/')] for _, url in links if url.rstrip('/') in chinese), '')
            translation_html = f'<p class="resource-zh" lang="zh-CN">{html.escape(translated)}</p>' if translated and translated != description else ''
            link_html = ' · '.join(f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>' for label, url in links)
            domain = urlsplit(links[0][1]).hostname
            card = f'<article class="card" data-category="{html.escape(category_id, quote=True)}"><div class="resource-body"><div class="resource-heading"><span class="resource-initial" aria-hidden="true">{html.escape(name[:1].upper())}</span><span class="category">{html.escape(category)}</span></div><h3><a href="{html.escape(links[0][1], quote=True)}">{html.escape(name)}</a></h3>{translation_html}<p>{html.escape(description)}</p></div><div class="resource-footer"><span class="resource-domain">{html.escape(domain)}</span><div class="resource-links">{link_html}</div></div></article>'
            cards.append((category_id, card))
    if not cards:
        raise ValueError('The catalog is empty')

    def render(template, scope='', prefix=''):
        choices = {scope: categories[scope]} if scope else categories
        options = ''.join(f'<option value="{key}">{html.escape(value)}</option>' for key, value in choices.items())
        buttons = ''.join(f'<button type="button" data-category="{key}" aria-pressed="false">{html.escape(value)}</button>' for key, value in choices.items())
        directory = '<nav class="category-directory" aria-label="分类专页">' + ''.join(
            f'<a href="{prefix}categories/{key}.html"' + (' aria-current="page"' if key == scope else '') + f'>{html.escape(value)} ↗</a>'
            for key, value in categories.items()) + '</nav>'
        rendered = template.replace('__CATEGORY_OPTIONS__', options).replace('__CATEGORY_BUTTONS__', buttons)
        rendered = rendered.replace('__RESOURCE_CARDS__', ''.join(card for key, card in cards if not scope or key == scope))
        return rendered.replace('__CATEGORY_DIRECTORY__', directory)

    outputs = {'index.html': render(TEMPLATE)}
    # Reuse the site's head, navigation, catalog controls and footer on category pages.
    head = TEMPLATE.split('<main>')[0]
    catalog = '<section id="resources"' + TEMPLATE.split('<section id="resources"', 1)[1].split('<section id="learn"', 1)[0]
    footer = '<footer class="site-footer">' + TEMPLATE.split('<footer class="site-footer">', 1)[1]
    for key, label in categories.items():
        title = f'Jev {label} — Awesome Jev'
        description = CATEGORY_INTROS[key]
        canonical = SITE + f'categories/{key}.html'
        category_head = re.sub(r'<title>.*?</title>', f'<title>{html.escape(title)}</title>', head)
        for attribute, value in [('name="description"', description), ('property="og:title"', title), ('property="og:description"', description), ('name="twitter:title"', title), ('name="twitter:description"', description)]:
            category_head = re.sub(f'(<meta {attribute} content=")[^"]*(")', lambda m: m[1] + html.escape(value, quote=True) + m[2], category_head)
        category_head = category_head.replace(f'rel="canonical" href="{SITE}"', f'rel="canonical" href="{canonical}"').replace(f'property="og:url" content="{SITE}"', f'property="og:url" content="{canonical}"')
        category_head = category_head.replace('href="css/', 'href="../css/').replace('src="js/', 'src="../js/').replace('href="./"', 'href="../"').replace('href="#featured"', 'href="../#featured"').replace('href="#learn"', 'href="../#learn"')
        intro = f'<section class="category-intro shell"><a class="text-link" href="../#resources">← 返回完整目录</a><p class="eyebrow">EXPLORE JEV</p><h1>{html.escape(label)}</h1><p>{html.escape(description)}</p></section>'
        category_catalog = catalog.replace('找到你需要的下一步。', '浏览本分类资源。')
        category_catalog = category_catalog.replace('class="mobile-category"', 'class="sr-only"')
        category_catalog = re.sub(r'<div class="category-buttons".*?</div>', '', category_catalog)
        category_catalog = category_catalog.replace('id="grid" class=', f'id="grid" data-label="{html.escape(label)}" class=')
        outputs[f'categories/{key}.html'] = render(category_head + '<main>' + intro + category_catalog + '</main>' + footer, key, '../')
    locations = ''.join(f'  <url><loc>{SITE + (name if name != "index.html" else "")}</loc></url>\n' for name in outputs)
    outputs['sitemap.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + locations + '</urlset>\n'
    return outputs

TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f3f0e9">
<title>Awesome Jev — 开源项目、工具与实践</title>
<meta name="description" content="查找 Jev / TypeSafe System One 的开源项目、SDK、浏览器自动化、教程与评测。从入门精选到完整资源目录，按用途探索。">
<meta name="google-site-verification" content="RU2-TUFIhPM_cDASRGjQicB0VysuuAHV3V9HiHZ9Yn0" />
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
<section class="topic-strip shell" aria-label="按用途探索"><a href="categories/sdks.html"><span>01 / INTEGRATE</span><strong>接入 Jev <i>↗</i></strong><p>SDK、客户端与集成</p></a><a href="categories/agents.html"><span>02 / AUTOMATE</span><strong>构建智能体 <i>↗</i></strong><p>路由、代码审查与工具调用</p></a><a href="categories/browser.html"><span>03 / INTERACT</span><strong>操作浏览器 <i>↗</i></strong><p>浏览器与电脑操作项目</p></a><a href="categories/research.html"><span>04 / EVALUATE</span><strong>理解能力边界 <i>↗</i></strong><p>评测、对比与开源实现</p></a></section>
<section id="featured" class="featured shell" aria-labelledby="featured-title"><div class="section-heading"><div><p class="eyebrow">A FEW PLACES TO BEGIN</p><h2 id="featured-title">先看这几个。</h2></div><a class="text-link" href="https://github.com/majiayu000/awesome-jev/blob/main/README_zh.md">查看全部入门精选 ↗</a></div>
<div class="featured-grid">
<article class="feature-card sdk-card"><div class="feature-visual" aria-hidden="true"><span class="code-tag">&lt;/&gt;</span><span class="visual-caption">THE BUILDING BLOCKS</span><span class="visual-index">01</span></div><div class="feature-body"><p class="eyebrow">OFFICIAL / SDK</p><h3>从官方客户端开始</h3><p>使用 JavaScript、TypeScript 或 Python，把 Jev 接入自己的程序。</p><div class="feature-links"><a href="https://github.com/typesafe-ai/typesafe-sdk-js">JavaScript ↗</a><a href="https://github.com/typesafe-ai/typesafe-sdk-python">Python ↗</a></div></div></article>
<article class="feature-card browser-card"><div class="feature-visual" aria-hidden="true"><span class="browser-glyph"><i></i><i></i><i></i><b>↗</b></span><span class="visual-caption">FROM CHOICE TO ACTION</span><span class="visual-index">02</span></div><div class="feature-body"><p class="eyebrow">BROWSER / AUTOMATION</p><h3>browser-use / jev-ultrafast</h3><p>由 Jev 选择浏览器操作与 DOM 元素，语言模型负责生成输入文字。</p><div class="feature-links"><a href="https://github.com/browser-use/jev-ultrafast">探索项目 ↗</a></div></div></article>
<article class="feature-card router-card"><div class="feature-visual" aria-hidden="true"><span class="route-glyph"><i></i><i></i><i></i></span><span class="visual-caption">FIND THE RIGHT ROUTE</span><span class="visual-index">03</span></div><div class="feature-body"><p class="eyebrow">AGENTS / ROUTING</p><h3>jev-router</h3><p>为 Claude Code 和 Codex 的任务选择模型，需要 Jev 密钥与对应 CLI。</p><div class="feature-links"><a href="https://github.com/gargpratyush/jev-router">探索项目 ↗</a></div></div></article>
</div><p class="featured-review">2026-09-20 已核对首页四个仓库的状态与接入要求。<a href="https://github.com/majiayu000/awesome-jev/blob/main/guides/featured-review.md">查看核对记录与未验证部分 ↗</a></p></section>
<section id="resources" class="catalog-section" aria-labelledby="catalog-title"><div class="shell"><div class="section-heading"><div><p class="eyebrow">THE RESOURCE INDEX</p><h2 id="catalog-title">找到你需要的下一步。</h2></div><p class="section-caption">项目、工具、教程与文章<br>原始链接，按用途整理。</p></div>
<div class="catalog-main"><div id="filters" class="catalog-controls" hidden><label class="search-label" for="q"><span class="sr-only">搜索资源</span><span class="search-symbol" aria-hidden="true">⌕</span><input id="q" aria-describedby="search-help" type="search" placeholder="搜索名称、用途或链接…" autocomplete="off"><kbd aria-hidden="true">/</kbd></label><label class="mobile-category" for="category"><span class="sr-only">分类</span><select id="category"><option value="">全部分类</option>__CATEGORY_OPTIONS__</select></label><button id="reset" class="reset" type="button">重置 ↺</button></div><p id="search-help" class="search-help">支持中文与多关键词，例如：浏览器 DOM。</p><div class="catalog-status"><p id="status" role="status" aria-live="polite">全部资源</p><div class="catalog-actions"><button id="share" type="button" hidden>复制筛选链接 ↗</button><div class="view-switch" id="view-switch" role="group" aria-label="目录显示方式" hidden><button type="button" data-view="grid" aria-pressed="true">▦ 卡片</button><button type="button" data-view="list" aria-pressed="false">☰ 列表</button></div></div></div><p id="share-status" role="status" aria-live="polite"></p><input id="share-url" aria-label="当前筛选链接" readonly hidden><div class="category-buttons" id="category-buttons" role="group" aria-label="按类别筛选" hidden><button type="button" data-category="" aria-pressed="true">全部分类</button>__CATEGORY_BUTTONS__</div>
<noscript><p>下方可直接阅读全部资源。启用 JavaScript 后可搜索、分类和翻页。</p></noscript><div id="grid" class="resource-list" data-view="grid">__RESOURCE_CARDS__</div><div id="empty" class="empty-state" hidden><span aria-hidden="true">∅</span><h3>暂时没有找到。</h3><p>试试项目英文名、相关用途，或重置筛选。</p><button type="button" id="empty-reset">重新浏览全部资源 ↗</button></div><nav id="pagination" class="pagination" aria-label="资源分页" hidden><button type="button" id="page-prev">← 上一页</button><span id="page-status" aria-live="polite"></span><button type="button" id="page-next">下一页 →</button></nav><p class="catalog-footnote">部分项目补充了中文用途说明，原始描述保留供对照。<a href="https://github.com/majiayu000/awesome-jev/blob/main/catalog/FULL.md">在 GitHub 阅读完整目录 ↗</a></p>__CATEGORY_DIRECTORY__</div></div></section>
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
    outputs = build()
    if args.check:
        stale = [name for name, content in outputs.items() if not (ROOT / 'docs' / name).exists() or (ROOT / 'docs' / name).read_text() != content]
        extra = [str(path.relative_to(ROOT / 'docs')) for path in (ROOT / 'docs/categories').glob('*.html') if str(path.relative_to(ROOT / 'docs')) not in outputs]
        if stale or extra:
            raise SystemExit('Website is stale: ' + ', '.join(stale + extra) + '. Run python3 scripts/build_site.py.')
        print('Website pages and sitemap match the catalog and Chinese README.')
    else:
        for name, content in outputs.items():
            output = ROOT / 'docs' / name
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(content)
        print(f'Generated {len(outputs) - 1} pages and sitemap from catalog/FULL.md and README_zh.md.')
