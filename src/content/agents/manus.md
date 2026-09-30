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
last_verified: "2026-09-30"
sources:
  - source_name: Manus official site
    source_url: https://manus.im/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Manus pricing
    source_url: https://manus.im/pricing
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Manus API documentation
    source_url: https://open.manus.ai/docs
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Manus (AI agent) — Wikipedia
    source_url: https://en.wikipedia.org/wiki/Manus_(AI_agent)
    source_type: industry_media
    last_verified: "2026-09-30"
    confidence: medium
---
**Short answer.** Manus is a general-purpose autonomous AI agent by Butterfly Effect (the company behind Monica.im) — an "action engine" that executes whole tasks end-to-end, automates workflows and operates a browser, sold directly to consumers and teams as a cloud subscription.

**Key facts.**

- Autonomous multi-step task execution with a browser operator and tool use — the flagship tasks are creating slides, building websites and simple games, video and design.
- Manus 2.0 (2026) reframed the product around "less structure, more intelligence," adding Wide Research, Mail Manus and Slack integration.
- Distributed via web, desktop and mobile clients, with a Team plan (SSO), a Startup program and a developer API at open.manus.ai.
- Cloud-only, proprietary, subscription-billed.
- Builds no foundation models of its own — it orchestrates third-party models; the official site does not name them (third-party sources describe Claude and Qwen routing).
- Butterfly Effect was founded in China and is based in Singapore, also known for the Monica assistant.

**What this means.** Manus is the clearest test of whether a general autonomous agent can be a standalone product — detached from any single model vendor, competing on doing whole tasks rather than on a model, benchmark or framework.

**What is uncertain.** The underlying model orchestration (which third-party models it routes to), exact subscription tiers (client-side rendered), the company's funding, and independent evaluation of its task-completion quality are not documented.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-manus-1 | Manus official site | https://manus.im/ | Official | — | 2026-09-30 | high | — |
| src-agents-manus-2 | Manus pricing | https://manus.im/pricing | Official | — | 2026-09-30 | high | — |
| src-agents-manus-3 | Manus API documentation | https://open.manus.ai/docs | Official documentation | — | 2026-09-30 | high | — |
| src-agents-manus-4 | Manus (AI agent) — Wikipedia | https://en.wikipedia.org/wiki/Manus_(AI_agent) | Literature | — | 2026-09-30 | medium | — |

## Why it matters

Manus matters because it is the agent itself, sold directly to end users. Every other agent in this database is either bound to a lab's models ([Kimi Code](/agents/kimi-code/), [GLM Coding Plan](/agents/glm-coding-plan/)) or is a platform/framework for building agents ([Dify](/agents/dify/), [MetaGPT](/agents/metagpt/)); Manus is the product.

China AI Hub analysis indicates Manus's structural role is demand creation: it demonstrated, at viral scale, that consumers and knowledge workers will pay for a general "do it for me" agent, which raised the bar for every other agent product to ship autonomous, end-to-end task completion rather than chat-plus-tools. That is a product-velocity bet, not a model bet.

China AI Hub analysis: Manus is the clearest case of the agent-decoupled-from-model bet — it rises or falls on execution quality and product design, not on a model it owns. The trade-off is that its capabilities are bounded by whatever third-party models it can route to, a supply-chain dependency the official site leaves unstated. Its dependence on undisclosed models is simultaneously its flexibility and its risk.

## How it differs from the vertical coding agents

Manus is a general agent, not a coding agent, and the contrast sharpens its position.

- **[Kimi Code](/agents/kimi-code/)** and **[Qwen Code](/agents/qwen-code/)** are coding agents bound (or, for Qwen Code, closely aligned) to their vendors' models, optimized for whole-repo software work.
- **[Trae](/agents/trae/)** is ByteDance's AI-native IDE, splitting a coding agent (TraeCode) from a work assistant (TraeWork).
- **Manus** is general: it builds slides, websites, games and video, runs research and automates email/Slack — not a code editor, but an "action engine" that happens to code when a task needs it.

China AI Hub analysis: the difference is scope-versus-depth. The vertical coding agents trade breadth for depth in software work and inherit a vendor's model ceiling; Manus trades depth-in-coding for breadth-across-tasks and inherits a *portfolio* of undisclosed third-party models instead of one vendor's. A buyer choosing Manus is choosing a general executor; a buyer choosing a coding agent is choosing a specialist bound to a known model.

## Practical implications

**For consumers and knowledge workers.** Manus is the "do it for me" surface — slides, websites, research, email/Slack automation — sold as a subscription. The cost is cloud-only lock-in and an undisclosed model supply chain.

**For teams.** The Team plan (SSO) and Startup program are the managed adoption path; the developer API at open.manus.ai extends the agent to programmatic use, though its boundary with the consumer product is not fully specified publicly.

**For evaluators.** Manus cannot be assessed against a model benchmark because it builds no model — it must be evaluated on end-to-end task completion, and no independent evaluation of that is recorded in this database.

## What the evidence shows

The evidence is strong on Manus's product surface and weak on its internals. The official site is explicit about the flagship tasks (slides, websites, games, video, design, browser operator, Wide Research, Mail Manus, Slack) and the Manus 2.0 "less structure, more intelligence" reframing, which grounds the "general executor" reading in primary material. The company's China-founded, Singapore-based identity and its Monica.im connection are documented in the Wikipedia entry.

The internals are the gap. The underlying model orchestration is not named on the official site — third-party sources describe Claude and Qwen routing, which the database records at medium confidence and does not treat as official fact. Subscription pricing is client-side rendered and was not extracted. China AI Hub analysis indicates this opacity is structural to the agent-decoupled-from-model bet: a product whose value is execution, not a model, has every incentive to document its *tasks* and little incentive to document its *model supply chain*, which it may not fully control.

## Where this fits

| Workload | Relevance |
|---|---|
| Autonomous end-to-end task execution | High |
| Slides, website, game and video creation | High |
| Browser automation via Manus browser operator | High |
| Deep research (Wide Research) | High |
| Email / Slack workflow automation | High |
| Whole-repo software development | Moderate (codes when a task needs it, not a coding IDE) |
| Self-hosted / on-premises deployment | None (cloud-only, proprietary) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

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
| Last verified | 2026-09-30 | Official |

See the [Butterfly Effect](/companies/butterfly-effect/) company profile, the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/) and [computer use](/technology/computer-use/) technology pages. For the structural reading of Manus as the general agent against the vertical coding agents, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) and [the rise of Chinese AI agents](/research/rise-of-chinese-ai-agents/).

*Labels used above: **Official fact** (from the Manus site, pricing and API docs), **Vendor-reported claim** (capability statements by Butterfly Effect), **Third-party** (the Wikipedia entry on the company's provenance and third-party model-routing descriptions), and **China AI Hub analysis** (our synthesis, always introduced as such). No independent evaluation of Manus's task-completion quality is currently recorded.*
