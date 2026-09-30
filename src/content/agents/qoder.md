---
image: "/images/ai/agents-qoder.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: qoder
agent_name: Qoder
company: alibaba-cloud
description: "Commercial agentic coding platform ('Qoder - The Agentic Platform') with desktop app (Qoder IDE / Qoder), CLI (qodercli), JetBrains plugin, Cloud Agents API, and work agents (QoderWork, QoderWake). Agentic loop of understand-plan-execute-verify-iterate with plan- or goal-driven workflows, Expert team multi-agent mode, built-in browser, Memory and Knowledge Base, scheduled automations and enterprise governance. Closed-source; presented under the Alibaba Cloud Model Studio ecosystem."
agent_type: platform
underlying_models:
  - qwen3.8-max
  - qwen3.8-flash
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
framework: "Commercial desktop/CLI platform; Auto tier smart-routes tasks across selectable models (Ultimate ~1.6x / Performance ~1.1x / Efficient ~0.3x credit multipliers)"
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "International (qoder.com): Free $0 (one-time 2-week Pro trial, 300 Credits); Pro $20/mo (4,000 Credits); Pro+ $60/mo (6,000); Ultra $200/mo (20,000); Credit Pack $20/1,500 (1-month validity). Enterprise via contact sales. China version (qoder.cn) billing via Alibaba Cloud plans - CN pricing not publicly disclosed."
deployment: both
open_source: false
license: proprietary
documentation: https://docs.qoder.com/qoder/overview.md
use_cases:
  - End-to-end delegated coding tasks (Quest mode)
  - IDE coding with autocomplete, chat and multi-agent Expert teams
  - Scheduled automations and headless CLI for CI/CD
  - Document, research, browser and desktop task delegation (QoderWork)
  - Enterprise AI coding governance and cloud agents via API
limitations:
  - CLI/IDE source is not open source; only SDKs, changelogs and skills are public
  - Free plan has limited completions; Pro trial once per account and not available on VMs
  - Unused monthly credits expire; no refunds after 24h or after credits are used
  - Tool execution limited to 500 rounds per task (IDE v1.28.0)
  - Exact launch date not publicly disclosed (IDE release notes start 2025-08-21)
  - Operating entity listed as BRIGHT ZENITH PRIVATE LIMITED; corporate ownership relationship to Alibaba not publicly disclosed
known_limitations:
  - "No public GitHub repository located as of 2026-09-27 (checked XGenerationLab and Qoder-AI orgs)"
last_verified: "2026-09-20"
sources:
  - source_name: Qoder official site
    source_url: https://qoder.com/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qoder docs - overview
    source_url: https://docs.qoder.com/qoder/overview.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qoder pricing
    source_url: https://qoder.com/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Alibaba Cloud Model Studio Qoder integration guide
    source_url: https://www.alibabacloud.com/help/en/model-studio/qoder-agent
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**Short answer.** Qoder is Alibaba Cloud's commercial agentic coding platform — desktop app (Qoder IDE), CLI (qodercli), JetBrains plugin, Cloud Agents API and work agents (QoderWork, QoderWake) — with plan- or goal-driven workflows and a multi-agent Expert team mode. It is Alibaba's closed, enterprise-governance coding surface, distinct from the open [Qwen Code](/agents/qwen-code/) and [Qwen-Agent](/agents/qwen-agent/).

**Key facts.**

- Its Auto tier smart-routes tasks across *multiple vendors'* models — [Qwen3.8-Max](/models/qwen38-max/), [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [GLM-5.3](/models/glm-53/), [Kimi K3](/models/kimi-k3/), [MiniMax-M3](/models/minimax-m3/) — with Ultimate/Performance/Efficient credit multipliers of ~1.6x/1.1x/0.3x.
- An agentic loop of understand-plan-execute-verify-iterate, with built-in browser, Memory and Knowledge Base, scheduled automations and enterprise governance.
- International pricing (qoder.com): Free $0 (one-time 2-week Pro trial, 300 Credits); Pro $20/mo (4,000 Credits); Pro+ $60/mo (6,000); Ultra $200/mo (20,000); Credit Packs $20/1,500. China (qoder.cn) via Alibaba Cloud plans, CN pricing undisclosed.
- Closed-source: only SDKs, changelogs and skills are public; no public GitHub repository (verified against XGenerationLab and Qoder-AI on 2026-09-27).
- Operating entity listed as BRIGHT ZENITH PRIVATE LIMITED; its corporate ownership relationship to Alibaba is not publicly disclosed.

**What this means.** Qoder's value is *routing and governance*, not any single model's capability — it deliberately spans competitors' models by credit tier, making it a managed multi-model orchestration layer rather than a model-bound agent.

**What is uncertain.** The exact launch date is not disclosed (IDE release notes start 2025-08-21), China pricing is not public, and the Alibaba ownership relationship is not publicly documented — the "Alibaba Cloud" association rests on the Model Studio integration guide, not a disclosed corporate link.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-qoder-1 | Qoder official site | https://qoder.com/ | Official | — | 2026-09-20 | high | — |
| src-agents-qoder-2 | Qoder docs - overview | https://docs.qoder.com/qoder/overview.md | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qoder-3 | Qoder pricing | https://qoder.com/pricing | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qoder-4 | Alibaba Cloud Model Studio Qoder integration guide | https://www.alibabacloud.com/help/en/model-studio/qoder-agent | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

Qoder is the multi-model aggregator in Alibaba's coding portfolio, and the database's clearest signal that the Chinese agent market has matured to an enterprise tier where the differentiator shifts from raw model access to managed orchestration. Its Auto tier routes work across Qwen, DeepSeek, GLM, Kimi and MiniMax models by credit multiplier — a *selection* layer, not a *binding* to any one model.

China AI Hub analysis indicates Qoder matters as evidence of the enterprise tier's logic: a closed platform that earns its margin from routing, governance, scheduled automation and team management — not from selling a model it built. The 1.6x/1.1x/0.3x credit multipliers are a pricing-encoded quality ladder across *rival* vendors' models, which is only coherent if Qoder's value proposition is "we pick the right model per task," a genuinely different bet from Qwen Code's "you pick."

## How it differs from Qwen Code and Qwen-Agent

Alibaba fields three coding/agent surfaces that split cleanly on openness and model posture.

- **[Qwen Code](/agents/qwen-code/)** is the open Apache-2.0 multi-protocol coding agent — a free CLI/desktop/browser surface where the user brings any model (Qwen, DeepSeek, Kimi, MiniMax, OpenAI, Anthropic, Gemini, local). Model-agnostic *and* open-source.
- **[Qwen-Agent](/agents/qwen-agent/)** is the open Apache-2.0 Python framework — the low-level, Qwen-native plumbing (Assistant/FnCallAgent/ReActChat, @register_tool) that Qwen Code and Qwen Chat build on.
- **Qoder** is the closed commercial platform — the governance layer with Auto-tier routing, Expert teams, Memory/Knowledge Base, scheduled automations and enterprise controls, presented under the Model Studio ecosystem.

China AI Hub analysis: the three are a ladder — Qwen-Agent is the framework, Qwen Code is the open client, Qoder is the managed product — and the openness declines as the governance rises. Qwen-Agent and Qwen Code are inspectable and free; Qoder is closed and billed, trading transparency for routing and controls. A self-hosting developer uses the open pair; an enterprise buying governance and multi-model routing buys Qoder.

## Practical implications

**For enterprises.** Qoder is the governance path — Expert team multi-agent mode, Memory and Knowledge Base, scheduled automations, cloud agents via API, and a 500-tool-round-per-task ceiling (IDE v1.28.0) that bounds runaway tasks. The cost is vendor opacity: the CLI/IDE source is closed, only SDKs/changelogs/skills are public, and the Alibaba ownership relationship is not disclosed.

**For cost management.** The credit system is strict — unused monthly credits expire, no refunds after 24h or after credits are used, and the free tier has limited completions with a one-time Pro trial unavailable on VMs. Teams must plan credit consumption deliberately.

**For evaluators.** The Alibaba association should be verified directly: the operating entity is BRIGHT ZENITH PRIVATE LIMITED, and the "Alibaba Cloud" link rests on a Model Studio integration guide rather than a disclosed corporate relationship.

## What the evidence shows

The evidence is strong on the product and pricing, and honest about the corporate opacity. The docs document the agentic loop, Auto-tier routing, Expert teams, Memory/Knowledge Base, scheduled automations and the multi-surface distribution (IDE, CLI, JetBrains, Cloud API, work agents); the pricing page fixes the international tiers ($20/$60/$200 plus Credit Packs); the Model Studio guide establishes the Alibaba Cloud ecosystem presentation.

The gaps are corporate and historical. The exact launch date is not disclosed (release notes start 2025-08-21), China pricing is not public, and the Alibaba ownership relationship is not documented — the operating entity is BRIGHT ZENITH PRIVATE LIMITED. China AI Hub analysis indicates this opacity is a known feature of the enterprise-closed tier: Qoder's value is governance and routing, which it can sell without disclosing its corporate structure — but a buyer whose procurement requires knowing the vendor's ownership should confirm the Alibaba relationship directly rather than infer it from the ecosystem positioning.

## Where this fits

| Workload | Relevance |
|---|---|
| End-to-end delegated coding (Quest mode) | High |
| Multi-model routing by credit tier (Auto) | High |
| Enterprise governance and Expert teams | High |
| Scheduled automations and CI/CD (headless CLI) | High |
| Cloud agents via API | High |
| Self-hosted / open-source inspection | Low (closed-source) |
| Independent verification of Alibaba ownership | Not publicly documented |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [Qwen3.8-Max](/models/qwen38-max/), [Qwen3.8-Flash](/models/qwen38-flash/), [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/), [GLM-5.3](/models/glm-53/), [GLM-5.3-Flash](/models/glm-53-flash/), [Kimi K3](/models/kimi-k3/), [MiniMax-M3](/models/minimax-m3/) | Official |
| Target users | Developers and enterprises (commercial platform) | Official |
| Platform | Desktop app (Qoder IDE), CLI (qodercli), JetBrains plugin, Cloud Agents API | Official |
| OS | Not publicly documented | Not publicly documented |
| Browser / computer use | Built-in browser and Computer Use | Vendor-reported |
| Coding | Yes (agentic coding platform) | Official |
| Autonomous task execution | Yes (plan/goal-driven, Expert team multi-agent) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | Yes (Memory and Knowledge Base) | Official |
| Workflow | Understand-plan-execute-verify-iterate; Auto tier smart-routes models | Official |
| API | Yes (Cloud Agents API) | Official |
| Pricing | International $20/$60/$200 per month; China via Alibaba Cloud | Vendor-reported |
| Region | International (qoder.com) and China (qoder.cn) | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud and self-hosted | Official |
| Limitations | Closed-source; 500 tool rounds/task; operating entity not Alibaba-disclosed | Official |
| Source | [Qoder docs](https://docs.qoder.com/qoder/overview.md) | Official |
| Last verified | 2026-09-20 | Official |

See the [Alibaba Cloud](/companies/alibaba-cloud/) company profile, the open [Qwen Code](/agents/qwen-code/) and [Qwen-Agent](/agents/qwen-agent/) counterparts, the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), and the site's [AI agents](/technology/ai-agents/) and [tool calling](/technology/tool-calling/) technology pages.

*Labels used above: **Official fact** (from the Qoder site, docs and the Alibaba Cloud Model Studio integration guide), **Vendor-reported claim** (pricing and credit-multiplier statements by Qoder), and **China AI Hub analysis** (our synthesis, always introduced as such).*
