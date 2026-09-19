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
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome Jev — Jev 项目、SDK、教程与评测</title>
  <meta name="description" content="查找 Jev / TypeSafe System One 的开源项目、SDK、浏览器自动化、教程与评测。按用途浏览完整目录，提供中英文入门与贡献说明。">
  <link rel="canonical" href="{SITE}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Awesome Jev">
  <meta property="og:title" content="Awesome Jev — Projects, SDKs, tutorials and evaluations">
  <meta property="og:description" content="Jev / TypeSafe System One 的项目与学习资料。Browse projects and learning resources with English and Chinese guides.">
  <meta property="og:url" content="{SITE}">
  <meta property="og:image" content="{SITE}social-preview.png">
  <meta property="og:image:width" content="1280">
  <meta property="og:image:height" content="640">
  <meta property="og:image:alt" content="Awesome Jev 项目与学习资源目录">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE}social-preview.png">
  <meta name="twitter:title" content="Awesome Jev">
  <meta name="twitter:description" content="Jev / TypeSafe System One projects, SDKs, tutorials and evaluations.">
  <link rel="stylesheet" href="css/style.css">
  <script src="js/app.js" defer></script>
</head>
<body>
<a class="skip" href="#resources">跳到资源目录</a>
<div class="wrap">
<header class="topbar"><a class="brand" href="./">Awesome <span>Jev</span></a><nav aria-label="主导航"><a href="#start">入门</a><a href="#resources">资源目录</a><a href="{REPO}README.md" lang="en">English</a><a href="https://github.com/majiayu000/awesome-jev">GitHub ↗</a></nav></header>
<main>
<section class="hero"><p class="eyebrow">JEV / TYPESAFE SYSTEM ONE</p><h1>找到合适的项目，<br><span>开始使用 Jev。</span></h1><p class="lede">从官方 SDK 到浏览器自动化，按用途查找开源项目、教程和评测。</p><div class="actions"><a class="button primary" href="#resources">浏览资源</a><a class="button" href="{REPO}README_zh.md">查看入门精选 ↗</a></div><p class="muted">社区维护，与 TypeSafe 无隶属关系。项目状态和测试结果请以原作者说明为准。</p></section>
<section class="section" id="start"><h2>从这里开始</h2><div class="primitives">
<article><h3>了解 Jev</h3><p>先看它能处理哪些选择、评分和条件判断。</p><p><a href="https://docs.typesafe.ai/">官方文档 ↗</a></p></article>
<article><h3>接入项目</h3><p>选择对应语言的客户端，再按使用方法尝试。</p><p><a href="{REPO}taxonomy/sdks.md">SDK 与客户端 ↗</a> · <a href="{REPO}patterns/routing.md">路由示例 ↗</a></p></article>
<article><h3>了解局限</h3><p>用自己的样本检查表现，记录失败情况与测试条件。</p><p><a href="{REPO}taxonomy/critique-limits.md">使用注意事项 ↗</a></p></article>
</div><aside class="notice">输出格式正确，不代表判断一定正确。收录表示值得参考，不代表经过安全或生产可用性验证。</aside></section>
<section class="section" id="resources"><h2>资源目录</h2><p>按分类浏览，或搜索项目名称、用途和链接。描述保留收集时的语言。</p>
<div class="controls" id="filters" hidden><label class="search">搜索<input id="q" type="search" placeholder="名称、SDK、browser、路由…" autocomplete="off"></label><label>分类<select id="category"><option value="">全部分类</option>{options}</select></label><button id="reset" type="button">重置</button></div>
<p id="status" role="status" aria-live="polite">完整目录</p><noscript><p>下面可直接浏览全部项目；启用 JavaScript 后可搜索和筛选。</p></noscript><div class="grid" id="grid">{''.join(cards)}</div>
</section></main>
<footer><strong>Awesome Jev</strong><p><a href="{REPO}CONTRIBUTING.md">参与贡献</a> · <a href="{REPO}SOURCE.md">资料来源</a> · <a href="{REPO}updates/README.md">社区动态</a> · <a href="{REPO}LICENSE">许可</a></p><p>English: <a href="{REPO}README.md">projects, SDKs, tutorials and evaluations for Jev</a>.</p></footer>
</div></body></html>
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
