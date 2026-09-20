# UPDATE_PIPELINE.md — China AI Hub

How data stays fresh. Design target: agents prepare updates; critical facts pass validation before publication. No blind auto-publish.

## 1. Monitoring targets (Phase 7+)

| Target | What changes | Priority |
|---|---|---|
| Official model docs | versions, context, capabilities | High |
| Official pricing pages | prices, tiers, discounts | High |
| Official announcements | new models, deprecations | High |
| Official GitHub | releases, license changes | High |
| Major benchmark orgs | new scores, versions | Medium |
| Company news | products, agents, partnerships | Medium |
| Agent product pages | features, models used | Medium |

## 2. Pipeline stages

```
Official Sources
→ Crawler (Firecrawl self-hosted: http://43.173.100.60:3002)
→ Change Detection (diff vs last snapshot)
→ Structured Extraction (agent-assisted)
→ Source Attribution (SOURCE_POLICY.md format)
→ Validation (quality gates)
→ Database (content collections, history preserved)
→ Page Rendering (build)
→ SEO/Schema check
→ QA (build green + gate pass)
→ Publication (push → Cloudflare)
```

## 3. Agent operating rules

- Agents assist discovery, extraction, normalization, change detection, source comparison, update proposals.
- Agents MUST NOT overwrite critical data without validation: any change to pricing, license, context window, benchmark score, or status requires a verified L1 source.
- Every update proposal records: old value, new value, effective date, source URL, verifier date.
- If verification fails (source unreachable), data stays unchanged; mark `verification_failed: <date>` for follow-up.

## 4. History preservation

- Pricing: append to `price_history` (never delete old).
- Benchmarks: new evaluation entries with dates; keep old ones labeled by model version.
- Models: version changes create new `model_id` entries (immutable IDs); old entries get `status: deprecated` + `superseded_by: <new_id>`.
- Companies/agents: `major_releases` chronology appended; corrections recorded in `notes` when public confusion existed.

## 5. Cadence

- Weekly (light): re-verify pricing + status for top 10 models/providers; update `last_verified`.
- Monthly (full): crawl all monitored targets; generate change proposals; review + apply validated ones.
- Event-driven: major releases (new DeepSeek/Qwen/Kimi/GLM model, price cuts, license changes) → immediate proposal within 24h.
- News section serves as the trigger log: each news item lists `trigger_updates` entity IDs.

## 6. Validation gates (rerun before every publication)

- Pricing gate (DATA_SCHEMA.md §5): currency/region/billing/unit/cache/batch/date/source
- Model gate (DATA_SCHEMA.md §1): name/provider/version/date/status/context/pricing/capabilities/license/API/source/verified
- Benchmark gate (§6): name/version/model version/score/method/source/date
- Content gate (CONTENT_GUIDELINES.md §9) for editorial
- `npm run build` green + sitemap URLs correct

## 7. Failure modes

- Update with no source → reject
- Update from L4-only source for critical fact → reject, request better source
- Silently deleting old price → prohibited (append history)
- Auto-publishing without gate → prohibited; proposals only
- Skipping `last_verified` refresh → page shows stale warning (SOURCE_POLICY.md §5)

## 8. Tools

- Crawl/extract: Firecrawl API (self-hosted, /v1/scrape + /v1/crawl) — see TOOLS.md
- Discovery: `web_search` / `tavily` / `chinese-web-research` skill for Chinese sources
- Verification: `source-verification` skill for conflicts
- Diffs: git history of content collections (each update = a commit)
