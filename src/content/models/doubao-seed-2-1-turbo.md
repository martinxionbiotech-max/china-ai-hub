---
image: "/images/ai/models-doubao-seed-2-1-turbo.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: doubao-seed-2-1-turbo
model_name: Doubao Seed 2.1 Turbo
provider: bytedance
model_family: Doubao Seed
version: "260628"
aliases:
  - doubao-seed-2-1-turbo-260628
release_date: "2026-06"
status: active
context_window: 262144
maximum_output: 262144
capabilities:
  reasoning: true
  vision: true
  tool_calling: true
  structured_output: true
  agent_capability: true
  computer_use: true
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 3.0
  output_price_per_1m: 15.0
  currency: CNY
  pricing_ref: bytedance
official_api: true
cloud_providers:
  - Volcengine Ark
regions:
  - china
known_limitations:
  - "API served from cn-beijing region only; no international endpoint verified as of 2026-09-20"
  - "No open-weight release; no self-hosting"
last_verified: "2026-09-20"
sources:
  - source_name: Ark official model list
    source_url: https://docs.volcengine.com/docs/ark/model-list?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark official model pricing
    source_url: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Doubao Seed 2.1 Turbo is the lower-priced variant of ByteDance's Seed 2.1 family, with a 256K-token
context window and the same documented capability set as the Pro model (deep thinking, text generation,
multimodal understanding, GUI task handling, tool calling, structured output).

API pricing is half that of the Pro model: 3.00 CNY input / 15.00 CNY output per 1M tokens, cache hits
at 0.60 (as of 2026-09-20). A higher-priced low-latency tier (6.00 / 30.00) is also listed on the
official pricing page.
