---
image: "/images/ai/agents-minimax-code.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: minimax-code
agent_name: MiniMax Code
company: minimax
description: "MiniMax's desktop AI agent app and CLI (mcode) for software development, everyday workflows, automation and remote collaboration. Desktop (macOS/Windows) features Coding and Work modes, built-in browser, Agent Team, memory, MCP servers, scheduled tasks, Remote Control from phone and messaging integrations. CLI is a terminal coding agent with interactive TUI, headless mode and ACP server; open source (MIT)."
agent_type: coding
underlying_models:
  - minimax-m3
  - minimax-m2.7
  - minimax-m2.7-highspeed
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "Billed via MiniMax Token Plan subscriptions: Plus $22/mo, Max $55/mo, Ultra $132/mo (5-hour rolling + weekly quota windows); credits 1,000 = $1 for overflow. API pay-as-you-go also available for enterprises."
deployment: both
open_source: true
license: MIT
github: https://github.com/MiniMax-AI/minimax-code
documentation: https://agent.minimax.io/docs/code/welcome.md
use_cases:
  - Repository/CI coding tasks via interactive TUI or headless mode
  - Everyday office workflows and scheduled automation
  - Remote collaboration from phone or messaging apps (Telegram, WeChat, Lark, Feishu)
  - Multimodal creation (documents, PPT, images, audio, video via H3 Max)
  - Custom agents, mini apps and plugin marketplace
limitations:
  - Browser/Computer Use are desktop-host capabilities; not available in the CLI
  - Desktop app is macOS/Windows only (no Linux)
  - Installer does not support Alpine/musl; no uninstall flag
  - Headless mode cannot use the ask permission mode
  - CLI default model is not pinned in docs; web app defaulted to M2.7 in rendered UI (M3 available)
  - GitHub repo has no release tags; first release date not publicly disclosed (repo created 2026-06-01)
  - Desktop app is proprietary (repo only hosts issue tracking); external PRs accepted only from collaborators
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax Code GitHub repository
    source_url: https://github.com/MiniMax-AI/minimax-code
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Code docs - welcome
    source_url: https://agent.minimax.io/docs/code/welcome.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Code CLI docs - features
    source_url: https://agent.minimax.io/docs/cli/features.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Token Plan pricing guide
    source_url: https://platform.minimax.io/docs/guides/pricing-token-plan
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
MiniMax Code is MiniMax's desktop AI agent app and CLI (mcode) for software development, everyday workflows, automation and remote collaboration, available on macOS and Windows. The code is open source under the MIT license.

Billing runs through MiniMax Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132 per month) with 5-hour rolling and weekly quota windows; enterprise API pay-as-you-go is also available.

See the [MiniMax](/companies/minimax/) profile.
