---
image: "/images/ai/pricing-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "Choosing by Price: Flash Tiers, Cache Discounts and the $0.15 Standard"
description: "A decision guide for selecting a Chinese model on price — reading the flash tier, cache-hit discounts, peak/off-peak differentials, regional splits and subscription structures from the pricing database and its documented price-history events."
published_date: "2026-09-29"
updated_date: "2026-09-29"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - qwen3.8-flash
  - qwen3.8-max
  - glm-5.3-flash
  - glm-5.3
  - kimi-k3
  - minimax-m3
  - doubao-seed-2-1-pro
  - deepseek
  - minimax
  - alibaba-cloud
  - moonshot-ai
  - zhipu-ai
sources:
  - source_name: "China AI Hub — Pricing database"
    source_url: "https://sinoaihub.com/pricing/"
    source_type: independent
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
  - source_name: "MiniMax API — pay-as-you-go pricing"
    source_url: "https://platform.minimax.io/docs/guides/pricing-paygo"
    source_type: official
  - source_name: "Alibaba Cloud — Model Studio pricing"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
    source_type: official
---

**Short answer.** Chinese frontier API pricing in September 2026 is organized around a flash tier that has converged on $0.15 input per 1M tokens across three providers (DeepSeek V4.1-Flash, Qwen3.8-Flash, GLM-5.3-Flash), cache-hit discounts of 80–98%, and peak/off-peak and regional differentials. The documented price events of 2026 — DeepSeek's V4.1-Flash launch price cut, MiniMax's permanent 50% discount, and Alibaba's flagship snapshot at an unchanged $2/$6 — are consistent with tier consolidation, not a race to zero. For most buyers the right choice is a flash-tier model with cache pricing; the premium tier is only justified by output headroom (Kimi K3's 1M output) or a specific capability.

## Decision criteria

| Criteria | Relevance / Notes |
|---|---|
| Flash-tier reference | $0.15 input / ~$0.50 output across DeepSeek, Alibaba, Zhipu |
| Flagship tier | Kimi K3 $3/$15 · Qwen3.8-Max $2/$6 · GLM-5.3 $1.40/$4.40 · V4-Pro $0.66/$1.98 · MiniMax-M3 $0.30/$1.20 |
| Cache-hit discount | 2–20% of input rate: DeepSeek $0.003, Alibaba $0.016, GLM $0.26, Kimi $0.30 — where the money moves |
| Peak/off-peak | DeepSeek 2x peak; ByteDance ~50% low-priority tier; GLM Coding Plan 2x peak credits |
| Regional split | Alibaba Singapore vs Beijing/Global; MiniMax & Zhipu separate USD/CNY platforms; ByteDance CNY-only |
| Subscription vs pay-as-you-go | GLM Coding Plan from $18/month; Qoder Pro $20/month vs model API pay-as-you-go |
| Price history | Only 3 documented events: DeepSeek billing-structure change (08-16), DeepSeek V4.1-Flash cut (09-10), MiniMax M3 50% cut |

## The price ladder

**Flash tier (cheapest general models):**

| Provider | Model | Input | Output | Cache hit |
|---|---|---|---|---|
| DeepSeek | [V4.1-Flash](/models/deepseek-v4-1-flash/) | $0.15 | $0.60 | $0.003 |
| Alibaba | [Qwen3.8-Flash](/models/qwen38-flash/) | $0.15 | $0.47 | $0.016 |
| Zhipu | [GLM-5.3-Flash](/models/glm-53-flash/) | $0.15 | $0.50 | $0.03 |

**Flagship tier (premium models):**

| Provider | Model | Input | Output | Cache hit |
|---|---|---|---|---|
| Moonshot | [Kimi K3](/models/kimi-k3/) | $3.00 | $15.00 | $0.30 |
| Alibaba | [Qwen3.8-Max](/models/qwen38-max/) | $2.00 | $6.00 | $0.25 |
| Zhipu | [GLM-5.3](/models/glm-53/) | $1.40 | $4.40 | $0.26 |
| DeepSeek | [V4-Pro](/models/deepseek-v4-pro/) | $0.66 | $1.98 | $0.022 |
| ByteDance | [Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) | ¥6.0 | ¥30.0 | ¥1.2 |
| MiniMax | [MiniMax-M3](/models/minimax-m3/) | $0.30 | $1.20 | $0.06 |

## Entity routing

Route by the cost structure that dominates your workload.

| Scenario | Best-documented fit | Why |
|---|---|---|
| Lowest unit cost, high volume | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) or [Qwen3.8-Flash](/models/qwen38-flash/) | $0.15/$0.60 or $0.15/$0.47 |
| Cache-heavy agent workloads | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) | Near-zero cache at 2% of input ($0.003) |
| Cheapest flagship | [MiniMax-M3](/models/minimax-m3/) | $0.30/$1.20, permanent 50% off list |
| Long-output generation, price follows output | [Kimi K3](/models/kimi-k3/) | $3/$15, but only 1M-output model |
| Enterprise multi-region pricing | [Alibaba Cloud pricing](/pricing/alibaba-cloud/) | Regional splits, batch discounts |
| Subscription coding | [GLM Coding Plan](/agents/glm-coding-plan/) or [Qoder](/agents/qoder/) | $18/month / $20/month |

Per-provider pricing records: [DeepSeek](/pricing/deepseek/), [Alibaba Cloud](/pricing/alibaba-cloud/), [ByteDance](/pricing/bytedance/), [MiniMax](/pricing/minimax/), [Moonshot](/pricing/moonshot-ai/), [Zhipu](/pricing/zhipu-ai/).

## What the evidence shows

What looks like a price war is better described as tier consolidation. The three events of 2026 that moved headline prices all anchored to the same $0.15/$0.50 flash reference and the same cache-hit multipliers. The database's price_history is populated only where an official page documents a change — three events total — and providers without a documented change are recorded as having no located price-change events rather than having synthetic history added.

The documented events, from the price_history arrays: DeepSeek-V4-Pro's billing structure moved from flat to peak/off-peak on 2026-08-16 (off-peak = 50% of peak); DeepSeek-V4.1-Flash launched 2026-09-10 with reduced pricing as V4-Flash was retired; and MiniMax-M3's input price dropped $0.60 → $0.30, output $2.40 → $1.20, and cache $0.12 → $0.06 — a permanent 50% discount encoded as a standing promotion.

The real cost driver is cache, not headline rate: a workload with 90% cache hits at DeepSeek flash prices pays roughly $0.15 + $0.027 + $0.60 per 1M in/out, with the cached portion of input nearly free. Some providers add separate cache-write fees (Moonshot $3.00 for 5-min TTL, $6.00 for 1-hour; MiniMax $0.375 per 1M written; Alibaba $2.5 create/$0.17 read). Premium pricing survives only at the top — Moonshot K3 at $3/$15 is the most expensive API flagship in the collection, roughly 20x DeepSeek flash on input, carrying a brand premium that the Kimi API inherits.

China AI Hub analysis indicates the market is converging on a shared price grammar — flash reference, cache multipliers, temporal and regional differentials — rather than racing to zero. Time-shifting batch workloads is now a first-class cost lever (DeepSeek's off-peak window, ByteDance's ~50% low-priority tier, GLM Coding Plan's 2x peak credits).

## Selection procedure

Work through these steps in order.

1. **Estimate your output-token mix, not just input.** Output tokens bill at 2–5x input rates and dominate reasoning workloads. If your task generates long chains of thought, compute expected output before comparing headline input prices.
2. **Start from the flash tier as the default.** At $0.15 input / ~$0.50 output across three providers, the flash tier is the reference point; the premium tier must be justified by output headroom or a specific capability, not by default.
3. **If stateful, compare cache, not headline rate.** For re-read-heavy workloads the cache-hit discount (2–20% of input) plus cache-write fees is where real cost lives. DeepSeek's $0.003 cache is near-free; Moonshot's $3–$6 write fees are not.
4. **Factor temporal and regional differentials.** DeepSeek's 2x peak, ByteDance's ~50% low-priority tier and GLM Coding Plan's 2x peak credits make time-shifting a cost lever. ByteDance is CNY-only, and Alibaba's Singapore and Beijing/Global prices differ.
5. **Decide subscription versus pay-as-you-go.** Subscription coding (GLM Coding Plan, Qoder) caps cost but adds quota, peak-hour and expiry rules that pay-as-you-go avoids.
6. **Re-verify the price.** Everything here is as of 2026-09-20; prices move frequently.

## Reading the price-history records correctly

The database's price_history arrays are deliberately conservative: a row is added only when an official page documents a change, so the three events recorded are the *verified* history, not a claim of completeness. Two providers — DeepSeek and MiniMax — have documented events; the other four have none located, which the database records as "No officially documented price-change events located" rather than padding with synthetic history. China AI Hub analysis indicates this asymmetry is itself informative: a provider that publishes a change log is one you can audit over time, while a provider with no documented history gives you a single-point snapshot with no trajectory.

When you compare, read the structure, not just the number. DeepSeek's peak/off-peak means the $0.15 flash rate is only half the story during weekday peak windows; MiniMax's $0.30/$1.20 is a permanent 50% discount off a $0.60/$2.40 list, so the "list price" and the "effective price" are different things; Alibaba's $2/$6 flagship in Singapore is $1.65/$4.951 in the Beijing/Global regions. A price quoted without its region, its peak/off-peak window and its cache terms is not a price — it is an incomplete sentence.

## Limitations

The price_history array is populated only where an official page documents a change; it is not a complete historical series for every provider. Prices change frequently and are verified as of 2026-09-20 — re-verify before committing. ByteDance is priced in CNY only (China region), so its ¥6/¥30 flagship should be compared in its own currency, not converted informally. Cache economics depend on workload statefulness, which varies by use case. Subscription pricing (GLM Coding Plan, Qoder) has quota caps, peak-hour multipliers and expiry rules that are separate from pay-as-you-go API pricing and are not fully extractable from sign-in-gated pages. DeepSeek's peak/off-peak and MiniMax's "permanent discount" are vendor-framed; the database records them as vendor statements.

## Sources

- [China AI Hub — Pricing database](/pricing/)
- [DeepSeek API docs — Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [MiniMax API — pay-as-you-go pricing](https://platform.minimax.io/docs/guides/pricing-paygo)
- [Alibaba Cloud — Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)

*Labels used above: **Official fact** (list prices, cache rates and documented price-history events from primary pricing pages), **Vendor-reported claim** (any discount or tier framing published by the vendor), and **China AI Hub analysis** (our synthesis, introduced as such). No third-party evaluation evidence is currently recorded for pricing.*
