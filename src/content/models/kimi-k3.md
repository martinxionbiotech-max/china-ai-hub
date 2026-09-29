---
image: "/images/ai/models-kimi-k3.webp"
image_credit: "AI-generated illustration (Seedream)"
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

**What it is.** Kimi K3 is Moonshot AI's flagship open-weight model ("Open Frontier Weights"), released 2026-07-16: a 2.8T-parameter MoE with 104B activated parameters and a 1,048,576-token context window. **Why it matters.** It is the only model in the China AI Hub database documented as capable of both 1M-token input *and* 1M-token output, making it the strongest long-form *generation* model tracked, and it carries native visual understanding plus always-on thinking. **Key characteristics.** Native vision and video input, `reasoning_effort` low/high/max (default max), tool calling, structured output, and agent capability. **What a professional should know.** Temperature is fixed at 1.0 and top_p at 0.95 — you cannot tune sampling — and the license is permissive only up to a $20M revenue / 100M MAU threshold, above which Moonshot requires a separate agreement and UI attribution.

## Architecture and parameters

K3 publishes the fullest architecture card in the database: 2.8T total / 104B activated (~3.7% activation), 93 layers (1 dense), 896 experts with 16 selected + 2 shared per token, 69 KDA + 24 Gated MLA attention layers, hidden dim 7168, SiTU-GLU, a 401M-parameter MoonViT-V2 vision encoder, and MXFP4 weights with MXFP8 activations. The KDA (Kimi Delta Attention) plus Gated MLA split is Moonshot's answer to long-context economics: linear-attention layers replace part of the dense attention stack so 1M-token context stays tractable. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

K3 is the database's unique 1M-in / 1M-out pairing. Most 1M-input models cap output at 131K–393K; K3 can *generate* up to 1,048,576 tokens, which reframes what it is for: long-form document synthesis, multi-file code generation, and agent runs with very long output trajectories — not just long-input analysis. The trade-off is cost: at $15/M output tokens, a single maximal response is a material expense. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

$3.00 input / $15.00 output per 1M tokens with automatic prefix caching ($0.30 cached input). The 5x input-to-output ratio is the highest in the flagship tier, reflecting the premium on generation. The $15 output price, combined with a 1M output ceiling, means K3's worst-case single-request cost is the highest in the database — budget-sensitive deployments should cap `max_completion_tokens` (default 131,072) rather than rely on the ceiling. API access requires a $1 minimum top-up. See the [MiniMax M3 comparison](/comparisons/kimi-k3-vs-minimax-m3/).

## API, coding, and agent implications

K3 targets software engineering and deep reasoning. Vendor-reported DeepSWE (67.5) and Terminal-Bench 2.1 (88.3) are strong coding/agentic signals, and agent capability is documented. The fixed sampling parameters (temperature 1.0, top_p 0.95) mean deterministic, low-temperature outputs are not achievable through the API — a real constraint for reproducible batch jobs. `max_completion_tokens` defaults to 131,072 and can be set to 1,048,576. The [Kimi Code](/agents/kimi-code/) agent runs on K3.

## Open weights and license

Weights are on Hugging Face and ModelScope under the "Kimi K3 License": MIT-style permissive, but operators with >$20M aggregate revenue over any 12 months must sign a separate agreement, and products over 100M MAU or $20M monthly revenue must display "Kimi K3" in the UI. This is a conditional-open license, not plain MIT — commercial self-hosters above the thresholds face obligations. See [licensing explained](/research/chinese-ai-model-licensing-explained/).

## Benchmark interpretation

Six vendor-reported rows: GPQA Diamond 93.5, HLE-Full 43.5 (56.0 with tools), DeepSWE 67.5, Terminal-Bench 2.1 88.3, MMMU-Pro 81.6, and Video-MME 90.0. The multimodal rows (MMMU-Pro, Video-MME) reflect K3's native vision/video; the HLE with-tools delta again shows tool access raising the ceiling. Moonshot notes some comparison scores are cited from Artificial Analysis — a third-party source — though the K3-specific rows here are vendor-reported.

## What the benchmarks do not prove

These scores do not independently verify K3 against competitors, and the modality documentation is itself inconsistent: the architecture table says Text+Image while the README, launch blog and API guide also show video input. Treat the exact input-modality boundary as uncertain. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** long-form document and code generation, deep reasoning, multimodal (vision/video) analysis, and agent workloads that benefit from 1M output headroom. **Less suited:** high-volume low-cost chat (priced at flagship tier), latency/reproducibility-sensitive batch work (fixed sampling), and commercial self-hosting above the license thresholds.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | High |
| Structured API workflows | High |
| Agent orchestration | High |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates that K3 occupies the top of the flagship tier on two axes — parameter scale (2.8T) and output ceiling (1M) — but pays for both in the highest output pricing and the most constrained sampling controls. The KDA/Gated-MLA architecture and 896-expert topology are the most technically transparent open release in the collection, which is an asset for researchers even if the $15 output price limits practical reach. The fixed temperature/top_p is a genuine, under-appreciated limitation for production users expecting standard sampling controls.

## What is uncertain

- The input-modality boundary is inconsistent across official sources: the architecture table says Text+Image, while the README, launch blog and API guide also list video input.
- Some comparison benchmark scores are cited from Artificial Analysis (third-party); the K3-specific rows here are vendor-reported.
- Sampling is fixed (temperature 1.0, top_p 0.95) and cannot be changed through the API.

## Sources

- [Kimi K3 GitHub README](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi API platform — model list](https://platform.kimi.ai/docs/models.md)
- [Kimi API — Chat Completions spec](https://platform.kimi.ai/docs/api/chat.md)
- [Kimi K3 launch blog](https://www.kimi.com/blog/kimi-k3)

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores published by Moonshot), **Third-party evidence** (Artificial Analysis, where cited), and **China AI Hub analysis** (our synthesis, always introduced as such).*
