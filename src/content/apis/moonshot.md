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

The Moonshot AI (Kimi) API serves the Kimi K-series at `api.moonshot.ai`. It exposes OpenAI-compatible
Chat Completions (`/v1/chat/completions`), OpenAI Responses (`/v1/responses`) and an Anthropic-compatible
Messages endpoint (`/anthropic/v1/messages`), plus files, batches, tokenizer and web-search tools.

Streaming is SSE with separate reasoning_content and content deltas. kimi-k3 uses top-level
reasoning_effort (low/high/max, default max); K2.x models use the thinking parameter. JSON mode /
structured output, automatic context caching and file upload (text/image/video) are supported.
Temperature and top_p are fixed for K3 and K2.x. Serving regions are not stated in the fetched docs.
