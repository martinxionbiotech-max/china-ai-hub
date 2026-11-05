---
image: "/images/ai/pricing-alibaba-cloud.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: alibaba-cloud
currency: USD
region: "Singapore (International)"
billing_mode: pay_as_you_go
models:
  - model: qwen3.8-max
    input_price_per_1m: 2.0
    output_price_per_1m: 6.0
    cached_input_price_per_1m: 0.25
    notes:
      - "Beijing & Global regions (HK/Frankfurt/US/Tokyo): $1.65 / $4.951"
      - "Beijing batch: 50% off"
      - "Explicit cache: $2.5 create / $0.17 read (Singapore)"
      - "Free quota: 1M tokens, 90 days (Singapore)"
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - model: qwen3.8-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.47
    cached_input_price_per_1m: 0.016
    notes:
      - "Beijing & Global regions: $0.113 / $0.382"
      - "Explicit cache: $0.2 create / $0.016 read (Singapore)"
      - "Batch inference not supported"
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - model: qwen3.7-plus
    input_price_per_1m: 0.4
    output_price_per_1m: 1.6
    notes:
      - "Up to 256K context tier (row price)"
      - "256K–1M tier: $1.2 / $4.8"
      - "Beijing: $0.276/$1.101 and $0.826/$3.301"
      - "Limited-time 20% console discount"
      - "Thinking billed same as output"
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
last_verified: "2026-11-05"
sources:
  - source_name: Model Studio — model pricing
    source_url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
---

**Short answer.** Alibaba prices the same model differently by region — Singapore costs about 17% more than Beijing and the global regions for Qwen3.8-Max — and offers the only explicit cache-creation charge in this database. The list price is therefore a function of where you deploy, which makes region a pricing decision, not just a latency one.

## The ladder

| Model | Input | Output | Out/in | Cache read | Singapore premium |
|---|---|---|---|---|---|
| Qwen3.8-Max | $2.00 | $6.00 | 3.00 | $0.25 (12.5%) | ~17.5% over Beijing |
| Qwen3.8-Flash | $0.15 | $0.47 | 3.13 | $0.016 (10.7%) | ~25% over Beijing |
| Qwen3.7-Plus | $0.40 | $1.60 | 4.00 | — | — |

The Singapore premium is not uniform: Flash carries a larger regional gap (25%) than Max (17.5%), which means the cheapest tier is also the most sensitive to where you buy it.

## Explicit caching has a creation cost

Alibaba charges $2.50 per 1M tokens to create an explicit cache and $0.17 per 1M to read it. The read price is 8.5% of input, in line with competitors; the creation charge is unusual and changes the arithmetic.

A cache pays for itself only after a few reads: at $2.50 creation against $2.00 input, the first reuse already saves money, but a cache that is created and read once costs more than not caching at all. Short-lived contexts should skip explicit caching and rely on the implicit discount.

## Batch pricing is tier-dependent

Batch inference is 50% off on Max and unavailable on Flash. That inversion is worth noticing: the model most likely to be used for bulk classification — the cheapest one — is the one that cannot use the batch tier. Bulk work on Flash pays full rate.

## Free quota

1M tokens for 90 days on the Singapore region is a genuine evaluation allowance, roughly enough to run a small pilot. It does not extend to batch or to the Beijing region.

## Our view

**Region is the first pricing decision with Alibaba, and most buyers make it on latency.** The 17-25% premium for Singapore buys data residency and lower latency to Southeast Asia; buying it without needing either is an avoidable cost.

**The explicit-cache creation fee makes caching a commitment.** Providers that charge only for reads let you cache speculatively; Alibaba makes you amortise the creation. Model it before enabling it on short-lived prompts.

**No batch tier on Flash is the biggest structural gap here.** Competitors discount batch work by half across the board. If your workload is bulk inference on the cheapest model, Alibaba is more expensive than its list price suggests.

**The three-tier ladder is shallow.** Max, Plus and Flash span 13x on input — narrower than Zhipu's 9x flagship-to-flash spread when normalised, and without a speed tier in between.
