---
title: "Build a 50-Item Eval Before You Choose"
description: "A half-day method for settling model selection with your own data: 50 stratified items, a fixed rubric, three metrics and a re-run schedule that keeps the answer honest."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: model-selection-by-workload
order: 8
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3-flash
  - qwen3.8-flash
  - minimax-m3
  - kimi-k3
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "China AI Hub — Benchmarks database"
    source_url: "https://sinoaihub.com/benchmarks/"
    source_type: independent
---

**The short answer.** Fifty labelled examples from your own work, run through every candidate with the same prompt, will beat any public leaderboard for the decision you are actually making. The whole exercise takes half a day, and it is the only comparison that survives a change of vendor, a price cut, or a colleague asking "why this model".

## Why 50

Fifty is enough to separate a 90% model from a 75% one, and small enough that two people can label it in an afternoon. It is not enough to detect a 2-point difference — and that is fine, because 2-point differences do not justify a 13x price gap.

The rule of thumb: **the eval should be able to change your mind.** If every plausible model scores within noise, the decision should fall to cost and constraints, and the eval has done its job by telling you that.

## Step 1: Sample for variety, not for volume

Fifty items, stratified:

| Stratum | Items | Why |
|---|---|---|
| Typical case | 25 | The bulk of production traffic |
| Hard case | 10 | Long inputs, ambiguous labels, messy layouts |
| Edge case | 8 | Empty fields, mixed language, unusual format |
| Adversarial | 4 | Prompt injection, contradictory instructions |
| Trivial | 3 | A sanity check the model must not fail |

Pull them from real history, not from the benchmark. If you do not have history yet, generate 50 from the schema and mark the eval as provisional.

## Step 2: Write the rubric before you see results

Decide what "correct" means per item, in one line each:

- **Exact match** — the extracted field equals the source value.
- **Semantic match** — the label maps to the same category, not the same words.
- **Partial credit** — 3 of 4 fields right; score 0.75.
- **Fatal error** — a hallucinated value where the document had none; score 0 regardless.

Writing the rubric after seeing outputs is how evals become rationalisations.

## Step 3: Fix everything except the model

Same prompt, same temperature (0 where supported), same max tokens, same schema, same validation layer. Pin the model version where the API allows it; record the version string where it does not.

Log for each run: model id, version, date, prompt hash, output, score, latency, tokens in/out, and cost.

## Step 4: Score four things, not one

| Metric | What it catches |
|---|---|
| Accuracy | Overall correctness against the rubric |
| First-pass validity | Share of outputs that parse without retry |
| Cost per item | Tokens × price, including retries |
| p95 latency | Whether the model is usable interactively |

A model that wins on accuracy but fails 12% of parses is not the better model; it is the better model plus an engineering project.

## Step 5: Compute the decision, not the ranking

Take the top two candidates and compute:

```
annual cost = items per year × (cost per item at observed retry rate)
```

Then compare against the accuracy difference in business terms: how many human reviews does a 5-point accuracy gap create, and what does each review cost? In most pipelines the answer is decisive and surprising — a 5-point gap on 100,000 items is 5,000 reviews, which usually dwarfs the token bill either way.

## Step 6: Schedule the re-run

An eval is a snapshot. Re-run it when:

- A candidate ships a new version (Kimi's K2 retirement is a live example).
- A price changes by more than 20%.
- Your own data drifts — new document layouts, new product names.
- Quarterly, whichever comes first.

Keep the items and the rubric under version control. The value of the eval compounds only if the item set is stable enough to compare across time.

## A worked example

A support ticket router, 1,000 tokens in, 1 label out, 200,000 tickets a year:

| Model | Accuracy | First-pass valid | Cost/item | Annual cost |
|---|---|---|---|---|
| Flash tier A | 88% | 97% | $0.00016 | $31 |
| Flash tier B | 89% | 94% | $0.00016 | $33 |
| Mid tier ($0.30 input) | 92% | 99% | $0.00030 | $61 |
| Flagship ($2.00 input) | 93% | 99% | $0.00200 | $404 |

The flagship costs 13x the flash tier for 5 points of accuracy — 14,000 misroutes a year against 24,000, for $373 more in tokens. If a misroute costs $0.10 in human correction, the flagship saves $1,000 and wins. If it costs $0.01, it saves $100 and loses by a wide margin.

**That calculation, not the leaderboard, is the decision.**

## Our view

**Fifty items is the highest-return half-day in an AI project.** It converts an argument about benchmarks into a number your finance team can read, and it is the only artefact that lets you say "we chose this model because" with evidence.

**Most teams should expect the cheap tier to win.** Not always, but often enough that starting from the flagship is backwards. The eval's job is to find the exception, not to justify the default.

**Cost per item must include the retry rate.** A model with 94% parse validity needs a retry layer and an engineer; at 100k items that is real money and real time, and it never appears in a price table.

**Never compare across eval versions.** If you change the rubric or the item set, you have a new eval and no history. Version both, and keep the old run results.

## Back to the pillar

[Choosing a Chinese AI model by workload](/guides/how-to-choose-a-chinese-ai-model/) — the five filters this eval feeds into, and the six workloads it applies to.
