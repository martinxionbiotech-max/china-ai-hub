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

The Z.ai API (Zhipu's international platform) serves the GLM family via an OpenAI-compatible Chat
Completions endpoint at `https://api.z.ai/api/paas/v4/chat/completions`. GLM-5.3 additionally supports
the OpenAI Responses protocol (base `https://api.z.ai/api/v1`) and the Anthropic Messages protocol (base
`https://api.z.ai/api/anthropic`); the GLM Coding Plan uses `https://api.z.ai/api/coding/paas/v4`.

Authentication is a Bearer API key. Streaming is supported, with `tool_stream: true` for tool-streaming
(recommended for Flash models). The China platform (BigModel, open.bigmodel.cn) is operated separately.
