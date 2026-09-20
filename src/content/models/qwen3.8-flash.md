---
model_id: qwen3.8-flash
model_name: Qwen3.8-Flash
provider: alibaba-cloud
model_family: Qwen3.8
release_date: "2026-08"
status: active
context_window: 1048576
maximum_output: 131072
capabilities:
  reasoning: true
  vision: true
  video: true
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 0.15
  output_price_per_1m: 0.47
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
known_limitations:
  - "Batch inference not supported"
  - "Prices differ by region: Singapore $0.15/$0.47; Beijing and Global regions $0.113/$0.382 per 1M tokens"
  - "Architecture details not published on the fetched official pages"
last_verified: "2026-09-20"
sources:
  - source_name: Model Studio — qwen3.8-flash model detail
    source_url: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Model Studio — model pricing
    source_url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Qwen3.8-Flash is the lightweight, low-cost model of the Qwen3.8 family: 1M-token context (991,808 max
input, 131,072 max output), multimodal input (image, text, video) with text output, and context caching.
Alibaba states it is fully compatible with both OpenAI and Anthropic API protocols.

Pricing: Singapore $0.15 input / $0.47 output per 1M tokens; Beijing and other Global regions
$0.113 / $0.382 (as of 2026-09-20). Batch inference is not supported.
