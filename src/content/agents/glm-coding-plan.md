---
image: "/images/ai/agents-glm-coding-plan.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: glm-coding-plan
agent_name: GLM Coding Plan
company: zhipu-ai
description: "Zhipu AI's coding-agent subscription (bigmodel.cn/glm-coding): one plan that powers ZCode (Zhipu's own coding client), AutoClaw (office agent) and 20+ third-party coding tools including Claude Code, Codex, Cursor and OpenClaw. Runs on GLM-5.3 / GLM-5.3-Flash with 1M-token context; credits refresh per 5-hour window and weekly. International counterpart on Z.AI from $18/month."
agent_type: coding
underlying_models:
  - glm-5.3
  - glm-5.3-flash
tool_calling: true
mcp: true
memory: true
planning: true
api: true
pricing: "China (bigmodel.cn): Lite ¥118/mo, Pro ¥538/mo, Max ¥1078/mo (quarterly 8-fold off, annual 7-fold off); credits per 5h 2,000/12,000/28,000 and weekly 10,000/60,000/140,000. Team seats: Standard ¥598/mo, Advanced ¥1198/mo. International (Z.AI): from $18/month. Off-peak = 50% credit rate; peak Mon-Fri 14:00-18:00 UTC+8 = 2x."
deployment: cloud
open_source: false
license: proprietary
documentation: https://docs.bigmodel.cn/cn/coding-plan/overview.md
use_cases:
  - Full development chain from requirements to deployable product in one task (1M context)
  - Code generation, debugging/repair and codebase Q&A
  - Agentic Engineering workflow (plan-implement-iterate)
  - ZCode coding client (150% quota, free idle-time tasks, data MCP)
  - AutoClaw office agent - deep research, business data analysis, task automation
  - Night campaign 23-00 to 09-00 - GLM-5.3-Flash unlimited via ZCode
limitations:
  - Quota caps (5-hour + weekly) with refresh waiting; no spillover billing to other balances
  - Valid only inside officially supported coding tools; self-built apps/SaaS must use the standard API
  - Peak hours (Mon-Fri 14:00-18:00) cost 2x credits
  - OpenClaw tasks run at secondary priority under load (preemption by coding-agent tasks)
  - Team plan - no mixed standard+advanced purchase; 1 seat per member; max 5 API keys per seat
  - Launch date not publicly disclosed in fetched sources (plan revision dated 2026-07-30)
known_limitations:
  - "No public GitHub repository located as of 2026-09-27 (checked THUDM org)"
last_verified: "2026-09-20"
sources:
  - source_name: GLM Coding Plan landing page
    source_url: https://bigmodel.cn/glm-coding
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: BigModel Coding Plan docs - overview
    source_url: https://docs.bigmodel.cn/cn/coding-plan/overview.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.AI Coding Plan international docs
    source_url: https://docs.z.ai/devpack/overview.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**Short answer.** GLM Coding Plan is Zhipu AI's coding-agent subscription: one plan that powers ZCode (Zhipu's own client), AutoClaw (office agent) and 20+ third-party coding tools including Claude Code, Codex, Cursor and OpenClaw, running on [GLM-5.3](/models/glm-53/) / [GLM-5.3-Flash](/models/glm-53-flash/) with 1M-token context.

**Key facts.**

- The same subscription unlocks GLM models across Zhipu's own tools (ZCode, AutoClaw) *and* third-party coding agents — the plan's defining characteristic.
- China tiers: Lite ¥118 / Pro ¥538 / Max ¥1,078 per month, with per-5-hour credits (2,000/12,000/28,000) and weekly credits (10,000/60,000/140,000); team seats at ¥598/¥1,198 per month. International Z.AI from $18/month.
- Time-based pricing: off-peak is 50% credit rate; peak (Mon–Fri 14:00–18:00 UTC+8) costs 2x credits.
- Runs on GLM-5.3 and GLM-5.3-Flash, both 1M-token context, with an Agentic Engineering plan-implement-iterate workflow.
- Valid only inside officially supported coding tools; self-built apps and SaaS must use the standard API.

**What this means.** GLM Coding Plan inverts the usual agent-vs-model relationship: instead of shipping its own coding agent as the primary surface, Zhipu makes its models available *inside* the tools developers already use, turning Claude Code, Codex, Cursor and OpenClaw into distribution channels for GLM-5.3 spend.

**What is uncertain.** The plan's launch date is not publicly disclosed (the plan revision is dated 2026-07-30), and there is no public GitHub repository (verified against THUDM on 2026-09-27). Whether the 20+ third-party integrations stay current as those tools evolve is an ongoing maintenance question, not a static guarantee.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-glm-coding-plan-1 | GLM Coding Plan landing page | https://bigmodel.cn/glm-coding | Official | — | 2026-09-20 | high | — |
| src-agents-glm-coding-plan-2 | BigModel Coding Plan docs - overview | https://docs.bigmodel.cn/cn/coding-plan/overview.md | Official documentation | — | 2026-09-20 | high | — |
| src-agents-glm-coding-plan-3 | Z.AI Coding Plan international docs | https://docs.z.ai/devpack/overview.md | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

GLM Coding Plan is the clearest example of a Chinese model vendor monetizing its models through *third-party* coding tools rather than competing with them. The plan's value is inseparable from GLM-5.3's capability — the 1M-token context and reasoning are what those external tools actually consume — while the pricing structure (5-hour and weekly credit windows, peak 2x, off-peak half) is a consumption-control layer on top of the model.

China AI Hub analysis indicates the plan is Zhipu's distribution strategy: it monetizes GLM models by embedding them in the coding-agent ecosystem rather than by winning the client war, and the pricing's peak/off-peak split is an explicit capacity-management lever — the 2x peak multiplier steers usage off business hours, mirroring the off-peak economics DeepSeek introduced on its API. This is a demand-shaping mechanism, not a neutral price list.

## How it differs from Kimi Code and Qwen Code

The three coding agents occupy distinct positions on the open-versus-closed and own-tool-versus-ecosystem axes.

- **[Kimi Code](/agents/kimi-code/)** is Moonshot's open-source (MIT) terminal agent — a first-party client bound to Kimi K3/K2.7-Code, monetized through Kimi membership and a pay-as-you-go API. The tool is free; the models are Moonshot's own.
- **[Qwen Code](/agents/qwen-code/)** is Alibaba's open-source (Apache-2.0) multi-protocol agent — the CLI is free, and it routes to *any* provider (OpenAI, Anthropic, Gemini, Qwen, DeepSeek, Kimi, MiniMax, local). Alibaba monetizes through its Coding Plan and Token Plan, but the agent itself stays model-agnostic.
- **GLM Coding Plan** is not a client at all — it is a *subscription that injects GLM models into other clients*. Zhipu ships ZCode as a first-party option but makes the plan's core value proposition "your existing tool, GLM's model."

China AI Hub analysis: the three represent three different answers to "how does a Chinese model vendor capture coding-agent demand." Moonshot binds a free open client to its own models; Alibaba gives away an open multi-protocol client and charges for access; Zhipu skips the client war and charges for model access inside everyone else's client. A developer already on Claude Code or Cursor faces the lowest switching cost with GLM Coding Plan — that is precisely its bet.

## Practical implications

**For developers.** The plan's headline value is running GLM-5.3's 1M context and reasoning inside a tool you already know. The cost is a quota system with two refresh cadences (5-hour and weekly) and no spillover billing — exhaust a window and you wait, rather than automatically paying overage.

**For cost-sensitive teams.** Off-peak usage halves credit cost, and the ZCode client's night campaign (23:00–09:00) makes GLM-5.3-Flash effectively unlimited — a concrete incentive to schedule batch or background work off-hours. Peak hours (14:00–18:00) doubling is the counterweight.

**For self-builders.** The plan is deliberately walled to officially supported tools; anyone building a custom app or SaaS must fall back to the standard per-token API, so the subscription does not substitute for API access.

## What the evidence shows

The evidence is strong on the pricing and routing mechanics but thin on the model's independent quality. The landing page and docs document the tier structure (¥118/¥538/¥1,078), the credit windows, the peak/off-peak multipliers, the ZCode/AutoClaw/third-party coverage, and the "valid only in supported tools" constraint; the Z.AI docs mirror the international plan from $18/month.

The gaps are launch date (not disclosed; revision dated 2026-07-30) and independent coding benchmarks for GLM-5.3 (the site records vendor-reported scores but no independent evaluation for this plan specifically). China AI Hub analysis indicates the plan's substance is its *business model* — a model-vendor-as-backend to third-party agents — more than any single capability claim, and its real risk is integration maintenance: a subscription whose value rides on staying compatible with two dozen external tools inherits those tools' release churn as an operational cost.

## Where this fits

| Workload | Relevance |
|---|---|
| Using GLM models inside existing tools (Claude Code, Codex, Cursor, OpenClaw) | High |
| Agentic Engineering (plan-implement-iterate, 1M context) | High |
| ZCode first-party client / AutoClaw office agent | High |
| Off-peak / scheduled batch work (night campaign) | High |
| Self-built apps / SaaS on the standard API | Low (plan not valid there) |
| Independent benchmark evaluation of GLM-5.3 coding | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [GLM-5.3](/models/glm-53/), [GLM-5.3-Flash](/models/glm-53-flash/) | Official |
| Target users | Developers using coding tools | Official |
| Platform | Coding-agent subscription (ZCode, AutoClaw, 20+ third-party tools) | Official |
| OS | Not publicly documented (via supported coding tools) | Not publicly documented |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Yes (coding-agent subscription) | Official |
| Autonomous task execution | Yes (Agentic Engineering plan-implement-iterate) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | Yes | Official |
| Workflow | Plan-implement-iterate; credits refresh per 5-hour window and weekly | Official |
| API | Yes | Official |
| Pricing | China ¥118/¥538/¥1,078 per month; international from $18/month | Vendor-reported |
| Region | China (bigmodel.cn) and international (Z.AI) | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Quota caps; valid only in supported tools; peak 2x credits | Official |
| Source | [BigModel Coding Plan](https://bigmodel.cn/glm-coding) | Official |
| Last verified | 2026-09-20 | Official |

See the [Zhipu AI](/companies/zhipu-ai/) company profile, the [GLM-5.3](/models/glm-53/) and [GLM-5.3-Flash](/models/glm-53-flash/) models, the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), and the site's [AI agents](/technology/ai-agents/) and [tool calling](/technology/tool-calling/) technology pages.

*Labels used above: **Official fact** (from the BigModel Coding Plan and Z.AI docs), **Vendor-reported claim** (pricing and capability statements by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
