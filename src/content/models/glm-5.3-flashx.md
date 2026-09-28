---
image: "/images/ai/models-glm-5.3-flashx.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.3-flashx
model_name: GLM-5.3-FlashX
provider: zhipu-ai
model_family: GLM-5.3-Flash
canonical_model: glm-5.3-flash
status: active
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 0.37
  output_price_per_1m: 1.25
  currency: USD
  pricing_ref: zhipu-ai
official_api: true
known_limitations:
  - "Context window, capabilities and benchmark results are not published on the official Z.ai pricing page; not publicly documented as of 2026-09-27"
last_verified: "2026-09-27"
sources:
  - source_name: Z.ai — API pricing (official)
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

GLM-5.3-FlashX is Zhipu AI's international-region Flash-tier API model, a sibling SKU of
[GLM-5.3-Flash](/models/glm-53-flash/) that serves the same model at higher throughput (up to 200
tokens/s) under a separate billing SKU. Z.ai's official navigation labels the pair
"GLM-5.3-Flash/FlashX" as a new offering; the two are billed separately on the Z.ai platform.

## How it differs from GLM-5.3-Flash

The only documented differences are **throughput and price**. FlashX is priced at $0.37 input / $1.25
output per 1M tokens versus $0.15 / $0.50 for Flash — roughly 2.5x the input and output rate — for
faster serving (up to 200 tokens/s, vendor-reported). Context window, capabilities and benchmark
results are not published separately on the official Z.ai pricing page as of 2026-09-27.

## What this means

China AI Hub analysis indicates FlashX is a speed tier, not a different model: you pay a 2.5x premium
for faster token generation on the same underlying GLM-5.3-Flash. For latency-sensitive or
throughput-bound workloads it is worth the premium; for everything else the standard Flash tier is the
same model at a lower price. The full model definition lives on the
[GLM-5.3-Flash](/models/glm-53-flash/) page, which is the canonical entry for this model.

*Labels used above: **Official fact** (pricing and throughput from Z.ai's pricing page), **Vendor-reported claim** (the 200 tokens/s throughput figure), and **China AI Hub analysis** (our synthesis, introduced as such).*
