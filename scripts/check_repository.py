"""Offline checks for the maintained Markdown list; run with Python 3."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")
errors = []


def links(path):
    return LINK.findall(path.read_text(encoding="utf-8"))


def anchors(path):
    text = path.read_text(encoding="utf-8")
    result = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        candidate, suffix = slug, 0
        while candidate in result:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        result.add(candidate)
    return result


# Historical research and the separately maintained website are outside this check.
files = list(ROOT.glob("*.md"))
for folder in ("taxonomy", "patterns", "catalog", "updates"):
    files.extend((ROOT / folder).glob("*.md"))
for path in files:
    for link in links(path):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing target {link}")
        elif parsed.fragment and target.suffix == ".md":
            if unquote(parsed.fragment) not in anchors(target):
                errors.append(f"{path.relative_to(ROOT)}: missing anchor {link}")

english, chinese = [
    {url for url in links(ROOT / name) if url.startswith("https://")}
    for name in ("README.md", "README_zh.md")
]
for url in sorted(english ^ chinese):
    errors.append(f"README language mismatch: {url}")

for path in (ROOT / "catalog/entries.json", ROOT / "docs/data/entries.json"):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            errors.append(f"{path.relative_to(ROOT)}: expected a nonempty resource list")
    except (ValueError, OSError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Passed: local Markdown links in {len(files)} files, bilingual external links, catalog JSON.")
