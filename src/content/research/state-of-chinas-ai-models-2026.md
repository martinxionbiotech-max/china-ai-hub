---
title: "The State of China's AI Models in 2026: A 19-Model Panorama"
description: "A cross-sectional view of China's frontier model landscape in September 2026 — 19 models across six labs, mapped by openness, context window and price band, with the structural patterns the distribution reveals."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "What does China's frontier model landscape look like in 2026, and what patterns emerge from the distribution of open vs closed, context length and pricing across 19 tracked models?"
related_entities:
  - deepseek-v3-2
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - doubao-seed-2-1-pro
  - doubao-seed-2-1-turbo
  - doubao-seed-evolving
  - glm-5.2
  - glm-5.3
  - glm-5.3-flash
  - kimi-k2.6
  - kimi-k2.7-code
  - kimi-k2.7-code-highspeed
  - kimi-k3
  - minimax-m2.7
  - minimax-m2.7-highspeed
  - minimax-m3
  - qwen3.8-2.4t-a95b
  - qwen3.8-flash
  - qwen3.8-max
author_view: true
image: "/images/cc/neural-glow.webp"
image_credit: "Michael Gaylard / CC BY 4.0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:Digital_Abstraction_Neural_Network_Glow_(55258890373).jpg"
sources:
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Alibaba Cloud Model Studio — model pricing"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai — GLM-5.3 model page"
    source_url: "https://docs.z.ai/guides/llm/glm-5.3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Moonshot AI — Kimi K3 model card"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "MiniMax API platform — pay-as-you-go pricing"
    source_url: "https://platform.minimax.io/docs/guides/pricing-paygo.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Volcengine Ark — model pricing"
    source_url: "https://docs.volcengine.com/docs/ark/model-pricing?lang=zh"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

All figures in this article come from the China AI Hub model and pricing databases (last verified 2026-09-20) and the primary sources linked at the bottom. Prices are list prices as published; currencies differ by provider and are stated per table. This is a snapshot, not a ranking — the database deliberately records no "best" model.

## Executive Summary

As of September 2026 the China AI Hub tracks 19 frontier models across six labs: DeepSeek (3), ByteDance (3), Zhipu (3), Moonshot (4), MiniMax (3) and Alibaba (3). Three structural facts stand out. First, openness is the default but not universal: 11 models are open-weight, 5 are proprietary, and 3 are undisclosed. Second, a 1M-token context window is now the frontier norm — 11 of 19 models offer it — while a 256K tier (5 models) and a 200K tier (2 models) serve the mid-range. Third, the market has converged on a $0.15 flash-tier input price (DeepSeek, Alibaba and Zhipu all list it), while flagship pricing spans an order of magnitude from $0.30 (MiniMax M3) to $3.00 (Kimi K3) input per 1M tokens.

## What We Know

The six labs split into three strategic camps. ByteDance runs the purest closed strategy — all three Doubao models are proprietary, with no open weights in the database. Zhipu and DeepSeek run the purest open strategy — all of their tracked models carry open weights (MIT for DeepSeek, Apache-2.0 for Zhipu). Alibaba and Moonshot run a hybrid: Alibaba keeps its two API flagships closed while releasing one open-weight model (Qwen3.8-2.4T-A95B), and Moonshot keeps K3 open while the three K2.x models are recorded as undisclosed. MiniMax sits between — all three M-series models are open-weight, but under conditional custom licenses.

Model status also varies. The database marks DeepSeek-V3.2 as discontinued, DeepSeek-V4-Pro and GLM-5.2 as deprecated, and the rest as active. Deprecation is not retirement: the 2026-09-10 change-log reversal kept DeepSeek-V4-Pro's API running past its announced cutoff, which is why a "deprecated" label and a live API coexist in the data.

## What the Data Shows

**Openness.** 11 of 19 models are open-weight (DeepSeek's three, Zhipu's three, Kimi K3, MiniMax's three, and Qwen3.8-2.4T-A95B). 5 are proprietary (Doubao Seed 2.1 Pro/Turbo/Evolving, Qwen3.8-Flash, Qwen3.8-Max). 3 are undisclosed (Kimi K2.6, K2.7-Code, K2.7-Code-Highspeed). "Open weight" here means downloadable weights, not necessarily a standard permissive license — the licensing regimes vary, as covered in the separate licensing analysis.

**Context window.** Three tiers emerge:

| Tier | Count | Models |
|---|---|---|
| 1M tokens | 11 | DeepSeek V4-Pro / V4.1-Flash, Doubao Seed 2.1 Pro / Evolving, GLM-5.2 / 5.3 / 5.3-Flash, Kimi K3, MiniMax M3, Qwen3.8-Flash / Max |
| 256K | 5 | Doubao Seed 2.1 Turbo, Kimi K2.6 / K2.7-Code / K2.7-Code-Highspeed, Qwen3.8-2.4T-A95B |
| 200K | 2 | MiniMax M2.7 / M2.7-Highspeed |

The 1M tier is no longer a differentiator; it is the default for flagship and flash models alike. Maximum output separates models further — DeepSeek's 384K and Kimi K3's 1M output stand apart from the 131K cap on Qwen and GLM flagships.

**Price band.** List prices, per 1M tokens, in the currency each provider publishes (ByteDance is the only CNY provider in the set):

| Model | Tier | Input | Output |
|---|---|---|---|
| MiniMax M3 | flagship | $0.30 | $1.20 |
| DeepSeek V4-Pro | flagship (off-peak) | $0.66 | $1.98 |
| Doubao Seed 2.1 Pro | flagship | ¥6 | ¥30 |
| GLM-5.3 | flagship | $1.40 | $4.40 |
| Qwen3.8-Max | flagship | $2.00 | $6.00 |
| Kimi K3 | flagship | $3.00 | $15.00 |
| DeepSeek V4.1-Flash | flash | $0.15 | $0.60 |
| Qwen3.8-Flash | flash | $0.15 | $0.47 |
| GLM-5.3-Flash | flash | $0.15 | $0.50 |

## What Has Changed

Three changes define the 2026 landscape relative to earlier snapshots. First, the flash tier has arrived as a distinct product category — cheap, fast, long-context models (DeepSeek V4.1-Flash, Qwen3.8-Flash, GLM-5.3-Flash) that did not exist as a named tier in the prior generation, and whose $0.15 input price is now a three-way tie. Second, context length compressed the gap between "flagship" and "everything else": a 1M context is now available at $0.15 input, which would have been a flagship-only feature a generation earlier. Third, openness fractured into a spectrum — the binary "open vs closed" no longer captures Alibaba's or Moonshot's split portfolios, or MiniMax's conditional licenses.

## Why It Matters

The distribution matters because it changes how an adopter should choose. The old decision tree — "pick the most capable flagship" — is now wrong for most workloads. The data shows a market where capability at the top is contested (Kimi K3, Qwen3.8-Max and GLM-5.3 all claim frontier results, all vendor-reported) but where the *price spread* between flagships ($0.30 to $3.00 input) is an order of magnitude larger than any verifiable capability gap. That asymmetry means price and licensing — not headline benchmark scores — are the actual decision variables for a rational buyer, because the benchmark data across vendors is not comparable on a shared methodology.

## Detailed Analysis

We read three patterns from the distribution.

**Pattern one: the flash tier is the new volume battleground.** Three labs list $0.15 input for their flash model. This is where long-context batch, RAG and agent workloads will land, because the price makes 1M-token processing cheap enough to run continuously. The flagship tier, by contrast, is where vendors monetize — $1.40 to $3.00 input — and where the buyer should demand the most evidence before paying.

**Pattern two: closed is a ByteDance-and-flagship phenomenon.** The five proprietary models are ByteDance's entire Doubao line plus Alibaba's two API flagships. In other words, labs close the models they expect to monetize directly through an API or consumer product, and open the models that seed developer adoption — a dual-track logic that mirrors the agent layer's openness-to-monetization mapping.

**Pattern three: Moonshot is the portfolio outlier.** Four models, the deepest coding specialization (two dedicated K2.7-Code variants), the highest flagship price ($3.00/$15.00), and the only fully-undisclosed mid-tier (K2.x). Moonshot bets on long-context reasoning (K3 at 1M/1M) plus specialized coding throughput, rather than competing on the $0.15 flash floor.

## Comparison / Evidence

The cleanest cross-lab comparison is the flagship price-to-openness trade. The open flagships — MiniMax M3 ($0.30), DeepSeek V4-Pro ($0.66), GLM-5.3 ($1.40), Kimi K3 ($3.00) — already span 10x on input price. The closed flagships sit inside that range (Qwen3.8-Max at $2.00; Doubao Seed 2.1 Pro at ¥6). There is no clean "closed costs more" or "open costs less" rule: the cheapest flagship in the set (MiniMax M3, $0.30) is open-weight, and the most expensive (Kimi K3, $3.00) is also open-weight. Price is set by vendor strategy, not by openness.

Benchmark claims should be read with the database's own caveat in mind: scores are vendor-reported on different benchmarks (GPQA Diamond, HLE, Terminal-Bench, DeepSWE, MMMU-Pro, CyberGym, and more) with no shared methodology, so any head-to-head ranking built from them is unreliable. The database's benchmark-methodology research covers why.

## Limitations and Uncertainty

This is a snapshot of 19 models at a single verification date (2026-09-20); the frontier moves quickly, and several fields are structurally incomplete. The three Kimi K2.x models have no published open-weight status or context output limits in our sources. ByteDance prices in CNY while all other providers publish USD, so cross-lab price comparison requires an exchange-rate assumption this article does not make. The open Qwen3.8-2.4T-A95B weights are text-only and thinking-only, which is not the same product as the Qwen3.8-Max API flagship — a distinction the database records explicitly. And no independent benchmark evaluation exists in the database for any model, so every score referenced is vendor-reported.

## China AI Hub View

Our assessment: China's model market in 2026 has matured from a single-axis "capability race" into a three-axis market — openness, context and price — where the axes no longer move together. The most consequential fact in the data is the $0.15 flash floor and the 1M context default, because together they mean frontier-scale context is now cheap, which changes what downstream products are economical to build. We expect the flash tier to consolidate further (three vendors at the same price is not a stable equilibrium), and the flagship tier to keep widening its price spread until independent, shared-methodology evaluation exists to justify the premium. Until then, the rational default for a price-sensitive adopter is a 1M-context flash model at $0.15, not a flagship.

## Conclusion

China's frontier model landscape in September 2026 is a 19-model, six-lab field defined by three convergences — a 1M-token context default (11 models), a $0.15 flash-tier input price (three labs), and an open-weight default with proprietary exceptions (11 open, 5 closed, 3 undisclosed) — layered over a flagship price spread of an order of magnitude. The takeaway for anyone evaluating the market: openness and price have diverged from raw capability claims, so the practical choice is less "which model is most capable" and more "which price, license and context tier fits the workload," with every benchmark claim treated as vendor-reported until proven otherwise.
