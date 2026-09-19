# GitHub Pages

The site is generated from `catalog/FULL.md`. Run `python3 scripts/build_site.py` after changing the catalog and commit `docs/index.html`. CI checks the generated output with `python3 scripts/build_site.py --check`.

Pages publishes `main` → `/docs` at https://majiayu000.github.io/awesome-jev/. Preview with `python3 -m http.server 8080 --directory docs`.

All resources are present in HTML without JavaScript. JavaScript adds search and category filtering. Canonical and social metadata use the project-site URL; sitemap.xml lists the main page. The project-level robots.txt does not control the host-root robots.txt.
