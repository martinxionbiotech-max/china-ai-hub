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

import json
import re
import sys
from pathlib import Path

import yaml

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

# ---------------------------------------------------------------------------
# Dimension hub support (Phase 2C C3). Hub pages live under /models/<slug>/
# but are NOT model entities, so they must be excluded from the sitemap
# surface (S3). Hub membership is single-sourced in scripts/hub-rules.json
# and generated into src/data/hubs.json by scripts/generate-hubs.mjs; this
# script independently re-reads frontmatter and re-applies the same rules to
# verify the generated count/membership.
# ---------------------------------------------------------------------------


def hub_doc(root: Path) -> dict:
    """Load scripts/hub-rules.json (rules + editorial) or {} if absent."""
    p = root / "scripts" / "hub-rules.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def hub_slugs(root: Path) -> set[str]:
    """Non-entity route slugs under /models/ (the six dimension hubs)."""
    return {h["slug"] for h in hub_doc(root).get("hubs", [])}


def resolve_path(obj, dotted: str):
    cur = obj
    for key in dotted.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def eval_hub_rule(data: dict, rule: dict) -> bool:
    op = rule.get("op")
    if op == "eq":
        return resolve_path(data, rule["path"]) == rule["value"]
    if op == "gte":
        v = resolve_path(data, rule["path"])
        return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= rule["value"]
    if op == "contains_ci":
        v = resolve_path(data, rule["path"])
        return isinstance(v, str) and str(rule["value"]).lower() in v.lower()
    if op == "present":
        v = resolve_path(data, rule["path"])
        return v is not None and v != ""
    if op == "any":
        return any(eval_hub_rule(data, r) for r in rule["rules"])
    raise ValueError(f"Unknown hub rule op: {op}")


def model_frontmatter(root: Path) -> dict[str, dict]:
    """Parse every model's YAML frontmatter, keyed by model_id."""
    out = {}
    d = root / "src" / "content" / "models"
    if not d.is_dir():
        return out
    for f in sorted(d.glob("*.md")):
        text = f.read_text()
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        data = yaml.safe_load(m.group(1))
        if isinstance(data, dict) and data.get("model_id"):
            out[data["model_id"]] = data
    return out


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


def sitemap_files(sitemap: Path, exclude: set[str] | None = None) -> dict[str, set[str]]:
    """S3: entity URLs per collection. `exclude` drops non-entity routes
    (the six dimension hub pages under /models/)."""
    exclude = exclude or set()
    out = {c: set() for c in COLLECTIONS}
    if not sitemap.exists():
        return out
    text = sitemap.read_text()
    for coll, prefix in URL_PREFIX.items():
        for m in re.finditer(re.escape(prefix) + r"([a-z0-9.-]+)/", text):
            slug = norm(m.group(1))
            if slug in exclude:
                continue
            out[coll].add(slug)
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


def verify_hubs(root: Path) -> bool:
    """Phase 2C C3: verify each dimension hub's generated count/membership
    against an independent re-read of the model frontmatter. Returns True when
    every hub matches exactly (count == member set size == entity count)."""
    doc = hub_doc(root)
    hubs = doc.get("hubs", [])
    if not hubs:
        return True

    gen_path = root / "src" / "data" / "hubs.json"
    generated = {}
    if gen_path.exists():
        generated = {h["slug"]: set(h.get("members", [])) for h in json.loads(gen_path.read_text()).get("hubs", [])}

    fm = model_frontmatter(root)

    print("Dimension hub verification (hub count == matching entity count)")
    print(f"  rules   : {root / 'scripts' / 'hub-rules.json'}")
    print(f"  output  : {gen_path}")
    print()

    ok = True
    for hub in hubs:
        slug = hub["slug"]
        expected = {mid for mid, data in fm.items() if eval_hub_rule(data, hub["rule"])}
        declared = generated.get(slug)
        if declared is None:
            flag, note = "FAIL", "missing from hubs.json"
            ok = False
        elif expected == declared:
            flag, note = "OK ", ""
        else:
            flag = "FAIL"
            missing = sorted(expected - declared)
            extra = sorted(declared - expected)
            note = f"missing={missing} extra={extra}"
            ok = False
        declared_s = str(len(declared)) if declared is not None else '—'
        print(f"[{flag}] {slug:12s} expected={len(expected):3d} declared={declared_s:>3s} {note}")

    print()
    if ok:
        print("HUB RESULT: 0 discrepancies (all six hub counts match their entity counts).")
    else:
        print("HUB RESULT: discrepancies found (see FAIL rows above).")
    return ok


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
    s3 = sitemap_files(sitemap, exclude=hub_slugs(root))
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

    hubs_ok = verify_hubs(root)
    print()
    return 0 if (ok and hubs_ok) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
