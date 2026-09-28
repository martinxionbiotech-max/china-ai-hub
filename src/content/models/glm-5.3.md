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

**What it is.** GLM-5.3 (2026-08-18) is Zhipu AI's flagship text model: a 744B-total / 40B-active open-weight model with a 1M-token context and 128K max output, released under Apache-2.0. **Why it matters.** It shares its base model with GLM-5.2 — all gains come from post-training — making it a direct study in how much post-training can move a fixed architecture, and it is one of only two open-weight 1M-context models in the database. **Key characteristics.** Text-only input, reasoning always enabled (low/high/max, default max), open weights in FP8 and BF16. **What a professional should know.** Reasoning cannot be disabled, and the headline "50% coding improvement" is measured on Z.ai Code Bench, a private in-house benchmark — treat it as a vendor claim, not an independent result.

## Architecture and parameters

GLM-5.3 is a 744B-total / 40B-active MoE (~5.4% activation), the same base model as GLM-5.2 with post-training improvements. Compared to the flash-tier's more extreme sparsity (GLM-5.3-Flash at 320B/18B), this is a conventional frontier activation ratio. Open weights ship in FP8 (with a BF16 variant), so self-hosting hardware requirements are documented rather than implied. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 1M-token context with a 131,072 output cap is the standard flagship split: long-input analysis, not long-form generation. The distinguishing factor is that this 1M window is available in *open weights* — GLM-5.3 and GLM-5.3-Flash are the only open-weight 1M-context models in the collection, which matters for enterprises that cannot use APIs. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

International $1.40 input / $4.40 output per 1M tokens (cached $0.26); China platform ¥8 / ¥28 (cached ¥2). The 3.1x input-to-output ratio and low cache pricing follow the market norm, and cached input at ~18% of input price rewards agent loops that re-read context. See the [GLM-5.3 vs Qwen3.8-Max comparison](/comparisons/qwen38-max-vs-glm-53/).

## API, coding, and agent implications

Vendor-reported Terminal-Bench 3.0 (28.3), DeepSWE v1.1 (66.9), Agents' Last Exam CLI (28.5) and CyberGym (84.5) describe a strong agentic and security-task profile, with a notably high CyberGym score. Zhipu positions GLM-5.3 as agent-oriented; see [GLM agent-oriented AI](/research/glm-agent-oriented-ai/). Reasoning is always on, which means no fast non-thinking mode — latency and cost are fixed at reasoning levels for every request.

## Open weights and license

Open weight, Apache-2.0 per GitHub repo metadata, self-hostable. The license caveat is important: the README has no separate weights-license section, so Zhipu's docs recommend verifying per-model Hugging Face cards before reuse. This is a permissive license but with a verification step prudent teams should not skip. See [licensing explained](/research/chinese-ai-model-licensing-explained/).

## Benchmark interpretation

The four rows are vendor-reported. Terminal-Bench 3.0 (note the version — 3.0, not the 2.1 used by DeepSeek/Qwen/Kimi) is not comparable to other vendors' 2.1 scores; DeepSWE v1.1 (66.9) is repository-scale coding; CyberGym 84.5 is security-oriented agentic work. The "50% coding improvement over GLM-5.2" claim is on Z.ai Code Bench, a private benchmark that cannot be externally reproduced.

## What the benchmarks do not prove

Version mismatches (Terminal-Bench 3.0 vs 2.1) make naive cross-vendor ranking invalid, and the private Code Bench result is unverifiable. All scores are vendor-reported. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [benchmark-methodology research](/research/benchmark-methodology-divergence/).

## Suitable and less suitable workloads

**Well-suited:** text-only agentic and coding work, security-oriented agent tasks, long-context analysis, and self-hosting where an open-weight 1M model is required. **Less suited:** vision/multimodal input (text-only), low-latency non-reasoning chat (reasoning cannot be disabled), and workloads needing independent benchmark verification before adoption.

## China AI Hub analysis

China AI Hub analysis indicates GLM-5.3's significance is structural rather than headline: it demonstrates that a fixed base model can be meaningfully improved purely through post-training, and it holds the open-weight 1M-context position that makes Zhipu the default answer for long-context self-hosters. The always-on reasoning and private Code Bench benchmark are the two caveats that should temper adoption decisions — the first constrains cost/latency, the second constrains verification. Its strongest independent-looking signal is CyberGym (84.5), but that too is vendor-reported.

## Market position and outlook

China AI Hub analysis indicates GLM-5.3's structural role is as the open-weight long-context anchor: the database records GLM-5.3 and GLM-5.3-Flash as the only open-weight 1M-context models in the collection, which makes Zhipu the default answer for enterprises that need long context but cannot use APIs. That position is reinforced by the model's release strategy — shipping the same 744B/40B base as GLM-5.2 and improving it purely through post-training is a low-cost way to extend a model family without a new architecture. The two caveats that define its adoption profile are always-on reasoning (no non-thinking mode, so every request carries reasoning latency and cost) and the reliance on the private Z.ai Code Bench for the headline improvement claim, which cannot be independently reproduced. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [context-window](/research/chinese-ai-context-windows/) research.

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores and the Code Bench improvement published by Zhipu), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
