---
image: "/images/ai/agents-kimi-code.webp"
image_credit: "AI-generated illustration (Seedream)"
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
**Short answer.** Kimi Code is Moonshot AI's terminal AI coding agent — the successor to the deprecated kimi-cli — shipped as a TypeScript CLI (MIT), VS Code extension and Desktop app. It is the coding front-end for [Kimi K3](/models/kimi-k3/)'s 1M-token output ceiling, turning long-context generation into long-horizon whole-repo work.

**Key facts.**

- A first-party client bound to Moonshot's own models ([Kimi K3](/models/kimi-k3/), [K2.7-Code](/models/kimi-k27-code/), [K2.7-Code-HighSpeed](/models/kimi-k27-code-highspeed/)); the CLI works out of the box with Kimi models and can be configured for other compatible providers.
- Ships as CLI (TypeScript, MIT), VS Code extension and Desktop app; subagents, MCP, Kimi Computer Use, browser control and multimodal input (text, images, video) are built in.
- Billed under Kimi membership (Plus $15 / Pro $31 / Max $79 / Ultra $159 per month), all clients sharing one rolling 5-hour quota plus a monthly total.
- Open Platform API pay-as-you-go: kimi-k3 $3.00/M input / $15.00/M output; kimi-k2.7-code $0.95/$4.00; high-speed variant $1.90/$8.00.
- Cloud inference only — managed endpoints (api.kimi.com / api.kimi.ai coding/v1), not self-hostable as a model service.

**What this means.** Kimi Code is the agent layer that operationalizes Kimi K3's distinguishing capacity: the database's only 1M-token maximum *output* ceiling is exactly what a long-horizon coding agent needs to emit large multi-file edits and long reasoning traces in a single pass.

**What is uncertain.** There is no dedicated OS-level sandbox engine (approval gates only), and independent benchmark evidence of Kimi Code's coding quality versus Qwen Code or GLM Coding Plan is not recorded in this database. The membership quota's interaction with the API's per-token rates is documented but not summarized in a single official comparison.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-kimi-code-1 | Kimi Code GitHub repository | https://github.com/MoonshotAI/kimi-code | Official documentation | — | 2026-09-20 | high | — |
| src-agents-kimi-code-2 | Kimi Code CLI documentation | https://moonshotai.github.io/kimi-code/en/ | Official documentation | — | 2026-09-20 | high | — |
| src-agents-kimi-code-3 | Kimi Code product docs | https://www.kimi.com/code/docs/en/ | Official documentation | — | 2026-09-20 | high | — |
| src-agents-kimi-code-4 | Kimi membership pricing | https://www.kimi.ai/membership/pricing | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

Kimi Code is the agent manifestation of Kimi K3's distinguishing capability. Where most coding agents are bounded by context *length*, Kimi Code is positioned around output *length*: K3's 1M-token output ceiling is a structural fact of the model, and the agent is the surface that consumes it for whole-repo, multi-file, long-horizon work.

China AI Hub analysis indicates Kimi Code is best read as Moonshot's bet that the coding-agent market will reward output-length and long-horizon reliability over raw price — a bet that runs directly on K3's differentiated capacity. The membership-billing model (one quota across CLI, extension and desktop) reinforces this: Moonshot sells the *workflow*, not just the tokens, and prices the agent as a consumer-plus product rather than a pure per-token utility.

## How it differs from Qwen Code and GLM Coding Plan

The three coding agents split on ownership, openness and monetization.

- **[Qwen Code](/agents/qwen-code/)** is Alibaba's open Apache-2.0 multi-protocol agent — a free CLI that routes to *any* provider (Qwen, DeepSeek, Kimi, MiniMax, OpenAI, Anthropic, Gemini, local). Model-agnostic by design; Alibaba monetizes access, not the tool.
- **[GLM Coding Plan](/agents/glm-coding-plan/)** is not a client — it is a subscription that injects GLM models into third-party tools (Claude Code, Codex, Cursor, OpenClaw). The model travels to your tool; the client is someone else's.
- **Kimi Code** is a first-party open client *bound to its own models* — the tool is free (MIT), the models are Moonshot's, and the two are designed together around K3's long-output edge.

China AI Hub analysis: Kimi Code is the only one of the three that is simultaneously open-source *and* single-vendor, the mirror image of Qwen Code's open multi-vendor stance. A developer who wants one open client and is indifferent to the model picks Qwen Code; a developer already committed to Kimi's long-output models gets the tightest integration from Kimi Code. GLM Coding Plan is the option for those who won't leave their existing client at all.

## Practical implications

**For long-horizon work.** Kimi Code's headline fit is whole-repo tasks where a single pass must emit large multi-file edits — the 1M-token output is the reason to choose it over a shorter-output agent. The cost is that this strength is only as good as K3's reasoning quality, which the database records as vendor-reported, not independently benchmarked.

**For deployment.** The CLI runs on the local machine with approval gates but no dedicated OS-level sandbox engine, so untrusted work needs external isolation. Computer Use on macOS requires Accessibility + Screen Recording permissions, and the Windows variant may briefly take over mouse/keyboard — a real interaction cost for GUI automation.

**For billing.** Membership (Plus and above) shares one quota across all clients on a rolling 5-hour window plus a monthly cap; the Open Platform API is separate, pay-as-you-go. Teams weighing the two should note that membership is the consumer path and API keys (max 5, shown once) are the programmatic path.

## What the evidence shows

The evidence is strong on the surface and the model lineup, weaker on independent quality. The GitHub repo and docs document the CLI/extension/desktop form factors, the subagents/MCP/Computer Use/browser/multimodal feature set, the kimi-cli deprecation (auto-migration on install), and the managed-endpoint architecture; the pricing page fixes the membership tiers and the API per-token rates.

The gaps are independence and sandboxing. No OS-level sandbox engine is documented (approval gates only), and no independent benchmark of Kimi Code's coding quality is recorded here. China AI Hub analysis indicates the honesty boundary is "capability and pricing documented, quality vendor-reported": the 1M output is a documented model fact, but whether that output is *correct* for a given repo is exactly what independent evaluation — absent here — would establish.

## Where this fits

| Workload | Relevance |
|---|---|
| Long-horizon whole-repo work (1M-token output) | High |
| Terminal / IDE coding (CLI, VS Code, desktop) | High |
| Multimodal input (text, images, video) | High |
| Scheduled and background tasks | High |
| OS-level sandboxed execution | Low (approval gates, no sandbox engine) |
| Self-hosted model service | Low (cloud inference only) |
| Independent coding benchmark | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [Kimi K3](/models/kimi-k3/), [Kimi K2.7 Code](/models/kimi-k27-code/), [Kimi K2.7 Code Highspeed](/models/kimi-k27-code-highspeed/) | Official |
| Target users | Developers (terminal/IDE coding) | Official |
| Platform | CLI (TypeScript), VS Code extension, Desktop app | Official |
| OS | macOS, Windows, Linux (CLI) | Official |
| Browser / computer use | Browser control and Kimi Computer Use | Vendor-reported |
| Coding | Yes (terminal coding agent) | Official |
| Autonomous task execution | Yes (planning, multi-agent subagents) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | Not publicly documented | Not publicly documented |
| Workflow | Plan-implement-iterate; long-horizon whole-repo work via 1M-token context | Official |
| API | Yes (Open Platform API pay-as-you-go) | Official |
| Pricing | Kimi membership (Plus and above); API $3.00/$15.00 per 1M tokens (kimi-k3) | Vendor-reported |
| Region | Global (api.kimi.com / api.kimi.ai) | Official |
| Open-source | Yes — MIT | Official |
| Deployment | Cloud and self-hosted | Official |
| Limitations | No OS-level sandbox engine; cloud inference only; Windows needs Git for Windows | Official |
| Source | [Kimi Code GitHub](https://github.com/MoonshotAI/kimi-code) | Official |
| Last verified | 2026-09-20 | Official |

See the [Moonshot AI](/companies/moonshot-ai/) company profile, the [Kimi K3](/models/kimi-k3/) model, the [K3 vs K2.7-Code comparison](/comparisons/kimi-k3-vs-kimi-k27-code/), the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), and the site's [AI agents](/technology/ai-agents/) and [computer use](/technology/computer-use/) technology pages.

*Labels used above: **Official fact** (from the Kimi Code GitHub repo and docs), **Vendor-reported claim** (pricing and capability statements by Moonshot AI), and **China AI Hub analysis** (our synthesis, always introduced as such). No independent benchmark of Kimi Code's coding quality is currently recorded.*
