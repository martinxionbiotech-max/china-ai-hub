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
last_verified: "2026-09-30"
sources:
  - source_name: DeepSeek Harness GitHub repository
    source_url: https://github.com/deepseek-ai/deepseek-harness
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness product page
    source_url: https://deepseek.com/harness
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness documentation
    source_url: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek API pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness architecture documentation
    source_url: https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Cordis meta-framework repository
    source_url: https://github.com/cordiverse/cordis
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Cordis paper (A Programming Paradigm for Spatiotemporal Composability)
    source_url: https://arxiv.org/abs/2608.25512
    source_type: academic
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness releases
    source_url: https://github.com/deepseek-ai/deepseek-harness/releases
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness Python SDK guide
    source_url: https://deepseek-harness.github.io/deepseek-harness/en/guide/python-sdk
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: DeepSeek Harness Cordis primer
    source_url: https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** DeepSeek Harness is DeepSeek's open-source agent harness ("Everything is a Plugin") that powers its coding agent: models, tools, skills, sessions, sandbox, storage, loops, scheduling and UI are all composed from replaceable plugins on the Cordis framework. It ships as five interchangeable surfaces — a `dsh` CLI, Web UI, Electron desktop app, Python SDK and an ACP (Agent Client Protocol) server — under an MIT license as a self-hosted developer preview.

**Key facts.**

- Built on Cordis, a meta-framework of "spatiotemporal composability" formalized in an August 2026 paper (arXiv:2608.25512); even the model adapter, the tool registry and the agent loop are plugins with no privileged core.
- Five form factors: `dsh` CLI, Web UI, Electron desktop app, Python SDK (`deepseek-harness-sdk`) and an ACP server for programmatic multi-session automation.
- Capabilities include tool calling, browser use, computer use and MCP; planning and multi-agent are supported; there is no built-in memory.
- Underlying models are [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) and [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) — both MIT, both 1M-token context — billed through the configured provider at DeepSeek's pay-as-you-go rates.
- MIT-licensed and free as software; model usage is the only cost.
- Developer preview: the README states "THERE WILL BE COMPATIBILITY-BREAKING CHANGES", and SAFETY.md warns it is not security-audited or production-ready.
- Recent releases (v0.2.0-rc.1 and rc.2, late September 2026) added desktop-side plugin management, scheduled tasks and keyboard shortcuts.

**What this means.** DeepSeek is extending its openness-and-cost strategy from models into orchestration: the company that set the API price floor and shipped MIT open weights now gives away the harness running its coding agent, turning it into another distribution channel for DeepSeek model spend.

**What is uncertain.** The API is explicitly unstable (developer preview with compatibility-breaking changes), so anything built against it today may need rework. Security and isolation guarantees are absent, and `memory: false` means cross-session recall is not built in. Whether the harness stays a coding-agent substrate or broadens into a general agent framework is not settled.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-deepseek-harness-1 | DeepSeek Harness GitHub repository | https://github.com/deepseek-ai/deepseek-harness | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-2 | DeepSeek Harness product page | https://deepseek.com/harness | Official | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-3 | DeepSeek Harness documentation (quickstart) | https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-4 | DeepSeek API pricing | https://api-docs.deepseek.com/quick_start/pricing | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-5 | DeepSeek Harness architecture documentation | https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-6 | Cordis meta-framework repository | https://github.com/cordiverse/cordis | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-7 | Cordis paper (A Programming Paradigm for Spatiotemporal Composability) | https://arxiv.org/abs/2608.25512 | Literature | 2026-08-26 | 2026-09-30 | high | — |
| src-agents-deepseek-harness-8 | DeepSeek Harness releases | https://github.com/deepseek-ai/deepseek-harness/releases | Official | 2026-09-29 | 2026-09-30 | high | — |
| src-agents-deepseek-harness-9 | DeepSeek Harness Python SDK guide | https://deepseek-harness.github.io/deepseek-harness/en/guide/python-sdk | Official documentation | — | 2026-09-30 | high | — |
| src-agents-deepseek-harness-10 | DeepSeek Harness Cordis primer | https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer | Official documentation | — | 2026-09-30 | high | — |

## Why the architecture matters

The unusual claim in DeepSeek Harness is that *there is no privileged core to patch*. A running `dsh` is a tree of plugins composed at boot from ordered layers — a **profile** names the composition, a **bundle** distributes config rows and the code they mount, and any row can be replaced by a patch of your own. The model adapter lives on `ctx.llm`, the tool registry on `ctx.tools`, the session log on `ctx.sessions` — and the agent loop itself is a plugin on `ctx.agentLoop`.

This matters because it inverts the dominant agent-framework shape. Monolithic frameworks fix the loop and tool pipeline and let you bolt on capabilities; DeepSeek Harness fixes nothing and lets you *swap* the loop, sandbox and storage backend. Cordis formalizes the idea — "temporal composability" (every context transformation carries an inverse the runtime holds) and "spatial composability" (every context change is classified against a component's dependency specification) — which is why the project calls itself a "meta-framework of spatiotemporal composability" rather than a single product. China AI Hub analysis indicates this is a strategic bet, not a convenience: making the agent loop replaceable positions the harness as a substrate that can outlive any single model or tool — mirroring how DeepSeek's MIT releases reset the ecosystem's licensing floor.

## How it differs from Dify, FastGPT and MetaGPT

DeepSeek Harness sits in a different cell of the agent ecosystem than the three neutral open-source projects the site already profiles.

- **[Dify](/agents/dify/)** is a general LLM-application platform — visual workflow canvas, RAG pipeline, agent and model-management layers, observability — explicitly model-agnostic across hundreds of providers, oriented to *prototype-to-production application building* under a license with commercial conditions for multi-tenant SaaS.
- **[FastGPT](/agents/fastgpt/)** is a knowledge-base platform — RAG retrieval, visual workflow orchestration with RPA nodes, bidirectional MCP — model-agnostic through an AI Proxy, aimed at knowledge Q&A and enterprise assistants.
- **[MetaGPT](/agents/metagpt/)** is a role-based multi-agent framework — "Code = SOP(Team)" — turning one-line requirements into a simulated software company of PM/architect/engineer agents; a pip-installable, model-agnostic SDK.

China AI Hub analysis indicates DeepSeek Harness is the one entry whose alignment is *with a vendor, not with the operator*. Dify, FastGPT and MetaGPT all defer model choice to the user; DeepSeek Harness defaults every profile toward DeepSeek's own tiers — the quickstart's first step is entering a DeepSeek API key, and the Python SDK's minimal example defaults to a `deepseek-v4-flash` model string — while remaining provider-agnostic through any OpenAI-compatible endpoint. The neutral platforms are neutral about *whose model*; DeepSeek Harness is neutral about *which surface* but opinionated about *whose model economics* it inherits.

## Practical implications

**As a coding agent.** The primary, documented use: the Web UI and desktop app run an interactive session that reads and edits workspace files, runs commands, delegates work and maintains a plan, gated by an approval policy. It is the experience behind DeepSeek's own coding agent, which is why pricing mirrors DeepSeek's tiers rather than a subscription.

**As headless automation.** `dsh --profile headless` runs a one-shot task with no server, and the ACP server (`dsh-acp-app`) exposes automation-only multi-session control over the Agent Client Protocol — the documented path for GitHub PR review via webhook overlay.

**Embedding in Python.** The `deepseek-harness-sdk` wheel bundles the `dsh` runtime so a Python program can construct a `DeepSeekHarness(...)` context manager, run a task, and read `result.final_response` — no system Node.js required. The `sdk-minimal` profile pins `danger-full-access` permissions, so the docs instruct running it against a disposable checkout or container.

**Self-hosting cost.** The software is free (MIT); the real cost is the model provider you configure (DeepSeek's pay-as-you-go, off-peak at half) plus the infrastructure you host it on. The Web server binds to loopback only, so LAN access needs a reverse proxy with an explicit trusted-host list.

## What the evidence shows

The evidence is unusually strong for a preview product because DeepSeek publishes both code and a formal architecture document. The "Everything is a Plugin" claim is not marketing: the document enumerates the core packages (session, system-prompt, tools, agent, agent-loop, scope, llm, webhook), the event model (`session/*`, `agent/*`, `tools/*`), and the capability-seam pattern that lets one filesystem-provider swap move Bash, PTY and LSP together. The Cordis paper (arXiv:2608.25512, submitted 2026-08-26) supplies the formal underpinning — revertible effects and reactive coeffects unified into a single context type.

The release cadence confirms the "iterating rapidly" caveat: the 0.2.0 candidates (v0.2.0-rc.1 on 2026-09-28, v0.2.0-rc.2 on 2026-09-29) bundled the `dsh` command into the desktop apps for plugin management and added scheduled tasks, reminders and keyboard shortcuts.

The main limitations are structural, not cosmetic. Developer-preview status means no stability guarantee and no security audit; sandboxing and approvals "do not guarantee isolation," so untrusted work belongs in a disposable VM or container. China AI Hub analysis indicates `memory: false` is a deliberate scope boundary rather than a defect — the harness treats the workspace filesystem and session log as the source of continuity for stateless coding sessions, framing third-party memory MCP servers as interoperability examples only, so teams needing cross-session recall must supply that layer themselves. OAuth-based providers (e.g. Codex) are not yet supported, and image input routes only through `deepseek-flash`, since V4-Pro is text-only.

## Where this harness fits

| Workload | Relevance |
|---|---|
| Interactive coding-agent chat (Web UI / desktop) | High |
| Headless one-shot task automation (`dsh --profile headless`) | High |
| Embedding agents in Python programs (Python SDK) | High |
| Programmatic multi-session automation (ACP) | High |
| Custom plugin / profile / preset composition | High |
| GitHub PR review via webhook overlay | High |
| Long-lived cross-session memory | Low (no built-in memory) |
| Production, security-audited deployment | Low (developer preview) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/), [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) | Official |
| Target users | Developers (agent/coding-tool builders) | Official |
| Platform | CLI (dsh), Web UI, Electron Desktop, Python SDK, ACP server | Official |
| OS | Not publicly documented | Not publicly documented |
| Browser / computer use | Browser and computer use | Vendor-reported |
| Coding | Yes (powers DeepSeek's coding agent) | Official |
| Autonomous task execution | Yes (planning, multi-agent) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes | Official |
| Memory | No | Official |
| Workflow | Plugin-composed: models, tools, skills, sessions, sandbox, storage, loops, scheduling, UI | Official |
| API | Yes (model usage via configured provider) | Official |
| Pricing | Software free/open-source; model usage billed by provider | Vendor-reported |
| Region | Not publicly documented | Not publicly documented |
| Open-source | Yes — MIT | Official |
| Deployment | Self-hosted | Official |
| Limitations | Developer preview; not security-audited; sandboxing not isolation-guaranteed | Official |
| Source | [DeepSeek Harness GitHub](https://github.com/deepseek-ai/deepseek-harness) | Official |
| Last verified | 2026-09-30 | Official |

See the [DeepSeek](/companies/deepseek/) company profile, the [DeepSeek API](/api/deepseek/) platform, the [V4.1-Flash vs V4-Pro comparison](/comparisons/deepseek-v4-pro-vs-deepseek-v4-1-flash/), and the site's [AI agents](/technology/ai-agents/), [tool calling](/technology/tool-calling/) and [MCP](/technology/mcp/) technology pages.

*Labels used above: **Official fact** (from the DeepSeek Harness GitHub repo and docs), **Vendor-reported claim** (pricing and capability statements by DeepSeek), **Academic** (the Cordis paper), and **China AI Hub analysis** (our synthesis, always introduced as such).*
