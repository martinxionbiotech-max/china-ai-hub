---
image: "/images/ai/models-qwen3.7-plus.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: qwen3.7-plus
model_name: Qwen3.7-Plus
provider: alibaba-cloud
model_family: Qwen3.7
release_date: "2026-05-26"
status: active
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 0.4
  output_price_per_1m: 1.6
  currency: USD
  pricing_ref: alibaba-cloud
official_api: true
known_limitations:
  - "Context window, capabilities and benchmark results are not published on the official pricing page; not publicly documented as of 2026-09-27"
  - "List price $0.4/$1.6 (≤256K) and $1.2/$4.8 (256K–1M) on the International region; Beijing region $0.276/$1.101 and $0.826/$3.301"
last_verified: "2026-09-27"
sources:
  - source_name: Alibaba Cloud Model Studio — model pricing (official)
    source_url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

Qwen3.7-Plus (equivalent to qwen3.7-plus-2026-05-26) is Alibaba Cloud's previous-generation
plus-tier API model, priced at $0.4 input / $1.6 output per 1M tokens on the International region
(≤256K context tier), with a limited-time 20% discount on list prices. It has been superseded in
the flagship line by Qwen3.8-Max, but remains listed and billable on Model Studio.
