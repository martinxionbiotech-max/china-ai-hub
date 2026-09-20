# DeepSeek Harness research (fetched 2026-09-20)

## Sources used
- https://github.com/deepseek-ai/deepseek-harness (README; repo facts via https://api.github.com/repos/deepseek-ai/deepseek-harness)
- https://deepseek.com/harness (official product page; served zh text)
- https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart (docs)
- https://api-docs.deepseek.com/ (home: Harness preview note) and https://api-docs.deepseek.com/quick_start/pricing (API model pricing)
- Raw docs from repo (fetched 2026-09-20):
  - README.md, SAFETY.md, AGENTS.md
  - docs/user/guide/index.md, providers.md, python-sdk.md, mcp-memory.md
  - apps/cli/README.md, apps/desktop/README.md
  - packages/bundle/base/README.md, packages/bundle/web-app/README.md
  - packages/llm/llm-deepseek/README.md, packages/hooks/README.md, packages/preset/README.md, packages/acp/README.md
  - GitHub contents API: packages/, apps/, docs/user/guide/

## Product facts
- Name: **DeepSeek Harness** (CLI `dsh`). Tagline: "Everything is a Plugin."
- Made by DeepSeek AI (深度求索); repo description: "DeepSeek Harness: Everything is a Plugin."
- Positioning: an **open-source agent harness** — the framework/runtime that powers DeepSeek's coding agent; all agent capabilities (models, tools, skills, sessions, sandbox, storage, loops, scheduling, UI) are composed from plugins and can be replaced/recombined (source: deepseek.com/harness, repo README).
- Status: **developer preview**, "iterating rapidly. THERE WILL BE COMPATIBILITY-BREAKING CHANGES." SAFETY.md calls it "experimental developer-preview software", not security-audited, not production-ready.
- First release date: not stated on any fetched page. Repo created 2026-08-13T11:56:32Z (GitHub API). API docs home page says it is "now in developer preview for agent harness developers worldwide" (as of fetch date).
- Built on **Cordis** (github.com/cordiverse/cordis); design described in arXiv:2608.25512 "A Programming Paradigm for Spatiotemporal Composability".

## Features & capabilities
- **Interfaces**: Web UI (`npx @deepseek-ai/dsh web`, default http://127.0.0.1:3080); headless one-shot mode (`dsh --profile headless "task"`); CLI profile system; Python SDK; ACP (Agent Client Protocol over JSON-RPC stdio) for programmatic automation; Electron **Desktop** app (port 19387, wraps the Web app). No VS Code extension found in the repo (apps/ = cli, desktop-host, desktop, web).
- **Coding agent tools** (dsh-base bundle): file editing (`read`/`write`/`edit` by default; `str_replace_editor` opt-in), shell commands (bash on Linux/macOS, PowerShell on Windows), web search + public HTTP(S) fetch, **subagents** (delegated agents, incl. out-of-process via ACP), task & goal tracking (`todo_write`, goals), logged **planning**, **skills** loading, **compaction**, durable sessions (SQLite + JSONL logs).
- **Sandboxing & permissions**: default permission policy confines file writes to the workspace and asks before risky actions; sandboxed filesystem provider; Windows ACL restricted-token runner. SAFETY.md: sandboxing/approvals "do not guarantee isolation" — run in disposable VM/container for untrusted work.
- **Git ops**: no dedicated git package found; agent does git via shell. Opt-in overlays ship for **GitHub review webhooks** (PR review) and session-local Schedule. `hooks` group runs existing **Claude Code / Codex** `hooks.json` hook configs (block/continue prompts and tool calls, add context).
- **MCP support**: yes — `@deepseek-ai/dsh-mcp-client`; stdio and Streamable HTTP transports; tools exposed as `mcp__<serverName>__<tool>`; MCP resources mounted in base bundle. No MCP server ships by default.
- **Memory**: none built-in; official guide shows default-off configs to connect third-party memory MCP servers (Memorix, MCP Reference Memory, Engram) — "interoperability examples only", no endorsement.
- **Browser use / computer use**: dedicated packages `browser-use` and `computer-use` exist in the repo; base bundle ships web search/fetch tools. Detail docs not fetched.
- **Multi-agent / presets**: per-session **agent presets** (each session composes its own agent from presets; one process can run several differently-composed agents).
- **Plugins**: everything is a plugin; profiles are ordered stacks of plugin-bundle patch layers; plugin manager via `dsh plugin` (pnpm); topic tag `dsh-plugin`; Discord community + GitHub Discussions.

## Underlying models
- Harness is **BYO-key**: configure a DeepSeek API key (or other providers) in Settings. Harness itself ships no model.
- Default provider/route: `deepseek-official`; **default model for Web/headless: `deepseek-flash` (DeepSeek-V4.1-Flash)**. Adapter default catalog advertises `deepseek-flash` (text+image) and `deepseek-v4-pro` (text-only), each 1,000,000-token context (source: packages/bundle/web-app/README.md, packages/llm/llm-deepseek/README.md).
- Adapter defaults: Anthropic-style Messages protocol (`https://api.deepseek.com/anthropic`), thinking **enabled**, reasoning effort default **high** (levels off/low/high/max), per-request output cap 256,000 tokens. Python SDK `minimal.py` example uses `provider="deepseek-official"`, `model="deepseek-v4-flash"` (legacy name), `max_tokens=49,152`.
- Multi-provider: built-in catalog includes `anthropic`, `openai`, `moonshotai` (Kimi), `zai` (GLM); custom providers via openai-completions / openai-responses / anthropic-messages protocols; OAuth sign-in providers (e.g. Codex) not supported yet.

## Pricing
- The Harness software itself: **free, open source**. No subscription or license fee appears anywhere in fetched sources.
- Model usage is billed by the **DeepSeek API** pay-as-you-go (per 1M tokens, fetched 2026-09-20):
  - deepseek-flash (V4.1-Flash): input cache hit $0.003 off-peak / $0.006 peak; cache miss $0.15 / $0.30; output $0.60 / $1.20. Concurrency limit 2500.
  - deepseek-v4-pro: input cache hit $0.022 / $0.044; cache miss $0.66 / $1.32; output $1.98 / $3.96. Concurrency limit 500.
  - Off-peak = half of peak; peak = 01:00–04:00 and 06:00–10:00 UTC Mon–Fri excluding Chinese public holidays. Context length 1M, max output 384K.
- Third-party providers billed on their own terms (configured by user).

## Deployment / open source
- **Open source: yes.** Repo: https://github.com/deepseek-ai/deepseek-harness — TypeScript, **MIT license**, default branch master.
- Repo stats (fetched 2026-09-20 via GitHub API): **230,576 stars**, **27,622 forks**, created 2026-08-13, last push 2026-09-17; Discussions enabled; Issues/PRs disabled (feedback via Discussions/Discord).
- **Deployment: self-hosted / local only** in documented paths. Node package `@deepseek-ai/dsh` (npx, needs Node.js); Python wheel `deepseek-harness-sdk` (Python 3.10+, Git; Linux x64/arm64, macOS 14+ arm64, Windows x64). No cloud-hosted/SaaS version of the Harness documented.
- **API/SDK availability**: yes — Python SDK (`deepseek_harness` package; starts `dsh --profile sdk-minimal` over JSON-RPC); Node/npm packages; ACP profile serves automation clients; the Web GUI has a remote BFF (packages/api). No hosted HTTP API for the Harness itself.

## Use cases & limitations
- Use cases (official docs): interactive coding-agent chat via Web UI; headless one-shot tasks (`dsh --profile headless "run the tests"`); embedding agents in Python programs; programmatic multi-session automation over ACP; GitHub PR review via webhook overlay; custom profiles/plugins/presets for different agent compositions.
- Limitations (as documented):
  - Developer preview with breaking changes expected; not security-audited; no warranty (MIT).
  - Sandbox/approvals reduce but don't guarantee safety; run untrusted work in disposable environments.
  - Web server binds loopback only (`--host 0.0.0.0` rejected); trusted-host list for LAN access.
  - OAuth providers (e.g. Codex) not yet supported; only API-key providers.
  - `sdk-minimal` profile: no filesystem tools/policies by default and pins `danger-full-access` permissions.
  - Image input only via `deepseek-flash`; `deepseek-v4-pro` is text-only (no vision).
  - Legacy model names (`deepseek-v4-flash`, `deepseek-v4-flash-vision-exp`) retired but still accepted, served by V4.1-Flash.

## Conflicts / uncertainty notes
- "First release date": no official launch date stated in fetched pages; GitHub repo creation (2026-08-13 UTC) is the only verifiable date. The dev-preview announcement page (deepseek.com/harness) carries no date.
- VS Code / editor integration: no VS Code extension exists in the repo; no editor integration is documented in fetched sources. ACP exists but is documented as automation-only. Not claiming editor support.
- Default model: web-app bundle README says default is `deepseek-flash`; the Python SDK minimal example defaults to the legacy `deepseek-v4-flash` name. Both point to the same Flash line; the exact default differs per surface.
- Star/fork counts are a point-in-time snapshot from the GitHub API on 2026-09-20.
- web_search and Tavily were unavailable (provider disabled / plan limit), so all facts come from direct fetches of official DeepSeek properties only.
