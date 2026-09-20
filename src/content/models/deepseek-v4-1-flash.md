---
model_id: deepseek-v4-1-flash
model_name: DeepSeek-V4.1-Flash
provider: deepseek
model_family: DeepSeek-V4.1
release_date: "2026-09-10"
status: active
architecture: "552B-parameter MoE; Causal Encoder-Decoder; 8B active parameters on input, 16B on output"
parameter_information:
  total_parameters: "552B"
  active_parameters: "8B (input) / 16B (output)"
context_window: 1048576
maximum_output: 393216
capabilities:
  reasoning: true
  coding: true
  vision: true
  tool_calling: true
  function_calling: true
  structured_output: true
open_weight: true
license: MIT
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.15
  output_price_per_1m: 0.6
  currency: USD
  pricing_ref: deepseek
official_api: true
cloud_providers:
  - DeepSeek Platform
regions:
  - unknown
benchmark_results:
  - benchmark: GPQA Diamond
    score: 90.9
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: HLE
    score: 36.8
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Codeforces
    score: 3471
    metric: rating
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench 2.1
    score: 90.6
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE v1.1
    score: 74.2
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
known_limitations:
  - "Pricing is peak/off-peak: listed prices are off-peak; peak (01:00-04:00 and 06:00-10:00 UTC, Mon-Fri) is 2x"
  - "Benchmarks are vendor-reported using DeepSeek Harness (minimal mode, max effort); not independently verified"
  - "HLE score is on the pure-text subset (39.1 on that subset; 36.8 full)"
  - "Legacy API names deepseek-v4-flash and deepseek-v4-flash-vision-exp route to V4.1-Flash"
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
  - source_name: DeepSeek-V4.1-Flash release announcement
    source_url: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
    source_type: official
    published_date: "2026-09-10"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V4.1-Flash
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

DeepSeek-V4.1-Flash is the current standard DeepSeek API model (`deepseek-flash`), released
2026-09-10 with MIT-licensed open weights. It is the smallest model of the "asymmetric architecture"
V4.1 family: a 552B-parameter MoE that activates only 8B parameters on input and 16B on output.

It has a 1M-token context window, 384K maximum output, and supports thinking (default) and non-thinking
modes, native vision understanding, JSON output and tool calls. DeepSeek claims 1/4 the HBM and 1/8 the
SSD KV-cache storage of the previous generation. API pricing is peak/off-peak: off-peak $0.15 input /
$0.60 output per 1M tokens, with cache hits at $0.003 (as of 2026-09-20).
