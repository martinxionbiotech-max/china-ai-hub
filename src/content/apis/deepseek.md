---
api_id: deepseek
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

The DeepSeek API is an OpenAI-compatible platform with two base URLs: `https://api.deepseek.com`
(OpenAI-compatible, also used by the native Responses API) and `https://api.deepseek.com/anthropic`
(Anthropic-compatible). Authentication is a Bearer API key; streaming is supported.

Current models are `deepseek-flash` (V4.1-Flash, multimodal) and `deepseek-v4-pro`, both with 1M-token
context and 384K max output, thinking and non-thinking modes, JSON output, tool calls, and automatic KV
context caching. Peak/off-peak pricing applies. FIM and Chat Prefix Completion are in beta
(non-thinking only). The serving regions are not stated in the official docs.
