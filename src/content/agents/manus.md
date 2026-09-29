---
agent_id: manus
agent_name: Manus
company: butterfly-effect
description: "Manus is a general-purpose autonomous AI agent developed by Butterfly Effect, a company founded in China and based in Singapore (also known for Monica.im). Positioned as 'the action engine that goes beyond answers,' it executes tasks, automates workflows, and operates a browser; Manus 2.0 (2026) adds slides, website, game and video creation, a browser operator, Wide Research, Mail Manus and Slack integration, with an API at open.manus.ai."
agent_type: autonomous
underlying_models: []
framework: "Autonomous task-execution agent with a browser operator and multi-step tool use; web app, desktop and mobile clients; Team plan with SSO; developer API at open.manus.ai."
tool_calling: true
computer_use: true
memory: true
planning: true
api: true
pricing: "Subscription-based with tiered plans (pricing at manus.im/pricing); a Team plan and Startup program are offered; API access is via open.manus.ai."
deployment: cloud
open_source: false
license: proprietary
documentation: https://manus.im/docs
use_cases:
  - Autonomous task execution across documents and websites
  - Building slides, websites and simple games
  - Browser-based automation via the Manus browser operator
  - Deep research via Wide Research
  - Email and Slack workflow automation
limitations:
  - Underlying model orchestration is not documented on the official site (third-party sources describe Claude and Qwen routing)
  - Subscription pricing tiers are rendered client-side and were not extracted from the pricing page
  - Cloud-only; no self-hosted or open-source edition
  - Builds no foundation models of its own — it is dependent on third-party model availability
last_verified: "2026-09-29"
sources:
  - source_name: Manus official site
    source_url: https://manus.im/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Manus pricing
    source_url: https://manus.im/pricing
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Manus API documentation
    source_url: https://open.manus.ai/docs
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Manus (AI agent) — Wikipedia
    source_url: https://en.wikipedia.org/wiki/Manus_(AI_agent)
    source_type: industry_media
    last_verified: "2026-09-29"
    confidence: medium
---
**What it is.** Manus is a general-purpose autonomous AI agent built by Butterfly Effect, a Singapore-based company founded in China — an "action engine" that goes beyond generating answers to executing tasks, automating workflows and operating a browser. **Why it matters.** It is the most prominent China-origin example of the "agent as product" thesis: a general agent that competes on doing whole tasks end-to-end rather than on a model, benchmark or developer framework. **Key characteristics.** Multi-step autonomous execution with a browser operator; Manus 2.0 (2026) adds slides, website, game and video creation, Wide Research, Mail Manus and Slack; a Team plan with SSO and an API at open.manus.ai. **What a professional should know.** Butterfly Effect builds no foundation model of its own — it orchestrates third-party models — and the exact underlying model routing is not documented on the official site; it is cloud-only and subscription-billed.

Manus describes itself as "the action engine that goes beyond answers to execute tasks, automate workflows, and extend your human reach." Its surface is broad: the flagship tasks are creating slides, building websites and simple games, video and design, plus a Manus browser operator for computer use, Wide Research for deep research, Mail Manus for email, and Slack integration. Manus 2.0 was announced in 2026, reframing the product around "less structure, more intelligence" — fewer prompt templates, more autonomous task completion.

The company behind it, Butterfly Effect, was founded in China and is based in Singapore, and is also known for the Monica assistant (Monica.im). Per third-party descriptions, it builds no foundation models of its own and orchestrates third-party models such as Claude and Qwen; the official site does not name the underlying models. Distribution is via web app, desktop and mobile clients, with a Team plan (SSO) and a developer API at open.manus.ai.

See the [Butterfly Effect](/companies/butterfly-effect/) profile.

## Why it matters

Manus matters because it is the clearest test of whether a general autonomous agent can be a standalone product — detached from any single model vendor. Every other agent in this database is either bound to a lab's models ([Kimi Code](/agents/kimi-code/), [GLM Coding Plan](/agents/glm-coding-plan/)) or is a platform/framework for building agents ([Dify](/agents/dify/), [MetaGPT](/agents/metagpt/)); Manus is the agent itself, sold directly to end users. China AI Hub analysis indicates its structural role is demand creation: it demonstrated, at viral scale, that consumers and knowledge workers will pay for a general "do it for me" agent, which in turn raised the bar for every other agent product to ship autonomous, end-to-end task completion rather than chat-plus-tools. Its dependence on undisclosed third-party models is simultaneously its flexibility and its supply-chain risk. China AI Hub analysis: this makes Manus the clearest case of the agent-decoupled-from-model bet — it rises or falls on execution quality and product design, not on a model it owns. The trade-off is that its capabilities are bounded by whatever third-party models it can route to, a dependency the official site leaves unstated.

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Not publicly documented (orchestrates third-party models) | Not publicly documented |
| Target users | Consumers, knowledge workers, teams | Official |
| Platform | Web app, desktop app, mobile app | Official |
| OS | Cross-platform (web + desktop + mobile) | Official |
| Browser / computer use | Yes (Manus browser operator) | Vendor-reported |
| Coding | Yes (builds websites and games) | Vendor-reported |
| Autonomous task execution | Yes (core capability) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes (browser operator, tools) | Official |
| Memory | Yes (task context and workspace) | Vendor-reported |
| Workflow | Autonomous multi-step task execution | Vendor-reported |
| API | Yes (open.manus.ai) | Official |
| Pricing | Subscription-based tiers (manus.im/pricing) | Vendor-reported |
| Region | Global | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Underlying models undisclosed; cloud-only; builds no own models | Official |
| Source | [manus.im](https://manus.im/) · [pricing](https://manus.im/pricing) · [API](https://open.manus.ai/docs) | Official |
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The underlying model orchestration (which third-party models Manus routes to) is not documented on the official site.
- Exact subscription pricing tiers are rendered client-side and were not extracted from the pricing page.
- The company's funding is not publicly documented.
- No independent third-party evaluation of Manus's task-completion quality is recorded in this database.
- The boundary between the consumer product and the developer API (open.manus.ai) is not fully specified on the public pages.

*Labels used above: **Official fact** (from the Manus site, pricing and API docs), **Vendor-reported claim** (capability statements by Butterfly Effect), and **China AI Hub analysis** (our synthesis, always introduced as such).*
