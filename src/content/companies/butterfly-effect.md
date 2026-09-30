---
company_id: butterfly-effect
company_name: Butterfly Effect (Manus)
description: "Butterfly Effect is the company behind Manus, the general-purpose autonomous AI agent; founded in China and based in Singapore, it is also known for the Monica (Monica.im) assistant. It builds no foundation models of its own and orchestrates third-party models."
aliases:
  - Monica.im
  - Monica
  - Manus AI
headquarters: "Singapore"
funding: "Not publicly documented as of 2026-09-29."
ai_products:
  - Manus (autonomous AI agent)
  - Monica (AI assistant)
foundation_models: []
agents:
  - manus
api: []
open_source_projects: []
official_documentation: https://manus.im/docs
official_website: https://manus.im/
related_entities: []
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
**What it is.** Butterfly Effect is the Singapore-based company (founded in China) behind [Manus](/agents/manus/), the general-purpose autonomous AI agent, and the Monica (Monica.im) assistant. **Why it matters.** It is the clearest example in this database of an "agent as product" company: it builds no foundation model of its own and instead orchestrates third-party models to deliver a general autonomous agent. **Key characteristics.** Manus executes tasks, automates workflows and operates a browser; Manus 2.0 (2026) adds slides, website, game and video creation; a Team plan with SSO and an API at open.manus.ai. **What a professional should know.** The exact underlying models are not documented on the official site, the company is cloud-only, and its funding is not publicly documented.

Butterfly Effect is a Singapore-headquartered company, founded in China, best known for Manus, the autonomous AI agent that went viral in 2025. Per third-party descriptions, it builds no foundation models of its own and orchestrates third-party models such as Claude and Qwen; the company is also known for the Monica assistant (Monica.im). Its product, [Manus](/agents/manus/), is distributed via web, desktop and mobile clients, with a Team plan (SSO) and a developer API at open.manus.ai.

## Why it matters

China AI Hub analysis indicates Butterfly Effect matters because it decoupled "agent" from "model vendor." Every other agent in this database is either bound to a lab's models ([Kimi Code](/agents/kimi-code/), [GLM Coding Plan](/agents/glm-coding-plan/)) or is a platform/framework for building agents ([Dify](/agents/dify/), [MetaGPT](/agents/metagpt/)); Manus is the agent itself, sold directly to end users.

China AI Hub analysis indicates the company's structural role is demand creation: it demonstrated, at viral scale, that consumers and knowledge workers will pay for a general "do it for me" agent, which raised the bar for every other agent product to ship autonomous, end-to-end task completion rather than chat-plus-tools. That is a product-velocity bet, not a model bet.

China AI Hub analysis indicates the model-decoupled bet is simultaneously the company's flexibility and its risk. Manus rises or falls on execution quality and product design, not on a model it owns, but its capabilities are bounded by whatever third-party models it can route to — a supply-chain dependency the official site leaves unstated. The opacity is structural: a product whose value is execution has every incentive to document its *tasks* and little incentive to document its *model supply chain*, which it may not fully control.

## How it differs from the model labs and the agent builders

Butterfly Effect sits outside both camps that dominate the rest of the database.

- **The model labs** ([DeepSeek](/companies/deepseek/), [Moonshot AI](/companies/moonshot-ai/), [ByteDance](/companies/bytedance/), [Zhipu AI](/companies/zhipu-ai/), [Alibaba Cloud](/companies/alibaba-cloud/), [MiniMax](/companies/minimax/)) all own the model their agents run on — Manus's maker owns none.
- **The open agent builders** ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/), [MetaGPT](/agents/metagpt/)) sell the *means* to build agents — Butterfly Effect sells the finished agent itself.
- **The bound platforms** ([Coze](/agents/coze/), [Yuanqi](/agents/yuanqi/), [Baidu AppBuilder](/agents/baidu-appbuilder/)) are distribution channels for a vendor's own model — Manus is model-agnostic by necessity, not by choice.

China AI Hub analysis: the difference is scope-versus-depth in one direction and ownership in the other. The vertical coding agents trade breadth for depth and inherit a vendor's model ceiling; Manus trades depth-in-coding for breadth-across-tasks and inherits a portfolio of undisclosed third-party models instead of one vendor's. A buyer choosing Manus is choosing a general executor with no model allegiances — the purest expression of the agent-as-product thesis in this database.

## Practical implications and limitations

**For consumers and knowledge workers.** Manus is the "do it for me" surface — slides, websites, research, email/Slack automation — sold as a subscription. The cost is cloud-only lock-in and an undisclosed model supply chain.

**For teams.** The Team plan (SSO) and Startup program are the managed adoption path; the developer API at open.manus.ai extends the agent to programmatic use, though its boundary with the consumer product is not fully specified publicly.

**For evaluators.** Manus cannot be assessed against a model benchmark because it builds no model — it must be evaluated on end-to-end task completion, and no independent evaluation of that is recorded in this database. The company's funding and the exact underlying model routing are the two structural unknowns a buyer must accept.

## Entity hub

### Products

- [Manus](/agents/manus/)

### Agents

- [Manus](/agents/manus/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [Computer Use](/technology/computer-use/)
- [Agent ecosystem structure and gaps](/research/china-ai-agent-ecosystem-structure-and-gaps/)

## What is uncertain

- The underlying model routing is not documented on the official site.
- Funding is not publicly documented.
- Headquarters (Singapore) and "founded in China" come from third-party sources rather than the company site.
- No independent evaluation of task-completion quality is recorded.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-butterfly-effect-1 | Manus official site | https://manus.im/ | Official | — | 2026-09-29 | high | — |
| src-companies-butterfly-effect-2 | Manus pricing | https://manus.im/pricing | Official | — | 2026-09-29 | high | — |
| src-companies-butterfly-effect-3 | Manus API documentation | https://open.manus.ai/docs | Official documentation | — | 2026-09-29 | high | — |
| src-companies-butterfly-effect-4 | Manus (AI agent) — Wikipedia | https://en.wikipedia.org/wiki/Manus_(AI_agent) | Third-party | — | 2026-09-29 | medium | — |

*Labels used above: **Official fact** (from the Manus site, pricing and API docs), **Vendor-reported claim** (product statements by Butterfly Effect), **Third-party** (the Wikipedia entry on company provenance and third-party model-routing descriptions), and **China AI Hub analysis** (our synthesis, always introduced as such). No independent evaluation of Manus's task-completion quality is currently recorded.*
