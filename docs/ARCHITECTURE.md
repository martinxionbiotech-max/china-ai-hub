# ARCHITECTURE.md — China AI Hub

> China AI Hub = the English-language structured information layer for China's AI ecosystem.
> Models + Companies + Agents + APIs + Pricing + Benchmarks + Technology + Comparisons + Original Research, connected as a knowledge graph.

## 1. Product Summary

- **Domain:** https://chinaaihub.com (single domain, Phase 1; no subdomains)
- **Audience:** international developers, engineers, researchers, enterprise buyers, analysts
- **Core question answered:** Which Chinese AI model / agent / API suits which task, at what cost, with what capabilities, under what deployment conditions?
- **Differentiation:** structured data + evidence + original analysis, not article volume.

## 2. Tech Stack (decided)

| Layer | Choice | Rationale |
|---|---|---|
| Framework | Astro 5.x (static) | Static generation, fast, content collections, minimal JS |
| Styling | Tailwind CSS v4 + `@tailwindcss/typography` | User standard; typography for editorial pages |
| Entity data | Astro Content Collections (`src/content/*`) with typed Zod schemas | File = stable ID; typed; version-controllable |
| Explorers | Client-side filtering over pre-baked JSON (vanilla JS) | No backend needed; fast; crawlable base tables |
| Schema.org | JSON-LD per template (Organization, TechArticle, ItemList, SoftwareApplication where justified) | SEO/GEO |
| Deployment | Cloudflare Pages, `dist/` output, GitHub `martinxionbiotech-max/China-AI-Hub` | User standard |

**Explicit non-goals for Phase 1:** backend server, database hosting, subdomains, monetization features, JSON/CSV export endpoints (schema is designed to allow them later).

## 3. Information Architecture (three layers)

- **Layer A — Structured Data:** /models, /companies, /agents, /api, /pricing, /benchmarks, /technology(also knowledge)
- **Layer B — Knowledge:** /technology, /guides, /comparisons
- **Layer C — Original Intelligence:** /research, /news (secondary)

Database pages answer *What is known?* Editorial pages answer *What does it mean?* Never mix the two on one page without clear separation.

## 4. URL Map

```
/                        Homepage (hero, explorer teasers, latest updates, research)
/models                  Model Explorer (filterable table)
/models/{model_id}       Model page
/companies               Company index
/companies/{company_id}  Company page
/agents                  Agent index
/agents/{agent_id}       Agent page
/api                     API database index
/api/{provider_id}       API detail page
/pricing                 Pricing Explorer (comparison table)
/pricing/{provider_id}   Provider pricing page (with history)
/benchmarks              Benchmark database index
/benchmarks/{benchmark_id} Benchmark page
/technology              Technology knowledge base index
/technology/{slug}       Technology page
/comparisons             Comparison index
/comparisons/{a}-vs-{b}  Comparison page
/guides                  Guides index
/guides/{slug}           Guide page
/research                Original research index
/research/{slug}         Research article
/news                    News index (secondary)
/news/{slug}             News item
/about                   About (mission, method, sources policy)
```

Stable IDs: `model_id`, `company_id`, `agent_id`, `provider_id` are lowercase-hyphen strings stored in frontmatter; never display names. URL = content collection filename.

## 5. Content Collections (schemas detailed in DATA_SCHEMA.md)

| Collection | Directory | Route |
|---|---|---|
| models | src/content/models | /models/{id} |
| companies | src/content/companies | /companies/{id} |
| agents | src/content/agents | /agents/{id} |
| apis | src/content/apis | /api/{id} |
| pricing | src/content/pricing | /pricing/{provider_id} |
| benchmarks | src/content/benchmarks | /benchmarks/{id} |
| technologies | src/content/technologies | /technology/{slug} |
| comparisons | src/content/comparisons | /comparisons/{a}-vs-{b} |
| guides | src/content/guides | /guides/{slug} |
| research | src/content/research | /research/{slug} |
| news | src/content/news | /news/{slug} |

Each collection: typed Zod schema + a source block (see SOURCE_POLICY.md) + `last_verified` + `sources`.

## 6. Entity Graph (relationships)

```
model      → company (provider), apis, pricing, benchmarks, technologies, agents, comparisons, research
company    → models, agents, apis, open_source_projects, related_entities
agent      → company, underlying_models, technologies (framework), comparisons
api        → provider, models served, pricing
pricing    → provider, models, history
benchmark  → models, source_type
technology → models, companies, guides, research
comparison → both entities, related research
research   → all entities mentioned
```

Implemented as frontmatter reference fields (arrays of stable IDs) resolved at build time via `getCollection()` + map lookups. Internal links are semantic (contextual anchors on entity pages).

## 7. Page Templates & Components

Templates: ModelPage, CompanyPage, AgentPage, APIDetailPage, PricingPage, BenchmarkPage, TechnologyPage, ComparisonPage, GuidePage, ResearchPage, NewsPage, HomePage.

Components (src/components/):
- `ModelCard`, `CompanyCard`, `AgentCard` — entity cards with key facts
- `PricingTable`, `BenchmarkTable`, `ComparisonTable` — semantic HTML tables (accessible, crawlable)
- `SourceBadge` — source tier + link + published date
- `LastVerified` — last_verified date + staleness styling
- `EntityLinks` — related-entity link strip
- `ModelExplorer` — filterable model table (provider, family, reasoning/coding/vision/audio, context, open weight, license, API, price range)
- `PricingExplorer` — comparison table with normalized prices, source + last-verified columns
- `ResearchCard` — editorial card
- `DataUpdateHistory` — change history block where present

## 8. Evidence System (cross-cutting)

Every important factual data point carries: `value`, `source`, `source_type` (official / academic / benchmark / industry_media / community / independent), `published_date`, `last_verified`, `confidence` (high / medium / low / estimate). See SOURCE_POLICY.md.

Claim classification used in editorial content: FACT / VENDOR CLAIM / INDEPENDENT FINDING / ANALYSIS / INTERPRETATION / ESTIMATE / UNCERTAINTY.

## 9. Design System

Professional, technical, data-centric, editorial. NO generic AI gradients, neon, robot illustrations, stock AI imagery, consumer-chatbot aesthetics. Palette: neutral light theme, one restrained accent; dense but legible data tables; clear typography hierarchy. Feels like an industry intelligence / research database.

## 10. Performance Rules

- Static generation (Astro) → HTML-first pages; JS only for explorers (progressive enhancement; table content is server-rendered HTML, filter script narrows client-side)
- Semantic HTML (article, table, figure, dl), responsive tables, minimal fonts, no heavy assets
- Core Web Vitals target: LCP < 2.5s, no layout shift, no render-blocking JS

## 11. Phases (see master prompt §55)

- Phase 0 ✅ audit (greenfield — done)
- Phase 1 — architecture (this doc set) + scaffold + schemas + templates + components (no mass content)
- Phase 2 — database: controlled number of high-quality verified records (initial: ~10-15 models, ~8 companies, ~6 agents, pricing for main providers, key benchmarks)
- Phase 3 — entity graph wiring + internal linking
- Phase 4 — Model Explorer + Pricing Explorer (functional)
- Phase 5 — content: guides, comparisons, technology pages, original research (via deep-research-writer + quality-gate)
- Phase 6 — SEO/GEO/AIO audit pass
- Phase 7 — automation: Firecrawl discovery, change detection, update proposals (never auto-publish critical data)
- Phase 8 — continuous intelligence cadence

## 12. Repository & Delivery

- Repo: `martinxionbiotech-max/China-AI-Hub` (public, main) — user creates repo (agent has no createRepository scope), then Cloudflare Pages links it
- Local: `projects/china-ai-hub/`
- Docs: `docs/` (this folder) — read by future Codex/OpenClaw agents before any change
- Build: `npm install && npm run build` → `dist/`

## 13. Maintenance Contract (for future agents)

1. Read `docs/` before changing anything.
2. Never overwrite entity data without source verification; propose updates, keep history.
3. Stable IDs are immutable; renames are new entities linked via `aliases`.
4. Every published entity page must pass its data quality gate (DATA_SCHEMA.md §14).
5. Every editorial page must pass the originality test (ORIGINAL_RESEARCH_GUIDE.md §4).
6. Build must be green before any push.
