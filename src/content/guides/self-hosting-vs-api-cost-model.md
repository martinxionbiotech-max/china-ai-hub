---
title: "Self-Hosting vs API: A Cost Model That Survives Utilisation"
description: "A break-even model for Chinese open-weight models: GPU throughput, utilisation and the two numbers that decide whether to self-host or buy tokens."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 7
related_entities:
  - qwen3.8-2.4t-a95b
  - glm-5.3-flash
  - minimax-m3
sources:
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
  - source_name: "Z.ai platform documentation"
    source_url: "https://docs.z.ai/"
    source_type: official
---

**The short version.** Self-hosting beats an API when your utilisation is high enough that the GPU's idle time is small. Below roughly 30% utilisation, a rented API almost always wins; above roughly 75%, owning hardware usually does. The number that decides it is not the price of the GPU — it is the fraction of the month it is generating tokens.

## The model, in one formula

```
cost per 1M output tokens = monthly infrastructure cost ÷ (tokens per second × 3,600 × 730 × utilisation ÷ 1,000,000)
```

Three inputs matter: throughput, utilisation and fully-loaded cost. Everything else — model quality, licence, ops burden — decides whether self-hosting is *allowed* and *wise*, not whether it is cheaper.

## Worked example (assumptions labelled)

Take a 32B open-weight model served on one H100 80GB at FP8:

| Assumption | Value | Note |
|---|---|---|
| Aggregate output throughput | 1,500 tokens/s | At batch 32; measure yours, do not trust a vendor chart |
| Hours per month | 730 | — |
| Cloud GPU price | $2.50/hour | Rental, on-demand |
| Purchase price | $25,000 | Server, amortised over 36 months |
| API comparison price | $0.60 per 1M output | Mid-range Chinese model, international list |

**Rented GPU, $1,825/month:**

| Utilisation | Tokens/month | Cost per 1M | API cost for same volume |
|---|---|---|---|
| 15% | 0.59B | **$3.09** | $355 (API 5x cheaper) |
| 30% | 1.18B | **$1.54** | $710 (API 2.6x cheaper) |
| 50% | 1.97B | **$0.93** | $1,183 (API 1.5x cheaper) |
| 80% | 3.15B | **$0.58** | $1,892 (self-host breaks even) |

**Owned hardware, $694/month amortised (excluding power, space, staff):**

| Utilisation | Cost per 1M |
|---|---|
| 15% | $1.17 |
| 30% | $0.59 |
| 50% | $0.35 |
| 80% | $0.22 |

Break-even against a $0.60 API sits at roughly **29% utilisation** for owned hardware and roughly **77%** for rented hardware.

## What the model leaves out

Four omissions that change the answer:

1. **People.** Someone has to run the inference stack. Even at 0.25 FTE, that is $2,000–4,000/month — more than the GPU at low utilisation.
2. **Idle capacity for peaks.** You provision for the 95th percentile, so average utilisation is lower than peak. A system sized for a launch spike may run at 10% most of the month.
3. **Quality gap.** A 32B open model is not a frontier model. If the workload needs the frontier, the comparison is not self-hosting versus API; it is self-hosting *plus* an API for the hard 10%.
4. **Engineering time to first token.** Getting from weights to a production endpoint with batching, caching and observability is weeks, not days.

## When self-hosting wins anyway

Cost is not the only reason to own the inference:

- **Data cannot leave your environment.** Regulated industries, or a contract that forbids sub-processors.
- **Latency and availability.** No dependency on a vendor's rate limits or regional outage.
- **Customisation.** Fine-tuning, constrained decoding, custom tokenisers.
- **Licence terms that permit it** — Apache-2.0 and MIT models, not the custom community licences.

Note the last point: several Chinese open-weight models carry licences with revenue triggers or non-commercial restrictions. Self-hosting is only an option if the licence allows your use.

## A decision procedure

1. Measure output tokens per month from your current API bill. Do not estimate.
2. Measure or benchmark throughput for the specific model and hardware you would buy.
3. Compute utilisation as `tokens per month ÷ theoretical maximum`.
4. Compare the cost per 1M at *that* utilisation, not at 100%.
5. Add people, peaks and the quality gap.
6. If the answer is close, stay on the API — optionality has value.

## Our view

**Most teams that self-host for cost reasons should not.** At realistic utilisation — 15–30% for a single product — a rented GPU costs two to five times the API. The teams that benefit are those with steady, high-volume generation: batch pipelines, data labelling, synthetic data, high-traffic consumer products.

**Utilisation is the variable nobody models, and it is the one that decides the answer.** A GPU that sits idle is the most expensive way to buy tokens. If your traffic is spiky, the API is buying insurance as much as compute.

**The real comparison is not "our GPU vs their price" — it is "our GPU plus an ops engineer vs their price".** Once people are included, the break-even utilisation roughly doubles.

**Hybrid is usually correct.** Route the high-volume, low-difficulty 80% to a self-hosted open model and the hard 20% to an API. That architecture captures most of the cost benefit without pretending a 32B model is a frontier one.

## What is uncertain

- Throughput figures are workload-dependent; your tokens-per-second will differ.
- GPU rental prices move with supply.
- Licence terms for several Chinese open-weight models are still being clarified by their authors.

## Next

[A vendor risk register](/guides/chinese-ai-vendor-risk-register/) — the last chapter, and the one that keeps the others honest.
