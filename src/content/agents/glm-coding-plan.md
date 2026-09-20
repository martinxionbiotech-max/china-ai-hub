---
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
