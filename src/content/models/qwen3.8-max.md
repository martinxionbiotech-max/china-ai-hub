---
image: "/images/ai/models-qwen3.8-max.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: qwen3.8-max
model_name: Qwen3.8-Max
provider: alibaba-cloud
model_family: Qwen3.8
version: "0902"
aliases:
  - qwen3.8-max-0902
  - qwen3.8-max-2026-09-02
release_date: "2026-08"
status: active
architecture: "2.4T-parameter MoE, 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, Gated DeltaNet + Gated Attention hybrid"
parameter_information:
  total_parameters: "2.4T"
  active_parameters: "95B"
context_window: 1048576
maximum_output: 131072
capabilities:
  reasoning: true
  coding: true
  vision: true
  video: true
  tool_calling: true
  structured_output: true
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 2.0
  output_price_per_1m: 6.0
  currency: USD
  pricing_ref: alibaba-cloud
official_api: true
cloud_providers:
  - Alibaba Cloud
regions:
  - china-beijing
  - singapore
  - hong-kong
  - germany-frankfurt
  - us-virginia
  - japan-tokyo
benchmark_results:
  - benchmark: Terminal-Bench 2.1
    score: 86.6
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: SWE-bench Pro
    score: 67.7
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: GPQA Diamond
    score: 92.6
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: HLE
    score: "43.6 (56.2 with tools)"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: MRCR v2 256K
    score: 92.9
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
known_limitations:
  - "Closed API model (the open Qwen3.8-2.4T-A95B weights are text-only and thinking-only - not the same product)"
  - "Exact API release date not stated; the 0902 snapshot is dated 2026-09-02"
  - "Prices differ by region: Singapore $2/$6; Beijing and Global regions $1.65/$4.951 per 1M tokens"
  - "Benchmarks are from the vendor model card (Qwen3.8-Max column); not independently verified"
last_verified: "2026-09-20"
sources:
  - source_name: Model Studio — qwen3.8-max model detail
    source_url: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Model Studio — model pricing
    source_url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — Qwen3.8-2.4T-A95B
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Qwen3.8-Max is Alibaba's flagship API model: a 2.4T-parameter MoE (95B activated) with a 1M-token context window, released August 2026 (0902 snapshot dated 2026-09-02). **Why it matters.** It is the closed-weight flagship of the Qwen line, positioned against DeepSeek-V4-Pro and Kimi K3, and one of the strongest coding models in the database on vendor numbers. **Key characteristics.** 1M context (991,808 max input), 131,072 max output, 262,144 max chain-of-thought, image/text/video input with text output, thinking and non-thinking modes, function calling, structured outputs, web search, prefix completion, context caching and batch inference. **What a professional should know.** It is a closed API model — the open Qwen3.8-2.4T-A95B weights are a different, text-only, thinking-only product — and fine-tuning is not supported. Prices differ by region.

## Architecture and parameters

Qwen3.8-Max is a 2.4T-parameter MoE with 95B activated (~4.0%), 512 experts (10 routed + 1 shared per token), 92 layers, and a Gated DeltaNet + Gated Attention hybrid. The DeltaNet/linear-attention component is Alibaba's long-context answer, analogous to Kimi's KDA and MiniMax's MSA — it replaces part of the quadratic attention stack so 1M context stays economical. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 1M context (991,808 max input) with a 131,072 output cap places Qwen3.8-Max firmly in the long-input-analysis camp rather than long-form generation. The 262,144 max chain-of-thought is a notable documented ceiling — long internal reasoning can run nearly twice the output cap. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

Singapore $2 input / $6 output per 1M tokens; Beijing and other Global regions $1.65 / $4.951. The 3x input-to-output ratio and ~18% region spread are the operative facts: where you are billed from changes cost meaningfully, and output tokens dominate. Context caching and batch inference (Beijing only) are the levers for reducing effective cost. See the [DeepSeek comparison](/comparisons/deepseek-v4-pro-vs-qwen38-max/) and [GLM-5.3 comparison](/comparisons/qwen38-max-vs-glm-53/).

## API, coding, and agent implications

The 0902 snapshot upgraded coding and vision. Vendor-reported Terminal-Bench 2.1 (86.6), SWE-bench Pro (67.7), GPQA Diamond (92.6), HLE 43.6 (56.2 with tools) and MRCR v2 256K (92.9) describe a strong all-round flagship with particular strength in long-context retrieval (MRCR). Function calling, structured outputs and web search make it a complete agent substrate. No fine-tuning is a hard constraint for domain-specialization strategies. See [Qwen agent](/agents/qwen-agent/) and [Qwen Code](/agents/qwen-code/).

## Open weights and license

Closed weight, proprietary license, no self-hosting. The open Qwen3.8-2.4T-A95B exists but is explicitly not the same product: text-only and thinking-only. Teams that need open weights for the Qwen line must accept those differences or use the API. See [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

All five rows are vendor-reported from the Qwen3.8-Max column of the model card. GPQA Diamond 92.6 and HLE 43.6 track the flagship reasoning ceiling; MRCR v2 92.9 is a 256K long-context retrieval metric, not a full-1M measure; Terminal-Bench 86.6 is an agentic-coding signal. Scores are from the vendor card, not independent re-measurement.

## What the benchmarks do not prove

Vendor-card numbers do not independently verify Qwen3.8-Max against competitors, and cross-vendor comparison is invalid without matching benchmark versions and harnesses. The exact API release date is also unstated — only the 0902 snapshot date is known — so version-drift caveats apply. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** general flagship work — coding, reasoning, long-context retrieval, multimodal input analysis, and agent workflows needing function calling and structured output. **Less suited:** fine-tuning or custom-domain specialization (unsupported), open-weight/self-hosting requirements, and budget work better served by the flash tier.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | High |
| Structured API workflows | High |
| Agent orchestration | High |
| Local self-hosted deployment | No evidence |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | High |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates Qwen3.8-Max is Alibaba's most complete closed flagship: competitive coding scores, a full agent toolkit, six serving regions, and a 1M window — at the cost of closed weights, no fine-tuning, and a region-dependent price. Its long-context strength (MRCR 92.9) and Gated DeltaNet architecture position it for retrieval-heavy and long-document workloads, while the open A95B's text-only/thinking-only limits mean Alibaba keeps the truly multimodal flagship behind the API. For API-only buyers it is a strong generalist; for fine-tuning or self-hosting teams it is the wrong tool.

## Market position and outlook

China AI Hub analysis indicates Qwen3.8-Max is the centerpiece of Alibaba's hybrid strategy: the database records Alibaba as keeping its two API flagships (Qwen3.8-Max and Qwen3.8-Flash) closed while releasing one open-weight model (Qwen3.8-2.4T-A95B), a pattern distinct from the fully-open Zhipu/DeepSeek and the fully-closed ByteDance. The six documented serving regions — Beijing, Singapore, Hong Kong, Frankfurt, US-Virginia and Tokyo — are the broadest regional footprint in the collection, which matters for data-residency and latency-sensitive international deployments. The ~18% region price spread ($1.65 vs $2.00 input) means region selection is itself a cost decision, and the Gated DeltaNet hybrid positions the model for the retrieval-heavy workloads where its MRCR v2 score is strongest. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [MoE architectures](/research/chinese-ai-moe-architectures/) research.

## What is uncertain

- The exact API release date is not stated; only the 0902 snapshot date (2026-09-02) is known.
- Benchmark scores come from the vendor model card and are not independently verified.
- The open Qwen3.8-2.4T-A95B weights are a different product (text-only, thinking-only), not this model.

## Sources

- [Model Studio — qwen3.8-max model detail](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- [Model Studio — model pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)
- [Hugging Face model card — Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores published by Alibaba), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
