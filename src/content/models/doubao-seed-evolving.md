---
model_id: doubao-seed-evolving
model_name: Doubao Seed Evolving
provider: bytedance
model_family: Doubao Seed
version: rolling
release_date: "2026-06"
status: active
context_window: 1048576
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
  input_price_per_1m: 6.0
  output_price_per_1m: 30.0
  currency: CNY
  pricing_ref: bytedance
official_api: true
cloud_providers:
  - Volcengine Ark
regions:
  - china
known_limitations:
  - "Rolling model: at least one version update per week; capabilities can change under the same model ID"
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
  - source_name: Ark model release announcements
    source_url: https://docs.volcengine.com/docs/ark/model-release-announcement
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Doubao Seed Evolving is a rolling model from ByteDance, first released in June 2026 and updated at least
once per week under a single stable model ID. ByteDance positions it for agent and coding scenarios. A
July 2026 update raised its context window to 1M tokens.

Official documentation lists the same capability set as Doubao Seed 2.1 Pro: deep thinking, text
generation, multimodal understanding, GUI task handling, tool calling and structured output. Because the
model changes weekly, capability claims and pricing should be re-verified frequently. API pricing is
6.00 CNY input / 30.00 CNY output per 1M tokens, cache hits at 1.20 (as of 2026-09-20).
