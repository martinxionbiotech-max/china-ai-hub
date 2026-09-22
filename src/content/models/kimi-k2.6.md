---
image: "/images/ai/models-kimi-k2.6.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.6
model_name: Kimi K2.6
provider: moonshot-ai
model_family: Kimi K2.6
release_date: "2026-04-20"
status: active
context_window: 262144
capabilities:
  reasoning: true
  vision: true
open_weight: null
api_available: true
pricing:
  input_price_per_1m: 0.95
  output_price_per_1m: 4.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Max output ceiling not stated in the fetched docs (256K context)"
last_verified: "2026-09-20"
sources:
  - source_name: Kimi API platform — model list
    source_url: https://platform.kimi.ai/docs/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API — pricing (chat)
    source_url: https://platform.kimi.ai/docs/pricing/chat
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Kimi K2.6 is Moonshot's visual + text model with thinking and non-thinking modes for dialogue and agent
tasks, in a 256K context window. Pricing is $0.95 input / $4.00 output per 1M tokens (cache hits $0.16,
as of 2026-09-20).
