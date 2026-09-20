---
model_id: kimi-k2.7-code
model_name: Kimi K2.7 Code
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
  input_price_per_1m: 0.95
  output_price_per_1m: 4.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Thinking is always on; temperature/top_p/n/penalties are fixed and must not be passed"
  - "Max output ceiling not stated in the fetched docs (256K context)"
  - "No open-weight release confirmed for K2.7 series"
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

Kimi K2.7 Code is Moonshot's dedicated coding model with a 256K context window and always-on thinking.
Pricing is $0.95 input / $4.00 output per 1M tokens (cache hits $0.19, as of 2026-09-20).

A highspeed variant (`kimi-k2.7-code-highspeed`, same model, ~180 tokens/s output) is priced at
$1.90 / $8.00.
