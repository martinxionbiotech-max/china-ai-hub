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
**What it is.** GLM Coding Plan is Zhipu AI's coding-agent subscription: one plan that powers ZCode (Zhipu's own client), AutoClaw (office agent) and 20+ third-party tools including Claude Code, Codex, Cursor and OpenClaw. **Why it matters.** It is the clearest example of a Chinese model vendor monetizing its models through *third-party* coding tools — routing external agents onto [GLM-5.3](/models/glm-53/) / [GLM-5.3-Flash](/models/glm-53-flash/) rather than competing with them. **Key characteristics.** Runs on GLM-5.3 / GLM-5.3-Flash with 1M-token context; credits refresh in 5-hour windows and weekly; peak hours cost 2x credits. **What a professional should know.** It is valid only inside officially supported coding tools (self-built apps use the standard API), and China billing (¥118–¥1,078/month) is separate from the international Z.AI plan (from $18/month).

GLM Coding Plan is Zhipu AI's coding-agent subscription: one plan that powers ZCode (Zhipu's own coding client), AutoClaw (office agent) and more than 20 third-party coding tools including Claude Code, Codex, Cursor and OpenClaw. It runs on GLM-5.3 / GLM-5.3-Flash with 1M-token context; credits refresh in 5-hour windows and weekly.

China billing on bigmodel.cn has Lite / Pro / Max tiers at ¥118 / ¥538 / ¥1,078 per month with team seats available; the international Z.AI counterpart starts at $18/month. Off-peak usage costs half the credits, and peak hours (Mon–Fri 14:00–18:00 UTC+8) cost double.

See the [Zhipu AI](/companies/zhipu-ai/) profile and the [GLM-5.3](/models/glm-53/) model page.

## Why it matters

GLM Coding Plan inverts the usual agent-vs-model relationship: instead of shipping its own coding agent as the primary surface (as DeepSeek Harness or Kimi Code do), Zhipu makes its models available *inside* the tools developers already use. That makes the plan's value inseparable from GLM-5.3's capability — the 1M-token context and reasoning are what those third-party tools actually consume — while the pricing structure (5-hour and weekly credit windows, peak 2x) is a consumption-control layer on top of the model. China AI Hub analysis indicates the plan is Zhipu's distribution strategy: it monetizes GLM models by embedding them in the coding-agent ecosystem rather than by winning the client war.

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

*Labels used above: **Official fact** (from the BigModel Coding Plan and Z.AI docs), **Vendor-reported claim** (pricing and capability statements by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
