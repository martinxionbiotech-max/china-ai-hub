---
model_id: minimax-m2.7-highspeed
model_name: MiniMax-M2.7-Highspeed
provider: minimax
model_family: MiniMax M2.7
release_date: "2026-03-18"
status: active
context_window: 204800
capabilities:
  reasoning: true
  tool_calling: true
  vision: false
open_weight: true
license: "Custom NON-COMMERCIAL license (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution 'Built with MiniMax M2.7' required)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.6
  output_price_per_1m: 2.4
  currency: USD
  pricing_ref: minimax
official_api: true
cloud_providers:
  - MiniMax Platform
regions:
  - china
  - international
known_limitations:
  - "Text-only input; interleaved thinking always on (cannot be disabled via API)"
  - "Must echo full assistant content (thinking blocks) back in multi-turn history"
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax API platform — pay-as-you-go pricing (intl)
    source_url: https://platform.minimax.io/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

MiniMax-M2.7-Highspeed is the same model as MiniMax-M2.7 served at higher throughput (~100 tokens/s,
vendor claim, "same quality, faster"). International pricing is 2x the standard tier: $0.60 input /
$2.40 output per 1M tokens, cache reads $0.06 (as of 2026-09-20).
