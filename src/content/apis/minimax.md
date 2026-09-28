---
image: "/images/ai/apis-minimax.webp"
image_credit: "AI-generated illustration (Seedream)"
api_id: minimax
description: "MiniMax's API platform with an Anthropic-compatible endpoint (api.minimax.io/anthropic): MiniMax-M3 (1M context) plus M2.7 and M2.7-HighSpeed, with vision, streaming and tool calling. Serves international and China regions; ANTHROPIC_API_KEY-style auth."
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
known_limitations:
  - "Rate limits published on a JS-rendered docs page; structured_output not publicly documented as of 2026-09-27"
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
**What it is.** The MiniMax API serves the M-series through Anthropic-compatible and OpenAI-compatible endpoints, with international (api.minimax.io) and China (api.minimax.cn) bases. **Why it matters.** It is the primary way to access [MiniMax-M3](/models/minimax-m3/)'s 1M-token context and multimodal input at the database's lowest flagship price ($0.30/$1.20 per 1M tokens). **Key characteristics.** Anthropic-compatible endpoint with `ANTHROPIC_API_KEY`-style auth; streaming with thinking/text deltas; `service_tier` (standard | priority, priority = 1.5x price); automatic prompt caching. **What a professional should know.** Rate limits are published on a JS-rendered page (not extractable), and structured output is not publicly documented — both are known limitations to verify before production use.

The MiniMax API serves the M-series through Anthropic-compatible and OpenAI-compatible endpoints:
international base `https://api.minimax.io/anthropic` (China: `https://api.minimax.cn/anthropic`), plus
OpenAI Chat Completions and Responses endpoints and legacy MiniMax-native endpoints.

Streaming is supported (thinking streamed as thinking_delta, text as text_delta). Key parameters:
max_tokens, temperature (0-2, recommended 1.0), top_p, tools/tool_choice, service_tier
(standard | priority, priority = 1.5x price). M3 supports the thinking parameter (disabled by default,
adaptive to enable) and multimodal Anthropic content blocks (image/video via URL, base64 or
mm_file://{file_id}). Prompt caching is automatic with explicit cache_control support.

## Why it matters

The MiniMax API matters as the Anthropic-compatibility play: by exposing an `ANTHROPIC_API_KEY`-style endpoint, it lets teams already on the Claude ecosystem switch models with minimal code change — a deliberate contrast to DeepSeek's OpenAI-first surface. The cost trade-off is the `service_tier` structure (priority = 1.5x) layered on top of already-low M3 pricing, plus automatic prompt caching that lowers repeat-query cost. China AI Hub analysis indicates the API's structural role is the value-compatible option: Anthropic-style integration at the database's cheapest flagship price, with the gaps being structured output and published rate limits.

*Labels used above: **Official fact** (from MiniMax's Anthropic-compatible API and pricing docs), **Vendor-reported claim** (pricing and capability statements by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such).*
