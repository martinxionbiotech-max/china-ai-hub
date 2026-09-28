---
image: "/images/ai/models-kimi-k2.7-code-highspeed.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.7-code-highspeed
model_name: Kimi K2.7 Code Highspeed
provider: moonshot-ai
model_family: Kimi K2.7
canonical_model: kimi-k2.7-code
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
  - "Architecture and parameter counts are not publicly disclosed by Moonshot for the K2.7 series (API-only coding models)"
  - "Output speed ~180 tokens/s, up to 260 tokens/s in short-context scenarios (official model list)"
  - "Thinking is always on; temperature/top_p/n/penalties are fixed and must not be passed"
  - "Max output ceiling not stated in the fetched docs (256K context)"
last_verified: "2026-09-27"
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

Kimi K2.7 Code Highspeed is the same model as [Kimi K2.7 Code](/models/kimi-k27-code/) served at
higher throughput: ~180 tokens/s output, up to 260 tokens/s in short contexts (official model list).
Pricing is doubled vs. the standard tier: $1.90 input / $8.00 output per 1M tokens (cache hits $0.38,
as of 2026-09-20).

## How it differs from Kimi K2.7 Code

The only documented differences are **throughput and price**. The standard K2.7 Code is priced at
$0.95 / $4.00; the Highspeed variant is exactly 2x ($1.90 / $8.00) for faster token generation. The
256K context window, always-on thinking, fixed sampling parameters and closed-weight (API-only)
status are identical to the parent entry.

## What this means

China AI Hub analysis indicates this is a speed tier for latency-sensitive coding work: you pay 2x for
higher output throughput on the same coding model. For interactive coding or agent loops where
per-token latency is the bottleneck, the premium may pay for itself; for batch or cost-bound coding
work the standard tier is the same model at half the price. The full model definition is on the
[Kimi K2.7 Code](/models/kimi-k27-code/) page, which is the canonical entry.

*Labels used above: **Official fact** (pricing and the 256K context from Kimi's model list), **Vendor-reported claim** (the ~180–260 tokens/s throughput figures), and **China AI Hub analysis** (our synthesis, introduced as such).*
