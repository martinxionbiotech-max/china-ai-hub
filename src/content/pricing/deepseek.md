---
image: "/images/ai/pricing-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: deepseek
currency: USD
billing_mode: pay_as_you_go
models:
  - model: deepseek-v4-1-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.6
    cached_input_price_per_1m: 0.003
    notes:
      - "Off-peak rates (row price)"
      - "Peak = 2x: $0.30 / $1.20 / $0.006 cache hit"
      - "Concurrency limit: 2500"
      - "No batch pricing listed"
    official_source: https://api-docs.deepseek.com/quick_start/pricing
  - model: deepseek-v4-pro
    input_price_per_1m: 0.66
    output_price_per_1m: 1.98
    cached_input_price_per_1m: 0.022
    notes:
      - "Off-peak rates (row price)"
      - "Peak = 2x: $1.32 / $3.96 / $0.044 cache hit"
      - "Concurrency limit: 500"
      - "Deprecation announced 2026-09-10 (service continues per change log)"
    official_source: https://api-docs.deepseek.com/quick_start/pricing
price_history:
  - model: deepseek-v4-pro
    field: billing_structure
    old_value: "Flat pricing"
    new_value: "Peak/off-peak pricing; off-peak = 50% of peak"
    effective_date: "2026-08-16"
    source: https://api-docs.deepseek.com/updates
  - model: deepseek-v4-1-flash
    field: api_pricing
    old_value: "V4-Flash list pricing (model retired)"
    new_value: "Reduced V4.1-Flash pricing"
    effective_date: "2026-09-10"
    source: https://api-docs.deepseek.com/updates
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek API docs — Models & Pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek-V4.1-Flash release announcement
    source_url: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
    source_type: official
    published_date: "2026-09-10"
    last_verified: "2026-09-20"
    confidence: high
---

**Short answer.** DeepSeek is the only Chinese provider in this database with time-of-day pricing: the listed rate is the off-peak rate, and peak hours cost exactly double. Its second distinguishing feature is the deepest cache discount in the set — a cache hit on V4.1-Flash costs $0.003 per 1M tokens, 2% of the input price.

## The two levers

| Lever | V4.1-Flash | V4-Pro |
|---|---|---|
| Input / output (off-peak) | $0.15 / $0.60 | $0.66 / $1.98 |
| Input / output (peak) | $0.30 / $1.20 | $1.32 / $3.96 |
| Cache hit | $0.003 | $0.022 |
| Cache as % of input | **2%** | **3.3%** |
| Concurrency limit | 2,500 | 500 |

Output costs 4x input on Flash and 3x on Pro, which is low by market standards — the output penalty that makes long generations expensive elsewhere is milder here.

## Time-of-day pricing changes architecture

Peak is 2x, and the definition of peak follows Beijing business hours. For a product serving European or American users, that means the cheap window overlaps with your own working day: a batch job scheduled for 02:00 CET runs at DeepSeek's 09:00 peak.

The practical consequence is that DeepSeek's cheap rate is available to asynchronous workloads and expensive for synchronous ones. Pipelines that can queue — document processing, evaluation runs, data labelling — get the off-peak rate almost for free. Chat products cannot.

## Caching is the real price

At 2% of input, a cache hit is close to free. An agent loop that re-reads the same 40K-token context twenty times pays 40K × input once and 40K × 0.02 for the remaining nineteen passes. For retrieval-heavy or long-system-prompt workloads, the effective price is a small fraction of the list rate.

The catch is that caching only helps when the prefix is stable. Prompts that reshuffle context on every call get no benefit, and there is no batch discount to fall back on: this provider lists none.

## Our view

**DeepSeek's pricing is designed for batch and agent workloads, not chat.** Off-peak discounts and near-free cache hits reward exactly the two patterns that dominate production AI — queued processing and repeated context — while peak pricing charges a premium for interactive use.

**The cache ratio is the number to model, not the headline price.** A 2% cache hit can make a "cheap" competitor at $0.10 input more expensive than DeepSeek at $0.15 for any workload with a stable prefix.

**No batch tier is a real gap.** Competitors offer 50% batch discounts; DeepSeek offers time-of-day instead. If your workload can be neither queued to off-peak nor cached, you pay full rate.

**Concurrency limits belong in the same table as price.** 500 concurrent requests on V4-Pro is a hard ceiling that changes what you can build, and it is invisible in a per-token comparison.
