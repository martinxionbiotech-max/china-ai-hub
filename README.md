# China AI Hub

Source of truth for the development of https://chinaaihub.com — an independent, English-language, structured knowledge platform for China's AI ecosystem (models, agents, APIs, companies, pricing, benchmarks, technology, comparisons, original research).

## Architecture docs (read before changing anything)

- [ARCHITECTURE_AUDIT.md](docs/ARCHITECTURE_AUDIT.md) — Phase 0 audit (greenfield)
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — product architecture, stack, URL map, entity graph, phases
- [DATA_SCHEMA.md](docs/DATA_SCHEMA.md) — field-level schemas + data quality gates
- [CONTENT_GUIDELINES.md](docs/CONTENT_GUIDELINES.md) — writing voice, originality test, quality gate
- [ORIGINAL_RESEARCH_GUIDE.md](docs/ORIGINAL_RESEARCH_GUIDE.md) — research workflow for Layer C content
- [SOURCE_POLICY.md](docs/SOURCE_POLICY.md) — source hierarchy, conflicts, last-verified system
- [SEO_GUIDE.md](docs/SEO_GUIDE.md) — entity SEO / GEO / AIO rules
- [UPDATE_PIPELINE.md](docs/UPDATE_PIPELINE.md) — freshness pipeline, monitoring, validation

## Stack

Astro 5 (static) + Tailwind CSS v4 + typed content collections. Deployed on Cloudflare Pages.

## Build

```bash
npm install
npm run build   # outputs to dist/
```

## Content layout

- `src/content/models/*.md` — one file per model (filename = stable model_id)
- `src/content/companies/*.md`
- `src/content/agents/*.md`
- `src/content/apis/*.md`
- `src/content/pricing/*.md` — one file per provider
- `src/content/benchmarks/*.md`
- `src/content/technologies/*.md`
- `src/content/comparisons/*.md`, `guides/`, `research/`, `news/`

## Rules for agents

1. Read `docs/` first.
2. Never invent data. Unknown = `null` / `"unknown"` / `"not publicly disclosed"`.
3. Critical facts (pricing, license, context, benchmarks, status) require a verified primary source before publication.
4. Preserve history (price_history, deprecated model entries).
5. Stable IDs are immutable.
6. `npm run build` must be green before any push.
