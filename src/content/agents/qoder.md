---
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
Qoder is Alibaba Cloud's commercial agentic coding platform: a desktop app (Qoder IDE), CLI (qodercli), JetBrains plugin and Cloud companion. Its Auto tier smart-routes tasks across selectable models — Ultimate, Performance and Efficient carry roughly 1.6x / 1.1x / 0.3x credit multipliers.

International pricing (qoder.com) runs Free $0 (with a one-time 2-week Pro trial), Pro $20/month, Pro+ $60/month and Ultra $200/month, plus Credit Packs; China billing (qoder.cn) goes through Alibaba Cloud plans.

See the [Alibaba Cloud](/companies/alibaba-cloud/) profile.
