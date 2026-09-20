---
agent_id: kimi-code
agent_name: Kimi Code
company: moonshot-ai
description: "Moonshot AI's terminal AI coding agent ('The Starting Point for Next-Gen Agents'), successor to the deprecated kimi-cli. CLI (TypeScript, MIT), VS Code extension and Desktop app; reads/edits code, runs shell commands, searches files, fetches web pages, plans and adjusts actions autonomously. Includes subagents, MCP, Kimi Computer Use, browser control (WebBridge/Browser Extension) and multimodal input (text, images, video). Billed under Kimi membership."
agent_type: coding
underlying_models:
  - kimi-k3
  - kimi-k2.7-code
  - kimi-k2.7-code-highspeed
tool_calling: true
browser_use: true
computer_use: true
mcp: true
framework: "TypeScript terminal agent (pi-tui); succeeds the deprecated Python kimi-cli"
planning: true
multi_agent: true
api: true
pricing: "Included with Kimi membership, Plus and above (Adagio free tier has no coding quota; Plus $15/mo, Pro $31/mo, Max $79/mo, Ultra $159/mo). All clients share one quota with rolling 5-hour window and monthly total. Open Platform API pay-as-you-go: kimi-k3 $3.00/M input / $15.00/M output; kimi-k2.7-code $0.95/$4.00; kimi-k2.7-code-highspeed $1.90/$8.00."
deployment: both
open_source: true
license: MIT
github: https://github.com/MoonshotAI/kimi-code
documentation: https://moonshotai.github.io/kimi-code/en/
use_cases:
  - Understanding unfamiliar codebases and implementing features
  - Bug fixing, writing tests, refactoring
  - Batch file processing
  - Long-horizon whole-repo work via 1M-token context (K3)
  - Video-input tasks (screen recording to code)
  - Scheduled and background tasks
  - IDE-driven sessions via VS Code extension or ACP (Zed, JetBrains)
limitations:
  - Runs on the local machine with approval gates; no dedicated OS-level sandbox engine
  - kimi-cli predecessor deprecated and being wound down (auto-migrated on install)
  - Computer Use (macOS) needs Accessibility + Screen Recording permissions; Windows version may briefly take over mouse/keyboard
  - Third-party tools must keep the real client identifier (User-Agent tampering restricted)
  - Cloud inference only (managed endpoints api.kimi.com/coding/v1 and api.kimi.ai/coding/v1); not self-hostable as a model service
  - Windows install requires Git for Windows
  - API keys shown only once (max 5); quota shared across devices; devices inactive >30 days unbound
last_verified: "2026-09-20"
sources:
  - source_name: Kimi Code GitHub repository
    source_url: https://github.com/MoonshotAI/kimi-code
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi Code CLI documentation
    source_url: https://moonshotai.github.io/kimi-code/en/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi Code product docs
    source_url: https://www.kimi.com/code/docs/en/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi membership pricing
    source_url: https://www.kimi.ai/membership/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
