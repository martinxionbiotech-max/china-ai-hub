---
image: "/images/ai/guides-how-to-choose-a-chinese-ai-model.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "Choosing a Chinese AI Model by Workload"
author: "SinoAI Hub Research Team"
description: "A selection method that starts from the task, not the leaderboard: five filters in order, the six workloads that differ, and when a cheap model is the wrong answer."
published_date: "2026-09-22"
updated_date: "2026-11-05"
pillar: model-selection-by-workload
order: 0
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3-flash
  - qwen3.8-flash
  - minimax-m3
  - kimi-k3
  - qwen3.8-max
  - doubao-seed-2-1-pro
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "China AI Hub — Pricing database"
    source_url: "https://sinoaihub.com/pricing/"
    source_type: independent
  - source_name: "DeepSeek API pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
  - source_name: "Z.ai — Pricing overview"
    source_url: "https://docs.z.ai/guides/overview/pricing"
    source_type: official
---

**The short version.** Model selection fails when it starts with a leaderboard. It works when it starts with the shape of the task: how much context it needs, how much output it produces, whether it must be self-hosted, and what a mistake costs. Those four questions eliminate most of the market before price is even discussed.

This pillar is the method, applied to the workloads buyers actually run.

## Why workload first

Two models with the same benchmark score can differ by 20x in cost per completed task, because cost depends on the ratio of input to output, cache behaviour and context length — none of which a benchmark measures.

Three models in this database sit at the same $0.15 input price:

| Model | Input | Output | Output/input | Cache hit |
|---|---|---|---|---|
| Qwen3.8-Flash | $0.15 | $0.47 | 3.13 | $0.016 (10.7%) |
| GLM-5.3-Flash | $0.15 | $0.50 | 3.33 | $0.03 (20%) |
| DeepSeek-V4.1-Flash | $0.15 | $0.60 | 4.00 | $0.003 (2%) |

At equal input price, the completed-task cost differs by 28% between the cheapest and most expensive output rate — and by far more once caching or time-of-day pricing applies. Choosing on input price is choosing on the smaller half of the bill.

## The five filters, in order

**1. Hard constraints.** Self-hosting requirement, data residency, licence terms, context ceiling. These eliminate options outright and cost nothing to check. A model you cannot legally deploy is not a candidate, regardless of quality.

**2. Task shape.** Input-heavy or output-heavy? Single-shot or multi-turn? Stable prefix or reshuffled context? This determines which pricing structure fits before any vendor is compared.

**3. Evidence.** What has actually been measured on a task like yours, by whom, under what harness. Vendor benchmarks rarely answer this; a 50-item eval on your own data usually does.

**4. Cost per completed task.** Not per token. Include retries, failed outputs and the human review a weaker model requires.

**5. Exit.** Can you switch in a week? Licence portability, API compatibility and provider concentration decide how much the first four filters are worth.

Most comparisons skip straight to step 4 and then argue about step 3, which is why they end in a tie.

## Context and output are different ceilings

Eleven tracked models list a 1M-token input window, but maximum output varies by almost an order of magnitude:

- **Kimi K3** — 1,048,576 output (the full window).
- **DeepSeek-V4-Pro / V4.1-Flash** — 393,216.
- **Doubao Seed 2.1 Pro** — 262,144.
- **Qwen3.8-Max / GLM-5.3** — 131,072.
- **MiniMax M3** — not publicly disclosed.

For long-form generation, whole-repository rewriting or multi-document synthesis, the output ceiling binds before the input window does. A 1M-context model that stops generating at 131K is a 131K model for writing tasks.

## The six workloads that actually differ

| Workload | Binding constraint | Where it usually lands |
|---|---|---|
| Document extraction | Structured-output reliability, cost per document | Flash tier, high volume, cheap output |
| Coding agents | Context window, tool-calling reliability | Mid-tier coding models, 262K–1M |
| Chinese customer support | Tone, compliance, latency | Cheap tier with strong Chinese, cached prompts |
| Long-document analysis | Effective context depth, price per long call | 1M-context models, or chunking |
| High-volume classification | Cost per million tokens | Cheapest flash, batch or off-peak |
| Research / browsing agents | Tool use, persistence, harness | Mid-tier with tool calling, plus orchestration |

Each chapter below takes one shape and works through it. None concludes "buy the flagship", which is the point.

## What the tiers look like

- **$0.15 input tier** — Qwen3.8-Flash, GLM-5.3-Flash, DeepSeek-V4.1-Flash; output $0.47–$0.60.
- **$0.30–$1.40 tier** — MiniMax M3 ($0.30/$1.20), DeepSeek-V4-Pro ($0.66/$1.98), GLM-5.3 ($1.40/$4.40).
- **$2.00+ tier** — Qwen3.8-Max ($2.00/$6.00), Kimi K3 ($3.00/$15.00), Doubao Seed 2.1 Pro (¥6/¥30, roughly $0.85/$4.23).

The capability gap between the first and second tier is smaller than the price gap in most published results; the gap between the second and third is task-specific. That asymmetry is where selection judgement lives.

## Selection matrix

A starting filter, not a ranking — verify price and capability on the model page before committing.

| Requirement | Best-documented fit | Why (verified field) |
|---|---|---|
| Lowest cost, budget tier | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) / [GLM-5.3-Flash](/models/glm-53-flash/) | $0.15/1M input; $0.50–$0.60 output |
| Lowest flagship cost | [MiniMax-M3](/models/minimax-m3/) | $0.30/$1.20 with a 1M window |
| Longest output | [Kimi K3](/models/kimi-k3/) | 1,048,576-token output ceiling |
| Permissive self-hosting | [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) | MIT licence, 1M context |
| Vision + video + structured output | [Qwen3.8-Max](/models/qwen38-max/) | Lists vision, video and structured output |
| Computer use (model) | [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) | Lists computer use |
| Multi-region enterprise API | [Model Studio](/api/model-studio/) | Six regions, documented rate limits |

## Our position

**Start at the cheapest tier that passes your eval, and move up only on a measured failure.** The default direction of travel in procurement is downward — teams over-buy "just in case" and never re-test. At a 9–20x spread between tiers, over-buying is usually the largest avoidable cost in an AI budget.

**The binding constraint is almost never capability.** In practice it is context length, self-hosting or a licence clause. Teams spend weeks comparing scores and five minutes checking whether the model may be deployed in their jurisdiction — which is backwards.

**Two models beat one.** A routing layer that sends easy traffic to a flash tier and hard traffic to a mid-tier model typically cuts spend by 70–80% with no measurable quality loss. A single-model architecture is a simplicity choice, not an optimisation.

**Every chapter ends in an eval, because selection without measurement is preference.** The last chapter is the method for building that eval in an afternoon.

## The chapters

1. [Choosing by price](/guides/choosing-by-price/) — cost per completed task, cache and tier structure.
2. [Long-context selection](/guides/long-context-model-selection/) — what 1M tokens really deliver.
3. [Multimodal selection](/guides/multimodal-model-selection/) — vision, video and computer use.
4. [Coding models](/guides/choosing-a-coding-model/) — evidence over claims.
5. [Agents](/guides/choosing-an-agent/) — models, tools and MCP.
6. [Document extraction](/guides/choosing-a-model-for-document-extraction/) — structured output at volume.
7. [High-volume classification](/guides/choosing-a-model-for-classification/) — cost per million tokens.
8. [Build a 50-item eval](/guides/build-your-own-model-eval/) — the method that settles it.
