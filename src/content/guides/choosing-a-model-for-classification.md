---
title: "Choosing a Model for High-Volume Classification"
description: "Millions of short documents and one label each: why input price decides the bill, how batching and caching change the maths, and when fine-tuning beats a bigger model."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: model-selection-by-workload
order: 7
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3-flash
  - qwen3.8-flash
  - minimax-m3
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "China AI Hub — Pricing database"
    source_url: "https://sinoaihub.com/pricing/"
    source_type: independent
---

**The short answer.** Classification is the simplest workload to cost and the easiest to over-buy. One label per document means output is almost free and input is everything, so the cheapest tier with acceptable accuracy wins by a wide margin — and the levers that matter are batching, off-peak scheduling and label taxonomy, not model size.

## The cost shape

A typical ticket or review is 500–1,500 tokens in and 1–5 tokens out. Take 1,000 tokens in and 3 out:

| Model | Input $/1M | Cost per 1M docs | Output cost | Total |
|---|---|---|---|---|
| DeepSeek-V4.1-Flash | $0.15 | $150 | $1.80 | **$152** |
| GLM-5.3-Flash | $0.15 | $150 | $1.50 | **$152** |
| MiniMax-M3 | $0.30 | $300 | $3.60 | **$304** |
| GLM-5.3 | $1.40 | $1,400 | $13 | **$1,413** |
| Qwen3.8-Max | $2.00 | $2,000 | $18 | **$2,018** |

The spread between the cheapest and the flagship is **13x**, and the output column is rounding error in every row. This is the one workload where the advertised input price is genuinely the whole story.

## Three levers bigger than model choice

**1. Batch or off-peak.** Zhipu and Alibaba discount batch inference by 50%; DeepSeek halves its price outside peak hours. Classification is the ideal batch workload — nobody needs a label in 300ms — so this lever alone can halve the bill.

**2. Cache the instructions, not the documents.** Classification prompts have a stable system message and a variable document. Providers that cache the prefix let you pay cache-hit rates on the instructions; the document is always a cache miss. On a 1,000-token request with a 400-token instruction block, that is a 20–40% saving depending on the provider's cache depth.

**3. Fewer tokens per document.** Truncate to the first 400 tokens for routing decisions; send the full text only to the ambiguous cases. A two-stage classifier (cheap gate, expensive review) routinely cuts spend by 60% at equal accuracy.

## Accuracy is a taxonomy problem first

Most classification failures are not model failures. They are label definitions that overlap:

- "Billing issue" and "refund request" describe the same ticket from different angles.
- "Angry customer" is a sentiment, not a topic, and it correlates with everything.
- Labels that require world knowledge the model does not have (account status, order history) should be filtered out before the model sees the text.

A tidy taxonomy with five mutually exclusive labels will outperform a flagship model on a messy one with twenty overlapping labels. Fix the labels first; then compare models.

## When fine-tuning wins

Prompting five labels with examples works well up to a point. Three situations justify fine-tuning an open-weight model:

1. **Very high volume** — above roughly 10M documents a month, a fine-tuned small model on owned GPUs can beat any API on cost.
2. **Domain vocabulary** that the base model misreads — internal product codes, legal citations, dialect.
3. **Strict latency** — a 7B model on local hardware is faster than a network round trip.

Everything else should stay on prompts, because fine-tuning adds a training pipeline, an evaluation harness and a model you now have to maintain.

## Calibration and abstention

A classifier that is 92% accurate but never says "unsure" is worse than one at 88% that flags its 10% least-confident cases for human review. Ask for a confidence score or a logprob, set a threshold, and route the tail to a human queue — the economics are almost always better than pushing accuracy up with a bigger model.

Not every provider exposes logprobs. Where it does not, ask for a structured output with a `confidence` field and treat it as a weak signal, not a probability.

## Our view

**Classification is where over-buying is most common and least defensible.** Teams route millions of short documents through a flagship because "quality matters", when a flash tier with a clean taxonomy would match it at one-thirteenth the cost — and the difference would pay for the human review queue several times over.

**Batching is worth more than any model upgrade.** A 50% batch discount on the cheapest tier beats a 13x cheaper model that is not batched only if the taxonomy is broken; in practice, batching plus a flash tier is the cheapest defensible configuration.

**The taxonomy is the model.** Every hour spent merging overlapping labels saves more accuracy than every hour spent benchmarking. This is the least glamorous and highest-return work in the pipeline.

**Fine-tuning is a volume decision, not an accuracy decision.** Below 10M documents a month it rarely pays back the maintenance cost, and above it, the model you fine-tune matters less than the data pipeline that keeps it current.

## Next

[Build a 50-item eval](/guides/build-your-own-model-eval/) — the chapter that turns all of this into a decision you can defend.
