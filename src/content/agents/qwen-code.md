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
**Short answer.** Qwen Code is the Qwen team's open-source AI coding agent (Apache-2.0) for terminal, editor, desktop, browser and chat, built as a multi-protocol, multi-platform TypeScript framework. It is Alibaba's flagship open coding agent and the most model-agnostic surface in its portfolio — supporting OpenAI, Anthropic, Gemini and Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models.

**Key facts.**

- Ships as a CLI (npm), Desktop app, VS Code "Qwen Code Companion" (Beta), Web UI and IM channels (Telegram/DingTalk/WeChat/Feishu); originally based on Google Gemini CLI v0.8.2, independent since v0.1.
- Five permission modes, Seatbelt/Docker sandboxing, auto-memory (with QWEN.md as the guaranteed instruction file), subagents, MCP, computer use and Agent Arena for head-to-head model comparison.
- The CLI is free (Apache-2.0); the user pays the model provider directly, and BYO keys work for any supported provider.
- Alibaba billing: international Coding Plan Pro $50/month; China Token Plan (Beijing only) Personal ¥39–¥499/month, team seats ¥150–¥1,398; or pay-as-you-go Model Studio API keys.
- Multi-protocol framework: OpenAI, Anthropic, Gemini and Qwen APIs, plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models (Ollama/vLLM).

**What this means.** Qwen Code's value is *optionality*, not a single model — it is the open client that explicitly supports competitors' models, making it the opposite of Qwen-Agent's Qwen-native design and complementary to Qoder's closed multi-model routing.

**What is uncertain.** The Web UI and daemon (`qwen serve`) are experimental, the Qwen OAuth free tier was discontinued 2026-04-15, and Auto Mode's classifier is biased toward blocking (failing closed on outage). Independent benchmark evidence of Qwen Code's coding quality is not recorded in this database.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-qwen-code-1 | Qwen Code GitHub repository | https://github.com/QwenLM/qwen-code | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-2 | Qwen Code docs - overview | https://qwenlm.github.io/qwen-code-docs/en/users/overview/ | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-3 | Alibaba Cloud Model Studio Coding Plan | https://www.alibabacloud.com/help/en/model-studio/coding-plan | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-4 | Alibaba Cloud Token Plan overview | https://help.aliyun.com/en/model-studio/token-plan-overview | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

Qwen Code is the most model-agnostic agent in Alibaba's portfolio, and the database's clearest example of a vendor shipping open tooling that works against its own model lock-in. Its multi-protocol TypeScript framework explicitly supports competitors' models — DeepSeek, Kimi, Z.AI, MiniMax, OpenAI, Anthropic, Gemini — alongside Qwen, with the CLI free and the user paying whatever provider they route to.

China AI Hub analysis indicates Qwen Code matters as Alibaba's bet that open tooling wins developer mindshare even when those developers ultimately route to other vendors' models — a bet that mirrors how the Qwen model family itself is open-weight. The agent's value is the framework (sandboxing, five permission modes, MCP, computer use, Agent Arena), not any single model, which is why it can afford to be genuinely model-optional: Alibaba monetizes the *access* (Coding Plan, Token Plan, Model Studio keys) rather than the *client*.

## How it differs from Kimi Code and GLM Coding Plan

The three coding agents split on openness and model posture.

- **[Kimi Code](/agents/kimi-code/)** is Moonshot's first-party open client *bound to its own models* (Kimi K3/K2.7-Code), monetized through Kimi membership — the tightest integration between tool and model, around K3's 1M-token output.
- **[GLM Coding Plan](/agents/glm-coding-plan/)** is not a client — it is a subscription that injects GLM models into third-party tools (Claude Code, Codex, Cursor, OpenClaw), monetizing model access inside everyone else's client.
- **Qwen Code** is an open multi-protocol client that routes to *any* provider — model-optional by design, free as a tool, with Alibaba monetizing access through its Coding/Token plans.

China AI Hub analysis: the three are the same question — "how does a Chinese vendor capture coding-agent demand?" — answered three ways. Moonshot binds a free open client to its own models; Zhipu skips the client and sells model access inside other tools; Alibaba gives away the most flexible client and charges for access. Qwen Code is the most open on both axes (open source *and* model-agnostic), which is precisely why it competes on framework quality rather than model exclusivity.

## Practical implications

**For developers.** Qwen Code is the "bring your own model" open client — free CLI, five permission modes, Seatbelt/Docker sandboxing, MCP, computer use, subagents and Agent Arena for head-to-head model comparison. It runs on npm, desktop, VS Code, Web UI and chat channels, and is pipe-friendly for CI (`qwen -p`).

**For self-hosters.** The framework is Apache-2.0 and the sandboxing is real — Seatbelt/Docker — but the default Docker image is intentionally minimal (Java not included), and sandboxing reduces rather than eliminates risk; GUI apps may not run in sandboxes.

**For cost-conscious users.** The CLI is free and BYO keys work for any provider, so the marginal cost is whatever model you point it at. Alibaba's own plans (Coding Plan $50/month international; Token Plan ¥39–¥499/month China, Beijing only) are optional, not required.

## What the evidence shows

The evidence is strong on the framework and honest about the experimental edges. The GitHub repo and docs document the multi-surface distribution (CLI, desktop, VS Code, Web UI, IM channels), the multi-protocol model support, the five permission modes, Seatbelt/Docker sandboxing, auto-memory/QWEN.md, MCP, computer use and Agent Arena; the Model Studio and Token Plan pages fix Alibaba's own billing options.

The caveats are explicit rather than hidden: the Web UI and daemon are experimental, the Qwen OAuth free tier ended 2026-04-15, Auto Mode's classifier is biased toward blocking and fails closed on outage, and sandboxing reduces but does not eliminate risk. China AI Hub analysis indicates this is a mature open project that discloses its own rough edges — the "experimental" and "fails closed" annotations are themselves evidence of production realism, not immaturity, and buyers should read the Auto Mode bias as a deliberate safety posture rather than a defect.

## Where this fits

| Workload | Relevance |
|---|---|
| Multi-protocol coding (any provider, local or API) | High |
| Sandboxed execution (Seatbelt/Docker, 5 permission modes) | High |
| CI automation and pipe-friendly workflows (qwen -p) | High |
| Remote agent via chat channels (Telegram/DingTalk/WeChat/Feishu) | High |
| Multi-model comparison (Agent Arena) | High |
| Production Web UI / daemon (qwen serve) | Low (experimental) |
| Independent coding benchmark | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Not pinned (multi-protocol: OpenAI, Anthropic, Gemini, Qwen, DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter, local) | Official |
| Target users | Developers (terminal, editor, desktop, browser, chat) | Official |
| Platform | CLI (npm), Desktop app, VS Code companion, Web UI, IM channels | Official |
| OS | Cross-platform (CLI/Desktop); Docker sandbox | Official |
| Browser / computer use | Browser and Computer Use | Vendor-reported |
| Coding | Yes (coding agent) | Official |
| Autonomous task execution | Yes (planning, multi-agent subagents) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | Yes (auto-memory, QWEN.md) | Official |
| Workflow | 5 permission modes; Seatbelt/Docker sandboxing; multi-protocol model routing | Official |
| API | Yes (user pays model provider) | Official |
| Pricing | CLI free; Alibaba Cloud Coding Plan Pro $50/month or Token Plan ¥39–¥499/month | Vendor-reported |
| Region | Not publicly documented | Not publicly documented |
| Open-source | Yes — Apache-2.0 | Official |
| Deployment | Self-hosted | Official |
| Limitations | Web UI/daemon experimental; sandboxing reduces but not eliminates risk | Official |
| Source | [Qwen Code GitHub](https://github.com/QwenLM/qwen-code) | Official |
| Last verified | 2026-09-20 | Official |

See the [Alibaba Cloud](/companies/alibaba-cloud/) company profile, the [Qwen-Agent](/agents/qwen-agent/) framework, the [Qoder](/agents/qoder/) platform, the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), the [Model Studio](/api/model-studio/) platform, and the site's [AI agents](/technology/ai-agents/) and [MCP](/technology/mcp/) technology pages.

*Labels used above: **Official fact** (from the Qwen Code GitHub repo and docs), **Vendor-reported claim** (pricing and capability statements by Alibaba Cloud), and **China AI Hub analysis** (our synthesis, always introduced as such). No independent benchmark of Qwen Code's coding quality is currently recorded.*
