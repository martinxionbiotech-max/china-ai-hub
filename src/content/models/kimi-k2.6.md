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

**What it is.** Kimi K2.6 is Moonshot AI's open-weight visual-and-text model, released 2026-04-20: a 1T-parameter MoE with 32B activated parameters and a 256K-token context window. **Why it matters.** It was Moonshot's open-weight workhorse before Kimi K3, and it publishes a full architecture card — a rarity among open releases — while remaining far lighter to self-host than the 2.8T K3. **Key characteristics.** 384 routed experts (8 selected + 1 shared), MLA attention with SwiGLU activation, 61 layers, a 400M MoonViT vision encoder, thinking and non-thinking modes, and a Modified MIT license. **What a professional should know.** It is superseded as Moonshot's flagship by K3 but is the practical open-weight Kimi to download; its only recorded benchmarks are two vendor-reported HLE rows.

## Architecture and parameters

K2.6 publishes a detailed card: 1T total / 32B activated (~3.2% activation), 384 routed experts with 8 selected + 1 shared per token, MLA (Multi-head Latent Attention) with SwiGLU activation, 61 layers (1 dense), and a 400M-parameter MoonViT vision encoder. China AI Hub analysis indicates this is a mid-scale MoE tuned for economy — the 32B active set keeps per-token cost low while the 1T total still dictates self-hosting memory, making it a multi-GPU but not datacenter-scale deployment. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 262,144-token context with a 98,304 output ceiling is the standard mid-tier split — long-input analysis, not long-form generation. China AI Hub analysis indicates this is the clearest spec-level gap from K3's 1M-in/1M-out pairing, and it is what keeps K2.6 a code/dialogue tool rather than a long-form synthesis tool. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

$0.95 input / $4.00 output per 1M tokens, cache hits $0.16 (17% of input). China AI Hub analysis indicates the 4.2x input-to-output ratio is mid-tier, and the cache pricing rewards agent loops that re-read shared context. See [choosing-by-price](/guides/choosing-by-price/).

## API, coding, and agent implications

K2.6 supports thinking and non-thinking modes for dialogue and agent tasks, with native vision. It is the model the K-series coding line ([Kimi K2.7 Code](/models/kimi-k27-code/)) and the [Kimi Code](/agents/kimi-code/) agent evolved from, though its own coding benchmark evidence is not separately recorded. See [choosing-a-coding-model](/guides/choosing-a-coding-model/).

## Open weights and license

Open weight under Modified MIT, self-hostable. China AI Hub analysis indicates the Modified MIT label is a softer constraint than plain MIT — permissive for most uses but with conditions that should be read before commercial redistribution, distinct from the revenue-threshold licenses on K3 and the Qwen3.8-Max-class weights. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and the [open-weights hub](/models/open-weights/).

## Benchmark interpretation

The two recorded rows are both vendor-reported HLE scores: 36.4 text-only (no tools) and 55.5 with tools. The 19-point gap is the same tool-access pattern the database records elsewhere — tool use materially raises the ceiling on the hardest knowledge exam.

## What the benchmarks do not prove

Two vendor-reported HLE rows do not independently verify K2.6 against competitors, and there are no recorded coding or agent benchmarks for K2.6 despite its positioning. Cross-vendor comparison is invalid without matched harnesses and versions. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [benchmark-methodology research](/research/benchmark-methodology-divergence/).

## Suitable and less suitable workloads

**Well-suited:** open-weight visual-and-text deployment, self-hosting where a permissive-ish license and a 1T/32B footprint fit, dialogue and agent tasks, and multimodal (vision) input. **Less suited:** 1M-context long-form work, frontier-scale generation, and any use case that has already standardized on K3.

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

China AI Hub analysis indicates K2.6's enduring value is as the practical open-weight Kimi: it retains a full architecture card and a permissive-style license while being roughly a third the total parameters of K3 (1T vs 2.8T), which is why it remains the more tractable self-host choice even after K3 took the flagship role. Its thin benchmark record — two HLE rows and nothing for coding or agents — is the clearest sign that it is a transitional release: capable and transparent, but quickly overtaken by the K2.7 coding line and K3 within the same family. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research and the [MoE hub](/models/moe/).

## What is uncertain

- The Modified MIT license's exact conditions are less fully spelled out than plain MIT and should be read before redistribution.
- Only two benchmark rows (both HLE, both vendor-reported) are recorded; no coding or agent benchmarks are published.
- The 98,304-token output ceiling is documented as the evaluation-configuration max, not necessarily a hard API cap.

## Sources

- [Kimi API platform — model list](https://platform.kimi.ai/docs/models.md)
- [Kimi API — pricing (chat)](https://platform.kimi.ai/docs/pricing/chat)
- [Hugging Face model card — Kimi K2.6 (architecture, parameters, benchmarks)](https://huggingface.co/moonshotai/Kimi-K2.6)

*Labels used above: **Official fact** (architecture, parameters and pricing from Moonshot's docs and the HF card), **Vendor-reported claim** (the two HLE benchmark scores), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
