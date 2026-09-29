#!/usr/bin/env python3
"""check-entity-counts.py — four-surface entity-count parity check.

Compares, per entity collection, four independent surfaces:

  S1  Main-site content files    src/content/<coll>/*.md
  S2  Data-hub entity records    <data-repo>/docs/<coll>/*.md (excl. index.md)
  S3  Main-site sitemap URLs     dist/sitemap-0.xml  (URL prefix per collection)
  S4  Data-hub declared entities mkdocs.yml nav + docs/<coll>/index.md link tables

All four surfaces must resolve to the SAME set of entity slugs. Any difference
prints a per-collection diff and exits 1.

Slug normalization: Astro's glob loader strips dots ("qwen3.8-max" -> "qwen38-max")
and the data hub keeps dots. We key everything on the dot-stripped slug so the
two forms compare equal.

Usage:
  python3 scripts/check-entity-counts.py [--data-repo PATH] [--sitemap PATH]

Env overrides:
  CHINA_AI_HUB_DATA   path to the china-ai-hub-data repo (default: ../china-ai-hub-data)
"""

import re
import sys
from pathlib import Path

# collection -> main-site URL prefix (Astro route; note apis -> /api/, singular)
URL_PREFIX = {
    "models": "/models/",
    "companies": "/companies/",
    "agents": "/agents/",
    "apis": "/api/",
    "pricing": "/pricing/",
    "benchmarks": "/benchmarks/",
}

COLLECTIONS = list(URL_PREFIX)


def norm(slug: str) -> str:
    """Dot-stripped canonical slug (matches Astro's glob-loader slugify)."""
    return slug.replace(".", "")


def main_files(root: Path) -> dict[str, set[str]]:
    out = {}
    for coll in COLLECTIONS:
        d = root / "src" / "content" / coll
        out[coll] = {norm(f.stem) for f in d.glob("*.md")} if d.is_dir() else set()
    return out


def data_files(data_root: Path) -> dict[str, set[str]]:
    out = {}
    for coll in COLLECTIONS:
        d = data_root / "docs" / coll
        slugs = set()
        if d.is_dir():
            for f in d.glob("*.md"):
                if f.name == "index.md":
                    continue
                slugs.add(norm(f.stem))
        out[coll] = slugs
    return out


def sitemap_files(sitemap: Path) -> dict[str, set[str]]:
    out = {c: set() for c in COLLECTIONS}
    if not sitemap.exists():
        return out
    text = sitemap.read_text()
    for coll, prefix in URL_PREFIX.items():
        for m in re.finditer(re.escape(prefix) + r"([a-z0-9.-]+)/", text):
            out[coll].add(norm(m.group(1)))
    return out


def declared_entities(data_root: Path) -> dict[str, set[str]]:
    """S4: slugs referenced by the data hub's nav (mkdocs.yml) and its
    per-collection index.md entity tables."""
    out = {c: set() for c in COLLECTIONS}
    nav = data_root / "mkdocs.yml"
    if nav.exists():
        for line in nav.read_text().splitlines():
            for coll in COLLECTIONS:
                m = re.search(rf"^{coll}/([a-z0-9.-]+)\.md\s*$", line.strip())
                if m:
                    out[coll].add(norm(m.group(1)))
    for coll in COLLECTIONS:
        idx = data_root / "docs" / coll / "index.md"
        if idx.exists():
            for m in re.finditer(r"\]\(([a-z0-9.-]+)\.md\)", idx.read_text()):
                slug = m.group(1)
                if slug != "index":
                    out[coll].add(norm(slug))
    return out


def diff(a: set[str], b: set[str]) -> tuple[list[str], list[str]]:
    return sorted(a - b), sorted(b - a)


def main(argv: list[str]) -> int:
    args = argv[1:]
    data_repo = None
    sitemap_path = None
    i = 0
    while i < len(args):
        if args[i] == "--data-repo" and i + 1 < len(args):
            data_repo = Path(args[i + 1]); i += 2
        elif args[i] == "--sitemap" and i + 1 < len(args):
            sitemap_path = Path(args[i + 1]); i += 2
        else:
            i += 1

    root = Path(__file__).resolve().parent.parent
    data_root = data_repo or Path(
        __import__("os").environ.get("CHINA_AI_HUB_DATA", root.parent / "china-ai-hub-data")
    )
    sitemap = sitemap_path or (root / "dist" / "sitemap-0.xml")

    s1 = main_files(root)
    s2 = data_files(data_root)
    s3 = sitemap_files(sitemap)
    s4 = declared_entities(data_root)

    labels = ["S1 main-files", "S2 data-records", "S3 sitemap", "S4 declared"]
    surfaces = [s1, s2, s3, s4]

    print("Four-surface entity-count comparison")
    print(f"  main repo : {root}")
    print(f"  data repo : {data_root}")
    print(f"  sitemap   : {sitemap}")
    print()

    ok = True
    for coll in COLLECTIONS:
        counts = [len(s[coll]) for s in surfaces]
        row = " | ".join(f"{lbl}={counts[j]}" for j, lbl in enumerate(labels))
        consistent = len(set(counts)) == 1
        flag = "OK " if consistent else "FAIL"
        print(f"[{flag}] {coll:11s} {row}")
        if not consistent:
            ok = False
            # report diffs against S1 (main files = source of truth)
            base = s1[coll]
            for j, (lbl, s) in enumerate(zip(labels, surfaces)):
                missing, extra = diff(base, s[coll])
                if missing or extra:
                    print(f"        {lbl}: missing={missing} extra={extra}")

    print()
    if ok:
        print("RESULT: 0 discrepancies across all six collections.")
    else:
        print("RESULT: discrepancies found (see FAIL rows above).")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
