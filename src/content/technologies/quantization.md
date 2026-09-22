---
slug: quantization
title: Quantization
definition: "Quantization compresses model weights and activations from high-precision formats (FP16/BF16) to lower precision (8-bit, 4-bit or mixed), shrinking memory and compute requirements — the standard way to run large models on limited hardware."
related_models:
  - deepseek-v3-2
  - glm-5.2
  - qwen3.8-2.4t-a95b
related_companies:
  - deepseek
  - zhipu-ai
  - alibaba-cloud
related_technologies:
  - inference
  - distillation
related_guides: []
last_verified: "2026-09-22"
sources:
  - source_name: "Frantar et al. — GPTQ: Accurate Post-Training Quantization"
    source_url: "https://arxiv.org/abs/2210.17323"
    source_type: academic
  - source_name: "Lin et al. — AWQ: Activation-aware Weight Quantization"
    source_url: "https://arxiv.org/abs/2306.00978"
    source_type: academic
---

## Technical background

Post-training quantization matured rapidly from 2022 onward: GPTQ (2022) made 4-bit LLMs practical, and AWQ (2023) improved accuracy by protecting salient weights. Today 4-bit and 8-bit formats (GGUF, GPTQ, AWQ, and increasingly FP8 for serving) are the default for local inference and cost-efficient serving.

## How it works

Weights are mapped from 16-bit floats to fewer bits using scaling factors, sometimes with calibration data to find the best mapping per layer. Mixed-precision schemes keep sensitive layers at higher precision. Trade-off: each bit level cut saves roughly proportional memory and bandwidth but adds approximation error, which grows non-uniformly across tasks.

## Why it matters

Quantization decides what hardware can run what model: a 70B model that needs ~140GB at FP16 fits in ~40GB at 4-bit — the difference between a GPU cluster and a workstation. It also dominates serving economics for open-weight models.

## Chinese adoption

Quantization is community infrastructure around Chinese open models rather than a vendor product. The open-weight models in the China AI Hub database — DeepSeek-V3.2 (MIT), GLM-5.2/5.3 (Apache-2.0), Qwen3.8-2.4T-A95B and others — are routinely distributed in community-quantized GGUF/GPTQ/AWQ formats for local deployment. Model pages list license and self-hosting status precisely because quantization is how self-hosting actually happens.

## Major Chinese companies and models

- **DeepSeek** — MIT-licensed open releases (V3.2, V4 line) are prime quantization targets.
- **Zhipu AI** — GLM-5.2/5.3 (Apache-2.0) open weight, self-hostable.
- **Alibaba Cloud** — Qwen3.8-2.4T-A95B open weight (custom MIT-style license); MoE quantization is actively researched because expert layers compress unevenly.

## Practical applications

Local LLM servers, edge and on-device models, cost-efficient API self-hosting, and fitting large models onto single consumer GPUs.

## Limitations

Quality loss is task-dependent and hard to predict (math and long-context degrade faster in some regimes); MoE models quantize unevenly; and evaluation gaps exist below 4-bit. Verify with your own evals, not vendor claims.

## Deployment considerations

Benchmark at the bit level you plan to serve; prefer AWQ/GPTQ for GPU serving and GGUF for CPU/edge; and re-evaluate after any framework upgrade, since kernels change results.

## Future development

FP8/FP4 native training and serving, quantization-aware training loops, and hardware-adaptive mixed precision are making lower precision safer.
