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

**What it is.** Qwen3.7-Plus (equivalent to `qwen3.7-plus-2026-05-26`) is Alibaba Cloud's previous-generation plus-tier API model: a closed-weight, proprietary mid-tier SKU on Model Studio. **Why it matters.** It is a documented, billable mid-tier option that remains listed after Alibaba's flagship line moved to Qwen3.8 — a live example of how Alibaba tiers its lineup by price while letting older SKUs keep billing for pinned integrations. **Key characteristics.** $0.4 input / $1.6 output per 1M tokens (≤256K tier) on the International region, a higher 256K–1M tier at $1.2 / $4.8, and a limited-time 20% console discount. **What a professional should know.** It has been superseded in the flagship line by [Qwen3.8-Max](/models/qwen38-max/), and its context window, capabilities and benchmark results are not published on the official pricing page as of 2026-09-27.

## Status and successor

Qwen3.7-Plus is **superseded** in Alibaba's line-up by [Qwen3.8-Max](/models/qwen38-max/) but is not discontinued — it remains an active, billable SKU on Model Studio. This matters for existing integrations: pinned deployments on `qwen3.7-plus` keep working and billing, but new workloads should evaluate Qwen3.8-Max first. China AI Hub analysis indicates this superseded-but-active state is the standard Chinese API pattern for mid-tier models — vendors rarely hard-deprecate a plus-tier SKU, they simply stop marketing it and let price-tier positioning do the migration.

## What is and is not documented

The pricing page is the only substantive source: it documents price tiers but does not publish a context window, capability list or benchmark results for Qwen3.7-Plus. China AI Hub analysis indicates this thin documentation is itself the clearest signal of the model's position — a superseded mid-tier SKU is documented only for billing, not for evaluation, which is why the database records it as `partially_verified` with the capability gap explicitly noted. The two context-tier price bands (≤256K and 256K–1M) imply a 1M-context option exists, but that is an inference from pricing, not a published specification.

## Pricing detail

List price is $0.4 / $1.6 (≤256K) and $1.2 / $4.8 (256K–1M) on the International region; the Beijing region lists $0.276 / $1.101 and $0.826 / $3.301. The 3x jump between the ≤256K and 256K–1M tiers is the operative cost fact for long-context use. The two context tiers imply the model supports up to a 1M context option, though the exact context window is not published on the official pricing page as of 2026-09-27 — recorded here as not publicly documented. The limited-time 20% console discount is a vendor-stated promotion, not a permanent list price.

## How it relates to Qwen3.8

China AI Hub analysis indicates Qwen3.7-Plus occupies the previous-generation mid-tier: it is cheaper than [Qwen3.8-Max](/models/qwen38-max/) ($0.4/$1.6 vs $1.65–$2/$4.951–$6) but lacks a published benchmark or capability card. The successor publishes a full architecture card (2.4T MoE, 95B active, Gated DeltaNet hybrid) and five vendor benchmark rows, whereas Qwen3.7-Plus publishes neither. For cost-sensitive text workloads where a mid-tier plus model is sufficient, it remains a documented, billable option; for capability-critical work, the successor's published benchmarks argue for Qwen3.8-Max. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research.

## Suitable and less suitable workloads

**Well-suited:** cost-sensitive text workloads where a mid-tier plus model is sufficient, and pinned integrations that already call `qwen3.7-plus` and prefer billing continuity over migration. **Less suited:** capability-critical work (no published benchmarks), long-context work above the ≤256K tier (3x price jump), and any deployment that needs a documented context window, capability list or self-hosting path (closed-weight, proprietary).

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Unknown |
| Coding | Unknown |
| Structured API workflows | Moderate |
| Agent orchestration | Unknown |
| Local self-hosted deployment | No evidence |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims. Capability-specific rows are Unknown because Alibaba publishes no capability or benchmark data for this model.

## China AI Hub analysis

China AI Hub analysis indicates Qwen3.7-Plus is best read as a legacy billing SKU rather than a model Alibaba wants you to evaluate: it is documented only for price, superseded in the flagship line by Qwen3.8-Max, and left active to avoid breaking pinned integrations. Its presence in the database is useful precisely as a cautionary data point — a model that is billable but effectively undocumented on capabilities illustrates how much of the Chinese API layer is priced-positioned rather than specification-positioned, and why "active on the pricing page" is not the same as "recommended for new work."

## What is uncertain

- The context window, capabilities and benchmark results are not published on the official pricing page as of 2026-09-27.
- Whether a 1M-context option exists is inferred from the two pricing tiers, not confirmed by a published specification.
- The limited-time 20% discount's end date is not documented.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-qwen3.7-plus-1 | Alibaba Cloud Model Studio — model pricing | https://www.alibabacloud.com/help/en/model-studio/model-pricing | Official documentation | — | 2026-09-27 | high | — |

*Labels used above: **Official fact** (pricing and SKU facts from Model Studio), **Vendor-reported claim** (the 20% limited-time discount, as stated by Alibaba), and **China AI Hub analysis** (our synthesis, introduced as such). Context window, capabilities and benchmark scores are not publicly documented for this model.*
