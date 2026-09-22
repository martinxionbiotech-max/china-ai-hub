---
title: "Context Windows in China's 2026 Model Market: 1M Tokens as Table Stakes and the Stratification Below It"
description: "An analysis of context-window distribution across 19 Chinese models: the 1M-token flagship norm, the 200K-256K mid tier, the wide output-token spread (131K to 1M), and what the stratification means for long-context workloads and self-hosting."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How do context windows and maximum output tokens distribute across Chinese frontier models in 2026, and what does the tiering reveal about the market's long-context economics?"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - doubao-seed-2-1-pro
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
  - qwen3.8-max
  - kimi-k2.7-code
author_view: true
image: "/images/ai/models-doubao-seed-2-1-pro.webp"
image_credit: "AI-generated illustration (Seedream)"
sources:
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — GLM-5.3 model page"
    source_url: "https://docs.z.ai/guides/llm/glm-5.3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — GLM-5.3-Flash model page"
    source_url: "https://docs.z.ai/guides/vlm/glm-5.3-flash"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Kimi — Kimi K3 release announcement"
    source_url: "https://platform.kimi.ai/docs/release-notes/kimi-k3"
    source_type: official
    published_date: "2026-07-16"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "QwenCloud — Qwen3.8-Max-0902 model page"
    source_url: "https://www.qwencloud.com/models/qwen3.8-max-0902"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Volcengine Ark — Seed 2.1 model docs"
    source_url: "https://docs.volcengine.com/docs/ark/seed-2-1-pro"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "MiniMax API — model documentation"
    source_url: "https://platform.minimax.io/docs/guides/models.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

# Context Windows in China's 2026 Model Market: 1M Tokens as Table Stakes and the Stratification Below It

## Executive Summary

The 1M-token context window has become table stakes for Chinese frontier models in 2026: ten of the nineteen models in the China AI Hub collection record a 1,048,576-token context window, spanning five of six vendors and both the flagship and flash tiers. Below that ceiling, the market stratifies cleanly — a 256K mid tier (Doubao Turbo, Kimi K2.6/K2.7, Qwen3.8-2.4T-A95B) and a 200K legacy tier (MiniMax M2.7) persist for cheaper or older models. The less-discussed dimension is output: maximum output tokens range from 131K (GLM, Qwen) to 1M (Kimi K3), a 7.6x spread that changes which models can actually generate long documents rather than merely accept long contexts. This article maps both dimensions, explains the tiering logic, and flags the verification gaps.

## What We Know

The database records context_window for all nineteen models and maximum_output for ten of them (nine models do not publish an output-token limit — recorded as absent, not as unlimited). The distribution:

**1M context (1,048,576 tokens, ten models):**
- DeepSeek V4.1-Flash (max output 393,216) and V4-Pro (393,216)
- Doubao Seed 2.1 Pro (262,144) and Seed Evolving (262,144)
- GLM-5.2, GLM-5.3 (131,072 each), GLM-5.3-Flash (131,072)
- Kimi K3 (1,048,576)
- MiniMax M3 (max output not published)
- Qwen3.8-Max (131,072) and Qwen3.8-Flash (131,072)

**256K context (four models):** Doubao Seed 2.1 Turbo (262,144), Kimi K2.6, Kimi K2.7-Code, K2.7-Code-Highspeed (output limits not published), Qwen3.8-2.4T-A95B.

**200K context (two models):** MiniMax M2.7 and M2.7-Highspeed.

FACT: 1M context is now the default position for new releases across DeepSeek, ByteDance, Zhipu, Moonshot, MiniMax and Alibaba. Only ByteDance maintains a current-generation model (Turbo) below 1M, deliberately — it is the low-latency tier.

## What the Data Shows

**Finding 1: context tiering now maps to product tiering, not vendor capability.** The 256K/200K models are not failures of capability; they are the cheap or legacy tiers of vendors whose flagships are 1M. MiniMax serves M2.7 at $0.30 alongside M3 at the same price with 1M — the older model's context is a historical artifact, not a pricing signal. The market has not stratified by "who can do long context" (everyone can) but by "where the vendor draws the product line."

**Finding 2: output tokens are the real differentiator.** Among models that publish the limit, the spread is: DeepSeek 393K, Doubao 262K, GLM 131K, Qwen 131K, Kimi K3 1M. A 1M-input model with a 131K output cap (GLM-5.3, Qwen3.8) is not a long-form generation tool; it is a long-input analysis tool. Kimi K3's 1M input / 1M output pairing is unique in the collection — it is the only model documented as capable of generating a million tokens of output, which reframes its $3/$15 pricing: per-token output pricing on a 1M-output model implies a different cost ceiling for any single request than a 131K-output competitor.

**Finding 3: open-weight long context is cheaper but capped.** The open Qwen3.8-2.4T-A95B carries 256K — below its closed sibling's 1M. GLM-5.3-Flash (open, 1M) is the exception that proves the pattern: Zhipu published the open model with the full 1M context, making it the only open-weight 1M-context model in the collection alongside GLM-5.3. Self-hosters chasing long context have a short list.

ANALYSIS: the 1M-input norm and the 131K-1M output spread encode an economic truth: input context is cheap to advertise, output tokens are expensive to serve. Vendors converge on 1M input because the marketing threshold is now there; they diverge on output because output tokens bill at 2-5x input rates and directly consume inference capacity. The output limit is the honest economic parameter.

## What Has Changed

The trajectory from the database's older entries:

- **2025-12 DeepSeek V3.2** and the early 2026 models established the 256K norm. The K2.6 (April 2026) and M2.7 (March 2026) still live there.
- **The 1M shift arrived in a six-week burst** (June-July 2026): MiniMax M3 (06-01), GLM-5.2 (06-16), Doubao Seed 2.1 family (June/September), Kimi K3 (07-16). By September, Qwen3.8-Max/Flash (August) and DeepSeek V4.1-Flash/V4-Pro completed the sweep.
- **Flash models inherited 1M without a price premium.** Qwen3.8-Flash ($0.15/$0.47), GLM-5.3-Flash ($0.15/$0.50) and DeepSeek V4.1-Flash ($0.15/$0.60) all carry 1M at the floor price — long context no longer costs extra at the entry tier.
- **The open-weight 1M option exists** (GLM-5.3, GLM-5.3-Flash) but Alibaba's open A95B remains at 256K — the open long-context crown currently sits with Zhipu.

## Why It Matters

- **For long-document analysis** (legal, financial, codebase review): any of the ten 1M models works, but output caps decide the deliverable. If the deliverable is a summary, 131K output is ample; if it is a generated report longer than ~100K tokens, only DeepSeek (393K) and Kimi K3 (1M) publish enough headroom.
- **For agent workloads**: 1M context plus cache pricing is the agent-economics sweet spot — the flash trio (DeepSeek/Qwen/GLM) all combine 1M with cache-hit discounts, which is why agent tooling has standardized on them.
- **For self-hosting**: the 1M open-weight list is GLM-5.3 (744B/40B) and GLM-5.3-Flash (320B/18B). Nothing else in the collection combines open weights with 1M. This is a real constraint for enterprises that cannot use APIs.
- **For latency-sensitive chat**: ByteDance Turbo's 256K at the low-latency tier shows a vendor explicitly trading context for speed — context and latency are still a trade in production, even if the spec sheet says otherwise.

## Comparison / Evidence

Normalized view by tier:

| Tier | Models | Context | Typical max output |
|---|---|---|---|
| Flagship | V4-Pro, K3, GLM-5.3, M3, Qwen3.8-Max, Seed 2.1 Pro/Evolving | 1M | 131K-1M (K3 outlier) |
| Flash | V4.1-Flash, GLM-5.3-Flash, Qwen3.8-Flash | 1M | 131K-393K |
| Mid / legacy | Turbo, K2.6, K2.7, A95B, M2.7 | 200K-256K | mostly unpublished |

DATA: compiled from context_window and maximum_output fields, verified 2026-09-20. Nine models do not publish maximum_output; the table records those absences rather than estimating.

## Limitations and Uncertainty

Three caveats. (1) **Output limits are under-disclosed**: nine of nineteen models publish no maximum_output; treating absent as "unlimited" would be wrong, so the analysis distinguishes published caps from unknown ones. (2) **Effective context ≠ advertised context**: long-context quality degradation is well documented in the field generally, and no vendor in the collection publishes a needle-in-haystack or long-context benchmark score per model — advertised windows are the vendor's guarantee, not a measured retrieval quality. (3) **Version drift**: Doubao Seed 2.1 Pro's 1M context is documented in the September version; earlier snapshots (260628) may differ, and the database records the latest documented value.

## China AI Hub View

Our assessment: context length has completed its transition from differentiator to baseline — 1M is now the price of entry for any serious 2026 release, available at $0.15 input. The frontier has moved to two secondary battles: output-token headroom (where Kimi K3's 1M stands alone) and the economics of long context under load (where cache pricing and linear-attention architectures matter more than the window number itself). For Q4, the database will watch three signals: whether any vendor pushes beyond 1M input; whether open-weight 1M options expand beyond Zhipu; and whether maximum_output disclosure becomes universal — currently the collection's biggest documentation gap.

## Conclusion

The 2026 Chinese market has standardized on 1M-token input across flagships and flash tiers alike, stratified the budget tier at 256K/200K, and quietly left output tokens as the true differentiator — a 131K-to-1M spread that decides what a model can produce, not just what it can read. Kimi K3's 1M/1M pairing, GLM-5.3-Flash's open-weight 1M, and the flash trio's long-context-at-floor-price are the three structural facts of the current window landscape. Buyers should now select on output caps and self-hosting context, because input context no longer discriminates.

## Sources

See the Sources list in the page metadata — context and output fields trace to official model pages across all six vendors, verified 2026-09-20. All tiering analysis is flagged ANALYSIS/VIEW and derived only from the recorded fields.
