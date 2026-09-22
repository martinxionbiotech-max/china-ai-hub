---
image: "/images/ai/models-kimi-k2.7-code-highspeed.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.7-code-highspeed
model_name: Kimi K2.7 Code Highspeed
provider: moonshot-ai
model_family: Kimi K2.7
status: active
context_window: 262144
capabilities:
  reasoning: true
  coding: true
open_weight: null
api_available: true
pricing:
  input_price_per_1m: 1.9
  output_price_per_1m: 8.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Thinking is always on; temperature/top_p/n/penalties are fixed and must not be passed"
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

Kimi K2.7 Code Highspeed is the same model as `kimi-k2.7-code` served at higher throughput: ~180
tokens/s output, up to 260 tokens/s in short contexts. Pricing is doubled vs. the standard tier: $1.90
input / $8.00 output per 1M tokens (cache hits $0.38, as of 2026-09-20).
