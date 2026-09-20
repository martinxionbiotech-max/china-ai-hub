# Qwen Code / Qoder / Qwen-Agent — Research Notes

- **Fetched:** 2026-09-20 (Asia/Shanghai)
- **Scope:** Official sources only (GitHub repos/APIs, qwenlm.github.io docs, qoder.com, docs.qoder.com, alibabacloud.com / help.aliyun.com Model Studio docs, npm registry)
- **Method:** web_fetch + browser (for JS-rendered qoder.com/pricing) + GitHub API via curl. No model-memory facts used; every fact below has a source URL.
- **Convention:** Anything not found in the fetched sources is marked "not publicly disclosed".

---

## Sources used

Qwen Code:
- https://github.com/QwenLM/qwen-code (repo, README via https://raw.githubusercontent.com/QwenLM/qwen-code/main/README.md)
- https://api.github.com/repos/QwenLM/qwen-code (metadata: created_at 2025-06-26, license, stars)
- https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=100&page=N (release history; oldest GitHub release v0.0.1-alpha.14 / v0.0.2, 2025-08-01)
- https://registry.npmjs.org/@qwen-code/qwen-code (first npm publish 0.0.1 on 2025-07-22; latest 0.24.1)
- https://qwenlm.github.io/qwen-code-docs/en/users/overview/ (product overview)
- https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/ (providers, plans, endpoints, model list)
- https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/ (5 permission modes)
- https://qwenlm.github.io/qwen-code-docs/en/users/features/sandbox/ (sandboxing)
- https://qwenlm.github.io/qwen-code-docs/en/users/features/memory/ (QWEN.md + auto-memory + team memory)
- https://qwenlm.github.io/qwen-code-docs/sitemap.xml (feature inventory: sub-agents, multi-agent-coordination, computer-use, browser-use, mcp, hooks, skills, goals, scheduled-tasks, worktree, lsp, etc.)
- https://www.alibabacloud.com/help/en/model-studio/coding-plan (Coding Plan intl pricing)
- https://help.aliyun.com/en/model-studio/token-plan-overview (Token Plan CN pricing; reached via https://help.aliyun.com/document_detail/3028856.html)

Qwen-Agent:
- https://github.com/QwenLM/Qwen-Agent (README via https://raw.githubusercontent.com/QwenLM/Qwen-Agent/main/README.md)
- https://api.github.com/repos/QwenLM/Qwen-Agent (created_at 2023-09-22, license, stars)
- https://api.github.com/repos/QwenLM/Qwen-Agent/releases?per_page=100 (first release v0.0.1 on 2024-04-07; latest v0.0.26 on 2025-05-29)
- https://qwenlm.github.io/Qwen-Agent/en/guide/ (docs overview)

Qoder:
- https://qoder.com/ , https://qoder.com/qoder , https://qoder.com/pricing (official site; pricing rendered via browser)
- https://qoder.cn/ (China site, HTTP 200, verified)
- https://docs.qoder.com/zh and https://docs.qoder.com/llms.txt + .md pages:
  - https://docs.qoder.com/product-series/what-is-qoder.md
  - https://docs.qoder.com/qoder/overview.md
  - https://docs.qoder.com/qoder/model-selector.md
  - https://docs.qoder.com/cli/overview.md
  - https://docs.qoder.com/release-notes/desktop.md
- https://www.alibabacloud.com/help/en/model-studio/qoder-agent (Model Studio integration guide)
- https://www.alibabacloud.com/en/marketplace/qoder (Qoder for Enterprise, via DuckDuckGo result; not directly fetched)
- https://api.github.com/orgs/QoderAI/repos (official Qoder GitHub org: changelogs, SDKs, skills, plugins — but no CLI/IDE source)
- https://html.duckduckgo.com/html/?q=Qoder+Alibaba+coding+agent+official (used only to locate official URLs; no third-party facts used)

---

## Product facts

### Qwen Code
- **Name / positioning:** "The open-source AI coding agent for your terminal, editor, desktop, browser, and chat." Repo tagline: "An open-source AI coding agent that lives in your terminal." (https://github.com/QwenLM/qwen-code README)
- **agent_type:** coding agent (CLI-first, with desktop app, Web UI, IDE plugins, chat integrations).
- **Vendor:** Qwen team (QwenLM org, Alibaba). Docs hosted at qwenlm.github.io/qwen-code-docs.
- **First release / creation:**
  - GitHub repo created **2025-06-26** (https://api.github.com/repos/QwenLM/qwen-code)
  - First npm publish: **0.0.1 on 2025-07-22** (https://registry.npmjs.org/@qwen-code/qwen-code)
  - Oldest GitHub releases: **v0.0.1-alpha.14 and v0.0.2 on 2025-08-01** (releases API)
  - Latest release at fetch time: **v0.24.1, 2026-09-19** (releases API)
- **History:** "Originally based on Google Gemini CLI v0.8.2. Starting from Qwen Code v0.1, we stopped syncing with upstream and began independent development as a multi-protocol, multi-platform agent framework." (README)
- **Repo stats (2026-09-20):** 28,005 stars, 3,075 forks, TypeScript, 1,501 open issues. (repo API)
- **License:** Apache-2.0. (repo API)
- **Ecosystem:** Qwen Code Desktop (macOS/Windows/Linux), VS Code extension "Qwen Code Companion" (Beta), Zed/JetBrains integrations, Web UI (`qwen serve --open`, experimental), SDKs (TypeScript/Python/Java), Aliyun Model Studio CLI (bailian-cli) extends it. (README, overview docs)

### Qwen-Agent
- **Name / positioning:** "A framework for developing LLM applications based on the instruction following, tool usage, planning, and memory capabilities of Qwen. It also comes with example applications such as Browser Assistant, Code Interpreter, and Custom Assistant. Now Qwen-Agent plays as the backend of Qwen Chat." (README)
- **agent_type:** agent framework (not a standalone product agent; powering Qwen Chat at chat.qwen.ai).
- **First release / creation:**
  - GitHub repo created **2023-09-22** (repo API)
  - First GitHub release **v0.0.1 on 2024-04-07**; latest release v0.0.26 on 2025-05-29; last push 2026-03-04 (releases/repo API)
- **Repo stats (2026-09-20):** 17,110 stars, 1,727 forks, Python. (repo API)
- **License:** Apache-2.0. (repo API)
- **Install:** `pip install -U "qwen-agent[gui,rag,code_interpreter,mcp]"` (README)
- **Recent news from README:** Qwen3.5 open-sourced 2026-02-16 with agent demo; DeepPlanning agent-evaluation benchmark + docs added 2026-01-27; MCP cookbooks since 2025-05-01.

### Qoder
- **Name / positioning:** "Qoder — The Agentic Platform"; "Agentic Coding Platform for Everyone"; "an agentic coding platform for software development that supports a desktop IDE, CLI, and JetBrains plugin." (https://qoder.com/qoder; https://www.alibabacloud.com/help/en/model-studio/qoder-agent)
- **agent_type:** coding agent product/IDE agent (commercial, closed-source), extended to general work agents (QoderWork, QoderWake "digital employees", Cloud Agents).
- **Product family** (https://docs.qoder.com/product-series/what-is-qoder.md): Qoder (new agentic desktop product, "originated from Quest mode in Qoder IDE"), Qoder IDE (formerly the main desktop app; renamed to "Qoder IDE" in v1.24.0/1.25.x, Aug 2026 per release notes), JetBrains Plugin, Qoder CLI (`qodercli`), Cloud Agents (managed agents via API), QoderWork (doc/spreadsheet/research/browser/desktop task delegation), QoderWake ("digital employees called Wakers"), Mobile & Web, Enterprise.
- **First release / creation:**
  - Official docs release notes (IDE) start at **0.1.15, 2025-08-21** (https://docs.qoder.com/release-notes/desktop.md) — exact product launch date earlier than that is **not publicly disclosed** in fetched sources.
  - Official GitHub org QoderAI's earliest repo (homebrew-qoder) created **2025-09-24** (org repos API).
  - "New Qoder" (agentic platform, qoder.com/qoder) appears in DuckDuckGo index with date 2026-01-30 (page date; launch date not explicitly stated in docs).
  - Current IDE version 1.31.0 (2026-09-18); CLI update docs recommend latest "0.16.0 or later" (release notes; https://www.alibabacloud.com/help/en/model-studio/qoder-agent FAQ).
- **Company/entities:** International site footer: "© 2026 BRIGHT ZENITH PRIVATE LIMITED — SOC 2 | ISO27001 Certified" (https://qoder.com/pricing footer). China site: https://qoder.cn/. Alibaba Cloud Model Studio lists "Qoder" (intl) and "Qoder CN" (China) as supported tools (coding-plan docs).
- **Open source:** Qoder CLI/IDE source is **not open source** — no public repo found (GitHub searches and org listing show only SDKs/changelogs/skills). Related open artifacts from official org QoderAI: qoder-action (MIT), qoder-acp-demos (Apache-2.0), cloud-agents SDKs (MIT), skills repo. (https://api.github.com/orgs/QoderAI/repos)

---

## Features & capabilities

### Qwen Code (README + docs feature pages)
- **Agentic out of the box:** Auto-Memory, Auto-Skills, SubAgents, Agent Teams, Dynamic Workflows, MCP — "zero setup" (README).
- **Tools:** file edit, shell/bash execution, web search (built-in when using Token Plan / Standard API Key), web scraping, git, LSP integration, MCP tool connections (Google Drive, Figma, Slack, Jira etc. via MCP) (README, auth docs, overview docs).
- **Permission modes (5):** Plan (read-only), Ask Permissions (default on first start; manual approval for edits+shell), Auto-Edit (auto-approve file edits, manual shell approval), Auto (LLM-classifier auto-approves safe actions, blocks risky ones — e.g. blocks `rm -rf /`, `curl | sh`, credential exfiltration, .bashrc/crontab edits, force-push; fail-closed when classifier unreachable), YOLO (auto-approve everything). Cycle with Shift+Tab. (https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/)
- **Planning:** Plan Mode + `/plan` command; plans with read-only analysis. (approval-mode docs)
- **Sandboxing:** macOS Seatbelt (`sandbox-exec`, 6 profiles: permissive/restrictive × open/closed/proxied) or Docker/Podman container (default published image ghcr.io/qwenlm/qwen-code:\<version\>; custom image via `.qwen/sandbox.Dockerfile`; UID/GID mapping on Linux; optional allowlist network proxy via QWEN_SANDBOX_PROXY_COMMAND). Enable with `-s` / QWEN_SANDBOX / tools.sandbox. "Sandboxing reduces but doesn't eliminate all risks." (sandbox docs)
- **Memory:** QWEN.md (user-written instructions: ~/.qwen/QWEN.md, project QWEN.md, .qwen/QWEN.local.md; also reads AGENTS.md), Auto-memory (agent-written markdown notes under ~/.qwen/projects/<project>/memory/, background daily cleanup via /dream), Team memory (.qwen/team-memory/ committed to git, optional auto-sync, secret scanning). Commands: /memory, /init, /remember, /forget, /dream. (memory docs)
- **Subagents & multi-agent:** SubAgents, Agent Teams, Agent Arena (multi-model head-to-head on same task), multi-agent coordination pages in docs. (README, sitemap)
- **MCP:** full MCP support (features/mcp page; MCP budget guardrails in daemon docs). (README, sitemap)
- **Browser / computer use:** Computer Use (desktop automation) and browser-use feature pages. (README, sitemap)
- **Other:** Hooks, built-in Skills (/review, /batch, /loop, /bugfix…), followup suggestions, checkpointing, scheduled tasks, goals, git worktrees, token caching, structured output, dual output, headless mode (`qwen -p`), daemon mode (`qwen serve`, ACP, experimental), IM channels (Telegram/DingTalk/WeChat/Feishu), SDKs (TypeScript/Python/Java). (README, sitemap)
- **Multi-protocol:** OpenAI, Anthropic, Gemini, Qwen APIs; third-party built-ins: DeepSeek, Grok, MiniMax, Z.AI, Kimi, Idealab, ModelScope, OpenRouter, Requesty; custom providers incl. local (Ollama/vLLM). (README, auth docs)
- **Eval:** SWE-bench Verified 500 cases, best avg score 77.80% (v0.0.14) using Qwen 3.7 Max; latest measured v0.22.0 at 77.33% avg. (README)

### Qwen-Agent (README + docs)
- **Core components:** LLM classes (BaseChatModel, function calling), Tools (BaseTool + @register_tool), Agents (Agent base; built-ins: Assistant, FnCallAgent, ReActChat). Parallel function calls supported by default tool-call template. (README)
- **Built-in tools/examples:** Code Interpreter (Docker-container based, isolated), RAG (fast RAG for 1M-token docs + parallel_doc_qa agent), image_gen example, MCP tool integration (npx/uvx MCP servers), GUI (Gradio 5 WebUI), Chrome extension / BrowserQwen browser assistant. (README)
- **Memory/planning:** framework is explicitly built around "instruction following, tool usage, planning, and memory capabilities of Qwen" (README). Reasoning support: `reasoning_content` field (2025-03-18), QwQ-32B parallel/multi-step tool calls demo (2025-03-07), Qwen3 native tool call via vLLM (2025-07-23), Qwen3.5 agent demo (2026-02-16).
- **Benchmark:** DeepPlanning — open-sourced agent evaluation benchmark (2026-01-27). (README)

### Qoder (docs.qoder.com + qoder.com)
- **Agentic loop:** "understand the task and its context, plan the work, use tools to execute it, verify the result, and iterate toward the requested outcome." (what-is-qoder.md)
- **Desktop product (Qoder):** modes (Coding = workspace-based w/ branch controls; General = folder-based), task composer, model selector w/ tiers (Auto/Ultimate/Performance/Efficient), plan- or goal-driven workflows, built-in browser tool, code review & commit flow, terminal, automations (scheduled agent runs), Knowledge Center (Knowledge Bases, Repo Wiki), extensions (Skills, Plugins, Connectors, Hooks, subagents, AppShot, Computer control), voice input, desktop companion/proactive mode. Claims on marketing page: "40+ connectors, 70+ plugins, 20K+ skills", "Agent Harness" with act-verify loops, cross-device task continuity. (qoder/overview.md, qoder.com/qoder)
- **Qoder CLI:** agentic terminal assistant — reads files, invokes tools, executes commands "with permission-based confirmations before critical operations"; built-in tools (file read/write/edit, shell, grep, glob, web search, web scraping); MCP; headless mode for CI/CD; extensible via Skills, Plugins, Subagents, Hooks, Custom Commands; Memory + Knowledge Base; project instructions (AGENTS.md) as context. Working modes: Interactive, Plan, Goal, Scheduled Task, /loop, Headless. Multimodal input (images, PDFs). (cli/overview.md)
- **Qoder IDE:** agentic IDE — Editor (in-flow assistance), Quest (long-running multi-step delegation); Expert team mode (multi-agent parallel dev); side tasks; live voice w/ voiceprint; AppShot (screen snapshot context); HTTP Hooks; static/light/deep security scans (L1/L2/L3); enterprise controls (disable browser external network, group management). Tool execution limit 500 rounds per task (v1.28.0). (release notes, what-is-qoder.md)
- **Cloud Agents:** managed agents via API (Agents, Environments, Sessions, streamed results); Agent SDK; SDKs in Go/Python/TS (MIT). (what-is-qoder.md, QoderAI org)
- **Security:** permission confirmations before side-effect operations (CLI); enterprise SSO (SAML/OIDC), unified privacy mode control, model policy control, plugin/skill distribution control, private marketplace, audit logs, centralized billing, group permissions. (cli/overview.md, qoder.com/pricing feature table)

---

## Underlying models

### Qwen Code
- **No fixed default model** — user configures provider + model via `/auth` and switches with `/model`; selection persists. (auth docs)
- **Recommended official setup = Alibaba ModelStudio.** Coding Plan-supported models listed in docs: qwen3.5-plus, qwen3.6-plus, qwen3.7-plus, qwen3-coder-plus, qwen3-coder-next, qwen3-max-2026-01-23, glm-5, glm-4.7, kimi-k2.5, MiniMax-M2.5. Settings examples use **qwen3-coder-plus**. (auth docs)
- **Eval model:** official SWE-bench runs use **Qwen 3.7 Max** (context 1M, max_tokens 64,000). (README)
- Any third-party model works: OpenAI, Anthropic Claude, Google Gemini, DeepSeek, Grok, MiniMax, Z.AI, Kimi, OpenRouter, Requesty, ModelScope, local via Ollama/vLLM. (auth docs, README)

### Qwen-Agent
- **Default example model:** `qwen-max-latest` via DashScope (`model_type: qwen_dashscope`, DASHSCOPE_API_KEY); docs guide uses `qwen3-max`. Any OpenAI-compatible endpoint (vLLM/Ollama) supported; Qwen2.5/3/QwQ/Qwen3-Coder/Qwen3.5 demos included. (README, guide docs)
- Qwen-Agent is the backend of Qwen Chat (chat.qwen.ai). (README)

### Qoder
- **Default:** Auto (Smart Routing) tier — "intelligently selects the most suitable model, balancing performance and cost"; "recommended as default". (model-selector.md)
- **Tiers:** Auto ~1.0×, Ultimate ~1.6×, Performance ~1.1×, Efficient ~0.3× (limited-time free for paid users). (model-selector.md)
- **Selectable models (intl product):** Qwen3.8-Max (0.5×), Qwen3.8-Flash (0.1×), Qwen3.7-Max (0.5×), Qwen3.7-Plus (0.1×), DeepSeek-V4-Pro (0.8×), DeepSeek-Flash (0.2×), GLM-5.3 (0.6×), GLM-5.3-Flash (0.1×), Kimi-K3 (0.8×), Kimi-K2.8-Preview (0.3×), MiniMax-M3 (0.2×). Context windows 200K/400K/1M; thinking effort low→max. (model-selector.md)
- **BYOK:** custom models via personal API key; BYOK providers for personal edition: OpenAI, Google, OpenRouter (since IDE 1.27.0). (model-selector.md, release notes)
- Via Alibaba Cloud Model Studio, Qoder can also be connected to Coding Plan / Token Plan models (only text-generation models supported in that configuration). (https://www.alibabacloud.com/help/en/model-studio/qoder-agent)

---

## Pricing

### Qwen Code (CLI itself is free, Apache-2.0; you pay the model provider)
- **Qwen OAuth free tier: discontinued 2026-04-15.** New requests rejected; migrate to Coding Plan / OpenRouter / etc. (auth docs)
- **Alibaba Cloud Coding Plan (intl):** Pro $50/month — up to 6,000 requests/5h, 45,000/week, 90,000/month; models: qwen3.7-plus, qwen3.6-plus, kimi-k2.5, glm-5, MiniMax-M2.5 (recommended) + qwen3.5-plus, qwen3-max-2026-01-23, qwen3-coder-next, qwen3-coder-plus, glm-4.7. Lite plan: new subscriptions stopped 2026-03-20, renewals/upgrades stopped 2026-04-13. Limited slots, restocked daily 00:00 Beijing. Non-refundable; API-key use outside interactive coding tools prohibited. Endpoints: coding.dashscope.aliyuncs.com/v1 (CN) / coding-intl.dashscope.aliyuncs.com/v1 (intl). (https://www.alibabacloud.com/help/en/model-studio/coding-plan)
- **Alibaba Cloud Token Plan (China Beijing region only):** usage-based Credits. Personal Edition: Lite ¥39/mo (orig ¥60; 2,500 Credits/7 days), Essential ¥79 (orig ¥120; 5,625), Standard ¥139 (orig ¥180; 10,000), Pro ¥499 (orig ¥600; 40,000); Extra bundle ¥100/20,000 Credits. Team Edition per seat: Standard ¥150/mo (25,000 Credits), Pro ¥550 (100,000), Max ¥1,398 (250,000); shared quota pack ¥5,000/625,000 Credits. Works across Claude Code, Cursor, Qwen Code, Codex, Qoder, Qoder CN, OpenClaw. (https://help.aliyun.com/en/model-studio/token-plan-overview)
- **Pay-as-you-go:** standard Model Studio API key (sk-…), billed per token per model. (coding-plan docs, auth docs)
- **Third-party:** bring your own keys (OpenAI/Anthropic/DeepSeek/etc.), costs are those providers'. (auth docs)

### Qwen-Agent
- Framework is free/open source (Apache-2.0). Model usage billed via DashScope API (pay-as-you-go per token) or self-hosted open models (free). No subscription of its own. (README)

### Qoder (qoder.com/pricing, browser-rendered 2026-09-20)
- **Individual plans (international):**
  - Free $0 — 2-week Pro trial with 300 Credits (one per account; not available on VMs), limited completions & Next Edits, BYOK.
  - Pro $20/month — 4,000 Credits, Quest Mode, Repo Wiki, extended chat/agent limits (Sept promo: 2,000 bonus credits first purchase; renewals +1,000).
  - Pro+ $60/month — 6,000 Credits, priority access to upcoming features.
  - Ultra $200/month — 20,000 Credits, early access.
  - Credit Pack add-on: $20 / 1,500 Credits, 1-month validity.
- **Teams plan tier exists** (small/medium teams) and **Enterprise** (custom; SSO, role/group management, cost center, pooled resources, private marketplace, audit, metrics, richer OpenAPI) — enterprise pricing not published on the page ("Contact Sales").
- Usage measured in Credits; unused monthly credits expire; refund only within 24h of subscribing if no credits used. Payments: Visa, Mastercard, Alipay, Google Pay, Apple Pay.
- **China version:** Qoder CN exists (qoder.cn); billing via Alibaba Cloud Model Studio (Coding Plan CN or Token Plan CN). CN pricing of Qoder CN itself: not publicly disclosed in fetched sources (Token Plan/Coding Plan are Alibaba Cloud's own plans).
- **Limited-time offers (2026-09):** Qwen3.8-Flash free; Efficient tier 0.0× for paid users.

---

## Deployment / open source

| Product | Type | License | Repo | Deployment |
|---|---|---|---|---|
| Qwen Code | coding agent CLI | Apache-2.0 | https://github.com/QwenLM/qwen-code | Local CLI (npm `@qwen-code/qwen-code`, Homebrew, or standalone installer script; Node.js ≥22); Desktop app; Web UI via `qwen serve` (experimental); IDE plugins; chat channels. Model calls go to cloud API (or local models). |
| Qwen-Agent | agent framework | Apache-2.0 | https://github.com/QwenLM/Qwen-Agent | Python library (pip); runs locally; connects to DashScope cloud API or self-hosted models (vLLM/Ollama); optional Gradio GUI. |
| Qoder | commercial agentic coding platform | closed-source (not publicly disclosed) | no public source repo; official org https://github.com/QoderAI (SDKs, changelogs, skills) | Desktop app (Qoder IDE / Qoder) for macOS/Windows/Linux; CLI (`curl -fsSL https://qoder.com/install | bash`, binary `qodercli`); JetBrains plugin; mobile & web companions; Cloud Agents run managed in Qoder cloud. Requires Qoder account login (browser or personal access token). |

- Qwen Code desktop app download: https://github.com/QwenLM/qwen-code/releases/tag/desktop-latest (README).
- Qoder CLI login: `/login` in TUI or QODER_PERSONAL_ACCESS_TOKEN env var for CI/CD. (https://www.alibabacloud.com/help/en/model-studio/qoder-agent)

---

## Use cases & limitations

### Use cases
- **Qwen Code:** build features from descriptions; debug/fix issues; navigate/explain codebases; automate lint fixes, merge conflicts, release notes; CI automation (`qwen -p`); pipe-friendly Unix workflows (`tail -f app.log | qwen -p …`); remote agent via chat channels (Telegram/DingTalk/WeChat/Feishu); multi-model Agent Arena comparisons; delegation target via ACP (Qwen Code Claw). (README, overview docs)
- **Qwen-Agent:** custom LLM apps (chatbots w/ tools), PDF reading + image-gen + code execution assistants, browser automation assistant (BrowserQwen), RAG over 1M-token documents, MCP tool use, evaluation via DeepPlanning. (README)
- **Qoder:** delegated end-to-end tasks (new Qoder); IDE coding w/ autocomplete/chat/Quest; terminal coding agent; scheduled automations; enterprise AI coding governance; document/research/browser/desktop tasks (QoderWork); long-running digital roles (QoderWake); cloud agents via API. Customer cases: AMAP/AMAP Automotive (one-shot pass rate 37.3%→61.5% with knowledge engine), Kidswant (400 business scenarios, 300 agents). (docs.qoder.com what-is-qoder.md, customer cases in llms.txt)

### Documented limitations / caveats
- **Qwen Code:** Web UI and daemon (`qwen serve`) marked *experimental* (README). Qwen OAuth free tier discontinued 2026-04-15 (auth docs). Sandbox "reduces but doesn't eliminate all risks"; GUI apps may not work in sandboxes; default Docker sandbox image is intentionally minimal — Java not included by default (sandbox docs). Auto Mode classifier is biased toward blocking; over-broad allow rules disabled in Auto Mode; fail-closed on classifier outage (approval-mode docs). Docs recommend against relying on auto-memory for critical facts ("auto-memory is best-effort, QWEN.md is guaranteed") (memory docs).
- **Qwen-Agent:** "The Docker container-based code interpreter mounts only the specified working directory and implements basic sandbox isolation, but it should still be used with caution in production environments." Python executor in TIR math demo "is not sandboxed and is intended for local testing only, not for production use." GUI requires Python 3.10+. (README)
- **Qoder:** Free plan limited completions; Pro trial one per account, excluded on VMs; unused credits don't roll over; no refunds after 24h/credit use (pricing FAQ). Coding Plan subscription is non-refundable and prohibits non-interactive API use (Alibaba Cloud docs). Coding Plan Pro slots limited, first-come-first-served; Lite plan retired Mar/Apr 2026; Token Plan only in China (Beijing) region (Alibaba Cloud docs).

---

## Conflicts / uncertainty notes

1. **Qoder launch date unknown.** Docs release notes only go back to 2025-08-21 (IDE 0.1.15); earlier public release/announcement date is not stated in any fetched official source. DuckDuckGo's index shows 2026-01-30 attached to qoder.com/qoder (likely page update date, not necessarily launch). Treat "launched mid-2025; new agentic Qoder app announced/rolled out around Jan 2026" as inference, not sourced fact.
2. **Coding Plan vs Token Plan messaging:** The Coding Plan page (intl) still describes Pro $50/mo with "limited availability, restocked daily", while the Token Plan overview says "Coding Plan Pro was a limited-quantity offering and is no longer available once sold out. We recommend Token Plan". Both pages were live 2026-09-20; the transition state is unclear.
3. **Qoder model names (Qwen3.8-Max, Kimi-K3, GLM-5.3 etc.)** come from Qoder's model selector docs, which note "Models … can change by client version and account availability; the selector in the task composer is authoritative." The Qwen3.8/Qwen3.7 family naming in Qoder differs from the qwen3.7-plus/qwen3.5-plus naming in Qwen Code/Alibaba docs — two naming schemes coexist.
4. **"Qoder CN" vs "Qoder":** Alibaba Cloud docs reference both as separate supported tools; qoder.cn serves the China version; CN-specific pricing tiers were not found in fetched official pages (only the shared Alibaba Cloud Token/Coding Plans).
5. **Qoder operating entity:** international site footer lists "BRIGHT ZENITH PRIVATE LIMITED" — the relationship to Alibaba (Qwen team) is not explained on the fetched pages; Qoder is consistently presented under the Alibaba Cloud Model Studio ecosystem and Qwen naming, but the corporate ownership line is not publicly disclosed in the sources checked.
6. **Qwen Code first-release nuance:** GitHub releases start 2025-08-01 (v0.0.1-alpha.14), npm 0.0.1 published 2025-07-22, repo created 2025-06-26. README mentions versions 0.0.14→0.22.0 in evals. All consistent with a July 2025 public debut, but no official "launch date" statement was found.
7. **Qwen Code default model:** no single documented default; docs examples vary (qwen3-coder-plus in settings/auth examples; Qwen 3.7 Max in evals; qwen3.7-plus in Token Plan example). Reported as-is above.
8. **Qoder website stats (40+ connectors, 70+ plugins, 20K+ skills)** are marketing claims from qoder.com/qoder; not independently verifiable from docs.
