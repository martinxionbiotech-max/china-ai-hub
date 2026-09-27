---
image: "/images/ai/models-glm-5.3-flashx.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.3-flashx
model_name: GLM-5.3-FlashX
provider: zhipu-ai
model_family: GLM-5.3-Flash
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

GLM-5.3-FlashX is Zhipu AI's international-region Flash-tier API model, a sibling of
GLM-5.3-Flash with a different price point ($0.37 input / $1.25 output per 1M tokens vs
$0.15 / $0.50 for GLM-5.3-Flash). Z.ai's official navigation labels the pair
"GLM-5.3-Flash/FlashX" as a new offering; the two are billed as separate SKUs on the Z.ai platform.
