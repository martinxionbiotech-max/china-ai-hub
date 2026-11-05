---
image: "/images/ai/pricing-minimax.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: minimax
currency: USD
region: "International"
billing_mode: pay_as_you_go
models:
  - model: minimax-m3
    input_price_per_1m: 0.3
    output_price_per_1m: 1.2
    cached_input_price_per_1m: 0.06
    notes:
      - "Standard tier ≤512K input (row price; permanent 50% off vs list $0.60/$2.40)"
      - ">512K input: $0.60/$2.40, cache $0.12"
      - "Priority tier (service_tier=priority): 1.5x"
      - "China platform: ¥2.1/¥8.4 (≤512K), ¥4.2/¥16.8 (>512K)"
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
  - model: minimax-m2.7
    input_price_per_1m: 0.3
    output_price_per_1m: 1.2
    cached_input_price_per_1m: 0.06
    notes:
      - "Cache write: $0.375 per 1M tokens"
      - "China platform: ¥2.1 / ¥8.4"
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
  - model: minimax-m2.7-highspeed
    input_price_per_1m: 0.6
    output_price_per_1m: 2.4
    cached_input_price_per_1m: 0.06
    notes:
      - "Cache write: $0.375 per 1M tokens"
      - "China platform: ¥4.2 / ¥16.8"
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
price_history:
  - model: minimax-m3
    field: input_price_per_1m
    old_value: 0.6
    new_value: 0.3
    effective_date: ""
    source: https://platform.minimax.io/docs/guides/pricing-paygo
  - model: minimax-m3
    field: output_price_per_1m
    old_value: 2.4
    new_value: 1.2
    effective_date: ""
    source: https://platform.minimax.io/docs/guides/pricing-paygo
  - model: minimax-m3
    field: cached_input_price_per_1m
    old_value: 0.12
    new_value: 0.06
    effective_date: ""
    source: https://platform.minimax.io/docs/guides/pricing-paygo
last_verified: "2026-11-05"
sources:
  - source_name: MiniMax API platform — pay-as-you-go pricing (intl)
    source_url: https://platform.minimax.io/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
  - source_name: MiniMax API platform — pay-as-you-go pricing (CN)
    source_url: https://platform.minimaxi.com/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
---

**Short answer.** MiniMax runs a permanent 50% discount against its own list price, tiers by context length with a hard doubling above 512K tokens, and sells a priority tier at 1.5x. The headline $0.30/$1.20 is real, but it applies only below the context cliff.

## The structure

| Model | Input | Output | Out/in | Cache | Condition |
|---|---|---|---|---|---|
| MiniMax-M3 | $0.30 | $1.20 | 4.00 | $0.06 (20%) | ≤512K input |
| MiniMax-M3 (>512K) | $0.60 | $2.40 | 4.00 | $0.12 | >512K input |
| MiniMax-M2.7 | $0.30 | $1.20 | 4.00 | $0.06 | ≤512K |
| M2.7 Highspeed | $0.60 | $2.40 | 4.00 | $0.06 | faster serving |
| Priority tier | 1.5x | 1.5x | — | — | service_tier=priority |

The price history recorded here shows M3 cut from $0.60/$2.40 to $0.30/$1.20 — in other words, the "permanent 50% discount" is a halving that has been left in place, not a promotional rate.

## The 512K cliff

This is the single most important fact on the page. A request with 600K input tokens is not charged a blended rate; the whole call moves to the higher tier. For long-document workloads the effective price doubles the moment a document crosses the threshold, and a 1M-context model whose price doubles at half its window is a different proposition from one priced flat.

Architecturally, that argues for chunking above 512K, or for comparing the effective price at your real input size rather than at the headline.

## Priority at 1.5x is cheap insurance

Most providers price priority implicitly or not at all. A 50% premium for a guaranteed service tier is modest, and for customer-facing workloads it is usually the cheapest reliability purchase available.

## Our view

**The context cliff is the point of this page.** A flat-looking $0.30 input that doubles above 512K is a worse deal for long-context work than a provider charging $0.45 flat. Compare at your actual context length, not at the marketing number.

**A permanent 50% discount means the list price is fiction.** MiniMax's list price is not a price anyone pays; it exists to make the discount legible. Treat the discounted number as the real one when comparing across providers.

**Priority at 1.5x is the most honest reliability pricing in the database.** It is stated, bounded and optional — which is more than most competitors offer, where priority is bundled or unstated.

**M3 and M2.7 at identical prices is a migration waiting to happen.** M2.7 has a 204K context and a non-commercial licence; M3 has 1M and a commercial one. There is no price reason to stay on M2.7.
