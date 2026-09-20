---
api_id: minimax
provider: minimax
api_type: official
endpoint: https://api.minimax.io/anthropic
authentication: "API key (Bearer-style, passed via ANTHROPIC_API_KEY), managed in the platform console"
streaming: true
function_calling: true
tool_calling: true
structured_output: null
vision: true
audio: null
context_limits:
  - model: minimax-m3
    input_limit: 1048576
  - model: minimax-m2.7
    input_limit: 204800
  - model: minimax-m2.7-highspeed
    input_limit: 204800
regions:
  - international
  - china
cloud_providers:
  - MiniMax Platform
pricing_ref: minimax
documentation: https://platform.minimax.io/docs
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax API — Anthropic-compatible API (intl)
    source_url: https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax API platform — pay-as-you-go pricing (intl)
    source_url: https://platform.minimax.io/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

The MiniMax API serves the M-series through Anthropic-compatible and OpenAI-compatible endpoints:
international base `https://api.minimax.io/anthropic` (China: `https://api.minimax.cn/anthropic`), plus
OpenAI Chat Completions and Responses endpoints and legacy MiniMax-native endpoints.

Streaming is supported (thinking streamed as thinking_delta, text as text_delta). Key parameters:
max_tokens, temperature (0-2, recommended 1.0), top_p, tools/tool_choice, service_tier
(standard | priority, priority = 1.5x price). M3 supports the thinking parameter (disabled by default,
adaptive to enable) and multimodal Anthropic content blocks (image/video via URL, base64 or
mm_file://{file_id}). Prompt caching is automatic with explicit cache_control support.
