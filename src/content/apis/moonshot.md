---
image: "/images/ai/apis-moonshot.webp"
image_credit: "AI-generated illustration (Seedream)"
api_id: moonshot
description: "Moonshot AI's Kimi API platform (api.moonshot.ai/v1): Kimi K3 with 1M-token input and output context, plus K2.7-Code and K2.7-Code-HighSpeed, with vision, streaming and structured output. MOONSHOT_API_KEY Bearer auth."
provider: moonshot-ai
api_type: official
endpoint: https://api.moonshot.ai/v1
authentication: "Bearer API key (MOONSHOT_API_KEY), managed in the platform console"
streaming: true
function_calling: true
tool_calling: true
structured_output: true
vision: true
audio: null
context_limits:
  - model: kimi-k3
    input_limit: 1048576
    output_limit: 1048576
  - model: kimi-k2.7-code
    input_limit: 262144
  - model: kimi-k2.7-code-highspeed
    input_limit: 262144
  - model: kimi-k2.6
    input_limit: 262144
regions: []
cloud_providers:
  - Moonshot AI Platform
pricing_ref: moonshot-ai
documentation: https://platform.kimi.ai/docs
known_limitations:
  - "Rate limits and regions are published behind a JS-rendered docs page; not extractable into structured data as of 2026-09-27"
last_verified: "2026-09-20"
sources:
  - source_name: Kimi API overview
    source_url: https://platform.kimi.ai/docs/api/overview.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API — Chat Completions spec
    source_url: https://platform.kimi.ai/docs/api/chat.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**What it is.** The Moonshot AI (Kimi) API serves the Kimi K-series at `api.moonshot.ai`, exposing OpenAI-compatible Chat Completions and Responses plus an Anthropic-compatible Messages endpoint. **Why it matters.** It is the developer path to [Kimi K3](/models/kimi-k3/)'s 1M-token input *and* output context — the database's only full-window output ceiling. **Key characteristics.** Separate `reasoning_content` and `content` stream deltas; K3 uses `reasoning_effort` (low/high/max) while K2.x uses `thinking`; JSON mode / structured output, automatic context caching, file upload (text/image/video). **What a professional should know.** Temperature and top_p are fixed for K3 and K2.x (not tunable), and rate limits/regions are published behind a JS-rendered page that could not be extracted into structured data.

The Moonshot AI (Kimi) API serves the Kimi K-series at `api.moonshot.ai`. It exposes OpenAI-compatible
Chat Completions (`/v1/chat/completions`), OpenAI Responses (`/v1/responses`) and an Anthropic-compatible
Messages endpoint (`/anthropic/v1/messages`), plus files, batches, tokenizer and web-search tools.

Streaming is SSE with separate reasoning_content and content deltas. kimi-k3 uses top-level
reasoning_effort (low/high/max, default max); K2.x models use the thinking parameter. JSON mode /
structured output, automatic context caching and file upload (text/image/video) are supported.
Temperature and top_p are fixed for K3 and K2.x. Serving regions are not stated in the fetched docs.

## Why it matters

The Kimi API matters as the long-context-generation path: Kimi K3's 1M-token output ceiling — unique in the database — is only reachable through this API, making it the reference surface for long-form generation and whole-repo rewriting. The cost trade-off is the premium: $3.00/$15.00 per 1M tokens for kimi-k3, the highest input/output pricing among the non-Doubao flagships. China AI Hub analysis indicates the API's structural role is the long-output specialist, with fixed sampling parameters (temperature/top_p) as the notable constraint for teams that normally tune generation.

*Labels used above: **Official fact** (from the Kimi API overview and Chat Completions spec), **Vendor-reported claim** (pricing and capability statements by Moonshot AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
