---
image: "/images/ai/models-kimi-k2.6.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.6
model_name: Kimi K2.6
provider: moonshot-ai
model_family: Kimi K2.6
release_date: "2026-04-20"
status: active
architecture: "Mixture-of-Experts (MoE): 1T total / 32B activated; 384 routed experts (8 selected + 1 shared); MLA attention, SwiGLU activation; 61 layers (1 dense); MoonViT vision encoder (400M)"
parameter_information:
  total_parameters: "1T"
  active_parameters: "32B"
context_window: 262144
maximum_output: 98304
capabilities:
  reasoning: true
  vision: true
open_weight: true
license: "Modified MIT"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.95
  output_price_per_1m: 4.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Maximum output of 98,304 tokens is the documented max generation length in the official model card's evaluation configuration"
last_verified: "2026-09-27"
benchmark_results:
  - benchmark: HLE
    score: "36.4 (text-only, no tools)"
    metric: accuracy
    date: "2026-04"
    source_type: vendor_reported
    source_url: https://huggingface.co/moonshotai/Kimi-K2.6
  - benchmark: HLE
    score: "55.5 (with tools)"
    metric: accuracy
    date: "2026-04"
    source_type: vendor_reported
    source_url: https://huggingface.co/moonshotai/Kimi-K2.6
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
  - source_name: Hugging Face model card — Kimi K2.6 (architecture, parameters, benchmarks)
    source_url: https://huggingface.co/moonshotai/Kimi-K2.6
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

Kimi K2.6 is Moonshot's visual + text model with thinking and non-thinking modes for dialogue and agent
tasks, in a 256K context window. Pricing is $0.95 input / $4.00 output per 1M tokens (cache hits $0.16,
as of 2026-09-20).
