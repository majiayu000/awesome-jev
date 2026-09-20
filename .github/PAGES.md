# GitHub Pages

The site is generated from `catalog/FULL.md`, with Chinese use-case descriptions reused from `README_zh.md`. Run `python3 scripts/build_site.py` after changing either source and commit `docs/index.html`, `docs/categories/`, and `docs/sitemap.xml`. CI checks all generated output with `python3 scripts/build_site.py --check`.

Pages publishes `main` → `/docs` at https://majiayu000.github.io/awesome-jev/. Preview with `python3 -m http.server 8080 --directory docs`.

All resources are present in HTML without JavaScript. Eleven category pages provide introductions, direct navigation, individual canonical URLs and social metadata; sitemap.xml lists the homepage and category pages. JavaScript adds multi-keyword search and filtering. Query parameters `q`, `category`, `page`, and `view` preserve the current selection across sharing, refresh, and browser history. Search terms are combined with AND and normalized for case and full-width characters. The project-level robots.txt does not control the host-root robots.txt.

Run `python3 -m unittest discover -s scripts -v` to check category coverage, metadata, internal navigation and static Chinese descriptions. Homepage project review notes are maintained in `guides/featured-review.md`.
