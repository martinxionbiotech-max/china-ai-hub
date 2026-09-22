---
title: "Multimodal Capability in China's 2026 Model Lineup: Vision, Video and the Computer-Use Frontier"
description: "A capability-map of multimodal support across 19 Chinese models in September 2026 — which flagships see, which generate video, where computer-use lives, and the counterintuitive pattern that cheap flash models are now more multimodal than some flagships."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "Which Chinese frontier models actually support vision, video and computer-use in 2026, and how does multimodal capability distribute across price tiers and vendors?"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - doubao-seed-2-1-pro
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
  - qwen3.8-max
  - qwen3.8-flash
author_view: true
image: "/images/ai/models-glm-5.3-flash.webp"
image_credit: "AI-generated illustration (Seedream)"
sources:
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — GLM-5.3-Flash model page"
    source_url: "https://docs.z.ai/guides/vlm/glm-5.3-flash"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — GLM-5.3 model page"
    source_url: "https://docs.z.ai/guides/llm/glm-5.3"
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
---

# Multimodal Capability in China's 2026 Model Lineup: Vision, Video and the Computer-Use Frontier

## Executive Summary

The China AI Hub models collection records capability flags for nineteen models across six vendors, and the multimodal map for September 2026 contains a counterintuitive finding: **multimodality has migrated downward in the price stack**. The cheapest tiers are now among the most capable — DeepSeek V4.1-Flash sees images while the flagship V4-Pro does not; GLM-5.3-Flash carries vision, video and computer-use while the pricier GLM-5.3 is text-only; Qwen3.8-Flash records video input at $0.15 while the open Qwen3.8-2.4T-A95B lists no vision flag. Only four models in the collection carry the computer_use flag, and three of them are ByteDance's. This article maps who sees what, explains the inversion pattern, and flags what the database cannot yet verify.

## What We Know

As of the 2026-09-20 verification pass, the capability flags distribute as follows (models with any multimodal flag listed):

**Vision (image input):** deepseek-v4-1-flash, doubao-seed-2-1-pro, doubao-seed-2-1-turbo, doubao-seed-evolving, glm-5.3-flash, kimi-k2.6, kimi-k3, minimax-m3, qwen3.8-flash, qwen3.8-max.

**Video (video input):** glm-5.3-flash, kimi-k3, minimax-m3, qwen3.8-flash, qwen3.8-max.

**Computer use (GUI operation):** doubao-seed-2-1-pro, doubao-seed-2-1-turbo, doubao-seed-evolving, glm-5.3-flash.

**No vision:** deepseek-v4-pro, glm-5.2, glm-5.3, kimi-k2.7-code, kimi-k2.7-code-highspeed, minimax-m2.7, minimax-m2.7-highspeed.

FACT: ten of nineteen models have vision; five have video input; four have computer use. Every model with computer_use also has vision and agent_capability — computer use sits on top of a full perception stack, never standalone.

## What the Data Shows

**Finding 1: the flagship/vision inversion.** DeepSeek's $0.66 flagship V4-Pro is text-only while its $0.15 V4.1-Flash sees images. GLM-5.3 ($1.40) is text-only while GLM-5.3-Flash ($0.15) has vision, video and computer use. In both cases the vendor's reasoning-specialized flagship predates or deliberately omits the multimodal stack, and the newer cheap model inherits the full capability set. The old assumption — pay more, get more modalities — is now falsified at two of six vendors.

**Finding 2: video input is the rarest mainstream flag.** Five models record video: GLM-5.3-Flash, Kimi K3, MiniMax M3, Qwen3.8-Flash, Qwen3.8-Max. Qwen is the only vendor where both its flash and flagship carry video. ByteDance's models — despite the vendor's Seedance video-generation product line — do not record video-input flags on the chat models in the collection. Video input and video generation are different capabilities and the database tracks them separately.

**Finding 3: computer use is a ByteDance stronghold.** Three of the four computer_use models are Doubao Seed (Pro, Turbo, Evolving); the fourth is GLM-5.3-Flash. No DeepSeek, Moonshot, MiniMax or Alibaba model in the collection records computer_use as of this date — though DeepSeek Harness and Qwen Qoder deliver agent behavior through product layers rather than a model-level flag. The distinction matters: a computer-use flag describes model-level capability; an agent product can orchestrate screen control with a text model plus external tooling.

ANALYSIS: the multimodal map reflects two different product theories. Vendors that ship open weights (Zhipu, Moonshot, MiniMax) treat multimodality as a spec to publish per model. Vendors that sell closed APIs treat capabilities as product releases — ByteDance's Seed family updates capability through version snapshots (260628 → 260915) rather than new model cards. The flag set is therefore not a pure capability map; it is a capability map filtered through disclosure policy.

## What Has Changed

The trajectory from the database's older models to the 2026 frontier:

- **K2.6 (2026-04)** had vision at 256K context — Moonshot's last vision model before K3 unified vision + video + 1M context in July.
- **GLM-5.2 (2026-06)** shipped text-only; ten weeks later GLM-5.3-Flash shipped vision + video + computer use in the cheapest tier. Zhipu's multimodal stack moved from premium to entry-level in a single generation.
- **MiniMax M3 (2026-06)** brought video input to the MiniMax line; the M2.7 predecessors are text-only.
- **DeepSeek's first vision API model arrived in the flash tier** (V4.1-Flash, 2026-09-10), not the flagship — the vendor's pricing strategy and capability strategy point the same way: vision is now baseline, so it ships where volume is.

## Why It Matters

Practical implications for builders:

- **If you need vision at minimum cost**, the candidates are DeepSeek V4.1-Flash and GLM-5.3-Flash — both $0.15 input with vision, and GLM adds video and computer use. There is no reason to pay flagship prices for image understanding in this market.
- **If you need video input**, the field is Qwen3.8 (Max or Flash), Kimi K3 and MiniMax M3. GLM-5.3-Flash is the budget option. Qwen3.8-Max's Singapore price of $2/$6 is the premium end; Qwen3.8-Flash at $0.15/$0.47 is the cheapest video-capable API in the collection.
- **If you need computer use**, the model-level options are the Doubao Seed family (Ark platform, China region, CNY pricing) and GLM-5.3-Flash (international USD pricing, open weights). The two are not substitutes — they live on different platforms with different licensing.
- **If you assumed flagships are the most capable**, re-check: at DeepSeek and Zhipu the cheapest tier now carries the broadest modality set. Capability selection is per-model, not per-tier.

## Comparison / Evidence

Cross-vendor modality matrix (from DB capability flags, 2026-09-20):

| Vendor | Vision | Video | Computer use | Notes |
|---|---|---|---|---|
| DeepSeek | Flash only | none | none | flagship text-only |
| Alibaba | Flash, Max | Flash, Max | none | open A95B: no vision flag |
| ByteDance | Pro, Turbo, Evolving | none on chat models | Pro, Turbo, Evolving | Seedance covers generation |
| Moonshot | K2.6, K3 | K3 | none | K3 unifies all |
| MiniMax | M3 | M3 | none | M2.7 line text-only |
| Zhipu | Flash | Flash | Flash | flagship 5.3 text-only |

DATA: compiled from per-model capability fields in the China AI Hub models collection. Every flag traces to an official model page or repo. Absence of a flag is recorded as absence in the source, not as verified non-capability — vendors that do not publish a flag may still expose the capability through products.

## Limitations and Uncertainty

Three cautions. (1) **Flag absence ≠ capability absence**: a model without a vision flag (e.g., Qwen3.8-2.4T-A95B) may still accept image input in some product surfaces; the database records what official pages state. (2) **Computer-use flags are model-level declarations**: agent products can deliver screen control without a model-level computer_use flag, so the flag map undercounts the practical agent landscape (which the agents collection covers separately). (3) **Flag granularity varies**: some vendors enumerate modalities in free text (Qwen's "image, text and video" appears in prose, not a structured list) — the database normalizes conservatively and may lag a vendor's latest silent capability additions.

## China AI Hub View

Our assessment: multimodal capability in China's 2026 market is best described as **baseline, not premium**. Vision has settled into the flash tier at two vendors; video is spreading at $0.15-2.00; computer use remains the only genuinely scarce flag, concentrated at ByteDance and Zhipu. The strategic reading is that Chinese vendors are using modality breadth to differentiate cheap models rather than to justify expensive ones — the opposite of the Western pattern. For the database, the monitoring question for Q4 2026 is whether computer_use spreads beyond its current four models, and whether ByteDance ever publishes architecture or modality documentation comparable to what open-weight vendors disclose.

## Conclusion

The 2026 Chinese model lineup inverts the old capability hierarchy: the cheapest models are now the most multimodal, vision is a baseline feature of the flash tier, video input is the practical frontier (five models), and computer use is the scarce capability (four models, three of them Doubao). Buyers who select models by tier instead of by flag will systematically overpay for multimodality at DeepSeek and Zhipu. The correct selection procedure in this market is flag-first: define the modality, then find the cheapest model that carries it — which, increasingly, is a flash model.

## Sources

See the Sources list in the page metadata — capability flags trace to official model pages and pricing pages for all six vendors, verified 2026-09-20. All interpretive claims are separated as ANALYSIS/VIEW; factual claims derive only from the recorded flags.
