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

DeepSeek-V3.2 (released 2025-12-01, MIT open weights) is the previous DeepSeek flagship. DeepSeek
claimed "GPT-5 level performance" at release, and that the API-only V3.2-Speciale variant rivaled
Gemini-3.0-Pro with gold-medal results in math/programming olympiads; the release page lists no numeric
scores. V3.2 has been replaced on the DeepSeek API by the V4 family (V4 Preview launched 2026-04-24),
but the open weights remain available on Hugging Face.

## Status and successor

DeepSeek-V3.2 is **discontinued** — superseded by [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) and the
wider V4 family on the DeepSeek API. It is kept in the database for historical and open-weight
reference. Because it is API-discontinued, no current API pricing applies; the architecture below is
recorded from the Hugging Face `config.json` (61 layers, hidden size 7168, 256 routed experts with
8 selected + 1 shared, vocab 129,280).

## What is and is not documented

DeepSeek's own release pages do not state a numeric context window or benchmark scores — the release
page carries qualitative claims ("GPT-5 level performance") rather than measurements. China AI Hub
analysis indicates the absence of numeric scores on a flagship release is itself informative: it
signals a positioning-by-claim rather than positioning-by-benchmark release, which the V4 family later
reversed by publishing concrete benchmark tables.

## Historical significance

V3.2 introduced DeepSeek Sparse Attention (DSA) and remains relevant as the MIT-licensed checkpoint
that preceded the V4 generation. For self-hosters and researchers it is a downloadable artifact; for
API users it is retired. See [how DeepSeek changed China's AI market](/research/how-deepseek-changed-chinas-ai-market/) for the market context.

*Labels used above: **Official fact** (architecture from config.json, release facts), **Vendor-reported claim** (the "GPT-5 level performance" claim), and **China AI Hub analysis** (our synthesis, introduced as such). Context window and benchmark scores are not publicly documented for this model.*
