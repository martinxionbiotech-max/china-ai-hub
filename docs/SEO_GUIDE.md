# SEO_GUIDE.md — China AI Hub

Optimize for Google Search, Google AI Overviews, ChatGPT, Gemini, Perplexity, and other AI search systems. Primary levers: Entity SEO, Semantic SEO, Topical Authority, Structured Data, Original Research, Comparison Intent, Long-Tail Search, Data Utility, First-Party Evidence, Knowledge Graph.

## 1. Hard rules

- No keyword stuffing. No thin programmatic pages. No fake ratings/reviews/aggregateRating.
- Programmatic pages allowed only when: real data, genuine utility, meaningful entity, complete page, unique structured info, source attribution, internal links — and not "one template + changed keyword".
- Never generate thousands of low-value model pages.

## 2. Title & meta conventions

- Title: `{Entity} | China AI Hub` for entities; `{Topic} | China AI Hub` for editorial. Keep ≤ 60 chars where possible.
- Meta description: factual, unique, ≤ 160 chars, includes the core fact (e.g. context window, price) when stable.
- Canonical: self-referencing absolute URL on every page. `site` = https://chinaaihub.com.

## 3. Search intent clusters (build content around these)

- **Model:** "DeepSeek V4 Pro" / "…API" / "…pricing" / "…context window" / "…benchmark"
- **Comparison:** DeepSeek vs Qwen, DeepSeek vs Kimi, Qwen vs GLM, Kimi vs MiniMax
- **Pricing:** Chinese AI API pricing, {provider} API pricing
- **Agent:** Chinese AI agents / coding agents / browser agents / research agents
- **Technology:** Chinese reasoning models / open-weight models / agent frameworks / AI infrastructure

## 4. Schema.org mapping

| Entity | Type |
|---|---|
| Company | Organization |
| Articles / guides / comparisons | Article, TechArticle; NewsArticle only when news |
| Software/model entities | SoftwareApplication / Product — only where semantically justified |
| Comparison tables | ItemList where appropriate |
| Site identity | WebSite + Organization in global head |

Never invent Schema.org properties. Never create fake reviews or unsupported aggregateRating.

## 5. Internal linking (semantic, not keyword-stuffed)

Every entity page links: model → company, API, pricing, benchmarks, agents, technologies, comparisons, research (as applicable). Contextual anchors; no repeated identical anchor text stacking; relationship-driven (see ARCHITECTURE.md §6).

## 6. AI-search readability (GEO/AIO)

Important pages contain: clear H1 → concise independently-understandable definition → key-fact table → detailed explanation → source attribution → related entities → last-verified date → original analysis where appropriate.

- Semantic HTML: article, section, table with caption + th, dl for fact lists.
- Facts in short declarative sentences; tables carry the data; no stuffed summaries.
- Every important fact: inline source + date (AI systems surface these).

## 7. Technical

- sitemap.xml: all indexable pages, absolute URLs on chinaaihub.com
- robots.txt: allow all + AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended decisions documented)
- Fast static HTML, minimal JS (explorers degrade gracefully), good Core Web Vitals
- Clean semantic URLs (no /blog/post123, no query-string routes, no date slugs)

## 8. Indexability checklist (Phase 6 audit, per page type)

Indexable ✔ / noindex ✔ / canonical ✔ / title ✔ / meta description ✔ / H1 unique ✔ / heading hierarchy ✔ / schema valid ✔ / sitemap entry ✔ / robots allowed ✔ / internal links ✔ / no duplicate near-copies ✔

## 9. What we do NOT do

- Buy links, spam directories, content farms
- Multi-domain doorway sites (single domain in Phase 1)
- Fake E-E-A-T signals (no invented authors, no fake "expert team")
- Keyword-density tricks
