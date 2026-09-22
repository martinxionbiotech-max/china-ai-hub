---
image: "/images/ai/apis-model-studio.webp"
image_credit: "AI-generated illustration (Seedream)"
api_id: model-studio
description: "Alibaba Cloud Model Studio (DashScope-compatible endpoint dashscope-us.aliyuncs.com): Qwen3.8-Max and Qwen3.8-Flash with ~968K context, vision and structured output. Region-bound API keys; global regions (Frankfurt / US / Tokyo / Hong Kong) at 30,000 RPM and 5,000,000 TPM."
provider: alibaba-cloud
api_type: official
endpoint: https://dashscope-us.aliyuncs.com/compatible-mode/v1
authentication: "API key (DASHSCOPE_API_KEY), created in the Model Studio console; keys are region-bound"
streaming: true
function_calling: true
tool_calling: true
structured_output: true
vision: true
audio: null
context_limits:
  - model: qwen3.8-max
    input_limit: 991808
    output_limit: 131072
  - model: qwen3.8-flash
    input_limit: 991808
    output_limit: 131072
rate_limits: "Global regions (Frankfurt / US / Tokyo / Hong Kong): 30,000 RPM, 5,000,000 TPM for qwen3.8-max and qwen3.8-flash; Beijing and Singapore limits are dynamic, tiered by monthly spend"
regions:
  - china-beijing
  - singapore
  - hong-kong
  - japan-tokyo
  - us-virginia
  - germany-frankfurt
cloud_providers:
  - Alibaba Cloud
pricing_ref: alibaba-cloud
documentation: https://www.alibabacloud.com/help/en/model-studio/
last_verified: "2026-09-20"
sources:
  - source_name: Model Studio — OpenAI-compatible API
    source_url: https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Model Studio — qwen3.8-max model detail
    source_url: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Model Studio — qwen3.8-flash model detail
    source_url: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Alibaba Cloud Model Studio (Bailian) serves the Qwen family through OpenAI-compatible Chat Completions
and Responses APIs (qwen3.8-flash also supports the Anthropic protocol). Regional base URLs follow the
pattern `https://{WorkspaceId}.{region}.maas.aliyuncs.com/compatible-mode/v1` for Singapore, Beijing,
Hong Kong and Tokyo; the US endpoint is `https://dashscope-us.aliyuncs.com/compatible-mode/v1`.

Authentication uses a region-bound API key. Streaming is supported (stream_options include_usage for
token counts). Thinking is toggled with `enable_thinking`; structured outputs, function calling, web
search, prefix completion, context caching and (Beijing-only) batch inference are available on
supported models. A managed API product also exists at qwencloud.com.
