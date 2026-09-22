---
image: "/images/ai/models-qwen3.8-2.4t-a95b.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: qwen3.8-2.4t-a95b
model_name: Qwen3.8-2.4T-A95B
provider: alibaba-cloud
model_family: Qwen3.8
release_date: "2026-08-12"
status: active
architecture: "2.4T-parameter MoE, 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, Gated DeltaNet + Gated Attention hybrid"
parameter_information:
  total_parameters: "2.4T"
  active_parameters: "95B"
context_window: 262144
capabilities:
  reasoning: true
  vision: false
open_weight: true
license: "Qwen3.8-Max License (custom MIT-style: unrestricted use/copy/modify/sell, but products with >100M MAU or >US$20M/month revenue must display the model name; Model-as-a-Service or AI Work Assistant businesses with >US$50M/12-month revenue need a separate license from Qwen)"
self_hosting: true
api_available: false
official_api: false
known_limitations:
  - "Text-only input; thinking cannot be disabled; reasoning_effort xhigh/medium/low"
  - "Native context 262,144 tokens, extensible to 1,010,000"
  - "Not the same product as the qwen3.8-max API model (which adds vision/video input, non-thinking mode and 1M default context)"
last_verified: "2026-09-20"
sources:
  - source_name: Hugging Face model card — Qwen3.8-2.4T-A95B
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen3.8 repository README
    source_url: https://github.com/QwenLM/Qwen3.8
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen3.8-2.4T-A95B license file
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Qwen3.8-2.4T-A95B is Qwen's first Qwen-Max-class open-weight release (2026-08-12): a 2.4T-parameter
MoE with 95B activated parameters using a Gated DeltaNet + Gated Attention hybrid. It is text-only and
thinking-only (reasoning cannot be disabled; reasoning_effort xhigh/medium/low), with a native 262,144
context extensible to 1,010,000 tokens.

The license is a custom MIT-style agreement with commercial attribution and revenue-threshold
requirements. The hosted qwen3.8-max API model is the related closed product with broader modalities.
