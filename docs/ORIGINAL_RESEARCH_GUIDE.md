# ORIGINAL_RESEARCH_GUIDE.md — China AI Hub

How to produce Layer C content (Original Intelligence): research articles, industry reports, China AI Hub View analyses.

## 1. When to use this workflow

For every substantial editorial page: research articles, major comparisons with analysis, industry reports. Not for entity database pages (those are data + sources).

## 2. Workflow (mandatory order)

```
Research Question
→ Primary Source Collection
→ Evidence Extraction
→ Cross-Source Verification
→ Structured Data Collection
→ Comparison
→ Historical Context
→ Pattern Identification
→ Independent Analysis
→ Original Synthesis
→ Author View
→ Conclusion
→ Fact QA
→ Originality QA
```

**Think first. Do not write immediately.** Establish before writing:
- What is the question?
- What entities are involved?
- What facts are needed?
- What sources are authoritative?
- What data has changed?
- What conflicts exist?

## 3. Tools (this workspace)

- **Research/writing:** `deep-research-writer` v2.1.0 skill (writing engine) → then `quality-gate` v1.0.0 (PASS/CONTINUE/REPAIR/BLOCKED)
- **Chinese sources:** `chinese-web-research` (mandatory for China-side primary sources)
- **Verification:** `source-verification` (source conflicts, claims checking)
- **Competitive landscape:** `competitor-intelligence` (what other sites already cover → avoid duplication, find gaps)
- **Data collection:** `firecrawl-scraper` / `tavily` for fetching official pages
- Live-check official documentation before any factual claim (never from memory).

## 4. Originality QA (pre-publication, from CONTENT_GUIDELINES §4)

Answer all seven questions; publish only if the article could NOT exist by simply rewriting another source.

## 5. Research topic checklist (before starting any topic)

- Is the topic still current? (verify, do not assume the title is accurate)
- What has changed since any prior version of this topic?
- Which entities (models/companies/agents) does it touch? (list IDs for entity graph wiring)
- What primary sources exist? (collect URLs before drafting)
- What is the deliverable: analysis / comparison / explainer / industry research / China AI Hub View?

## 6. Initial research backlog (master prompt §67, first 10)

1. The State of China's AI Models in 2026
2. How Chinese AI Model Pricing Has Changed
3. The Rise of Chinese AI Agents
4. Chinese AI Models and Task Efficiency
5. Open-Weight AI Models in China
6. Chinese AI APIs Compared
7. Chinese AI Coding Models
8. China's Long-Context AI Models
9. Chinese AI Model Deployment Options
10. China AI Benchmark Landscape

(Full 20-topic backlog in master prompt §31.)

## 7. Research article frontmatter requirements

```yaml
title: …
description: …            # ≤160 chars
published_date: …
updated_date: …
research_question: …
related_entities: [deepseek-v4-pro, …]
author_view: true
sources: [ … ]
```

## 8. Citation rules

- Every L1/L2 claim: inline source reference (SourceBadge or bracketed link).
- Sources section at end lists every source used.
- Vendor-reported vs independent explicitly labeled per score.
- China AI Hub View never cites itself as fact; it references the evidence above.

## 9. Failure modes (do not ship)

- Article assembled from five existing articles (no original data work)
- Benchmark table copied from vendor marketing without labels
- "Best model" verdicts from one benchmark
- Interpretation written as fact
- No Limitations and Uncertainty section on a major analysis
- Word count inflation to hit a target
