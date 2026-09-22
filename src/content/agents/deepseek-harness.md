---
image: "/images/ai/agents-deepseek-harness.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: deepseek-harness
agent_name: DeepSeek Harness
company: deepseek
description: "Open-source agent harness from DeepSeek ('Everything is a Plugin') that powers its coding agent. All capabilities - models, tools, skills, sessions, sandbox, storage, loops, scheduling and UI - are composed from replaceable plugins. Developer preview; ships as CLI (dsh), Web UI, Electron Desktop app, Python SDK and ACP server."
agent_type: framework
underlying_models:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
framework: Cordis
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: false
planning: true
multi_agent: true
api: true
pricing: "Software itself free and open source. Model usage billed by the configured provider (DeepSeek API pay-as-you-go: flash $0.15-$0.30/M input cache-miss, $0.60-$1.20/M output, off-peak = half of peak; v4-pro $0.66-$1.32/M input, $1.98-$3.96/M output)."
deployment: self_hosted
open_source: true
license: MIT
github: https://github.com/deepseek-ai/deepseek-harness
documentation: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
use_cases:
  - Interactive coding-agent chat via Web UI
  - Headless one-shot tasks via dsh --profile headless with a task prompt
  - Embedding agents in Python programs (Python SDK)
  - Programmatic multi-session automation over ACP (Agent Client Protocol)
  - GitHub PR review via webhook overlay
  - Custom profiles/plugins/presets for different agent compositions
limitations:
  - Developer preview - compatibility-breaking changes expected; not security-audited, not production-ready (SAFETY.md)
  - Sandboxing/approvals do not guarantee isolation - run untrusted work in a disposable VM or container
  - Web server binds loopback only; trusted-host list required for LAN access
  - No VS Code/editor extension found in repo; ACP is automation-only
  - Image input only via deepseek-flash; deepseek-v4-pro is text-only
  - OAuth providers (e.g. Codex) not yet supported; API-key providers only
  - No built-in memory; third-party memory MCP servers are interoperability examples only
  - sdk-minimal profile pins danger-full-access permissions by default
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek Harness GitHub repository
    source_url: https://github.com/deepseek-ai/deepseek-harness
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Harness product page
    source_url: https://deepseek.com/harness
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Harness documentation
    source_url: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
DeepSeek Harness is DeepSeek's open-source agent harness ("Everything is a Plugin") that powers its coding agent. Models, tools, skills, sessions, sandbox, storage, loops, scheduling and the UI are all composed from replaceable plugins on the Cordis framework. It is a developer preview that ships as a CLI (dsh), Web UI, Electron Desktop app, Python SDK and ACP server.

The software is free and self-hosted; model usage is billed by the provider you configure. DeepSeek API pay-as-you-go ranges from $0.15–$0.30/M input (cache-miss) for flash up to $1.98–$3.96/M output for V4-Pro, with off-peak at half price.

See the [DeepSeek](/companies/deepseek/) profile and the [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) model page.
