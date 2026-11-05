---
model_id: kimi-k3.1-pro
model_name: Kimi K3.1 Pro
provider: moonshot-ai
model_family: Kimi K3.1 series
status: active
architecture: "Post-trained from Kimi K3 with substantially larger post-training compute; provider describes it as a 3T-class open-weight model"
context_window: 1048576
capabilities:
  reasoning: true
  coding: true
  vision: true
  tool_calling: true
  structured_output: true
  agent_capability: true
open_weight: true
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 13.0
  output_price_per_1m: 68.0
  currency: CNY
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Priced in CNY on the China platform; the international USD list was not published when this record was created, so cross-provider comparison needs an explicit exchange-rate assumption"
  - "Cache writes are billed separately by TTL tier (5 minutes / 1 hour); partial blocks that do not fill a cache block are billed as cache misses"
last_verified: "2026-11-05"
sources:
  - source_name: "Kimi API Platform — K3.1 Pro quickstart"
    source_url: "https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart.md"
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
  - source_name: "Kimi API Platform — model inference pricing"
    source_url: "https://platform.kimi.ai/docs/pricing/chat.md"
    source_type: official
    last_verified: "2026-11-05"
    confidence: medium
---

Kimi K3.1 Pro is Moonshot's first K3.1-series model: a post-trained version of Kimi K3 with substantially larger post-training compute, a 1,048,576-token context window, vision input and reasoning effort control. The provider describes it as its most capable 3T-class open-weight model.

## Pricing

The China platform lists **¥13 per 1M input tokens, ¥68 per 1M output tokens**, with cached input at **¥1.3 per 1M** — a 90% cache discount. A `kimi-k3.1-pro-highspeed` variant lists ¥26 / ¥136 with roughly 2–3x the throughput.

At an indicative 7.1 CNY/USD, that is about **$1.83 input / $9.58 output** per 1M tokens. The comparison to the previous flagship is the point: Kimi K3 lists $3.00/$15.00 on the international platform, so K3.1 Pro is roughly a third cheaper on input and a third cheaper on output — consistent with the provider's own "about one-third lower" framing.

The number to be careful with is the currency. This record is in CNY because that is how the price was published; the international USD list was not available when the record was created. Any cross-provider comparison that mixes this row with USD rows without stating an exchange rate is not a comparison.

## What changed from K3

- **Larger post-training**, described by the provider as joint RL across hundreds of downstream domains, rather than a new base model.
- **Flat pricing**: no tiering by context length, but cache writes are billed separately by TTL (5 minutes or 1 hour).
- **Batch inference** at 60% of the standard price, for `kimi-k3.1-pro` and `kimi-k3`.
- **A highspeed variant** at exactly double the standard price.

## How to read it

China AI Hub analysis: K3.1 Pro is a price cut wrapped in a capability release. The architecture is inherited from K3; the changes are post-training and packaging. That makes the migration decision unusually simple for existing K3 users — same window, same deployment model, lower price — and unusually hard for K2 users, whose models retire by the end of December 2026 and who now face a flagship price instead of a mid-tier one.

Verify the CNY price on the platform before budgeting: it is the number most likely to move, and the international list may appear at a different level.
