---
image: "/images/ai/models-qwen3.7-plus.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: qwen3.7-plus
model_name: Qwen3.7-Plus
provider: alibaba-cloud
model_family: Qwen3.7
superseded_by: qwen3.8-max
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
the flagship line by [Qwen3.8-Max](/models/qwen38-max/), but remains listed and billable on Model Studio.

## Status and successor

Qwen3.7-Plus is **superseded** in Alibaba's line-up by Qwen3.8-Max but is not discontinued — it
remains an active, billable SKU on Model Studio. This matters for existing integrations: pinned
deployments on `qwen3.7-plus` keep working and billing, but new workloads should evaluate Qwen3.8-Max
first.

## Pricing detail

List price is $0.4 / $1.6 (≤256K) and $1.2 / $4.8 (256K–1M) on the International region; the Beijing
region lists $0.276 / $1.101 and $0.826 / $3.301. The two context tiers imply the model supports up to
a 1M context option, though the exact context window, capabilities and benchmark results are not
published on the official pricing page as of 2026-09-27 — recorded here as not publicly documented.

## What this means

China AI Hub analysis indicates Qwen3.7-Plus occupies the previous-generation mid-tier: it is cheaper
than Qwen3.8-Max ($0.4/$1.6 vs $1.65–$2/$4.951–$6) but lacks a published benchmark or capability card.
For cost-sensitive text workloads where a mid-tier plus model is sufficient, it remains a documented,
billable option; for capability-critical work, the successor's published benchmarks argue for Qwen3.8-Max.

*Labels used above: **Official fact** (pricing and SKU facts from Model Studio), **Vendor-reported claim** (the 20% limited-time discount, as stated by Alibaba), and **China AI Hub analysis** (our synthesis, introduced as such). Context window, capabilities and benchmark scores are not publicly documented for this model.*
