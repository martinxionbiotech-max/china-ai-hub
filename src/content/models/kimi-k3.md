---
model_id: kimi-k3
model_name: Kimi K3
provider: moonshot-ai
model_family: Kimi K-series
release_date: "2026-07-16"
status: active
architecture: "MoE: 2.8T total / 104B activated; 93 layers (1 dense); 896 experts (16 selected + 2 shared per token); 69 KDA + 24 Gated MLA layers; hidden dim 7168; SiTU-GLU; MoonViT-V2 vision encoder (401M); MXFP4 weights / MXFP8 activations"
parameter_information:
  total_parameters: "2.8T"
  active_parameters: "104B"
context_window: 1048576
maximum_output: 1048576
capabilities:
  reasoning: true
  coding: true
  vision: true
  video: true
  tool_calling: true
  structured_output: true
  agent_capability: true
open_weight: true
license: "Kimi K3 License (permissive MIT-style, but Model-as-a-Service operators with >$20M aggregate revenue over any 12 months must sign a separate agreement; products with >100M MAU or >$20M monthly revenue must display 'Kimi K3' in the UI)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 3.0
  output_price_per_1m: 15.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
benchmark_results:
  - benchmark: GPQA Diamond
    score: 93.5
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: HLE-Full
    score: "43.5 (56.0 with tools)"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: DeepSWE
    score: 67.5
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: Terminal-Bench 2.1
    score: 88.3
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: MMMU-Pro
    score: 81.6
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: Video-MME (with subtitles)
    score: 90.0
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
known_limitations:
  - "Temperature fixed at 1.0 and top_p at 0.95 - cannot be modified"
  - "API access requires a minimum $1 top-up"
  - "Modality documentation inconsistent: architecture table says Text+Image, while the README, launch blog and API guide also show video input"
  - "Benchmarks vendor-reported; some comparison scores cited from Artificial Analysis"
last_verified: "2026-09-20"
sources:
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API platform — model list
    source_url: https://platform.kimi.ai/docs/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API — Chat Completions spec
    source_url: https://platform.kimi.ai/docs/api/chat.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K3 launch blog
    source_url: https://www.kimi.com/blog/kimi-k3
    source_type: official
    published_date: "2026-07-16"
    last_verified: "2026-09-20"
    confidence: high
---

Kimi K3 is Moonshot AI's flagship open-weight model ("Open Frontier Weights", released 2026-07-16): a
2.8T-parameter MoE with 104B activated parameters, a 1M-token context window, native visual
understanding, and always-on thinking with reasoning_effort low/high/max (default max). It targets
software engineering, knowledge work and deep reasoning.

The API model `kimi-k3` (min $1 top-up) prices at $3.00 input / $15.00 output per 1M tokens with
automatic prefix caching ($0.30 cached input); max_completion_tokens defaults to 131,072 and can be set
up to 1,048,576. Temperature (1.0) and top_p (0.95) are fixed. Full weights are on Hugging Face and
ModelScope under the Kimi K3 License.
