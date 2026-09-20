"""Offline checks for category discovery, preserved resources and page metadata."""
import unittest
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import PurePosixPath
from urllib.parse import urlsplit, unquote
import build_site


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.links, self.assets, self.ids, self.categories = [], [], set(), []
        self.canonical, self.h1 = None, 0
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'script' or tag == 'img':
            self.assets.append(attrs.get('src', ''))
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.assets.append(attrs['href'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'h1':
            self.h1 += 1
        if tag == 'article' and attrs.get('class') == 'card':
            self.categories.append(attrs['data-category'])


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = build_site.build()
        cls.pages = {name: Page(content) for name, content in cls.outputs.items() if name.endswith('.html')}

    def test_categories_preserve_every_resource_once(self):
        home = Counter(self.pages['index.html'].categories)
        categories = Counter()
        for name, page in self.pages.items():
            if name != 'index.html':
                key = PurePosixPath(name).stem
                self.assertTrue(page.categories)
                self.assertEqual(set(page.categories), {key})
                categories.update(page.categories)
        self.assertEqual(categories, home)

    def test_canonicals_and_sitemap_cover_all_pages(self):
        locations = {node.text for node in ET.fromstring(self.outputs['sitemap.xml']).iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
        self.assertEqual(locations, {page.canonical for page in self.pages.values()})
        self.assertEqual(len(locations), len(self.pages))
        for name, page in self.pages.items():
            self.assertEqual(page.h1, 1, name)
            self.assertEqual(page.canonical, build_site.SITE + (name if name != 'index.html' else ''))

    def test_local_navigation_and_assets_resolve(self):
        root = (build_site.ROOT / 'docs').resolve()
        for name, page in self.pages.items():
            for link in page.links + page.assets:
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc:
                    continue
                path = ((root / name).parent / unquote(parsed.path)).resolve() if parsed.path else root / name
                if parsed.path.endswith('/'):
                    path /= 'index.html'
                relative = str(path.relative_to(root))
                self.assertTrue(relative in self.outputs or path.is_file(), (name, link))
                if parsed.fragment and relative in self.pages:
                    self.assertIn(unquote(parsed.fragment), self.pages[relative].ids, (name, link))
        for name in self.pages:
            if name != 'index.html':
                self.assertIn(name, self.pages['index.html'].links)

    def test_chinese_use_cases_are_in_static_html(self):
        home = self.outputs['index.html']
        self.assertIn('class="resource-zh" lang="zh-CN"', home)
        self.assertIn('浏览器自动化工具', home)
        self.assertIn('代码审查', home)
        for content in self.outputs.values():
            self.assertNotIn('__RESOURCE_CARDS__', content)
            self.assertNotIn('__CATEGORY_DIRECTORY__', content)


if __name__ == '__main__':
    unittest.main()
