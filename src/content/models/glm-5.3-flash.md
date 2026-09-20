---
model_id: glm-5.3-flash
model_name: GLM-5.3-Flash
provider: zhipu-ai
model_family: GLM-5.3-Flash
version: FlashX
aliases:
  - glm-5.3-flashx
  - GLM-5.3-FlashX
release_date: "2026-08-26"
status: active
architecture: "320B total / 18B active; first open-source frontier model combining sparse + linear attention; mHC hyper-connections; 30T-token multimodal pre-training corpus"
parameter_information:
  total_parameters: "320B"
  active_parameters: "18B"
context_window: 1048576
maximum_output: 131072
capabilities:
  reasoning: true
  coding: true
  vision: true
  video: true
  computer_use: true
  agent_capability: true
open_weight: true
license: "Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.15
  output_price_per_1m: 0.5
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
  - benchmark: Artificial Analysis Intelligence Index v4.1.1
    score: 57
    metric: index score
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
  - benchmark: DeepSWE v1.1
    score: 63.4
    metric: accuracy
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
  - benchmark: AutomationBench
    score: 48.8
    metric: accuracy
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
known_limitations:
  - "FlashX tier not yet available on the GLM Coding Plan (pay-as-you-go only)"
  - "Reasoning always enabled; cannot be disabled"
  - "Z.ai Code Bench is a private in-house benchmark"
  - "Benchmarks vendor-reported; not independently verified"
last_verified: "2026-09-20"
sources:
  - source_name: Z.ai docs — GLM-5.3-Flash model page
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
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

GLM-5.3-Flash (2026-08-26) is Zhipu's multimodal coding model with open weights (320B total / 18B
active, FP8): 1M context, 128K max output, input modalities of video, image, text and file. It combines
sparse and linear attention and is positioned for visual coding loops (observe - code - test), computer
use (BUA/CUA), browser/GUI agents, office workflows, video understanding, 3D and CAD tasks. The FlashX
tier serves at up to 200 tokens/s.

International pricing: Flash $0.15 input / $0.50 output per 1M tokens (cached $0.03); FlashX
$0.37 / $1.25 (cached $0.075), as of 2026-09-20. Zhipu states all Flash traffic is served on Chinese AI
chips.
