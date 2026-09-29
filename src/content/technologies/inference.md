---
image: "/images/ai/technologies-inference.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: inference
title: Inference
author: "SinoAI Hub Research Team"
definition: "Inference is the process of running a trained model to generate outputs — and, as a discipline, the engineering of making that process fast and cheap through attention optimizations, caching, and serving systems."
related_models:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - minimax-m3
related_companies:
  - deepseek
  - minimax
related_technologies:
  - quantization
  - mixture-of-experts
  - long-context
related_guides: [open-weight-vs-api]
last_verified: "2026-09-22"
sources:
  - source_name: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
    source_url: "https://arxiv.org/abs/2405.04434"
    source_type: academic
  - source_name: "Kwon et al. — PagedAttention (vLLM)"
    source_url: "https://arxiv.org/abs/2309.06180"
    source_type: academic
---

## Technical background

Inference used to be an afterthought to training; it is now where most production cost lives. The modern stack — continuous batching, paged KV-cache (PagedAttention/vLLM), speculative decoding, prefix caching — came out of 2023-2024 serving research. Attention architecture itself became an inference-optimization target: DeepSeek-V2's Multi-head Latent Attention (MLA) cut KV-cache size dramatically, a design now common in Chinese models.

## How it works

The key resources: prefill (processing the prompt) and decode (generating tokens one at a time). Serving systems batch many requests together, manage KV-cache in paged memory, reuse cached prefixes across requests, and trade latency against throughput. Long context multiplies KV-cache cost, which is exactly what MLA-style compressed attention attacks.

## Why it matters

Inference economics decide API prices, and API prices decide what gets built. The Chinese API market's price competition (DeepSeek-V4.1-Flash lists $0.15/1M input tokens, GLM-5.3-Flash $0.15/1M input in our database) is, at root, an inference-engineering competition. DeepSeek's off-peak discount model — where listed prices are off-peak and peak windows bill 2x — is itself an inference-capacity-management decision, not just a marketing one.

## Chinese adoption

Chinese labs have led on open inference infrastructure. DeepSeek's open project list includes FlashMLA, DeepGEMM and DeepEP — kernel and communication libraries released alongside their models — plus 3FS, a distributed filesystem for training/inference clusters. DeepSeek-V2's MLA attention is cited in its own paper and widely adopted. On the serving side, vLLM-class runtimes are the community default for open-weight Chinese models.

## Major Chinese companies and models

- **DeepSeek** — MLA attention (V2 paper); FlashMLA/DeepGEMM/DeepEP/3FS open infrastructure projects; V4-Pro and V4.1-Flash list 1M-token context and 393K max output.
- **MiniMax** — MSA sparse attention (open project list) targets long-context serving efficiency.

## Practical applications

API cost management, self-hosted open-model serving, batch/off-peak processing (DeepSeek lists off-peak discounts), and edge deployment of quantized models.

## Limitations

Serving optimizations are workload-dependent; prefix caching helps repetitive prompts but not diverse ones; and vendor "tokens per second" claims are meaningless without batch-size and hardware context.

## Deployment considerations

Choose runtime by workload (vLLM for GPU serving, llama.cpp-family for CPU/edge); enable prefix caching for agent loops with stable system prompts; and measure end-to-end cost per completed task.

## What the available evidence actually shows

The database records the artifacts of inference engineering — MLA attention (DeepSeek-V2 paper), open kernels (FlashMLA/DeepGEMM/DeepEP), MSA sparse attention (MiniMax), and the resulting price floor ($0.15/1M input on two flash models). What it does not record is throughput: the database has no tokens-per-second or batch-size field, because vendor t/s claims are not comparable without hardware and batch context. China AI Hub analysis indicates price is the database's most reliable inference-economics signal — architecture and kernels explain why the price floor exists, but any throughput comparison would require controlled benchmarking the database deliberately does not perform.

## Future development

Expect attention compression (MLA/MSA-style) to spread, speculative decoding as default, and disaggregated prefill/decode serving across fleets.

*Labels used above: **Official fact** (from the DeepSeek-V2 and PagedAttention papers and the China AI Hub database), **Vendor-reported claim** (pricing and speedup figures), and **China AI Hub analysis** (our synthesis, always introduced as such).*
