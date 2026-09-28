---
image: "/images/ai/models-minimax-m2.7-highspeed.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: minimax-m2.7-highspeed
model_name: MiniMax-M2.7-Highspeed
provider: minimax
model_family: MiniMax M2.7
canonical_model: minimax-m2.7
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
  - "Parameter counts are not published in the official MiniMax-M2.7 model card (HF)"
  - "Text-only input; interleaved thinking always on (cannot be disabled via API)"
  - "Must echo full assistant content (thinking blocks) back in multi-turn history"
last_verified: "2026-09-27"
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

MiniMax-M2.7-Highspeed is the same model as [MiniMax-M2.7](/models/minimax-m27/) served at higher
throughput (~100 tokens/s, vendor claim — "same quality, faster"). International pricing is 2x the
standard tier: $0.60 input / $2.40 output per 1M tokens, cache reads $0.06 (as of 2026-09-20).

## How it differs from MiniMax-M2.7

The only documented differences are **throughput and price**. The standard M2.7 serves at ~60 tokens/s
at $0.30 / $1.20; the Highspeed variant serves at ~100 tokens/s at exactly 2x the price ($0.60 /
$2.40). Parameter counts, context window (204,800 tokens) and the non-commercial license are
identical to the parent entry.

## What this means

China AI Hub analysis indicates this is a throughput tier, not a distinct model. The 2x price buys
roughly 1.7x output speed, so the value depends on whether latency or cost dominates your workload.
For latency-bound interactive use the premium may be justified; for throughput- or cost-bound batch
work the standard tier is the same model at half the price. The full model definition is on the
[MiniMax-M2.7](/models/minimax-m27/) page, which is the canonical entry.

*Labels used above: **Official fact** (pricing and the 204,800-token context from MiniMax's docs), **Vendor-reported claim** (the ~100 tokens/s throughput figure), and **China AI Hub analysis** (our synthesis, introduced as such).*
