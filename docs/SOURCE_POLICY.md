# SOURCE_POLICY.md — China AI Hub

The evidence system is a core product feature. Every important factual claim must be traceable.

## 1. Source hierarchy

| Tier | Type | Examples |
|---|---|---|
| L1 | Primary sources | Official documentation, official model cards, official API pricing pages, official technical papers, official GitHub, official announcements |
| L2 | High-quality technical sources | Academic papers, benchmark organizations, cloud provider documentation, independent technical research |
| L3 | Major industry media | Reuters, Bloomberg, Financial Times, TechCrunch, specialist publications |
| L4 | Community | GitHub discussions, Hugging Face, Reddit, developer communities |

**Rules:**
- L4 alone can never carry a critical fact (pricing, license, context window, benchmark score).
- L1 is required for: pricing, API availability, license, official release dates.
- Prefer the most primary source available; when a fact is first seen in media, trace it to its L1 source before publishing.

## 2. Source record format (attached to every entity and to editorial pages)

```
source_name: DeepSeek API Docs
source_url: https://api-docs.deepseek.com/quick_start/pricing
source_type: official          # official|academic|benchmark_org|cloud_doc|industry_media|community|independent
published_date: 2026-05-01
last_verified: 2026-09-20
confidence: high               # high|medium|low|estimate
```

## 3. Confidence levels

- **high** — current L1 source directly states the fact
- **medium** — L2 source, or L1 source older than 6 months for a dynamic field
- **low** — L3/L4 only, or conflicting sources
- **estimate** — derived value; must be labeled ESTIMATE everywhere it appears

## 4. Source conflict handling (mandatory sequence)

1. Never silently pick one side.
2. Identify the conflicting claims.
3. Identify the source of each claim.
4. Check source dates.
5. Check model versions (many "conflicts" are version drift).
6. Check region/pricing conditions.
7. Explain likely reasons for the difference.
8. Preserve uncertainty when it cannot be resolved.

Output format in editorial text: "Source A (date) reports X; source B (date) reports Y. The difference likely reflects … We treat this as uncertain."

## 5. Last Verified system

- Dynamic fields (pricing, API availability, context, benchmarks, status, license) display `Last verified: YYYY-MM-DD` wherever shown.
- Staleness display: < 30 days = current; 30–90 days = "may be outdated"; > 90 days = prominent "verify before relying" styling.
- Verification = an agent actually re-fetched the L1 source and confirmed the value, not a guess.

## 6. Verification workflow (per update)

1. Open the official source URL(s).
2. Extract the exact statement (quote or structured value).
3. Compare with current stored value.
4. If same → update `last_verified`.
5. If different → create a change proposal (UPDATE_PIPELINE.md), record old→new + effective date + source, do not silently overwrite history for pricing/benchmarks.
6. If source unavailable → do not change data; mark `verification_failed: date`.

## 7. What can never be published

- Fabricated prices, benchmarks, parameters, context windows, capabilities, licenses, release dates, company info, customer counts, market share
- "Best model" claims from a single benchmark
- Vendor-reported scores presented as independent
- Anything sourced only from an unreliable community post without further verification

## 8. Citation display

- Entity tables: each row's source shown via SourceBadge (tier icon + name + link + date).
- Editorial: inline bracketed source links or footnote-style source list; China AI Hub View is clearly labeled as analysis, not fact.
- Research articles end with a Sources section listing every L1/L2/L3 source used.
