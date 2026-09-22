---
image: "/images/ai/models-deepseek-v4-pro.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: deepseek-v4-pro
model_name: DeepSeek-V4-Pro
provider: deepseek
model_family: DeepSeek-V4
version: "0813"
aliases:
  - deepseek-v4-pro-0813
release_date: "2026-04-24 (V4 Preview) / 2026-08-13 (GA)"
status: deprecated
architecture: "MoE: 1.6T total / 49B active parameters"
parameter_information:
  total_parameters: "1.6T"
  active_parameters: "49B"
context_window: 1048576
maximum_output: 393216
capabilities:
  reasoning: true
  coding: true
  math: true
  vision: false
  tool_calling: true
  function_calling: true
  structured_output: true
open_weight: true
license: MIT
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.66
  output_price_per_1m: 1.98
  currency: USD
  pricing_ref: deepseek
official_api: true
cloud_providers:
  - DeepSeek Platform
regions:
  - unknown
benchmark_results:
  - benchmark: HLE
    score: "42.7 (60.0 with tools)"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench 2.1
    score: 87.9
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE
    score: 62.7
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Agents' Last Exam
    score: 25.7
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
known_limitations:
  - "Deprecation announced 2026-09-10: news page says V4-Pro requests will route to V4.1-Flash after 2026-09-14 until V4.1-Pro launches, but the same-day change log says V4-Pro API service continues with unchanged billing - the official pages conflict"
  - "Vision not supported"
  - "Open-weight HF checkpoint last modified 2026-06-22; unclear whether it matches the 0813 GA checkpoint"
  - "Pricing is peak/off-peak: listed prices are off-peak; peak is 2x"
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek API docs — Models & Pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek-V4 Preview release
    source_url: https://www.deepseek.com/en/news/v4-preview/
    source_type: official
    published_date: "2026-04-24"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V4-Pro
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

DeepSeek-V4-Pro is a 1.6T-parameter MoE (49B active) flagship with MIT open weights, live on the API
since the V4 Preview (2026-04-24) and updated to the 0813 GA checkpoint on 2026-08-13. It supports
thinking (default) and non-thinking modes with reasoning_effort low/high/max, 1M-token context, 384K
maximum output, JSON output and tool calls; vision is not supported.

DeepSeek positions it as open-source SOTA in agentic coding and leading open models in world knowledge,
math/STEM and coding. Deprecation was announced on 2026-09-10 as the V4.1 family rolls out; official
pages conflict on whether V4-Pro API service continues after 2026-09-14 (change log) or is routed to
V4.1-Flash (news page). Off-peak pricing: $0.66 input / $1.98 output per 1M tokens (as of 2026-09-20).
