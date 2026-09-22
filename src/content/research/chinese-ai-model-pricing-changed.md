---
title: "How Chinese AI Model Pricing Has Changed: Flash Tiers, Cache Discounts and the $0.15 Input Standard"
description: "A price-structure analysis of Chinese frontier API pricing in September 2026: the emergence of a $0.15 flash tier across three providers, cache-hit discounts of 80-98%, peak/off-peak differentials, regional splits, and what the documented price events of 2026 reveal about where this market is heading."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "What has actually changed in Chinese AI model API pricing during 2026, and what does the current price structure across six providers reveal about the economics of the market?"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - qwen3.8-max
  - qwen3.8-flash
  - doubao-seed-2-1-pro
  - kimi-k3
  - minimax-m3
  - glm-5.3
  - glm-5.3-flash
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
  - source_name: "Kimi API — pricing"
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

# How Chinese AI Model Pricing Has Changed: Flash Tiers, Cache Discounts and the $0.15 Input Standard

## Executive Summary

Chinese frontier API pricing in September 2026 is organized around three structural devices rather than a single price war: a **flash tier** that has converged on $0.15 input per 1M tokens across three independent providers (DeepSeek, Alibaba, Zhipu); **cache-hit discounts** of 80-98% that reward repeated contexts; and **temporal and regional differentials** — peak/off-peak multipliers and separate USD/CNY price lists. The documented price events of 2026 are consistent with this structure: DeepSeek cut prices at the V4.1-Flash launch (2026-09-10), MiniMax lists its flagship at a permanent 50% discount to list price, and Alibaba shipped a flagship snapshot upgrade at an unchanged $2/$6 price. This article maps the current price structure across all six providers, identifies what verifiably changed, and explains what the structure implies for buyers.

## What We Know

The China AI Hub pricing collection records pay-as-you-go list prices for six providers, captured and verified against official pricing pages on 2026-09-20. All numbers below are list prices in USD per 1M tokens unless stated, with the provider's own peak/off-peak and regional variants noted.

**Flash tier (cheapest general models):**

| Provider | Model | Input | Output | Cache hit |
|---|---|---|---|---|
| DeepSeek | V4.1-Flash | $0.15 | $0.60 | $0.003 |
| Alibaba | Qwen3.8-Flash | $0.15 | $0.47 | $0.016 |
| Zhipu | GLM-5.3-Flash | $0.15 | $0.50 | $0.03 |

Three providers independently list a flash model at $0.15 input. Output prices cluster at $0.47-$0.60. This is the clearest pricing signal in the market: $0.15 input / ~$0.50 output is now the reference price for the fast tier.

**Flagship tier (premium models):**

| Provider | Model | Input | Output | Cache hit |
|---|---|---|---|---|
| Moonshot | Kimi K3 | $3.00 | $15.00 | $0.30 |
| Alibaba | Qwen3.8-Max | $2.00 | $6.00 | $0.25 |
| Zhipu | GLM-5.3 | $1.40 | $4.40 | $0.26 |
| DeepSeek | V4-Pro | $0.66 | $1.98 | $0.022 |
| ByteDance | Seed 2.1 Pro | ¥6.0 | ¥30.0 | ¥1.2 |
| MiniMax | MiniMax-M3 | $0.30 | $1.20 | $0.06 |

FACT: DeepSeek's V4-Pro sits below every other provider's flagship tier — its off-peak price ($0.66/$1.98) is lower than Moonshot's coding model. ByteDance is priced in CNY only (China region, Ark platform); its standard tier (¥6/¥30) converts to roughly $0.84/$4.2 at typical rates, but the official price list is CNY and should be compared in its own currency.

## What the Data Shows

**Cache pricing is where the money actually moves.** Cache-hit input is priced at 2-20% of the standard input rate across providers: DeepSeek $0.003 (2% of $0.15), Alibaba $0.016 (11%), GLM-5.3 $0.26 (19%), Kimi K3 $0.30 (10%). A workload with 90% cache hits at DeepSeek flash prices pays roughly $0.15 + $0.027 + $0.60 per 1M in/out — the cached portion of input is nearly free. Some providers add separate cache-write fees (Moonshot: $3.00 for 5-min TTL, $6.00 for 1-hour TTL; MiniMax: $0.375 per 1M written; Alibaba: $2.5 creation / $0.17 read in Singapore). Cache economics, not headline rates, determine real cost for any stateful workload.

**Peak/off-peak pricing is spreading beyond DeepSeek.** DeepSeek applies a 2x peak multiplier (all times except 01:00-04:00 and 06:00-10:00 UTC Mon-Fri). ByteDance offers low-priority tiers at roughly 50% (Pro ¥3.00/¥15.00; Turbo ¥1.50/¥7.50). Zhipu's GLM Coding Plan applies peak/off-peak credit multipliers (peak Mon-Fri 14:00-18:00 UTC+8 = 2x; off-peak = 50%). Time-shifting batch workloads is now a first-class cost lever.

**Regional splits are structural.** Alibaba prices Singapore differently from Beijing/Global (Qwen3.8-Max: $2.00/$6.00 vs $1.65/$4.951). MiniMax and Zhipu run separate international (USD) and China (CNY) platforms with different operators. ByteDance serves only cn-beijing. A buyer's effective price depends on which region they can legally and practically consume.

**Premium pricing survives at the top.** Moonshot K3 at $3/$15 is the most expensive API flagship in the collection — roughly 20x DeepSeek flash on input. Moonshot's position is unusual in a market otherwise compressing toward flash pricing; the Kimi product brand carries a price premium that the API inherits.

## What Has Changed

The China AI Hub database does not yet hold a complete historical price series for every provider — price_history arrays are populated only where an official page documents a change. What can be stated with confidence:

- **2026-09-10: DeepSeek V4.1-Flash launch with a price reduction.** The API change log lists the release alongside a price reduction; the news page describes "lower API prices" for the new multimodal flash model. V4-Flash and V4-Flash-Vision-Exp were retired and temporarily routed to V4.1-Flash for compatibility.
- **2026-09-10: DeepSeek V4-Pro deprecation reversed.** An earlier announced cutoff (2026-09-14, with requests redirected to V4.1-Flash) was reversed "in response to user demand"; billing unchanged.
- **2026-09-02: Qwen3.8-Max-0902 snapshot at unchanged price.** Alibaba upgraded the API flagship (coding, multi-tool orchestration, vision) while holding list price at $2/$6 — a quality improvement delivered as a price cut in real terms.
- **MiniMax M3 permanent 50% discount.** The international list is $0.60/$2.40; the effective standard tier is $0.30/$1.20 described as a permanent discount — a price cut encoded as a standing promotion.
- **Flash-tier formation.** GLM-5.3-Flash (2026-08-26) and DeepSeek V4.1-Flash (2026-09-10) both launched into the $0.15 input band that Alibaba's Qwen3.8-Flash already occupied. In 2025 a flash model was a discount variant; in 2026 it is the entry product of every API platform.

ANALYSIS: what looks like a price war is better described as tier consolidation. The three events of 2026 that moved headline prices (DeepSeek cut, MiniMax discount, flash launches) all anchored to the same $0.15/$0.50 flash reference and the same cache-hit multipliers. The market is converging on a shared price grammar, not racing to zero.

## Why It Matters

For buyers, the practical implications are concrete:

- **If your workload is cache-friendly** (long system prompts, document Q&A, agent loops with stable context), your effective input cost can be 80-98% below list. Optimize for cache-hit rate before negotiating list price.
- **If your workload is batch or latency-tolerant**, ByteDance's low-priority tier and Alibaba's Beijing batch discount (50%) are the strongest documented levers.
- **If your workload is China-region**, compare in CNY on the provider's own platform: the international price lists do not govern domestic consumption.
- **If you need the absolute floor**, DeepSeek V4.1-Flash off-peak at $0.15/$0.60 with $0.003 cache is the cheapest general flash configuration documented in the collection.
- **If you need top-tier reasoning**, Moonshot K3 at $3/$15 is an outlier on price — verify whether the premium buys measurable capability for your task before committing.

## Comparison / Evidence

The cleanest cross-provider comparison normalizes to the flash tier, where five of six providers have a comparable product (Moonshot's nearest equivalent, k2.7-code, sits at $0.95/$4.0 — no flash-class model is listed):

- Input $0.15: DeepSeek V4.1-Flash, Qwen3.8-Flash, GLM-5.3-Flash
- Output $0.47-$0.60: same three, tightly clustered
- Cache-hit 2%-20% of input: all providers
- Peak multiplier 2x: DeepSeek (time-based), Zhipu Coding Plan (credit-based)
- Low-priority ~50%: ByteDance, DeepSeek off-peak, Alibaba batch

The evidence supports one clean generalization: **list price now signals tier, not provider.** Any two flash models are within a few percent on output price; any two flagships are separated by provider strategy, not by an order of magnitude.

## Limitations and Uncertainty

Three cautions. First, **no complete historical series**: the pricing collection records current list prices plus documented change events; it cannot reconstruct month-by-month price history for every provider, so statements about "the pace of price decline" are inferences from the documented events, not a measured time series. Second, **currency**: ByteDance is compared here in CNY, converted informally for orientation only — cross-currency comparisons embed an exchange-rate assumption the official price lists do not make. Third, **promotional volatility**: MiniMax's permanent discount and Zhipu's limited-time free cache storage show that list prices and effective prices diverge; any figure here should be re-verified against the official page before a purchasing decision.

## China AI Hub View

Our assessment: Chinese API pricing has stopped being a race to the bottom and become a **tiered grid** — flash/fast, flagship, and cache-discounted variants of each, with time and region as two more axes. The meaningful negotiation is no longer "who is cheaper" but "which cell of the grid does my workload sit in." A provider's cache-hit multiplier and peak-hour policy now matter more than its headline rate. We expect the next pricing moves to be structured (cache write fees, longer off-peak windows, batch tiers) rather than headline cuts, because the flash floor at $0.15 input leaves little room for another order-of-magnitude drop without reworking the cost structure itself.

## Conclusion

Chinese API pricing in 2026 changed in three measurable ways: a flash tier standardized at $0.15 input across three providers; cache-hit discounts deepened to 80-98%; and price management moved from headline cuts to structural devices — permanent discounts, snapshot upgrades at unchanged prices, peak/off-peak windows and dual-region lists. The result is a market where effective cost is a function of workload shape (cache rate, timing, region) more than provider choice. Buyers who still compare providers on headline input price are optimizing the wrong number.

## Sources

See the Sources list in the page metadata — all figures trace to official pricing pages (DeepSeek, Alibaba Model Studio, Volcengine Ark, MiniMax, Kimi, Z.ai/BigModel) and the DeepSeek change log / release announcement, verified 2026-09-20.
