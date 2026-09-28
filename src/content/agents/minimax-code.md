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
framework: "TypeScript terminal coding agent (open-source, verified via GitHub repo description 2026-09-27)"
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
**What it is.** MiniMax Code is MiniMax's desktop AI agent app and CLI (mcode) for software development, everyday workflows, automation and remote collaboration, on macOS and Windows. **Why it matters.** It is MiniMax's open-source (MIT) coding front-end for its [MiniMax-M3](/models/minimax-m3/) / [M2.7](/models/minimax-m27/) models — the developer-facing counterpart to the closed [MiniMax Agent](/agents/minimax-agent/). **Key characteristics.** Coding and Work modes, built-in browser, Agent Team, memory, MCP servers, scheduled tasks, remote control from phone and messaging apps; CLI with interactive TUI, headless mode and ACP server. **What a professional should know.** Browser/Computer Use are desktop-only (not in the CLI), the desktop app is macOS/Windows-only (no Linux), and billing runs on Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132 per month).

MiniMax Code is MiniMax's desktop AI agent app and CLI (mcode) for software development, everyday workflows, automation and remote collaboration, available on macOS and Windows. The code is open source under the MIT license.

Billing runs through MiniMax Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132 per month) with 5-hour rolling and weekly quota windows; enterprise API pay-as-you-go is also available.

See the [MiniMax](/companies/minimax/) profile.

## Why it matters

MiniMax Code is the open, developer-side of MiniMax's agent strategy, and its capability is directly downstream of the M-series models: M3's MSA sparse attention and 1M-token context are what the CLI consumes for repository-scale work. Its relationship to the underlying models is the clearest in the MiniMax family — the CLI defaults to M2.7 in the rendered UI while M3 is available, a pairing that shows how MiniMax tiers its open models against its agent surface. China AI Hub analysis indicates MiniMax Code matters as MiniMax's commitment to the open coding-agent ecosystem (MIT code, MCP, ACP), which anchors the company's developer credibility even as its flagship M3 remains under a conditional Community License.

*Labels used above: **Official fact** (from the MiniMax Code GitHub repo and docs), **Vendor-reported claim** (capability and pricing statements by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such).*
