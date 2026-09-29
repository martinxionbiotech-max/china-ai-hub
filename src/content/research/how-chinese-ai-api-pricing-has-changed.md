---
title: "How Chinese AI API Pricing Has Changed: From a DeepSeek Price War to Subscription and Tiered Economics"
author: "SinoAI Hub Research Team"
description: "A price-history analysis of China's frontier API market: the five documented price-change events, the $0.15 flash floor DeepSeek triggered, and the structural migration away from per-token price cuts toward subscription, credit and time-based tiering."
published_date: "2026-09-29"
updated_date: "2026-09-29"
research_question: "What do the documented price-change events in China's AI API market actually show — is the market still racing to the bottom on per-token price, or has it migrated to a different pricing instrument?"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - qwen3.8-flash
  - qwen3.8-max
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
  - doubao-seed-2-1-pro
  - glm-coding-plan
  - qoder
  - minimax-agent
author_view: true
image: "/images/ai/pricing-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
sources:
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "DeepSeek API Change Log"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Alibaba Cloud Model Studio — model pricing"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Volcengine Ark — model pricing"
    source_url: "https://docs.volcengine.com/docs/ark/model-pricing?lang=zh"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "MiniMax API platform — pay-as-you-go pricing"
    source_url: "https://platform.minimax.io/docs/guides/pricing-paygo.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Kimi API — pricing (chat)"
    source_url: "https://platform.kimi.ai/docs/pricing/chat"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai pricing"
    source_url: "https://docs.z.ai/guides/overview/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "DeepSeek — Introducing DeepSeek-V4.1-Flash"
    source_url: "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"
    source_type: official
    published_date: "2026-09-10"
    last_verified: "2026-09-20"
    confidence: high
---

Every factual claim in this article is drawn from the China AI Hub database (pricing and model records, last verified 2026-09-20) and the official pricing pages linked at the bottom. All prices are USD per 1M tokens unless stated. Where the database records a field as null or a price history as absent, this article says so rather than inferring a change that is not documented.

## Research Question

How has Chinese AI API pricing actually changed, and — more importantly — *how is it changing now*? The market narrative in early 2026 was "price war." The database lets us test that narrative against evidence: the five officially documented price-change events, the current price structure across six providers, and the parallel growth of subscription and credit-based products. The question matters because a buyer who optimizes for headline token price in a market that has moved to subscription billing is optimizing the wrong instrument.

## Methodology

This analysis uses three distinct sources of evidence, kept separate so that a documented change is never confused with an inferred one.

First, **price history records** — the `price_history` arrays in the pricing collection, populated only where an official page (pricing page, change log, or announcement) documents a before-and-after change. Second, **current list prices** — the per-model input/output/cache rates captured and verified against official pricing pages on 2026-09-20. Third, **adjacent billing surfaces** — the subscription and credit products recorded in the agents collection (GLM Coding Plan, Qoder, MiniMax Token Plan, Kimi membership, Qwen Code's Token Plan, Doubao's subscription), which are not API price changes but are part of the same economic picture.

The discipline here is deliberately conservative: only five price-change events are documented across all six providers. The absence of a price-history record for Alibaba, ByteDance, Moonshot and Zhipu is itself a finding — it means those providers either did not change headline prices in a way their official pages record, or encode changes differently (permanent discounts, snapshot upgrades, separate CNY lists). Both readings are stated rather than resolved.

## Evidence

The database records **five documented price-change events**, all from two providers:

| Model | Field | Old | New | Effective |
|---|---|---|---|---|
| deepseek-v4-pro | billing_structure | Flat pricing | Peak/off-peak; off-peak = 50% of peak | 2026-08-16 |
| deepseek-v4-1-flash | api_pricing | V4-Flash list (retired) | Reduced V4.1-Flash pricing | 2026-09-10 |
| minimax-m3 | input_price_per_1m | $0.60 | $0.30 | — |
| minimax-m3 | output_price_per_1m | $2.40 | $1.20 | — |
| minimax-m3 | cached_input_price_per_1m | $0.12 | $0.06 | — |

Three observations follow directly from this table. **First, the events are not uniform cuts.** Two of the five are DeepSeek, and one of those is not a price cut at all but a billing-structure change — the introduction of peak/off-peak pricing on 2026-08-16, a *mechanism* change rather than a number change. **Second, the MiniMax rows are one event recorded as three fields** — a permanent 50% discount across input, output and cache-hit, described on the official page as a standing promotion rather than a new list price. **Third, four of the six providers have no documented price-history at all** — their `price_history` arrays carry the honest annotation "No officially documented price-change events located as of 2026-09-22." That is not evidence they never changed prices; it is evidence they did not record a change in a form the database can cite.

## Data

The current price structure across the six providers is the second body of evidence.

**Flash tier (cheapest general models):**

| Provider | Model | Input | Output | Cache hit |
|---|---|---|---|---|
| DeepSeek | V4.1-Flash | $0.15 | $0.60 | $0.003 |
| Alibaba | Qwen3.8-Flash | $0.15 | $0.47 | $0.016 |
| Zhipu | GLM-5.3-Flash | $0.15 | $0.50 | $0.03 |

Three independent providers list a flash model at $0.15 input. This is the price floor DeepSeek triggered and the market matched — the clearest single fact in the entire pricing collection.

**Flagship tier (premium models):**

| Provider | Model | Input | Output |
|---|---|---|---|
| Moonshot | Kimi K3 | $3.00 | $15.00 |
| Alibaba | Qwen3.8-Max | $2.00 | $6.00 |
| Zhipu | GLM-5.3 | $1.40 | $4.40 |
| DeepSeek | V4-Pro | $0.66 | $1.98 |
| ByteDance | Seed 2.1 Pro | ¥6.0 | ¥30.0 |
| MiniMax | MiniMax-M3 | $0.30 | $1.20 |

The flagship tier spans a 20x range on input ($0.30 to $6.00, or roughly $0.84/$4.2 for ByteDance converted informally from CNY). Moonshot's K3 at $3/$15 is the most expensive API flagship in the collection — an outlier in a market otherwise compressing toward flash pricing.

**Structural devices around the headline rate:**

- **Cache-hit discounts** of 80–98%: cached input is priced at 2–20% of standard input across all providers.
- **Peak/off-peak and time-based tiering**: DeepSeek applies a 2x peak multiplier; ByteDance offers low-priority tiers at ~50%; Zhipu's GLM Coding Plan applies 2x peak / 50% off-peak credit multipliers.
- **Regional splits**: Alibaba prices Singapore ($2.00/$6.00) differently from Beijing/Global ($1.65/$4.951); MiniMax and Zhipu run separate international (USD) and China (CNY) platforms.
- **Subscription and credit products**: GLM Coding Plan (¥118–¥1,078/month in China, from $18/month internationally), Qoder ($20–$200/month), MiniMax Token Plan ($22–$132/month), Kimi membership ($15–$159/month), Qwen Code Token Plan (¥39–¥499/month), Doubao (¥68–¥500/month).

## Analysis

Read together, the evidence and the data point to a market in the middle of a **structural migration away from per-token price competition**.

The five documented price events are almost all from late 2026, and only DeepSeek's V4.1-Flash launch (2026-09-10) is a classic headline cut. MiniMax's "cut" is a permanent 50% discount — a *price encoded as a promotion* rather than a new list number. DeepSeek's other event is not a cut at all but the invention of a demand-shaping mechanism. Meanwhile the flash floor has settled at $0.15 input across three providers, which leaves essentially no room for another order-of-magnitude drop without reworking the cost structure itself.

China AI Hub analysis indicates: the price war, in the sense of headline per-token cuts, has largely run its course — not because competition stopped, but because the competitive surface moved. The growth now is in **subscription and credit-based billing** (GLM Coding Plan, Qoder, the Token Plans, Kimi membership) and in **time/region-based tiering** (peak/off-peak, low-priority, dual-region lists). These instruments share one property: they make cross-provider comparison harder than a flat per-token rate does, and they let a vendor capture spend (and lock in usage patterns) without touching the headline number. The $0.15 flash floor is the *last* widely-copied number; what has not been copied — and what now differentiates providers — is everything wrapped around it.

China AI Hub analysis indicates: this migration is a rational response to DeepSeek's specific strategy. DeepSeek won the floor on MIT weights and $0.15 flash pricing, so rivals that cannot (or will not) match MIT-and-cheap have moved *up* the stack into bundled subscription products and enterprise-tier routing — where the unit of comparison is "credits per 5-hour window" or "peak multiplier," not "$ per 1M tokens." Moonshot's K3 at $3/$15 is the extreme case: a provider declining to compete on price at all, betting the premium on long-context output capability that the flash tier does not offer.

China AI Hub analysis indicates: the most consequential change for a buyer is not any single number but the **loss of comparability**. In 2025 a buyer could compare providers on one number. In September 2026, a fair comparison requires normalizing for cache-hit rate, peak-hour policy, region, currency, and — increasingly — whether the product is even sold per-token at all. The database's own comparison records already treat ByteDance's CNY-only list and MiniMax's "permanent discount" as cases that cannot be dropped into a single USD table without caveats.

## Counterpoints / Limitations

Several counterpoints must be stated against the migration thesis.

**First, the evidence for "migration" is circumstantial, not causal.** The database shows subscription products growing alongside flat per-token pricing, but it does not record that providers *replaced* per-token pricing with subscriptions — most providers still sell both. The claim is a structural reading of where differentiation is now happening, not a measured shift in revenue mix, which no provider discloses.

**Second, the five price events understate real change.** Providers that ship "snapshot upgrades at unchanged price" (Alibaba's Qwen3.8-Max-0902 at the same $2/$6) or "permanent discounts" (MiniMax) are changing *effective* price without a documented price_history entry. The database records list price and documented events; it cannot fully capture effective price, which is what buyers actually pay.

**Third, currency and region make any single table provisional.** ByteDance prices only in CNY for the China region, and Alibaba/MiniMax/Zhipu maintain separate domestic and international platforms. Cross-currency comparisons embed an exchange-rate assumption the official lists do not make.

**Fourth, promotional volatility is real.** Zhipu's limited-time free cache storage and MiniMax's standing 50% discount show that list and effective prices diverge, and both can change without a formal price-history record. Any figure here should be re-verified against the official page before a purchasing decision.

**Fifth, this analysis cannot reconstruct a month-by-month series.** The pricing collection holds current list prices plus documented events; statements about "the pace" of price decline are inferences from five data points, not a measured time series.

## China AI Hub Interpretation

Our interpretation, on the balance of the evidence: **China's AI API market has completed the "price floor" phase of its price war and entered a "repackaging" phase.** The documented record shows DeepSeek triggering the floor ($0.15 flash, MIT weights, peak/off-peak), two rivals matching the floor on the input side, and the market then differentiating on everything *except* the floor — cache economics, time-based tiering, regional splits, and above all subscription/credit billing.

We read the near-total absence of documented price_history records at Alibaba, ByteDance, Moonshot and Zhipu as consistent with this: those providers are not competing by cutting list prices, but by repackaging (ByteDance's low-priority tiers, Alibaba's regional spread, Moonshot's premium long-output positioning, Zhipu's cross-tool coding subscription). The price war did not end; it changed shape.

We flag one risk explicitly, because it is where the data is thinnest: **the migration thesis could be wrong if the subscription products are niche rather than mainstream.** The database records subscription pricing for coding agents and consumer apps, but it does not record what share of total Chinese AI spend flows through subscriptions versus per-token API. If subscriptions remain a coding-tool niche, the market is simply a flat-token-price market with a $0.15 floor and some clever discounting — and the "migration" is ours, not the market's. We state the uncertainty rather than resolve it.

## Conclusion

The documented evidence supports three conclusions. **One:** the flash tier has standardized at $0.15 input across DeepSeek, Alibaba and Zhipu, and that floor leaves no room for another dramatic per-token cut. **Two:** the five officially documented price-change events are mostly not simple cuts — they are a mechanism change (DeepSeek's peak/off-peak) and a permanent discount (MiniMax), which is how price competition now expresses itself. **Three:** the growth area of pricing is subscription, credit and time/region-based tiering, which erodes cross-provider comparability. For a buyer, the actionable lesson is to stop optimizing headline token price and start modeling the full instrument: cache-hit rate, peak-hour policy, region, currency, and whether the workload is even sold per-token anymore.

## Sources

See the Sources list in the page metadata — all figures trace to official pricing pages (DeepSeek, Alibaba Model Studio, Volcengine Ark, MiniMax, Kimi, Z.ai/BigModel), the DeepSeek change log and release announcement, and the agent product pages for subscription pricing, verified 2026-09-20.

*Labels used above: **Official fact** (prices and price-history rows from vendor pricing pages and change logs), **Vendor-reported claim** (promotional and capability statements), and **China AI Hub analysis** (our interpretation, always introduced as such).*
