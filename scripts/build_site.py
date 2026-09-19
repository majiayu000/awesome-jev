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
            cards.append(f'<article class="card" data-category="{html.escape(category_id, quote=True)}"><div class="category">{html.escape(category)}</div><h3>{html.escape(name)}</h3><p>{html.escape(description)}</p><p class="resource-links">{link_html}</p></article>')
    if not cards:
        raise ValueError('The catalog is empty')
    options = ''.join(f'<option value="{key}">{html.escape(value)}</option>' for key, value in categories.items())
    return TEMPLATE.replace('__CATEGORY_OPTIONS__', options).replace('__RESOURCE_CARDS__', ''.join(cards))

TEMPLATE = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101c1d"><title>Awesome Jev — 项目、工具与实践</title>
<meta name="description" content="探索 Jev / TypeSafe System One 的开源项目、SDK、教程与评测。提供完整资源目录、分类搜索和中英文入门说明。">
<link rel="canonical" href="https://majiayu000.github.io/awesome-jev/">
<meta property="og:type" content="website"><meta property="og:site_name" content="Awesome Jev">
<meta property="og:title" content="Awesome Jev — 项目、工具与实践">
<meta property="og:description" content="探索 Jev / TypeSafe System One 的开源项目、SDK、教程与评测。">
<meta property="og:url" content="https://majiayu000.github.io/awesome-jev/">
<meta property="og:image" content="https://majiayu000.github.io/awesome-jev/social-preview.png">
<meta property="og:image:width" content="1280"><meta property="og:image:height" content="640">
<meta property="og:image:alt" content="Awesome Jev 蓝色插画画廊与项目目录">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Awesome Jev">
<meta name="twitter:description" content="Jev projects, SDKs, tutorials and evaluations.">
<meta name="twitter:image" content="https://majiayu000.github.io/awesome-jev/social-preview.png"><link rel="stylesheet" href="css/style.css"></head>
<body><a class="skip" href="#resources">跳至资源目录</a><header><a href="#" class="brand" aria-label="Awesome Jev 首页">awesome jev<span>PROJECTS & POSSIBILITIES</span></a><nav aria-label="主导航"><a href="#resources">探索 <span>EXPLORE</span></a><a href="#approach">入门 <span>START</span></a><a href="https://github.com/majiayu000/awesome-jev/blob/main/README.md" lang="en">English</a></nav><a class="contact" href="https://github.com/majiayu000/awesome-jev">GitHub <span>↗</span></a></header>
<main><section class="hero" style="--focus:68%" aria-label="艺术作品轮播" data-scene="0"><img class="scene" src="assets/bloom.webp" alt="蓝白花卉插画" fetchpriority="high"><canvas id="dissolve" aria-hidden="true"></canvas><div class="shade"></div><div class="hero-top"><span><i></i> A COMMUNITY COLLECTION FOR JEV</span><span class="edition">TYPESAFE SYSTEM ONE / OPEN-SOURCE RESOURCES</span></div><div class="hero-copy"><p class="eyebrow">项目、工具与实践</p><h1>Explore Jev.<br>Build <em>what’s next.</em></h1><p class="intro">发现值得尝试的项目，<br>为你的下一个想法找到起点。</p><a class="round-link" href="#resources"><span>探索资源目录</span><b>↗</b></a></div><aside class="floating"><a class="note" href="https://github.com/majiayu000/awesome-jev/blob/main/README_zh.md"><span class="micro">A PLACE TO START <b>↗</b></span><div>第一次遇见 Jev？<br>从这里开始。</div><p>认识模型、选择 SDK，再试一个项目。</p><span class="note-bottom">READ THE INTRODUCTION <span>01</span></span></a></aside><div class="slide-selectors" role="group" aria-label="选择画面"><button type="button" data-select="0" aria-label="第1幅：花卉" aria-pressed="true"><span>01</span></button><button type="button" data-select="1" aria-label="第2幅：锦鲤" aria-pressed="false"><span>02</span></button><button type="button" data-select="2" aria-label="第3幅：白鹭" aria-pressed="false"><span>03</span></button><button type="button" data-select="3" aria-label="第4幅：月夜" aria-pressed="false"><span>04</span></button><button type="button" data-select="4" aria-label="第5幅：人物" aria-pressed="false"><span>05</span></button></div><div class="hero-bottom"><span id="scene-name">01 — A BOTANICAL DREAM</span><div class="player"><button id="prev" aria-label="上一幅">←</button><span id="counter" aria-live="polite">01 / 05</span><button id="next" aria-label="下一幅">→</button><span class="divider"></span><button id="pause" aria-label="暂停轮播" aria-pressed="false">Ⅱ</button></div><a href="#resources" class="scroll">SCROLL TO DISCOVER <span>↓</span></a></div><div class="progress"><span></span></div><p id="media-error" role="alert" hidden>画面加载失败，请刷新页面重试。</p></section>
<div class="under-hero"><span>OPEN SOURCE · SDKs · TUTORIALS · EVALUATIONS</span><span>一份持续整理的 Jev 社区资源清单。</span></div>
<section id="resources" class="work resources" aria-labelledby="resources-title"><div class="section-label"><span>01 / THE COLLECTION</span><span>项目与学习资料</span></div><div class="work-heading"><div><p class="eyebrow">从一个问题，找到一种可能</p><h2 id="resources-title">Ideas worth <em>exploring.</em></h2></div><p>按用途浏览，找到适合你的下一步。<br>项目描述保留收集时的语言。</p></div>
<div id="filters" class="catalog-controls" hidden><label class="search-label" for="q"><span>搜索目录 / SEARCH</span><input id="q" type="search" placeholder="项目名称、SDK、browser、路由…" autocomplete="off"></label><label class="category-label" for="category"><span>分类 / CATEGORY</span><select id="category"><option value="">全部分类</option>__CATEGORY_OPTIONS__</select></label><button id="reset" type="button">重置 ↺</button></div>
<div class="catalog-status"><p id="status" role="status" aria-live="polite">完整目录</p><a href="https://github.com/majiayu000/awesome-jev/blob/main/catalog/FULL.md">在 GitHub 阅读 ↗</a></div>
<noscript><p>下面可直接浏览全部项目；启用 JavaScript 后可使用搜索和分类。</p></noscript><div id="grid" class="resource-grid">__RESOURCE_CARDS__</div></section>
<section id="approach" class="approach"><div class="section-label"><span>02 / GETTING STARTED</span><span>从了解，到第一次使用</span></div><div class="steps"><article><span>01 — UNDERSTAND</span><h3>先了解它。</h3><p>从官方文档认识 Jev 能处理的选择、评分和条件判断。</p><a href="https://docs.typesafe.ai/">阅读官方文档 ↗</a></article><article><span>02 — TRY</span><h3>动手试一次。</h3><p>选择对应语言的 SDK，参考路由与结果检查的使用方法。</p><a href="https://github.com/majiayu000/awesome-jev/blob/main/taxonomy/sdks.md">选择 SDK ↗</a></article><article><span>03 — EVALUATE</span><h3>看看哪里会错。</h3><p>格式正确不代表判断正确。用自己的样本评估，保留失败结果。</p><a href="https://github.com/majiayu000/awesome-jev/blob/main/taxonomy/critique-limits.md">了解使用限制 ↗</a></article></div></section>
<footer id="about"><p>MADE FOR THE CURIOUS. MAINTAINED BY THE COMMUNITY.</p><h2>A good find.<br><em>Pass it on.</em></h2><a class="footer-action" href="https://github.com/majiayu000/awesome-jev/blob/main/CONTRIBUTING.md">分享你发现的项目 <span>↗</span></a><p class="footer-note">社区维护，与 TypeSafe 无隶属关系。收录表示值得参考，不代表已验证安全性或生产可用性。</p><div class="footer-bottom"><a class="brand" href="#">awesome jev<span>PROJECTS & POSSIBILITIES</span></a><div><a href="https://github.com/majiayu000/awesome-jev/blob/main/SOURCE.md">资料来源</a> · <a href="https://github.com/majiayu000/awesome-jev/blob/main/updates/README.md">社区动态</a> · <a href="https://github.com/majiayu000/awesome-jev/blob/main/LICENSE">许可</a></div><a href="#">BACK TO TOP ↑</a></div></footer></main>
<script src="js/app.js"></script></body></html>
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
