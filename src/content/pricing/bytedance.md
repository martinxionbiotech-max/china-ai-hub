---
image: "/images/ai/pricing-bytedance.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: bytedance
currency: CNY
region: china
billing_mode: pay_as_you_go
models:
  - model: doubao-seed-2-1-pro
    input_price_per_1m: 6.0
    output_price_per_1m: 30.0
    cached_input_price_per_1m: 1.2
    notes:
      - "Standard tier (row price)"
      - "Low-priority tier ~50%: 3.00/15.00"
      - "Cache storage: 0.017 CNY per 1M tokens/hour"
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
  - model: doubao-seed-evolving
    input_price_per_1m: 6.0
    output_price_per_1m: 30.0
    cached_input_price_per_1m: 1.2
    notes:
      - "Standard tier (row price)"
      - "Pricing row matches Doubao Seed 2.1 Pro"
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
  - model: doubao-seed-2-1-turbo
    input_price_per_1m: 3.0
    output_price_per_1m: 15.0
    cached_input_price_per_1m: 0.6
    notes:
      - "Standard tier (row price)"
      - "Low-latency tier: 6.00/30.00"
      - "Low-priority tier: 1.50/7.50"
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
last_verified: "2026-09-20"
sources:
  - source_name: Ark official model pricing
    source_url: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**Short answer.** ByteDance (Volcano Engine) prices in CNY only, which makes it the one provider in this database where the dollar cost is a currency decision as much as a pricing one. Its structure also includes two features no competitor has: a low-priority tier at roughly half price, and hourly billing for cache storage.

## The ladder (CNY per 1M tokens)

| Model | Input | Output | Out/in | Cache | Low-priority |
|---|---|---|---|---|---|
| Doubao Seed 2.1 Pro | ¥6.00 | ¥30.00 | 5.00 | ¥1.20 (20%) | ~¥3.00 / ¥15.00 |
| Doubao Seed Evolving | ¥6.00 | ¥30.00 | 5.00 | ¥1.20 | — |
| Doubao Seed 2.1 Turbo | ¥3.00 | ¥15.00 | 5.00 | ¥0.60 (20%) | — |

At an indicative 7.1 CNY/USD, Pro works out to roughly $0.85 input / $4.23 output — competitive with the mid-tier flagships, and cheaper than Kimi K3 by a factor of three on input.

## The 5:1 output ratio is the steepest here

Every ByteDance model prices output at 5x input. For generation-heavy workloads — long reports, code synthesis, multi-turn agents — that ratio dominates the bill far more than the input rate. A model that looks cheap on input can be the most expensive option per completed task.

## Cache storage is billed hourly

¥0.017 per 1M tokens per hour is a small number that compounds: a 1M-token cache held for a month costs about ¥12, roughly two full re-reads of the same context. For long-lived system prompts this is fine; for caches created per session and forgotten, it is pure waste.

This is the only provider here that charges for cache *residency* rather than cache *reads*, and it changes the discipline: you must expire caches, not just create them.

## Low-priority is batch by another name

The ~50% low-priority tier is the closest thing to a batch discount in this database, but it is a scheduling class rather than an API mode: work is served when capacity allows, with no latency guarantee. For offline evaluation and data processing it is the cheapest option here; for anything user-facing it is unusable.

## Our view

**CNY-only pricing is a real procurement cost.** It creates FX exposure, complicates budgeting, and puts the invoice in a currency your finance system may not handle. The discount versus international providers has to cover that friction.

**The 5:1 output ratio is the fact that decides workloads.** Pro is competitive for input-heavy tasks (RAG, classification, extraction) and expensive for output-heavy ones. Most buyers compare input prices and get this backwards.

**Hourly cache storage is the most under-appreciated charge in Chinese AI pricing.** It is small per token-hour and large per forgotten cache. Any team using long system prompts should model it explicitly.

**Low-priority is the best batch substitute in the market — if your pipeline can wait.** Half price for offline work is a better deal than a 50% batch discount with a fixed turnaround, provided you can tolerate indefinite queueing.
