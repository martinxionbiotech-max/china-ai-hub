---
image: "/images/ai/models-deepseek-v3-2.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: deepseek-v3-2
model_name: DeepSeek-V3.2
provider: deepseek
model_family: DeepSeek-V3
superseded_by: deepseek-v4-pro
release_date: "2025-12-01"
status: discontinued
architecture: "DeepSeek Sparse Attention (DSA) MoE — 61 layers, hidden size 7168, MoE intermediate 2048, 256 routed experts (8 selected + 1 shared expert), vocab 129,280 (from config.json)"
capabilities:
  reasoning: true
  coding: true
  tool_calling: true
  agent_capability: true
open_weight: true
license: MIT
self_hosting: true
api_available: false
official_api: false
known_limitations:
  - "Replaced on the DeepSeek API by the V4 family"
  - "Context window not stated on the official release pages fetched"
  - "Vendor performance claims are qualitative ('GPT-5 level performance'); no numeric scores on the release page"
last_verified: "2026-09-27"
sources:
  - source_name: DeepSeek-V3.2 release
    source_url: https://www.deepseek.com/en/news/deepseek-v3-2/
    source_type: official
    published_date: "2025-12-01"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Transparency Center
    source_url: https://www.deepseek.com/en/transparency/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V3.2
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V3.2
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
  - source_name: Hugging Face config.json — DeepSeek-V3.2 (layer/expert/hidden dimensions)
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V3.2/raw/main/config.json
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

**What it is.** DeepSeek-V3.2 (released 2025-12-01, MIT open weights) is the previous DeepSeek flagship: a DeepSeek Sparse Attention (DSA) MoE that introduced the sparse-attention direction the V4 family later commercialized. **Why it matters.** It is the MIT-licensed checkpoint that marked DeepSeek's turn from dense attention toward sparse-attention cost economics, and it remains a downloadable artifact for self-hosters and researchers even though the API is retired. **Key characteristics.** 61 layers, hidden size 7168, 256 routed experts (8 selected + 1 shared), vocab 129,280 (from `config.json`); reasoning, coding, tool-calling and agent capabilities. **What a professional should know.** It is **discontinued** on the DeepSeek API (superseded by the [V4 family](/models/deepseek-v4-pro/)), the release page carries qualitative rather than numeric performance claims, and no numeric context window or benchmark scores were published.

## Status and successor

DeepSeek-V3.2 is **discontinued** — superseded by [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) and the wider V4 family on the DeepSeek API. It is kept in the database for historical and open-weight reference. Because it is API-discontinued, no current API pricing applies. China AI Hub analysis indicates V3.2's supersession is the pivot point where DeepSeek moved from a conventional MoE (V3.2's 256-expert dense-attention design) to the sparse-attention V4 generation, so the model's historical role is as the last of the pre-sparse DeepSeek flagships.

## Architecture and parameters

The architecture is recorded from the Hugging Face `config.json`: 61 layers, hidden size 7168, MoE intermediate 2048, 256 routed experts with 8 selected + 1 shared per token, and a 129,280 vocab. DeepSeek Sparse Attention (DSA) is the headline innovation — a linear-attention-style mechanism that makes long context cheaper by cutting the quadratic cost of standard attention. China AI Hub analysis indicates DSA is the architectural through-line from V3.2 to the V4 family: V3.2 introduced the direction, and V4.1-Flash's 552B asymmetric sparse design is the commercial maturation of the same cost-per-token logic. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What is and is not documented

DeepSeek's own release pages do not state a numeric context window or benchmark scores — the release page carries qualitative claims ("GPT-5 level performance") and notes that the API-only V3.2-Speciale variant rivaled Gemini-3.0-Pro with gold-medal results in math/programming olympiads, but lists no numbers. China AI Hub analysis indicates the absence of numeric scores on a flagship release is itself informative: it signals a positioning-by-claim rather than positioning-by-benchmark release, which the V4 family later reversed by publishing concrete benchmark tables.

## Open weights and license

MIT-licensed open weight and self-hostable. This is the most permissive license in the collection, and — combined with the fact that the weights remain downloadable after API discontinuation — it is the main reason V3.2 retains reference value. The practical caveat is that this is a 2025-generation model: a 256-expert dense-attention MoE of this scale is a substantial multi-GPU deployment, and it is no longer a frontier model. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

There are no numeric benchmark rows recorded: the release page publishes qualitative comparisons only. This is a genuine absence in the source material, not a gap in the database — DeepSeek did not publish a numeric score table for V3.2 on the fetched release pages.

## What the benchmarks do not prove

With no numeric scores, there is nothing with which to rank V3.2 against competitors, and the "GPT-5 level performance" and "gold-medal olympiad" claims are qualitative and cannot be independently verified from the release page. Treat capability as vendor-positioned. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** historical and open-weight research, self-hosting where a permissive MIT license and a downloadable 2025-generation checkpoint are the goal, and reproducibility work on the sparse-attention lineage. **Less suited:** any production API workload (discontinued), frontier-scale reasoning (superseded), and long-context work without a documented context window.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Unknown |
| Coding | Moderate |
| Structured API workflows | No evidence |
| Agent orchestration | Unknown |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | No evidence |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims. API-dependent rows are No evidence because the model is API-discontinued; long-context and agent rows are Unknown because no context window or benchmark data was published.

## Historical significance

China AI Hub analysis indicates V3.2's enduring relevance is as the architectural waypoint between DeepSeek's dense-attention past and its sparse-attention future: it introduced DSA and the MIT-licensed checkpoint that preceded the V4 generation, and its qualitative-only release framing is the contrast against which the V4 family's benchmark-table releases should be read. For self-hosters and researchers it is a downloadable artifact; for API users it is retired. See [how DeepSeek changed China's AI market](/research/how-deepseek-changed-chinas-ai-market/) for the market context.

## What is uncertain

- The numeric context window is not stated on the official release pages fetched.
- Vendor performance claims are qualitative; no numeric benchmark scores were published.
- Whether the MIT-licensed weights match the final API checkpoint is not separately documented.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-deepseek-v3-2-1 | DeepSeek-V3.2 release | https://www.deepseek.com/en/news/deepseek-v3-2/ | Official | 2025-12-01 | 2026-09-20 | high | — |
| src-models-deepseek-v3-2-2 | DeepSeek Transparency Center | https://www.deepseek.com/en/transparency/ | Official | — | 2026-09-20 | high | — |
| src-models-deepseek-v3-2-3 | Hugging Face model card — DeepSeek-V3.2 | https://huggingface.co/deepseek-ai/DeepSeek-V3.2 | Model card | — | 2026-09-20 | high | — |
| src-models-deepseek-v3-2-4 | Hugging Face config.json — DeepSeek-V3.2 (layer/expert/hidden dimensions) | https://huggingface.co/deepseek-ai/DeepSeek-V3.2/raw/main/config.json | Official documentation | — | 2026-09-27 | high | — |

*Labels used above: **Official fact** (architecture from config.json, release facts), **Vendor-reported claim** (the "GPT-5 level performance" claim), and **China AI Hub analysis** (our synthesis, introduced as such). Context window and benchmark scores are not publicly documented for this model.*
