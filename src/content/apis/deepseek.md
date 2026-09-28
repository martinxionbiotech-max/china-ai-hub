---
image: "/images/ai/apis-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
api_id: deepseek
description: "DeepSeek's official API platform (api.deepseek.com): OpenAI-compatible endpoints for DeepSeek-V4-Pro and V4.1-Flash with vision, function calling, tool calling and structured output. Bearer API key authentication."
provider: deepseek
api_type: official
endpoint: https://api.deepseek.com
authentication: "Bearer API key (created at platform.deepseek.com/api_keys)"
streaming: true
function_calling: true
tool_calling: true
structured_output: true
vision: true
audio: null
context_limits:
  - model: deepseek-v4-1-flash
    input_limit: 1048576
    output_limit: 393216
  - model: deepseek-v4-pro
    input_limit: 1048576
    output_limit: 393216
rate_limits: "Concurrency: deepseek-flash 2500; deepseek-v4-pro 500 (per official pricing page)"
regions: []
cloud_providers:
  - DeepSeek Platform
pricing_ref: deepseek
documentation: https://api-docs.deepseek.com/
known_limitations:
  - "Official docs publish concurrency limits only; no regional deployment breakdown as of 2026-09-27"
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek API docs
    source_url: https://api-docs.deepseek.com/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API docs — Models & Pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**What it is.** The DeepSeek API is DeepSeek's official, OpenAI-compatible platform serving [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) and [V4-Pro](/models/deepseek-v4-pro/), with an additional Anthropic-compatible base URL. **Why it matters.** It is the price-floor API of the Chinese market — V4.1-Flash lists $0.15/1M input — and the most compatibility-complete (OpenAI, Responses and Anthropic surfaces in one platform). **Key characteristics.** Two base URLs (`api.deepseek.com` and `api.deepseek.com/anthropic`); 1M-token context and 384K max output on both models; thinking/non-thinking modes, JSON output, tool calls, automatic KV caching. **What a professional should know.** Peak/off-peak pricing applies (peak is 2x the listed off-peak), concurrency limits are 2500 (flash) / 500 (v4-pro), and serving regions are not stated in the official docs.

The DeepSeek API is an OpenAI-compatible platform with two base URLs: `https://api.deepseek.com`
(OpenAI-compatible, also used by the native Responses API) and `https://api.deepseek.com/anthropic`
(Anthropic-compatible). Authentication is a Bearer API key; streaming is supported.

Current models are `deepseek-flash` (V4.1-Flash, multimodal) and `deepseek-v4-pro`, both with 1M-token
context and 384K max output, thinking and non-thinking modes, JSON output, tool calls, and automatic KV
context caching. Peak/off-peak pricing applies. FIM and Chat Prefix Completion are in beta
(non-thinking only). The serving regions are not stated in the official docs.

## Why it matters

The DeepSeek API matters as the cost-and-compatibility reference point: its $0.15/1M flash input price is the lowest budget tier in the database, and its triple surface (OpenAI / Responses / Anthropic) minimizes integration friction for teams migrating from either ecosystem. The trade-off is operational opacity — no published serving regions and a peak/off-peak structure that doubles cost during peak windows. China AI Hub analysis indicates the API's structural role is the low-cost default: it is the surface most likely to be chosen on price alone, with compatibility as the secondary moat and region transparency as the notable gap.

*Labels used above: **Official fact** (from DeepSeek API docs and pricing page), **Vendor-reported claim** (pricing and concurrency figures published by DeepSeek), and **China AI Hub analysis** (our synthesis, always introduced as such).*
