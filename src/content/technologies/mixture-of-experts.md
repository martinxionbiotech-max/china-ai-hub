---
image: "/images/ai/technologies-mixture-of-experts.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: mixture-of-experts
title: Mixture of Experts
author: "SinoAI Hub Research Team"
definition: "Mixture of Experts (MoE) is a model architecture where each layer contains many small 'expert' networks and a router activates only a few per token, so total parameters can scale up while per-token compute stays roughly flat."
related_models:
  - qwen3.8-2.4t-a95b
  - deepseek-v4-pro
  - kimi-k3
  - minimax-m3
  - glm-5.3
related_companies:
  - alibaba-cloud
  - deepseek
  - moonshot-ai
  - minimax
  - zhipu-ai
related_technologies:
  - inference
  - quantization
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "Shazeer et al. — Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
    source_url: "https://arxiv.org/abs/1701.06538"
    source_type: academic
  - source_name: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
    source_url: "https://arxiv.org/abs/2405.04434"
    source_type: academic
  - source_name: "Qwen3 Technical Report (Qwen team)"
    source_url: "https://qwenlm.github.io/blog/qwen3/"
    source_type: official
---

## Technical background

MoE dates to the early 1990s and was revived for deep learning in 2017 by Shazeer et al. at Google. It became central to large language models when DeepSeek-V2 (2024) demonstrated an economical open MoE design that served as the basis for many subsequent Chinese open models.

## How it works

A sparse MoE transformer replaces the feed-forward network in each layer with N experts (each its own FFN) plus a router that scores tokens and picks the top-k experts per token. Total parameters include all experts, but only k experts run per token. The router is trained jointly, with load-balancing losses to avoid expert collapse.

## Why it matters

MoE decouples capacity from compute: a 2.4-trillion-parameter MoE can run with roughly the cost of a dense model an order of magnitude smaller. This is how several Chinese labs reached frontier capability while underlining cost efficiency. It does, however, concentrate memory requirements — all experts must be resident in memory (GPU or CPU offload).

## Chinese adoption

MoE is widely used across the Chinese open-model ecosystem. Alibaba's Qwen line is the clearest public example: Qwen3.5 ships MoE variants such as 397B-A17B, 122B-A10B and 35B-A3B (the A suffix denoting active parameters), and the current Qwen3.8-2.4T-A95B open release continues the pattern. DeepSeek's architecture work on economical MoE training is documented in the DeepSeek-V2 paper. Across the database, most current flagships are MoE: DeepSeek-V4-Pro (1.6T/49B active), Kimi K3 (2.8T/104B active), Qwen3.8-Max (2.4T/95B active), GLM-5.3 (744B/40B active), and MiniMax-M3 (~428B/~23B active).

## Major Chinese companies and models

- **Alibaba Cloud (Qwen)** — Qwen3.5 MoE family (397B-A17B etc.) and Qwen3.8-2.4T-A95B (open weight, custom MIT-style license).
- **DeepSeek** — DeepSeek-V2 introduced the economical MoE design widely adopted afterward.

## Practical applications

Frontier-scale language models at reduced serving cost, dense-tier replacements in latency-sensitive pipelines, and the base architecture behind several flagship reasoning models.

## Limitations

High memory footprint for serving (all experts resident); routing can be unstable under distribution shift; and MoE models are harder to fine-tune and quantize well than dense models of comparable active size.

## Deployment considerations

Plan memory around total parameters, not active parameters. Use MoE-aware serving stacks and vLLM-class runtimes that offload idle experts. Verify quantization quality on MoE specifically, since router and expert quantization interact.

## What the available evidence actually shows

The database directly evidences both MoE's breadth (five of the six companies' flagships are MoE) and its cost logic (DeepSeek-V4-Pro runs 49B active out of 1.6T total — a 3.1% activation ratio — which is why it can list $0.66/$1.98 off-peak). What is harder to evidence is the memory consequence: total parameters still dictate serving memory, so a 2.4T MoE is not a cheap-to-self-host model despite its low activation. China AI Hub analysis indicates MoE is now the default architecture for Chinese frontier flagships because it decouples capability from per-token cost — but the "capability at reduced cost" story must be read alongside the "all experts resident in memory" constraint that the parameter fields make visible.

## Future development

Deeper integration of sparsity with attention (e.g., MiniMax's MSA sparse-attention work), expert specialization, and MoE-aware compression continue to develop. Treat sparsity claims as architecture details, not quality guarantees.

*Labels used above: **Official fact** (from the Shazeer et al. and DeepSeek-V2 papers and the China AI Hub database), **Vendor-reported claim** (architecture and parameter figures published by vendors), and **China AI Hub analysis** (our synthesis, always introduced as such).*
