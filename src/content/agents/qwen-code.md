---
image: "/images/ai/agents-qwen-code.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: qwen-code
agent_name: Qwen Code
company: alibaba-cloud
description: "Alibaba Qwen team's open-source AI coding agent (Apache-2.0) for terminal, editor, desktop, browser and chat. Originally based on Google Gemini CLI v0.8.2, independent development since v0.1 as a multi-protocol, multi-platform agent framework. Ships as CLI (npm), Desktop app, VS Code 'Qwen Code Companion' (Beta), Web UI and IM channels (Telegram/DingTalk/WeChat/Feishu). Includes 5 permission modes, Seatbelt/Docker sandboxing, auto-memory, subagents, MCP, computer use and multi-protocol model support."
agent_type: coding
underlying_models: []
framework: "Multi-protocol agent framework (TypeScript); supports OpenAI, Anthropic, Gemini, Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models (Ollama/vLLM)"
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "CLI free (Apache-2.0); user pays the model provider. Alibaba Cloud Coding Plan (intl) Pro $50/month; Token Plan (CN, Beijing only) Personal Lite ¥39 / Essential ¥79 / Standard ¥139 / Pro ¥499 per month, team seats ¥150-¥1398; or pay-as-you-go Model Studio API keys; BYO keys to other providers."
deployment: self_hosted
open_source: true
license: Apache-2.0
github: https://github.com/QwenLM/qwen-code
documentation: https://qwenlm.github.io/qwen-code-docs/en/users/overview/
use_cases:
  - Building features from natural-language descriptions
  - Debugging and fixing issues in existing codebases
  - CI automation and pipe-friendly Unix workflows (qwen -p)
  - Remote agent via chat channels (Telegram, DingTalk, WeChat, Feishu)
  - Multi-model head-to-head comparisons via Agent Arena
limitations:
  - Web UI and daemon (qwen serve) marked experimental
  - Qwen OAuth free tier discontinued 2026-04-15
  - Sandboxing reduces but does not eliminate all risks; GUI apps may not work in sandboxes
  - Default Docker sandbox image is intentionally minimal (Java not included by default)
  - Auto Mode classifier biased toward blocking and fails closed on classifier outage
  - Auto-memory is best-effort; QWEN.md is the guaranteed instruction file
last_verified: "2026-09-20"
sources:
  - source_name: Qwen Code GitHub repository
    source_url: https://github.com/QwenLM/qwen-code
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen Code docs - overview
    source_url: https://qwenlm.github.io/qwen-code-docs/en/users/overview/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Alibaba Cloud Model Studio Coding Plan
    source_url: https://www.alibabacloud.com/help/en/model-studio/coding-plan
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Alibaba Cloud Token Plan overview
    source_url: https://help.aliyun.com/en/model-studio/token-plan-overview
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
Qwen Code is the Qwen team's open-source AI coding agent (Apache-2.0) for terminal, editor, desktop, browser and chat. Its multi-protocol TypeScript framework supports OpenAI, Anthropic, Gemini and Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models (Ollama/vLLM).

The CLI is free and the user pays the model provider. Alibaba Cloud billing options include the international Coding Plan (Pro $50/month), the China Token Plan (Personal ¥39–¥499/month, team seats ¥150–¥1,398) or pay-as-you-go Model Studio API keys.

See the [Alibaba Cloud](/companies/alibaba-cloud/) profile.
