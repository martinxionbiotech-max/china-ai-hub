---
api_id: ark
description: "ByteDance's Volcengine Ark AI API platform (ark.cn-beijing.volces.com): OpenAI-compatible endpoints for the Doubao Seed 2.1 family (Pro / Evolving / Turbo) with up to 1M-token context, vision, tool calling and structured output. Flagship rate limits 500 RPM / 1,000,000 TPM; Bearer API key auth."
provider: bytedance
api_type: official
endpoint: https://ark.cn-beijing.volces.com/api/v3
authentication: "API key (Bearer token); AK/SK also documented for the chat API"
streaming: true
tool_calling: true
structured_output: true
vision: true
context_limits:
  - model: doubao-seed-2-1-pro
    input_limit: 1048576
    output_limit: 262144
  - model: doubao-seed-evolving
    input_limit: 1048576
    output_limit: 262144
  - model: doubao-seed-2-1-turbo
    input_limit: 262144
    output_limit: 262144
rate_limits: "Flagship Doubao models: 500 RPM / 1,000,000 TPM (as of 2026-09-20)"
regions:
  - china
cloud_providers:
  - Volcengine
pricing_ref: bytedance
documentation: https://docs.volcengine.com/docs/ark
last_verified: "2026-09-20"
sources:
  - source_name: Ark product overview (base URL, auth)
    source_url: https://docs.volcengine.com/docs/ark/product-overview?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark Responses API reference
    source_url: https://docs.volcengine.com/docs/ark/responses-api-text-generation?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark Chat API reference
    source_url: https://docs.volcengine.com/docs/ark/chat-api?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Volcengine Ark is ByteDance's official AI API platform, serving the Doubao Seed model family from the
cn-beijing region. It exposes a Responses API (`POST /api/v3/responses`) and an OpenAI-compatible Chat
API (`POST /api/v3/chat/completions`), both with SSE streaming. Authentication uses a Bearer API key
obtained from the Ark console; the chat API additionally documents AK/SK access-key authentication.

The API supports thinking toggles (`thinking={"type":"enabled"|"disabled"}`, `reasoning_effort`),
tool calling and structured output (json_schema recommended). Chat API messages can carry text, image,
video and audio content; a Files API handles uploads of video, image and PDF inputs. Third-party models
(such as DeepSeek and GLM) are also hosted on Ark.
