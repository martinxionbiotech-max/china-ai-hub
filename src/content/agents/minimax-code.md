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
**Short answer.** MiniMax Code is MiniMax's desktop AI agent app and CLI (mcode) for software development, everyday workflows, automation and remote collaboration, on macOS and Windows. It is the open-source (MIT) developer surface for [MiniMax-M3](/models/minimax-m3/) / [M2.7](/models/minimax-m27/) models — the counterpart to the closed [MiniMax Agent](/agents/minimax-agent/).

**Key facts.**

- Two form factors: a desktop app (macOS/Windows) with Coding and Work modes, built-in browser, Agent Team, memory, MCP servers, scheduled tasks and remote control from phone; and an open-source CLI (mcode) with interactive TUI, headless mode and an ACP server.
- The CLI is open source (MIT); the desktop app is proprietary (the repo hosts issue tracking only).
- Runs on [MiniMax-M3](/models/minimax-m3/), [M2.7](/models/minimax-m27/) and [M2.7-HighSpeed](/models/minimax-m27-highspeed/); M3's MSA sparse attention and 1M-token context are what the CLI consumes for repository-scale work.
- Billed via MiniMax Token Plan (Plus $22 / Max $55 / Ultra $132 per month) with 5-hour rolling and weekly quotas; enterprise API pay-as-you-go also available.
- Remote collaboration from phone or messaging apps (Telegram, WeChat, Lark, Feishu); multimodal creation via H3 Max.

**What this means.** MiniMax Code anchors MiniMax's developer credibility in the open coding-agent ecosystem (MIT CLI, MCP, ACP) while its flagship M3 stays under a conditional Community License — the open *tool* is the bridge to a semi-open *model*.

**What is uncertain.** The CLI's default model is not pinned in docs (the web app defaulted to M2.7 in rendered UI, with M3 available), there are no release tags and no disclosed first release date (repo created 2026-06-01). Browser/Computer Use are desktop-only and absent from the CLI.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-minimax-code-1 | MiniMax Code GitHub repository | https://github.com/MiniMax-AI/minimax-code | Official documentation | — | 2026-09-20 | high | — |
| src-agents-minimax-code-2 | MiniMax Code docs - welcome | https://agent.minimax.io/docs/code/welcome.md | Official documentation | — | 2026-09-20 | high | — |
| src-agents-minimax-code-3 | MiniMax Code CLI docs - features | https://agent.minimax.io/docs/cli/features.md | Official documentation | — | 2026-09-20 | high | — |
| src-agents-minimax-code-4 | MiniMax Token Plan pricing guide | https://platform.minimax.io/docs/guides/pricing-token-plan | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

MiniMax Code is the open, developer-side of MiniMax's agent strategy, and its capability is directly downstream of the M-series models: M3's MSA sparse attention and 1M-token context are what the CLI consumes for repository-scale work. The GitHub repo's tagline — "Turn a prompt into something that works… with MiniMax or your own model" — makes the openness explicit: the CLI works with MiniMax's models or a self-configured provider.

China AI Hub analysis indicates MiniMax Code matters as MiniMax's commitment to the open coding-agent ecosystem (MIT code, MCP, ACP), which anchors the company's developer credibility even as its flagship M3 remains under a conditional Community License. The asymmetry — open tool, semi-open model — is the point: the free MIT CLI funnels usage toward M3/M2.7, and the enterprise pay-as-you-go path is where MiniMax recovers value from heavy users.

## How it differs from MiniMax Agent

The two MiniMax surfaces are complementary, not competing, and the split is the strategy.

- **[MiniMax Agent](/agents/minimax-agent/)** is the closed cloud platform — a web app of capability areas (Skills, Schedules, Websites, Research, AI PPT) plus always-on assistants MaxClaw/MaxHermes, for non-developers, billed by Token Plan subscription.
- **MiniMax Code** is the open developer surface — a desktop app and MIT CLI for coding, workflows, automation and remote collaboration, with MCP, memory, Agent Team and an ACP server.

China AI Hub analysis: MiniMax Code is where the company earns developer trust (open code, inspectable, MCP/ACP), and MiniMax Agent is where it captures non-developer spend (closed, subscription, memory, always-on). One model family, two monetization surfaces — the open CLI lowers the bar for developer adoption while the closed platform carries the subscription revenue. A developer picks MiniMax Code; a daily user picks MiniMax Agent; MiniMax wins either way because both consume the same M-series tokens.

## Practical implications

**For developers.** The CLI (mcode) is the open path: interactive TUI for repository/CI work, headless mode for automation, and an ACP server for programmatic use. But Browser/Computer Use are desktop-host only — the CLI does not get them — so GUI automation requires the proprietary desktop app.

**For cross-platform teams.** The desktop app is macOS/Windows only (no Linux), and the installer does not support Alpine/musl; the CLI is the Linux path. Headless mode cannot use the "ask" permission mode, a real constraint for semi-autonomous batch work that needs human approval.

**For cost-sensitive users.** Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132) carry the consumer path; enterprises get API pay-as-you-go. The CLI's default model is not pinned in docs, so teams should explicitly select M3 rather than assume it is the default.

## What the evidence shows

The evidence is strong on the surface and the model lineup, and honest about its own boundaries. The GitHub repo and docs document the desktop/CLI split, Coding and Work modes, built-in browser, Agent Team, memory, MCP, scheduled tasks, remote control, and the H3 Max multimodal creation; the Token Plan guide fixes the pricing. The repo is transparent that the desktop app is proprietary (repo hosts issue tracking only) and that external PRs are accepted only from collaborators.

The gaps are release history and defaults. There are no release tags, no disclosed first release date (repo created 2026-06-01), and the CLI default model is not pinned (the web app rendered M2.7 as default with M3 available). China AI Hub analysis indicates these are not defects but a maturity marker: a young, fast-moving open project that has not yet stabilized versioning or made its default model explicit — buyers should treat the "default model" question as something to configure, not assume.

## Where this fits

| Workload | Relevance |
|---|---|
| Repository/CI coding (TUI or headless) | High |
| Everyday office workflows and scheduled automation | High |
| Remote collaboration (phone, Telegram/WeChat/Lark/Feishu) | High |
| Multimodal creation (H3 Max) | High |
| Browser / Computer Use in the CLI | Low (desktop-host only) |
| Linux desktop app | Low (macOS/Windows only; CLI covers Linux) |
| Independent coding benchmark | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [MiniMax-M3](/models/minimax-m3/), [MiniMax-M2.7](/models/minimax-m27/), [MiniMax-M2.7-Highspeed](/models/minimax-m27-highspeed/) | Official |
| Target users | Developers (desktop app and CLI) | Official |
| Platform | Desktop app (macOS/Windows), CLI (mcode) | Official |
| OS | macOS, Windows (desktop); CLI cross-platform | Official |
| Browser / computer use | Built-in browser and Computer Use (desktop-host) | Vendor-reported |
| Coding | Yes (coding agent) | Official |
| Autonomous task execution | Yes (planning, multi-agent Agent Team) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | Yes | Official |
| Workflow | Coding and Work modes; scheduled tasks; remote control from phone | Official |
| API | Yes (enterprise pay-as-you-go) | Official |
| Pricing | Token Plan: Plus $22 / Max $55 / Ultra $132 per month | Vendor-reported |
| Region | Not publicly documented | Not publicly documented |
| Open-source | Yes — MIT (desktop app proprietary) | Official |
| Deployment | Cloud and self-hosted | Official |
| Limitations | Browser/Computer Use desktop-only; no Linux desktop; no Alpine/musl | Official |
| Source | [MiniMax Code GitHub](https://github.com/MiniMax-AI/minimax-code) | Official |
| Last verified | 2026-09-20 | Official |

See the [MiniMax](/companies/minimax/) company profile, the [MiniMax-M3](/models/minimax-m3/) model, the [MiniMax-M3 vs M2.7 comparison](/comparisons/minimax-m3-vs-minimax-m2.7/), the closed [MiniMax Agent](/agents/minimax-agent/) counterpart, the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), and the site's [AI agents](/technology/ai-agents/) technology page.

*Labels used above: **Official fact** (from the MiniMax Code GitHub repo and docs), **Vendor-reported claim** (capability and pricing statements by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such).*
