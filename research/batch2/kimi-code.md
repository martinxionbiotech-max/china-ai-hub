# Kimi Code / kimi-cli research (fetched 2026-09-20)

## Sources used
- https://github.com/MoonshotAI/kimi-cli (README, releases)
- https://github.com/MoonshotAI/kimi-code (README) + GitHub API for both repos (stars, license, dates)
- https://moonshotai.github.io/kimi-cli/en/ and /kimi-code/en/ docs (getting started, config files, built-in tools, use cases, changelog, llms-full.txt)
- https://www.kimi.com/ and https://www.kimi.com/code/ (product pages)
- https://www.kimi.com/code/docs/en/ (official Kimi Code product docs: overview, membership)
- https://www.kimi.ai/membership/pricing (rendered via browser; JS-heavy)
- https://platform.kimi.ai/docs (overview, pricing/chat.md, guide/product-plans.md, llms.txt)
- https://www.moonshot.ai/ (corporate)

## Product facts
- Two-generation product: **Kimi CLI (kimi-cli)** — Python terminal agent launched Oct 2025, now being wound down; and its successor **Kimi Code CLI (kimi-code)** — "The Starting Point for Next-Gen Agents" (TypeScript, first release May 2026). Installing Kimi Code CLI auto-migrates kimi-cli config and sessions.
- Kimi Code is Moonshot AI's developer AI coding service, part of Kimi membership benefits; ships as Desktop app (macOS/Windows), CLI, and VS Code extension. Tagline: "One subscription, code anywhere".
- kimi-cli repo: created 2025-10-15; first GitHub release v0.33 on 2025-10-21; latest v1.50.0 on 2026-09-01 (adds one-key migration to Kimi Code). 11,409 stars, 1,324 forks, Apache-2.0, Python. Also on PyPI.
- kimi-code repo: created 2026-05-22; earliest release @moonshot-ai/kimi-code@0.2.0 on 2026-05-26; latest 2.0.2 on 2026-09-19. 7,525 stars, 1,224 forks, MIT license, TypeScript (npm package @moonshot-ai/kimi-code).
- Corporate context: Moonshot AI's flagship model is Kimi K3 (2.8T parameters, natively multimodal, 1M-token context; "built for long-horizon coding").

## Features & capabilities
Kimi Code CLI (current generation, verified from README + docs):
- Terminal AI coding agent: reads/edits code, runs shell commands, searches files, fetches web pages, plans and adjusts actions autonomously from feedback.
- Single-binary install (curl/irm scripts; no Node.js needed; npm install also available). Millisecond TUI startup (built on pi-tui).
- Built-in tools: Read, Write, Edit, Grep (ripgrep), Glob, ReadMediaFile, Bash, WebSearch, FetchURL, EnterPlanMode, TodoList, Agent (subagents), AskUserQuestion, NotifyUser, Skill, TaskList/TaskOutput/TaskStop (background tasks), WaitFor, CronCreate/CronList/CronDelete (scheduled tasks).
- Permission model: read-only tools auto-allowed; write/exec tools need approval; modes manual / yolo / auto; Plan mode (Shift-Tab or `kimi --plan`).
- Subagents (coder, explore, plan) for parallel isolated work; lifecycle hooks (e.g. PreToolUse Bash gating); plugin marketplace; Agent Skills.
- MCP support: `kimi mcp add/list/remove/auth` (HTTP/stdio/OAuth) plus ad-hoc `--mcp-config-file`; AI-native /mcp-config in Kimi Code CLI.
- Editor/IDE integration: VS Code extension (marketplace item moonshot-ai.kimi-code); Agent Client Protocol (`kimi acp`) for Zed, JetBrains and any ACP client.
- Multimodal input: text, images, and video (drop a screen recording; agent reads frames).
- Official plugins/capabilities: **Kimi Computer Use** (operate desktop apps: click/drag/scroll/type; macOS silent background mode + Windows), **Kimi WebBridge / Kimi Browser Extension** (drive your own browser), **Kimi Datasource** (natural-language queries over financial/macro/legal/academic data).
- Sessions: resume with `kimi -c`, `/fork`, `/compact`, background tasks (max 4), scheduled tasks, telemetry on by default (config toggle).
- kimi-cli legacy extras: built-in shell mode (Ctrl-X), zsh plugin (MoonshotAI/zsh-kimi-cli); note: built-in shell commands like `cd` not supported.
- No dedicated sandboxing (runs on the local machine with approval gates); "sandbox" in docs only refers to isolated config dirs via KIMI_CODE_HOME. No separate git tool — git operations go through the Bash tool.

## Underlying models
- Kimi Code models (product docs, model IDs accepted by both OpenAI/Anthropic-protocol endpoints): `k3` (K3 flagship, 2.8T params; Plus and above; Pro and above unlock up to 1M context; low/high/max thinking effort), `k3-256k` (same quality within 256K, no video input), `kimi-for-coding` (K2.8 Preview, up to 1M context), `kimi-for-coding-highspeed` (K2.7 Code HighSpeed, output up to 260 tokens/s, Pro and above).
- Kimi Code CLI default: `default_model = "kimi-code/k3"` with managed provider base_url `https://api.kimi.com/coding/v1`, default effort "max" (config file example).
- CLI also configurable with third-party providers: anthropic, openai, openai_responses, google-genai, vertexai.
- Related Open Platform API models (platform.kimi.ai): kimi-k3 (1M ctx, reasoning_effort low/high/max, default max), kimi-k2.7-code and kimi-k2.7-code-highspeed (256K ctx, thinking, text/image/video), kimi-k2.6.

## Pricing
- Kimi Code itself has no separate price — included with Kimi membership, Plus and above. Free tier ("Adagio" / legacy "Go") has no coding quota. All clients (CLI/VS Code/Desktop/third-party) share one quota; new plans removed the weekly window, keep a rolling 5-hour rate window and monthly total quota.
- Membership plans (kimi.ai/membership/pricing, fetched 2026-09-20): Adagio $0; Plus $15/mo or $180/yr; Pro $31/mo or $372/yr; Max $79/mo or $948/yr; Ultra $159/mo or $1,908/yr. Agent credits: Plus "more", Pro 2x, Max 5x, Ultra 10x.
- Extra Usage top-up when quota exhausted: pay-as-you-go balance shared between Kimi web and Kimi Code; "pricing is close to the official API pricing of the Kimi Open Platform".
- Open Platform API pay-as-you-go (per 1M tokens, platform.kimi.ai/docs/pricing/chat.md): kimi-k3 input $3.00 / output $15.00; cache write $3.00 (TTL 5min) or $6.00 (TTL 1h), cached input $0.30. kimi-k2.7-code: input $0.95 (cache hit $0.19) / output $4.00; kimi-k2.7-code-highspeed: $1.90 (hit $0.38) / $8.00; kimi-k2.6: $0.95 (hit $0.16) / $4.00. Enterprise plans via contact sales.

## Deployment / open source
- Client is fully open source on GitHub (MoonshotAI/kimi-cli Apache-2.0; MoonshotAI/kimi-code MIT). Runs locally (macOS/Linux/Windows — Windows uses bundled Git Bash, KIMI_SHELL_PATH override).
- Inference is cloud: managed service api.kimi.com/coding/v1 (China) / api.kimi.ai/coding/v1 (overseas); login via Kimi Code OAuth (device-code) or Kimi Platform API key.
- Not self-hostable as a model service; the open client can point at any compatible provider (Anthropic/OpenAI/Google-compatible endpoints).
- Docs hosted at moonshotai.github.io/kimi-code (en/zh); product docs at kimi.com/code/docs.
- Server mode exists: kimi-code ships a Server API (endpoints incl. /api/v1/capabilities etc.) and web/browser UI ("Using Kimi Code in the browser", Remote Control page) — self-hosted web interface for a local agent.

## Use cases & limitations
- Documented use cases: understanding unfamiliar codebases, implementing features, bug fixing, writing tests/refactoring, batch file processing, running builds/tests, web search/fetch during coding, long-horizon whole-repo work via 1M context, video-input tasks (screen recording → code, LUT generation), scheduled/background tasks, IDE-driven sessions.
- Documented limitations/notes: kimi-cli deprecated ("gradually wound down"; docs remain); kimi-cli built-in `cd` not supported in shell mode; Windows install requires Git for Windows; Computer Use Windows version may briefly take over mouse/keyboard; macOS Computer Use needs Accessibility + Screen Recording permissions; third-party tool use must keep the real client identifier (User-Agent tampering restricted); API keys (max 5) shown only once; quota shared across devices; devices inactive >30 days unbound.

## Conflicts / uncertainty notes
- Membership tier naming: pricing page uses Adagio/Plus/Pro/Max/Ultra; Kimi Code product docs still reference legacy musical names (Moderato/Andante/Allegretto) mapped to Plus/Pro — docs say tiers were renamed with unchanged pricing; "K3 available on plans and above" vs "Plus and above" wording differs across pages.
- Kimi Code CLI config example lists kimi-for-coding max_context_size 262,144, while product docs say K2.8 Preview supports up to 1M context (config example likely stale default).
- kimi-cli earliest GitHub release (v0.33, 2025-10-21) postdates repo creation (2025-10-15); actual launch-day version could not be confirmed beyond releases API (103 releases; page 1 shows 100, earliest v0.36 on 2025-10-23 — earlier tags on page 2).
- Star counts are point-in-time (2026-09-20, GitHub API).
- Pricing figures taken from the rendered membership pricing page (USD, monthly billing tab); page notes "new membership plan now available" — figures may differ for legacy plan holders.
