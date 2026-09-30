---
image: "/images/ai/models-glm-5.3-flash.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.3-flash
model_name: GLM-5.3-Flash
provider: zhipu-ai
model_family: GLM-5.3-Flash
version: Flash
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

**What it is.** GLM-5.3-Flash (2026-08-26) is Zhipu AI's multimodal coding model: an open-weight 320B-total / 18B-active sparse-plus-linear-attention model with a 1M-token context and 128K max output. **Why it matters.** It is the first native multimodal model in the GLM-5 series and the first open-source frontier model Zhipu says combines sparse and linear attention — a cost-reduction architecture aimed at making visual coding loops cheap enough to run continuously. **Key characteristics.** 1M context, input modalities of video / image / text / file with text output, native computer use (BUA/CUA), browser/GUI agent support, and a FlashX speed tier at up to 200 tokens/s. **What a professional should know.** Reasoning is always enabled (cannot be disabled), the headline coding numbers are partly measured on a private in-house benchmark, and Zhipu states all Flash traffic is served on Chinese AI chips.

## Architecture and parameters

GLM-5.3-Flash is a 320B-total / 18B-active MoE — a ~5.6% activation ratio, more extreme than the flagship [GLM-5.3](/models/glm-53/)'s 744B/40B (~5.4%). The distinguishing claim is architectural: Zhipu says it is the first open-source frontier model to combine sparse and linear attention, cutting attention computation and KV cache by 3.01x and 4.44x versus GLM-5.3. That combination — sparse experts plus linear attention — is the same cost direction the market is converging on (DeepSeek's sparse attention, Qwen's DeltaNet, MiniMax's MSA), but Zhipu pairs it with multimodal input rather than a text-only corpus. The 30T-token multimodal pre-training corpus and mHC hyper-connections round out the card. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 1M-token context with a 131,072 output cap is the standard flagship split, but Flash's significance is that this window is available at the $0.15 flash price — long context no longer costs a frontier premium. For a multimodal coding model this means a full repository, a long agent trace, or a sequence of UI screenshots can stay in context while the model iterates on visual output. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

Flash $0.15 input / $0.50 output per 1M tokens (cached $0.03); the [FlashX speed tier](/models/glm-53-flashx/) is $0.37 / $1.25 (cached $0.075). At $0.15 input, Flash sits at the three-way $0.15 floor the database records across DeepSeek, Alibaba and Zhipu flash tiers. The 3.3x input-to-output ratio and low cache pricing reward agent loops that re-read visual context. See the [GLM-5.3 vs GLM-5.3-Flash comparison](/comparisons/glm-5.3-vs-glm-5.3-flash/) and [choosing-by-price](/guides/choosing-by-price/).

## API, coding, and agent implications

Flash is positioned for the visual coding loop: observe an interface or rendered result, write code, test, and repeat — coordinating work across code, browsers and GUIs (frontend, game development, Blender 3D scenes, and real-world operation via BUA/CUA). Vendor-reported DeepSWE v1.1 (63.4) and AutomationBench (48.8) describe repository-scale coding and GUI automation respectively, while the Artificial Analysis Intelligence Index v4.1.1 score of 57 is a third-party aggregate index that Zhipu cites. The operational caveat is always-on reasoning: there is no fast non-thinking mode, so every request carries reasoning latency and cost. See [computer use](/technology/computer-use/) and the [coding hub](/models/coding/).

## Open weights and license

Open weight, Apache-2.0 per the GitHub repo metadata, self-hostable in FP8. The license caveat matters: the README has no separate weights-license section, so Zhipu's docs recommend verifying per-model Hugging Face cards before reuse. This is a permissive license with a verification step prudent teams should not skip. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and the [open-weights hub](/models/open-weights/).

## Benchmark interpretation

The three recorded rows mix source types. DeepSWE v1.1 (63.4) and AutomationBench (48.8) are vendor-reported; the Artificial Analysis Intelligence Index v4.1.1 (57) is an aggregate index that is itself a third-party construction even though Zhipu is the one citing it. None of the three is an independent re-measurement in this database. See the [GLM-5.3-Flash vs Qwen3.8-Flash comparison](/comparisons/glm-5.3-flash-vs-qwen3.8-flash/).

## What the benchmarks do not prove

The private Z.ai Code Bench — the source of the headline coding-improvement claim — cannot be externally reproduced, and the two vendor rows (DeepSWE, AutomationBench) are not independently verified. Cross-vendor comparison is invalid without matching benchmark versions and harnesses. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [benchmark-methodology research](/research/benchmark-methodology-divergence/).

## Suitable and less suitable workloads

**Well-suited:** visual coding loops and multimodal agent work (browser/GUI/computer-use), long-context analysis, self-hosting where an open-weight 1M model is required, and cost-sensitive multimodal workloads. **Less suited:** text-only frontier reasoning (the flagship GLM-5.3 has a larger active set), low-latency non-reasoning chat (reasoning cannot be disabled), and workloads needing independent benchmark verification before adoption.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | High |
| Structured API workflows | Moderate |
| Agent orchestration | High |
| Local self-hosted deployment | High |
| GUI automation | High |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates GLM-5.3-Flash is Zhipu's cost-leadership play in the multimodal agentic tier: it packages a frontier-adjacent architecture (320B/18B sparse-plus-linear) with native vision, computer use and a 1M window at the $0.15 flash floor. The model's distinguishing bet is that multimodal coding and GUI automation can be a flash-tier product rather than a flagship one — the same logic the database sees in the deepseek-v4-1-flash and qwen3.8-flash tiers, but extended to visual and computer-use workloads. The two caveats that should temper adoption are always-on reasoning (no cheap non-thinking mode) and the reliance on the private Z.ai Code Bench for the headline improvement claim.

## Market position and outlook

China AI Hub analysis indicates Flash's structural role is as the open-weight multimodal anchor at the flash price point: the database records GLM-5.3-Flash as one of the flash-tier models delivering a 1M window, and the only one in that tier pairing it with native video input and computer-use (BUA/CUA). Zhipu's claim that all Flash traffic is served on Chinese AI chips is a supply-chain signal worth noting — it positions Flash as partly an infrastructure statement about domestic chip capability, not only a model release. The FlashX speed tier extends the same model to latency-sensitive users at ~2.5x price. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [multimodal capabilities](/research/chinese-ai-multimodal-capabilities/) research.

## What is uncertain

- The headline coding-improvement claim is measured on Z.ai Code Bench, a private in-house benchmark that cannot be independently reproduced.
- The Apache-2.0 label comes from GitHub metadata; the README has no separate weights-license section, so per-model HF cards should be verified before reuse.
- The Artificial Analysis Intelligence Index v4.1.1 score is an aggregate third-party index cited by Zhipu, not an independent re-measurement in this database.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-glm-5.3-flash-1 | Z.ai docs — GLM-5.3-Flash model page | https://docs.z.ai/guides/vlm/glm-5.3-flash | Official documentation | — | 2026-09-20 | high | — |
| src-models-glm-5.3-flash-2 | Z.ai pricing | https://docs.z.ai/guides/overview/pricing | Official documentation | — | 2026-09-20 | high | — |
| src-models-glm-5.3-flash-3 | GLM-5 GitHub repository | https://github.com/zai-org/GLM-5 | Official documentation | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (architecture, pricing, context and capability facts from Z.ai docs and the GLM-5 repo), **Vendor-reported claim** (the DeepSWE, AutomationBench and Code Bench improvement claims published by Zhipu), and **China AI Hub analysis** (our synthesis, always introduced as such). The Artificial Analysis index is cited by Zhipu but is not an independent re-measurement in this database.*
