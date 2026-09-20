---
model_id: doubao-seed-2-1-pro
model_name: Doubao Seed 2.1 Pro
provider: bytedance
model_family: Doubao Seed
version: "260915"
aliases:
  - doubao-seed-2-1-pro-260915
  - doubao-seed-2-1-pro-260628
release_date: "2026-09"
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
benchmark_results:
  - benchmark: Code Arena Frontend
    score: "1539 (rank 8)"
    metric: arena score
    model_version: "Seed 2.1 (preview)"
    date: "2026-06-23"
    source_type: vendor_reported
    source_url: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity
known_limitations:
  - "API served from cn-beijing region only; no international endpoint verified as of 2026-09-20"
  - "No open-weight release; no self-hosting"
  - "Exact release day for the 260915 version not officially stated (month 2026-09 only)"
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
  - source_name: ByteDance Seed official blog — Seed 2.1 release
    source_url: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity
    source_type: official
    published_date: "2026-06-23"
    last_verified: "2026-09-20"
    confidence: high
---

Doubao Seed 2.1 Pro is ByteDance's flagship text model, served through the Volcengine Ark API in the
cn-beijing region. The 260915 version supports a 1M-token context window, which ByteDance positions for
long-running agent tasks, asynchronous sub-task verification, multimodal understanding, deep research,
tool execution, cross-application office workflows and coding.

The official model list documents deep thinking, text generation, multimodal understanding (image,
video and PDF input), GUI task handling, tool calling and structured output (json_schema). As with all
Doubao Seed API models, no downloadable weights are offered. API pricing is tiered in CNY per 1M tokens:
6.00 input / 30.00 output, with cache hits billed at 1.20 (as of 2026-09-20).
