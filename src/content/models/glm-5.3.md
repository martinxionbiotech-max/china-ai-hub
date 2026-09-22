---
image: "/images/ai/models-glm-5.3.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.3
model_name: GLM-5.3
provider: zhipu-ai
model_family: GLM-5
release_date: "2026-08-18"
status: active
architecture: "744B total / 40B active (open-weight FP8); same base model as GLM-5.2 with post-training gains"
parameter_information:
  total_parameters: "744B"
  active_parameters: "40B"
  parameter_precision: "FP8 (BF16 variant also released)"
context_window: 1048576
maximum_output: 131072
capabilities:
  reasoning: true
  coding: true
  vision: false
open_weight: true
license: "Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse)"
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
benchmark_results:
  - benchmark: Terminal-Bench 3.0
    score: 28.3
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: DeepSWE v1.1
    score: 66.9
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: Agents' Last Exam (CLI)
    score: 28.5
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: CyberGym
    score: 84.5
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
known_limitations:
  - "Text-only input"
  - "Reasoning always enabled (low/high/max, default max); cannot be disabled"
  - "Z.ai Code Bench is a private in-house benchmark"
  - "Benchmarks vendor-reported; not independently verified"
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
  - source_name: GLM-5 GitHub repository
    source_url: https://github.com/zai-org/GLM-5
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

GLM-5.3 (2026-08-18) is Zhipu's flagship text model: a 744B-total / 40B-active open-weight model with a
1M-token context and 128K max output. It shares its base model with GLM-5.2; all gains come from
post-training, with a claimed 50% coding improvement on Z.ai Code Bench. Reasoning is always enabled
(low/high/max, default max).

International pricing is $1.40 input / $4.40 output per 1M tokens with cached input at $0.26 (as of
2026-09-20); the China platform lists ¥8 / ¥28 with cached hits at ¥2. Open weights (FP8 and BF16) are
on Hugging Face and ModelScope under Apache-2.0 (per GitHub repo metadata).
