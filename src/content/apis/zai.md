---
image: "/images/ai/apis-zai.webp"
image_credit: "AI-generated illustration (Seedream)"
api_id: zai
description: "Zhipu AI's Z.AI API platform (api.z.ai/api/paas/v4/chat/completions): GLM-5.3 and GLM-5.3-Flash with 1M-token context and vision. Bearer API key; available internationally via Z.ai and in China via BigModel."
provider: zhipu-ai
api_type: official
endpoint: https://api.z.ai/api/paas/v4/chat/completions
authentication: "Bearer API key"
streaming: true
function_calling: true
tool_calling: true
structured_output: null
vision: true
audio: null
context_limits:
  - model: glm-5.3
    input_limit: 1048576
    output_limit: 131072
  - model: glm-5.3-flash
    input_limit: 1048576
    output_limit: 131072
regions:
  - international
  - china
cloud_providers:
  - Z.ai
  - BigModel
pricing_ref: zhipu-ai
documentation: https://docs.z.ai/
known_limitations:
  - "Rate limit documentation page not located (docs.z.ai paths 404) as of 2026-09-27"
last_verified: "2026-09-20"
sources:
  - source_name: Z.ai docs — Quick Start
    source_url: https://docs.z.ai/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**What it is.** The Z.ai API is Zhipu AI's international platform serving the GLM family through an OpenAI-compatible Chat Completions endpoint, with Responses and Anthropic Messages protocols on GLM-5.3. **Why it matters.** It is the international distribution path for [GLM-5.3](/models/glm-53/) and [GLM-5.3-Flash](/models/glm-53-flash/), the latter at a budget-tier $0.15/$0.50 per 1M tokens. **Key characteristics.** Three protocol surfaces (Chat Completions, Responses, Anthropic Messages) plus a dedicated coding-plan endpoint; `tool_stream: true` for tool streaming (recommended for Flash models); 1M-token context. **What a professional should know.** The China platform (BigModel, open.bigmodel.cn) is operated separately, and the rate-limit documentation page was not located (docs.z.ai paths 404) — a gap to verify before production use.

The Z.ai API (Zhipu's international platform) serves the GLM family via an OpenAI-compatible Chat
Completions endpoint at `https://api.z.ai/api/paas/v4/chat/completions`. GLM-5.3 additionally supports
the OpenAI Responses protocol (base `https://api.z.ai/api/v1`) and the Anthropic Messages protocol (base
`https://api.z.ai/api/anthropic`); the GLM Coding Plan uses `https://api.z.ai/api/coding/paas/v4`.

Authentication is a Bearer API key. Streaming is supported, with `tool_stream: true` for tool-streaming
(recommended for Flash models). The China platform (BigModel, open.bigmodel.cn) is operated separately.

## Why it matters

The Z.ai API matters as the multi-protocol surface for open-weight GLM models: it is one of the few tracked APIs exposing OpenAI, Anthropic *and* a coding-plan endpoint from a single provider, which lowers migration cost for teams that want both general and coding access to the same GLM-5.3 family. The cost trade-off is favorable at the flash tier ($0.15/$0.50) and moderate at the flagship ($1.40/$4.40), while the documented gap — no located rate-limit page — is an operational uncertainty. China AI Hub analysis indicates the API's structural role is the international, protocol-flexible entry to Zhipu's open model family, with the BigModel split meaning China and international are managed as separate surfaces.

*Labels used above: **Official fact** (from Z.ai Quick Start and GLM-5.3 docs), **Vendor-reported claim** (pricing and capability statements by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
