---
agent_id: deepseek-harness
agent_name: DeepSeek Harness
company: deepseek
description: "DeepSeek's open-source agent harness (CLI 'dsh') - 'Everything is a Plugin'. A developer-preview framework/runtime for composing coding agents from pluggable models, tools, skills, sessions and UIs."
agent_type: framework
underlying_models:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
framework: "Built on Cordis; everything (models, tools, skills, sessions, sandbox, UI) is composed from plugins"
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: false
planning: true
multi_agent: true
api: true
pricing: "Harness software is free and open source. Model usage billed by DeepSeek API pay-as-you-go: flash $0.15-0.30/M input, $0.60-1.20/M output; v4-pro $0.66-1.32 input, $1.98-3.96 output (off-peak = half peak)."
deployment: self_hosted
open_source: true
license: MIT
github: https://github.com/deepseek-ai/deepseek-harness
documentation: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
use_cases:
  - Interactive coding-agent chat via Web UI
  - Headless one-shot tasks (dsh --profile headless)
  - Embedding agents in Python programs via SDK
  - Programmatic multi-session automation over ACP
  - GitHub PR review via webhook overlay
  - Custom profiles, plugins and agent presets
limitations:
  - "Developer preview: breaking changes expected, not security-audited, no production-readiness guarantee"
  - Sandboxing and approvals reduce but do not guarantee isolation; untrusted work should run in disposable environments
  - Web server binds to loopback only; no cloud-hosted version documented
  - OAuth sign-in providers (e.g. Codex) not yet supported; API-key providers only
  - No VS Code extension or editor integration documented; ACP is automation-only
  - No built-in memory; third-party memory MCP servers are interoperability examples only
  - sdk-minimal profile pins danger-full-access permissions by default
last_verified: "2026-09-20"
sources:
  - source_name: deepseek-ai/deepseek-harness GitHub repository
    source_url: https://github.com/deepseek-ai/deepseek-harness
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Harness official guide (quickstart)
    source_url: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API pricing page
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
