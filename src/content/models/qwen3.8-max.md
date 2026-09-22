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

Qwen3.8-Max is Alibaba's flagship API model: a 2.4T-parameter MoE (95B activated) with a 1M-token
context window (991,808 max input), 131,072 max output and 262,144 max chain-of-thought. Input
modalities are image, text and video; output is text. It supports thinking and non-thinking modes,
function calling, structured outputs, web search, prefix completion, context caching and batch
inference (Beijing only).

The 0902 snapshot (2026-09-02) upgraded coding and vision. API pricing: Singapore $2 input / $6 output
per 1M tokens; Beijing and other Global regions $1.65 / $4.951 (as of 2026-09-20). Fine-tuning is not
supported.
