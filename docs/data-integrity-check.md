# Data Integrity Check — Four-Surface Entity-Count Parity

**Date:** 2026-09-29 · **Batch:** Phase 2B P0 · **Scope:** `china-ai-hub` (main site) + `china-ai-hub-data` (data hub)

This document records the four-surface entity-count audit and the automated check that keeps the two repos in sync.

## The four surfaces

Every entity collection (models / companies / agents / apis / pricing / benchmarks) is counted independently across four surfaces:

| # | Surface | Source |
|---|---------|--------|
| S1 | Main-site content files | `china-ai-hub/src/content/<coll>/*.md` |
| S2 | Data-hub entity records | `china-ai-hub-data/docs/<coll>/*.md` (excl. `index.md`) |
| S3 | Main-site sitemap URLs | `china-ai-hub/dist/sitemap-0.xml` (per-collection URL prefix) |
| S4 | Data-hub declared entities | `mkdocs.yml` nav + `docs/<coll>/index.md` link tables |

Slugs are normalized by stripping dots before comparison, because Astro's glob loader slugifies `qwen3.8-max` → `qwen38-max` while the data hub keeps the dotted form. The dot-stripped form is the shared key.

## Current comparison table

| Collection | S1 main-files | S2 data-records | S3 sitemap | S4 declared | Verdict |
|------------|--------------|-----------------|-----------|-------------|---------|
| models | 21 | 21 | 21 | 21 | ✅ |
| companies | 12 | 12 | 12 | 12 | ✅ |
| agents | 18 | 18 | 18 | 18 | ✅ |
| apis | 6 | 6 | 6 | 6 | ✅ |
| pricing | 6 | 6 | 6 | 6 | ✅ |
| benchmarks | 18 | 18 | 18 | 18 | ✅ |

**Total: 81 entities** (21 + 12 + 18 + 6 + 6 + 18), 0 discrepancies.

## The 21-vs-19 models discrepancy (resolved)

The P0 audit reported "21 models on the main site vs 19 models on the data hub". Root cause: **both** `glm-5.3-flashx` and `qwen3.7-plus` already existed as files in `china-ai-hub-data/docs/models/`, but were **not declared** on the data hub's two "declared" surfaces:

- `mkdocs.yml` — Models nav listed 19 entries (missing the two)
- `docs/models/index.md` — Entities table listed 19 rows (missing the two)
- `docs/index.md` — status read "Models: 19 tracked"

The main-site content files (S1), data-hub files (S2), and the sitemap (S3) all already agreed at 21 — only S4 lagged. No entity was missing on the data hub's file surface; the two pages were simply unwired.

### Fix applied

1. `mkdocs.yml` — added `GLM-5.3-FlashX` and `Qwen3.7-Plus` to the Models nav.
2. `docs/models/index.md` — added both rows to the Entities table.
3. `docs/index.md` — corrected "Models: 19 tracked" → "Models: 21 tracked".

After the fix, all four surfaces agree at 21. (The reverse case — main site holding an unsourced extra page — did not apply: every one of the 21 main-site models has a verifiable official source and a matching data-hub record.)

## Automated check

**Script:** `china-ai-hub/scripts/check-entity-counts.py`

It reads the four surfaces, prints a per-collection table, and exits non-zero if any surface disagrees. Run it manually or via npm:

```bash
# from china-ai-hub/
python3 scripts/check-entity-counts.py   # exit 0 == 0 discrepancies
npm run check:counts                      # same, via npm
npm run verify                            # build then check
```

Options: `--data-repo PATH` (default `../china-ai-hub-data`), `--sitemap PATH` (default `dist/sitemap-0.xml`). Env override `CHINA_AI_HUB_DATA` for the data-repo location.

**Wiring:**

- `china-ai-hub/package.json` — added `check:counts` and `verify` scripts.
- Data hub CI — no `.github/workflows` exists in either repo; the check is invoked from the main repo against the sibling data repo. When CI is introduced later, add a `npm run verify` (or the raw python invocation) step after checkout of both repos.

## Data hub migration status

The data hub's "Skeleton (2026-09-21)" declaration and "being migrated" wording are removed. In their place, `docs/index.md` now carries a **formal status section** plus a **completeness self-check** section. `README.md` no longer calls the data hub "future subdomain" / "planned data layer"; it is live at `data.sinoaihub.com`.

Eight-element coverage (B3) was re-audited: all 81 entity pages carry Definition/Description + Key facts + Sources + a canonical main-site link; source-history notes present where applicable. No gaps found.
