---
agent_id: minimax-code
agent_name: MiniMax Code
company: minimax
description: "MiniMax's desktop AI agent app (macOS/Windows) plus the open-source 'mcode' CLI terminal coding agent, built on MiniMax M-series models. Coding and Work modes, multi-agent collaboration, remote control from phone."
agent_type: coding
underlying_models:
  - minimax-m3
  - minimax-m2.7
  - minimax-m2.7-highspeed
framework: "TypeScript CLI (mcode) with TUI / headless exec / ACP server entry points; desktop app with Agent Team multi-agent workflows"
tool_calling: true
browser_use: false
computer_use: false
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "Token Plan subscription: Plus $22 / Max $55 / Ultra $132 per month; credits 1,000 = $1. Covers M3/M2.7/image/speech; excludes H3 and some speech specials. Pay-as-you-go API pricing exists separately."
deployment: both
open_source: true
license: "MIT (mcode CLI); desktop app proprietary"
github: https://github.com/MiniMax-AI/minimax-code
documentation: https://agent.minimax.io/docs/code/welcome.md
use_cases:
  - Repository and CI coding tasks
  - Everyday office workflows and scheduled automation
  - Remote collaboration via phone or messaging (Telegram, WeChat, Lark, Feishu)
  - Multimodal creation (documents, PPT, images, audio, video via H3 Max)
  - Deep research and website building
  - Multi-agent decomposition with Agent Team and Custom Agents
limitations:
  - Browser use and computer use are desktop-host capabilities; not automatically available in the CLI
  - Desktop app is macOS/Windows only (no Linux)
  - CLI default model is not pinned in docs; web app defaulted to M2.7 in rendered UI (M3 available)
  - Headless mode cannot use the "ask" permission mode
  - Installer does not support Alpine/musl; no uninstall flag
  - GitHub repo has no release tags; external PRs only from collaborators
  - First release date not publicly disclosed; repo created 2026-06-01
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax Code docs — welcome
    source_url: https://agent.minimax.io/docs/code/welcome.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Code CLI docs — features
    source_url: https://agent.minimax.io/docs/cli/features.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax-AI/minimax-code GitHub repository
    source_url: https://github.com/MiniMax-AI/minimax-code
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Token Plan pricing guide
    source_url: https://platform.minimax.io/docs/guides/pricing-token-plan
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
