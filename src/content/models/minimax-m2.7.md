---
image: "/images/ai/models-minimax-m2.7.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: minimax-m2.7
model_name: MiniMax-M2.7
provider: minimax
model_family: MiniMax M2.7
release_date: "2026-03-18"
status: active
context_window: 204800
capabilities:
  reasoning: true
  tool_calling: true
  vision: false
open_weight: true
license: "Custom NON-COMMERCIAL license (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution 'Built with MiniMax M2.7' required)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.3
  output_price_per_1m: 1.2
  currency: USD
  pricing_ref: minimax
official_api: true
cloud_providers:
  - MiniMax Platform
regions:
  - china
  - international
benchmark_results:
  - benchmark: GDPval-AA ELO
    score: 1495
    metric: ELO
    date: "2026-03-18"
    source_type: vendor_reported
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
  - benchmark: MM Claw end-to-end benchmark
    score: 62.7
    metric: accuracy
    date: "2026-03-18"
    source_type: vendor_reported
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
known_limitations:
  - "Text-only input; interleaved thinking always on (cannot be disabled via API)"
  - "Parameter count and max output tokens not publicly disclosed"
  - "Must echo full assistant content (thinking blocks) back in multi-turn history"
  - "Benchmarks vendor-reported; not independently verified"
last_verified: "2026-09-27"
sources:
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official release notes
    source_url: https://platform.minimaxi.com/docs/release-notes/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — MiniMax-M2.7
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** MiniMax-M2.7 (2026-03-18) is MiniMax's "self-evolving" open-weight model: a text-only, 204,800-token-context model that MiniMax positions as the first to "deeply participate in its own evolution" through recursive self-improvement, agent teams, complex skills and dynamic tool search. **Why it matters.** It was MiniMax's open-weight workhorse before [MiniMax-M3](/models/minimax-m3/), and its release is the database's clearest documentation of "self-evolution" as a training narrative — a positioning claim worth understanding on its own terms rather than accepting at face value. **Key characteristics.** 204,800-token context, text-only input, interleaved thinking that is always on, open weights under a custom non-commercial license, and ~60 tokens/s output (a 2x-priced highspeed variant serves ~100 TPS). **What a professional should know.** Parameter count and maximum output are not publicly disclosed, the recorded benchmark rows are vendor-reported, and the custom license forbids commercial use without written authorization — three constraints that materially shape whether M2.7 fits a given workload.

## Architecture and parameters

MiniMax does not publish a parameter count for M2.7, and the database records that absence rather than estimating — the parameter count and maximum output are "not publicly disclosed" per the official model card. China AI Hub analysis indicates this is the inverse of the disclosure pattern the database records at Moonshot (a full K2.6 architecture card) and Zhipu (an explicit 744B/40B for GLM-5.3), and it points to M2.7 being positioned on a product narrative ("self-evolving") ahead of a hardware specification. The contrast is sharpest against MiniMax's own successor: [MiniMax-M3](/models/minimax-m3/) does publish an approximate ~428B-total / ~23B-active MoE figure. See [Mixture-of-Experts](/technology/mixture-of-experts/) for the architectural context MiniMax does not provide here.

## What "self-evolving" actually means

M2.7's headline is its "self-evolution" loop: MiniMax describes the model updating its own memory, building skills for reinforcement-learning experiments, and improving its learning process based on results, with an internal version autonomously optimizing a programming scaffold over 100+ rounds to a claimed 30% improvement. This is a vendor-reported training-methodology claim, not an independent measurement. China AI Hub analysis indicates the concept is best read as a training-data and RL-loop innovation — the model participates in generating and refining its own improvement signal during development — rather than a runtime capability: buyers do not receive a model that rewrites itself in production, they receive a model trained with a self-improvement loop. See [synthetic-data](/technology/synthetic-data/) and [distillation](/technology/distillation/) for the adjacent techniques.

## What the context window actually means

204,800 tokens is the collection's lower-mid context tier: above the 128K era, below the 256K of the Kimi K2.7 line, and a fraction of the 1M windows on M3, [Kimi K3](/models/kimi-k3/) and [Qwen3.8-Max](/models/qwen38-max/). For a text-only model this is enough for long code review, multi-document analysis and agent traces, but it is not a long-document-synthesis tool. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

$0.30 input / $1.20 output per 1M tokens, cache reads at $0.06 and cache writes at $0.375. The 4x input-to-output ratio is standard, and the low cache-read price rewards agent loops that re-read shared context. At $0.30 input, M2.7 shares the database's cheapest flagship input price with M3 — but the [highspeed variant](/models/minimax-m27-highspeed/) doubles it to $0.60 for roughly 1.7x throughput, so the value question reduces to latency-versus-cost. See the [M3 vs M2.7 comparison](/comparisons/minimax-m3-vs-minimax-m2.7/) and [choosing-by-price](/guides/choosing-by-price/).

## API, coding, and agent implications

The two recorded benchmark rows are vendor-reported: GDPval-AA ELO 1495 and the MM Claw end-to-end benchmark 62.7. The model card adds more granular software-engineering claims — SWE-Pro 56.22% (matching GPT-5.3-Codex, per the card), Terminal Bench 2 57.0%, SWE Multilingual 76.5, Multi SWE Bench 52.7, and an MLE Bench Lite 66.6% medal rate said to be second only to Opus-4.6 and GPT-5.4 — but all of these are vendor-reported and none are independently re-measured. The operational constraint is interleaved thinking that is always on and cannot be disabled: every request pays reasoning latency and cost, and multi-turn history must echo the full assistant content (including thinking blocks) back. See [reasoning models](/technology/reasoning-models/) and the [coding hub](/models/coding/).

## Open weights and license

Open weight (~1.46M downloads) under a custom non-commercial license: MIT-style terms for non-commercial use only, commercial use requires prior written authorization, and "Built with MiniMax M2.7" attribution is required. China AI Hub analysis indicates this is the most restrictive open-weight license in the collection — stricter than MiniMax's own [M3 Community License](/models/minimax-m3/), which permits commercial use with attribution up to a revenue threshold — so M2.7 is closer to a research artifact than a deployable commercial base. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and the [open-weights hub](/models/open-weights/).

## Benchmark interpretation

GDPval-AA ELO 1495 is a preference-based ELO rating on a generative-dynamics benchmark, not an accuracy percentage, so it cannot be compared to accuracy rows; the MM Claw end-to-end 62.7 is a task-completion accuracy. Both are vendor-reported. The richer software-engineering numbers on the card (SWE-Pro, Terminal Bench 2, MLE Bench Lite) describe a strong but unverified coding profile.

## What the benchmarks do not prove

All M2.7 numbers are vendor-reported and not independently verified; the "self-evolving" 30% improvement and the MLE Bench Lite medal rate are MiniMax's own claims. Cross-vendor comparison is invalid without matching benchmark versions and harnesses. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [benchmark-methodology research](/research/benchmark-methodology-divergence/).

## Suitable and less suitable workloads

**Well-suited:** non-commercial research and experimentation, self-hosting where a text-only open model is enough, and agent/coding prototyping on MiniMax's API. **Less suited:** commercial production (license requires written authorization), multimodal input (text-only), long-form 1M-context synthesis, and any workload needing a documented parameter count or output ceiling.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Moderate |
| Coding | Moderate |
| Structured API workflows | Moderate |
| Agent orchestration | Moderate |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates M2.7's significance is as a positioning experiment rather than a specification milestone: it is the model through which MiniMax introduced the "self-evolving" training narrative that the database does not see the company repeat in the same form for M3. Its restrictive non-commercial license and undisclosed parameter count mark it as a transitional release — open in the sense of downloadable weights, but closed in the sense of commercial terms and technical disclosure. The enduring lesson for buyers is that "open weight" and "usable for commercial work" are separate questions in this collection, and M2.7 sits on the closed side of the latter.

## Market position and outlook

China AI Hub analysis indicates M2.7 occupies the pre-M3 generation of MiniMax's open line: it was superseded as the company's open flagship by [MiniMax-M3](/models/minimax-m3/) — which adds multimodal input, a 1M window, disclosed ~428B/23B parameters, and a less restrictive Community License — within three months of release. That rapid turnover is itself informative: it shows MiniMax treating open-weight releases as a recurring visibility channel while the commercial API carries the revenue, a pattern the database records across the Chinese open-weight layer. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [open-weight economics](/research/open-weight-vs-api-economics-in-china/) research.

## What is uncertain

- Parameter count and maximum output are not publicly disclosed.
- The "self-evolving" 30% improvement and the MLE Bench Lite medal rate are vendor-reported and not independently verified.
- The custom non-commercial license's exact scope of "commercial use" is not further specified beyond requiring written authorization.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-minimax-m2.7-1 | MiniMax API platform — model overview (CN) | https://platform.minimaxi.com/docs/guides/models-intro | Official documentation | — | 2026-09-20 | high | — |
| src-models-minimax-m2.7-2 | MiniMax official release notes | https://platform.minimaxi.com/docs/release-notes/models.md | Official documentation | — | 2026-09-20 | high | — |
| src-models-minimax-m2.7-3 | Hugging Face model card — MiniMax-M2.7 | https://huggingface.co/MiniMaxAI/MiniMax-M2.7 | Model card | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (pricing, context window, license and release facts from MiniMax's docs and the HF card), **Vendor-reported claim** (the benchmark scores and the self-evolution improvement claims), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
