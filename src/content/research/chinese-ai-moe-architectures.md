---
title: "How Chinese Frontier Models Use Mixture-of-Experts: Active Parameters, Linear Attention and the Economics of Sparsity"
description: "An architecture-level analysis of MoE design across Chinese frontier models in 2026 — activation ratios from 1.4% to 4.3%, hybrid linear-attention variants, and what sparse architectures mean for inference cost, self-hosting and the open-weight ecosystem."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How do Chinese frontier labs design Mixture-of-Experts architectures in 2026, and what do activation ratios and linear-attention hybrids reveal about the economics of serving these models?"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - kimi-k3
  - glm-5.3
  - glm-5.3-flash
  - minimax-m3
  - qwen3.8-max
  - qwen3.8-2.4t-a95b
author_view: true
image: "/images/ai/models-deepseek-v4-pro.webp"
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
  - source_name: "MiniMax API — model documentation"
    source_url: "https://platform.minimax.io/docs/guides/models.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "GitHub — zai-org/GLM-5"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

# How Chinese Frontier Models Use Mixture-of-Experts: Active Parameters, Linear Attention and the Economics of Sparsity

## Executive Summary

Every frontier Chinese model released in 2026 is a Mixture-of-Experts (MoE) architecture, and the China AI Hub models database records the design parameters with unusual completeness. Activation ratios range from 1.4% (DeepSeek V4.1-Flash: 8B active of 552B) to 4.3% (Qwen3.8: 95B active of 2.4T); three labs have shipped hybrid architectures that replace part of the attention stack with linear variants (Qwen's Gated DeltaNet, Kimi's Gated MLA/KDA layers, MiniMax's MiniMax Sparse Attention, GLM-5.3-Flash's sparse-plus-linear combination); and the open-weight ecosystem now exposes these architectures at FP8, MXFP4/MXFP8 and BF16 precisions. This article maps the architecture landscape from the database, explains what the parameter choices mean, and draws out the economic logic — MoE is fundamentally a serving-cost technology, and Chinese labs have pushed it furthest precisely because their market competes on price per token.

## What We Know

The database records architecture fields for nine of the nineteen models; the remaining ten (older or closed models) do not publish architecture details. The documented frontier designs, as of the 2026-09-20 verification pass:

| Model | Total params | Active params | Activation ratio | Attention design |
|---|---|---|---|---|
| DeepSeek V4.1-Flash | 552B | 8B in / 16B out | 1.4% / 2.9% | Causal Encoder-Decoder |
| DeepSeek V4-Pro | 1.6T | 49B | 3.1% | MoE (details not published) |
| Kimi K3 | 2.8T | 104B | 3.7% | 69 KDA + 24 Gated MLA layers, SiTU-GLU |
| GLM-5.3 / 5.2 | 744B | 40B | 5.4% | not published beyond MoE |
| GLM-5.3-Flash | 320B | 18B | 5.6% | sparse + linear attention, mHC hyper-connections |
| MiniMax M3 | ~428B | ~23B | ~5.4% | MiniMax Sparse Attention (MSA) |
| Qwen3.8 (Max / open A95B) | 2.4T | 95B | 4.0% | Gated DeltaNet + Gated Attention hybrid |

FACT: activation ratio is not quality; it is a cost dial. The database records it as reported, and each vendor discloses it selectively — DeepSeek publishes precise active counts for V4.1-Flash (8B on input, 16B on output) but not for V4-Pro beyond "49B active"; Moonshot publishes the fullest architecture card in the collection (expert counts, layer counts, even the vision encoder size); Alibaba publishes the same architecture string for both the open A95B and the closed Max.

## What the Data Shows

Three patterns are legible in the architecture records:

**Pattern 1: activation ratios cluster in two bands.** The cheap-tier models (V4.1-Flash, GLM-5.3-Flash, MiniMax M3) activate 1.4-5.6% of parameters; the flagship tier (V4-Pro, K3, Qwen3.8) activates 3-4.3%. But the clustering is not by tier — it is by release date. The newest models are the sparsest. V4.1-Flash at 1.4% activation is the most extreme example: only 8B parameters compute on each input token. This matters for inference cost because active parameters, not total parameters, determine per-token FLOPs.

**Pattern 2: linear attention is replacing part of the dense attention stack.** Four documented designs move in the same direction: Qwen3.8's Gated DeltaNet + Gated Attention hybrid; Kimi K3's 69 KDA (Kimi Delta Attention) layers alongside 24 Gated MLA layers; MiniMax's MSA with claimed 9x prefill / 15x decode speedups at 1M context; GLM-5.3-Flash described as the first open-source frontier model combining sparse and linear attention with mHC hyper-connections. This is an architectural answer to the long-context economics problem: quadratic attention at 1M context is the dominant serving cost, and linear variants trade some fidelity for scaling.

**Pattern 3: precision is now part of the open-release spec.** GLM-5.3 ships open weights in FP8 (with BF16 also released); Kimi K3 ships MXFP4 weights with MXFP8 activations; GLM-5.2 lists BF16/FP8. Open releases are no longer single-precision artifacts — they are published with the precision that makes self-hosting affordable, and the precision choice is itself an architecture statement.

ANALYSIS: the deeper pattern is that Chinese labs treat architecture as a pricing strategy. A 1.4% activation model at $0.15 input is not an accident of design taste; it is the engineering path to a margin at a price point that would be loss-making at higher activation. The MoE/linear-attention convergence across four independent labs is best read as market pressure converging on the same engineering answer.

## What Has Changed

Compared with the 2024-2025 baseline recorded in the database's older models, the shift is measurable:

- **2024-style dense and early-MoE models** (K2.6, M2.7 families at 256K/200K context) did not publish architecture details at all — architecture transparency was not yet a release norm.
- **2026 models publish architecture at release.** Moonshot's K3 card (896 experts, 16 selected + 2 shared per token, 93 layers, MoonViT-V2 encoder at 401M) is the most detailed in the collection and arrived with the model announcement.
- **Sparse-plus-linear shipped as open weights.** GLM-5.3-Flash (320B/18B, 30T-token multimodal pre-training) made the hybrid architecture open-source in August 2026; the older GLM-5.2, also open, is conventional in comparison.
- **Expert counts scaled to 512-896.** Qwen3.8: 512 experts, 10 routed + 1 shared per token; Kimi K3: 896 experts, 16 selected + 2 shared. Finer expert granularity is the dominant 2026 design trend.

## Why It Matters

For four audiences, the architecture data changes decisions:

- **API buyers**: active-parameter count is a leading indicator of inference cost sustainability. A provider serving 104B active parameters (K3) at $3/$15 and one serving 8-16B active (V4.1-Flash) at $0.15/$0.60 are in different cost structures — which predicts different long-run price floors.
- **Self-hosters**: the open releases now carry precision metadata (FP8, MXFP4/MXFP8) that directly determines hardware requirements. GLM-5.3-Flash's 320B/18B sparse+linear design is documented by Zhipu as deployable on far fewer GPUs than its 744B siblings — the architecture is the self-hosting pitch.
- **Long-context users**: at 1M context, the attention design (MSA, KDA, DeltaNet) is what keeps latency and cost workable. The 9x/15x speedup claims are vendor-reported, but the architectural direction is consistent across labs and independently observable in release notes.
- **Researchers**: the collection now documents enough of the design space (activation ratios, expert topologies, attention hybrids, precision) to support comparative analysis that was impossible when vendors published nothing.

## Comparison / Evidence

The cleanest cross-lab comparison normalizes on what each lab discloses. Moonshot discloses the most (experts, layers, attention split, encoder, precision); DeepSeek discloses active counts but not expert topology; Alibaba reuses one architecture string across open and closed models; ByteDance discloses nothing (Doubao Seed models are closed with no architecture fields). This disclosure gradient correlates with openness strategy: labs that release weights publish architecture cards; labs that sell only APIs publish benchmarks instead.

DATA: all figures in this article are taken from the China AI Hub models collection architecture and capabilities fields, captured from official pages and repos on 2026-09-20. Claimed speedups (MiniMax 9x/15x) and the GLM-5.3-Flash "first open-source frontier sparse+linear" designation are vendor statements and are recorded as such.

## Limitations and Uncertainty

Three honest caveats. (1) **Disclosure is uneven**: ten of nineteen models publish no architecture data; every cross-lab comparison here is conditioned on what vendors chose to disclose. (2) **Activation asymmetry**: DeepSeek's 8B-in/16B-out asymmetry is the only published input/output activation split; other labs report a single number, so ratios are not perfectly comparable across vendors. (3) **Claims vs measurements**: speedup multiples and "first" designations are vendor-reported; no independent third-party measurement of these architectures exists in the collection's sources.

## China AI Hub View

Our assessment: MoE with aggressive sparsity and linear-attention hybrids is the signature engineering pattern of China's 2026 frontier, and it exists because the market prizes token economics above everything else. The open-weight releases of GLM-5.3-Flash and Qwen3.8-2.4T-A95B mean the architecture itself is now inspectable — a development with no US parallel at this scale in 2026. The strategic question for the rest of the year is whether the sparsity frontier (sub-1.5% activation, as in V4.1-Flash) becomes the new normal for flash tiers, and whether linear-attention hybrids hold up quality-wise as context windows stretch further. The database will track both questions via the architecture field as vendors publish updates.

## Conclusion

Chinese frontier models in 2026 are built on three converging architectural decisions: MoE with activation ratios between 1.4% and 5.6%; hybrid attention stacks that replace part of dense attention with linear variants; and precision-aware open releases (FP8/MXFP4/MXFP8) that make the sparsity self-hostable. The convergence is not coincidence — it is the engineering expression of a market that competes on price per token. The data allows one confident prediction: the next generation of Chinese frontier models will activate a smaller share of total parameters than the last, and the open-weight releases will document it.

## Sources

See the Sources list in the page metadata — architecture fields trace to official model pages (DeepSeek, Z.ai, Kimi platform, QwenCloud, MiniMax platform) and the GLM-5 GitHub repository, verified 2026-09-20. All benchmark-adjacent claims are flagged vendor-reported.
