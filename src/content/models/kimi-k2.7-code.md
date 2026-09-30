---
image: "/images/ai/models-kimi-k2.7-code.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.7-code
model_name: Kimi K2.7 Code
provider: moonshot-ai
model_family: Kimi K2.7
status: active
context_window: 262144
capabilities:
  reasoning: true
  coding: true
open_weight: null
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
  - "Architecture and parameter counts are not publicly disclosed by Moonshot for the K2.7 series (API-only coding models)"
  - "Thinking is always on; temperature/top_p/n/penalties are fixed and must not be passed"
  - "Max output ceiling not stated in the fetched docs (256K context)"
  - "No open-weight release confirmed for K2.7 series"
last_verified: "2026-09-27"
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
---

**What it is.** Kimi K2.7 Code is Moonshot AI's dedicated coding model, an API-only member of the Kimi K2.7 family with a 256K-token context window and always-on thinking. **Why it matters.** It is Moonshot's code-specialist tier — distinct from the general-purpose, open-weight Kimi K2.6 and the flagship Kimi K3 — priced for high-volume coding and agent work rather than frontier reasoning. **Key characteristics.** 262,144-token context, reasoning and coding capabilities, $0.95 input / $4.00 output per 1M tokens (cache hits $0.19), and a doubled-price highspeed variant. **What a professional should know.** Architecture and parameter counts are not disclosed for the K2.7 series, thinking cannot be disabled, and sampling parameters (temperature, top_p, n, penalties) are fixed — you cannot tune them through the API.

## Architecture and parameters

Moonshot discloses no architecture or parameter counts for the K2.7 series, and the database records that absence rather than estimating. China AI Hub analysis indicates this is a deliberate API-only posture: Moonshot publishes full architecture cards for its open-weight models ([Kimi K2.6](/models/kimi-k26/), [Kimi K3](/models/kimi-k3/)) but keeps the coding line closed and undocumented, which points to a monetization strategy rather than an engineering omission. See [Mixture-of-Experts](/technology/mixture-of-experts/) for the architectural context Moonshot does not provide here, and the [MoE architectures research](/research/chinese-ai-moe-architectures/) for how the disclosure gradient runs across labs.

## What the context window actually means

A 262,144-token context is the mid tier of the collection — above MiniMax-M2.7's 204,800 but a quarter of the 1M windows on Kimi K3, Qwen3.8 and the Doubao Seed Pro/Evolving models. For coding work this is enough to hold a full repository, a large diff, or a long agent trace in a single request, but it is not a long-document-analysis tool. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

$0.95 input / $4.00 output per 1M tokens with cache hits at $0.19 (20% of input). China AI Hub analysis indicates the 4.2x input-to-output ratio sits between the general K2.6's identical list price and K3's 5x flagship ratio, and the aggressive cache-hit discount is aimed squarely at agent loops that re-read shared context. A highspeed variant serves the same model at 2x the price for latency-sensitive work. See the [Kimi K3 vs K2.7 Code comparison](/comparisons/kimi-k3-vs-kimi-k27-code/) and the [choosing-by-price guide](/guides/choosing-by-price/).

## API, coding, and agent implications

K2.7 Code targets software engineering: it carries coding and reasoning capabilities and is served through the Moonshot AI Platform. The operational constraints are the story — always-on thinking means every request pays reasoning latency and cost, and fixed sampling (temperature/top_p/n/penalties) removes the usual reproducibility levers. China AI Hub analysis indicates the fixed sampling is a deliberate product choice that trades deterministic-output control for a curated coding response, which is an under-appreciated constraint for batch and CI/CD workloads that expect reproducible generation. The [Kimi Code](/agents/kimi-code/) agent is the product built on the K-series. See [choosing-a-coding-model](/guides/choosing-a-coding-model/) and the [coding model hub](/models/coding/).

## Open weights and license

API-only: no open-weight release is confirmed for the K2.7 series, and the model cannot be self-hosted. This contrasts with Moonshot's open-weight K2.6 (Modified MIT) and K3 (Kimi K3 License). See [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

No benchmark scores are recorded for K2.7 Code in the database. This is an absence of evidence, not evidence of absence — Moonshot has not published K2.7-Code-specific benchmark results on the fetched official pages.

## What the benchmarks do not prove

With no recorded benchmarks, there is nothing with which to rank K2.7 Code against competitors, and any third-party claims about its coding ability cannot be verified against official numbers. Treat capability as vendor-positioned until Moonshot publishes results. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** high-volume coding and agent work on the Moonshot platform where the cache-hit pricing and coding focus pay off, and interactive coding where the highspeed variant's faster throughput matters. **Less suited:** long-document analysis (256K, not 1M), workloads needing deterministic or tunable sampling, and open-weight or self-hosting requirements.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Moderate |
| Coding | High |
| Structured API workflows | Moderate |
| Agent orchestration | Moderate |
| Local self-hosted deployment | No evidence |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates that K2.7 Code is Moonshot's code-monetization line: an API-only, closed-weight coding SKU that sits below the flagship K3 on price ($0.95 vs $3.00 input) while inheriting none of K3's 1M output headroom or open weights. Its fixed sampling and always-on thinking are the two constraints that most shape real use — together they mean K2.7 Code optimizes for a curated, reasoning-heavy coding output rather than reproducible, tunable generation. The pairing with a 2x-priced highspeed tier is the same throughput-segmentation pattern the database records at [MiniMax](/models/minimax-m27-highspeed/) and [Zhipu](/models/glm-53-flashx/), which signals that speed-tiered billing is now standard across the Chinese API layer. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research and the [reasoning hub](/models/reasoning/).

## What is uncertain

- Architecture and parameter counts are not publicly disclosed for the K2.7 series.
- No benchmark scores are published for K2.7 Code.
- The maximum output ceiling is not stated in the fetched docs.
- Sampling parameters are fixed and cannot be modified through the API.

## Sources

- [Kimi API platform — model list](https://platform.kimi.ai/docs/models.md)
- [Kimi API — pricing (chat)](https://platform.kimi.ai/docs/pricing/chat)

*Labels used above: **Official fact** (pricing and context window from Moonshot's docs) and **China AI Hub analysis** (our synthesis, always introduced as such). No benchmark evidence is currently recorded for this model.*
