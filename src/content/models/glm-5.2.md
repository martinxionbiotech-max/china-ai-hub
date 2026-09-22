---
image: "/images/ai/models-glm-5.2.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.2
model_name: GLM-5.2
provider: zhipu-ai
model_family: GLM-5
release_date: "2026-06-16"
status: deprecated
architecture: "744B total / 40B active (open weights, BF16/FP8)"
parameter_information:
  total_parameters: "744B"
  active_parameters: "40B"
context_window: 1048576
capabilities:
  reasoning: true
  vision: false
open_weight: true
license: Apache-2.0
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 1.4
  output_price_per_1m: 4.4
  currency: USD
  pricing_ref: zhipu-ai
official_api: true
cloud_providers:
  - Z.ai
  - BigModel
regions:
  - international
  - china
known_limitations:
  - "Superseded by GLM-5.3 (same base model, improved post-training) but still listed on the API pricing page at the same price"
  - "Text-only input; reasoning supports high/max only"
last_verified: "2026-09-20"
sources:
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai pricing
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai release notes
    source_url: https://docs.z.ai/release-notes/new-released
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

GLM-5.2 (2026-06-16) is Zhipu's previous flagship text model - a 744B-total / 40B-active open-weight
model with 1M context. It has been superseded by GLM-5.3, which uses the same base model with improved
post-training, but GLM-5.2 remains on the pricing page at the same price ($1.40 / $4.40 per 1M tokens,
cached $0.26, as of 2026-09-20).
