# MiniMax Agent / MiniMax Code research (fetched 2026-09-20)

## Sources used
- https://agent.minimax.io/ (homepage, rendered in browser; web app at /home, /max-claw, /max-hermes)
- https://agent.minimax.io/docs/llms.txt (docs index)
- https://agent.minimax.io/docs/code/welcome.md
- https://agent.minimax.io/docs/code/get-started/download.md
- https://agent.minimax.io/docs/code/account/usage.md
- https://agent.minimax.io/docs/code/help/faq.md
- https://agent.minimax.io/docs/cli/quick-start.md
- https://agent.minimax.io/docs/cli/features.md
- https://agent.minimax.io/docs/cli/configuration.md
- https://agent.minimax.io/docs/cli/security.md
- https://github.com/MiniMax-AI/minimax-code (README + GitHub API)
- https://github.com/MiniMax-AI (org repos via GitHub API)
- https://www.minimax.io/ (corporate site)
- https://platform.minimax.io/docs/llms.txt, /docs/guides/pricing-token-plan, /docs/guides/models-intro.md, /docs/guides/text-m2-agent-generalization.md, /docs/token-plan/hermes-agent.md

## Product facts (MiniMax Agent)
- "MiniMax Agent" is the brand/name of the agent product surface at agent.minimax.io; page title: "MiniMax Agent: Minimize Effort, Maximize Intelligence" (https://agent.minimax.io/).
- It is a web app ("The All-New MiniMax for Web" update) positioned as "MiniMax Agent, making work easier" (https://agent.minimax.io/home, rendered).
- Web-app capability chips: Skills, Schedules, Websites, Research, AI PPT; "Expert Collection" areas: Office, Finance, Coding (https://agent.minimax.io/home).
- Advertised M3-update features: persistent memory ("your Agent remembers what you've shared"), evolving skills ("turns complex tasks into skills made just for you"), unified billing integrated with Token Plan (in-app update modal, https://agent.minimax.io/).
- Two cloud agent products on the platform:
  - **MaxClaw**: "Your 24/7 personal assistant." Cloud-hosted, always-on ("Live in 10 seconds, running 24/7 in the cloud"), accessible in daily apps incl. Telegram (https://agent.minimax.io/max-claw).
  - **MaxHermes** (Beta): "An Agent That Grows With You." Self-evolution — "each completion of a complex task unlocks a brand-new skill"; always-on 24/7 cloud; accessible in daily apps (https://agent.minimax.io/max-hermes).
- First release date: `not publicly disclosed` in fetched sources. No dated announcement page found; the M3/"All-New MiniMax for Web" update is undated in the fetched modal.

## Product facts (MiniMax Code)
- Official description: "MiniMax Code is a desktop AI Agent app for software development, everyday workflows, automation, and remote collaboration" (https://agent.minimax.io/docs/code/welcome.md).
- Desktop app: macOS (macOS 12 Monterey+; arm64/x64 builds) and Windows (Windows 10+) only. Global download at agent.minimax.io/download; China download at agent.minimaxi.com/download (https://agent.minimax.io/docs/code/get-started/download.md).
- Desktop features: Coding mode and Work mode, workspace/project context, built-in browser (preview/debug HTML), Files/Changes/Terminal panels, Infinite Canvas (organize image/video assets), Goal (verifiable outcome, agent works until done/blocked), Agent Team (multi-agent decomposition/collaboration/verification), Custom Agents, Custom Mini Apps, plugin marketplace, MCP servers, memory (preferences/project conventions), scheduled tasks, Remote Control from phone, messaging integrations (Telegram, WeChat, Lark, Feishu), code review command, H3 Max video generation (https://agent.minimax.io/docs/llms.txt index).
- CLI "mcode" (MiniMax Code CLI): terminal coding agent; three entry points — interactive TUI (`mcode`), headless (`mcode exec`, output text/json/stream-json), and ACP server (`mcode acp`) for editors/clients (https://agent.minimax.io/docs/cli/quick-start.md).
- CLI features: read/edit files, run shell commands and tests, inspect diffs, permission modes (Ask/Auto/Full access/Off; headless: smart/full/off), Plan Mode, sessions (create/search/resume/fork/rewind/compact/export), goals with token budgets, side conversations (`/btw`, since 0.3.2), subagents, plugins (official/local marketplace), skills, MCP (`/mcp`), built-in web search tool (since 0.4.5), mcode-tools media tools, clipboard image/video paste, AGENTS.md project rules via `mcode init .`, context-window status display (e.g. "Context 1M") since 0.4.12 (https://agent.minimax.io/docs/cli/features.md, /docs/cli/configuration.md).
- Latest published npm version referenced in README: `@minimax-ai/code@0.4.12`; source preview targets 0.4.12 (https://github.com/MiniMax-AI/minimax-code).
- Install: one-command installer `curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash` (no sudo) or `npm install -g @minimax-ai/code`; requires Node.js 22.19+ (22.x), 24, 25, or 26; Alpine/musl not supported by the installer (README + quick-start).
- Accounts: mainland China (`mcode login`) vs Global (`mcode login --region global`).
- Corporate site lists MiniMax Code among products "MiniMax Code, MiniMax Design, MiniMax Audio, Talkie" (https://www.minimax.io/).
- First release date: repo created and first commit 2026-06-01 (GitHub API); same date the MiniMax-M3 repo was created. No official launch-date statement fetched.

## Features & capabilities
- **Editor integration**: ACP (Agent Client Protocol) stdio server for editors/Agent hosts; no native VS Code/JetBrains plugin confirmed in fetched docs (https://agent.minimax.io/docs/cli/features.md).
- **Sandboxing**: README states permissions and sandboxing control tool execution ("control tool execution with permissions and sandboxing"); permission modes documented; no OS-level sandbox engine named in fetched pages (https://github.com/MiniMax-AI/minimax-code, /docs/cli/security.md).
- **Git operations**: handled via shell-command execution (run commands, inspect diffs); no dedicated git tool documented (https://agent.minimax.io/docs/cli/features.md).
- **MCP support**: yes — `/mcp` in CLI, MCP Servers page in desktop docs; official MiniMax MCP servers exist (see below) (https://agent.minimax.io/docs/code/agents/mcp.md, /docs/cli/configuration.md).
- **Browser use / computer use**: desktop-host capabilities only; explicitly NOT automatically available in the CLI ("Browser and Computer Use are desktop-host capabilities and are not automatically available in the CLI") (https://agent.minimax.io/docs/cli/security.md, /docs/cli/features.md).
- **Memory**: desktop "Memory" feature retains preferences, project conventions, long-term working patterns; web M3 update advertises Persistent Memory (llms.txt; in-app modal).
- **Planning**: Plan Mode (Shift+Tab), goals with budgets; Agent Team multi-agent workflows (features.md; llms.txt).
- **Multi-agent**: subagents (CLI), Agent Team, Custom Agents (desktop), MaxHermes/MaxClaw cloud agents (features.md; llms.txt; web app).

## Underlying models
- Current MiniMax language lineup (https://platform.minimax.io/docs/guides/models-intro.md):
  - **MiniMax-M3**: "Frontier multimodal coding model with 1M context window"; docs call it "an Agentic Model with exceptional Tool Use capabilities"; supports interleaved thinking (models-intro.md; llms.txt text-m3-function-call.md).
  - **MiniMax-M2.7**: "Beginning the journey of recursive self-improvement"; "top real-world engineering" (plus M2.7-highspeed variant).
  - Legacy: M2.5 (code gen/refactoring), M2.1 (230B total / 10B activated, code-optimized), M2 (200k context, 128k max output incl. CoT; "agentic capabilities, function calling, advanced reasoning").
- Model repo creation dates (GitHub API): MiniMax-M2 2025-10-25 ("built for Max coding & agentic workflows"), M2.1 2025-12-22, M2.5 2026-02-13, M2.7 2026-04-09, M3 2026-06-01.
- MiniMax Code CLI default model: not pinned in docs — config uses `defaultModel: provider/model` with `minimaxModelSource: token_plan` or `minimax_api_key` (https://agent.minimax.io/docs/cli/configuration.md). Token Plan docs consistently say "latest MiniMax M-series models" for coding integrations; Hermes setup guide selects MiniMax-M3 (https://platform.minimax.io/docs/token-plan/hermes-agent.md).
- Web app model selector showed "MiniMax-M2.7" as the active model chip with MiniMax-M3 available (https://agent.minimax.io/home, rendered).
- M2 agent design: "Interleaved Thinking" — thinking can occur at any point during a task; context is the agent's memory; keep full session history including thinking steps (https://platform.minimax.io/docs/guides/text-m2-agent-generalization.md).

## Pricing
- MiniMax has two pricing categories: API Pricing (pay-as-you-go per token/call, "for enterprises") and Subscription Plans (fixed monthly quotas, "for individuals and small teams"); plus Audio Subscription and Video Packages (https://platform.minimax.io/docs/pricing/overview).
- **Token Plan** (official figures, https://platform.minimax.io/docs/guides/pricing-token-plan):
  - Plus: **$22/month** — "Personal projects and prototyping" — 3-4 agents.
  - Max: **$55/month** — "Daily coding with agents and multimodal work" — 4-5 agents.
  - Ultra: **$132/month** — "Heavy Agent workflows and extended sessions" — 6-7 agents.
  - Quota windows: 5-hour rolling and weekly windows; covers full MiniMax lineup (M3/M2.7/image/speech); excludes special models (MiniMax H3, voice design, rapid voice cloning).
  - Credits packages: **1,000 credits = $1**; $5→5,000, $25→25,000, $100→100,000; validity 365 days. Token Plan quota used first, credits cover overflow.
- MiniMax Code in-app usage page: daily check-in earns 400 points; day 4 and day 7 award 1,000 points each; full week = 4,000 points; points valid 30 days; usable for office work, Coding, deep research, database calls, multimodal creation (https://agent.minimax.io/docs/code/account/usage.md).
- Free tier: `not publicly disclosed` — no free plan listed on the pricing pages fetched; check-in points act as free credits.
- Agent/Coding-specific pricing beyond Token Plan: web-app plan/pricing page requires sign-in; exact web-agent prices `not publicly disclosed` from fetched sources.

## Deployment / open source
- **MiniMax Code CLI**: open source, MIT license (first-party code; existing file/package licenses remain), GitHub https://github.com/MiniMax-AI/minimax-code — TypeScript, created 2026-06-01, ~1,408 stars / 153 forks as fetched via API. Published npm package @minimax-ai/code. No git tags/releases found. PRs currently accepted only from repo collaborators.
- **MiniMax Code desktop app**: proprietary (source not published; repo only hosts issue tracking for it).
- **MiniMax Agent / MaxHermes / MaxClaw**: cloud-hosted web/app agents, always-on 24/7; no self-host option documented.
- **BYOK / custom providers**: CLI and desktop support custom OpenAI- or Anthropic-compatible endpoints incl. self-hosted (config.yaml `custom_provider`; `minimax_api` reserved for official API) (README; configuration.md).
- **Open models self-hosting**: platform docs offer "Run and self-host MiniMax Open Models" for MiniMax-M3, M2.7, Music 3, H3 via SGLang cookbook (https://platform.minimax.io/docs/guides/local-deploy.md).
- Related open repos (GitHub API, 2026-09-20): MiniMax-AI/cli ("mmx-cli", 2,157 stars, created 2026-03-25, no license listed; "one prompt to bring MiniMax into your AI agent"); MSA (Python SDK, 422 stars, created 2026-06-11, MIT, no description); MiniMax-Code-Plugins (community plugin registry, created 2026-08-17, Apache-2.0, 17 stars); MiniMax-Code-MiniApps (created 2026-09-20).

## API availability
- MiniMax API is Anthropic- and OpenAI-compatible: call MiniMax models via **Anthropic SDK**, **OpenAI SDK**, and **AI SDK** (https://platform.minimax.io/docs/api-reference/text-anthropic-api.md, text-openai-api.md, text-ai-sdk.md); quickstart uses the Anthropic SDK with MiniMax-M3 (quickstart-sdk.md).
- MCP servers (official GitHub org): **MiniMax-MCP** (Python, 1,585 stars; TTS/image gen/video gen), **MiniMax-MCP-JS** (TypeScript, 130 stars), **MiniMax-Coding-Plan-MCP** (Python, 102 stars; "AI-powered search and vision analysis APIs optimized for code development workflows", created 2025-11-20), minimax_search MCP server (57 stars). Token Plan MCP exposes web_search and understand_image tools (https://platform.minimax.io/docs/guides/token-plan-mcp-guide.md).
- Video Agent API: create/query video Agent tasks (https://platform.minimax.io/docs/api-reference/video-agent-create.md).
- Documented third-party agent integrations under Token Plan: Claude Code, Codex, Hermes Agent (Nous Research), Pi, OpenClaw, via `npx -y mmx-cli@latest agent setup` wizard (https://platform.minimax.io/docs/token-plan/… pages).

## Use cases & limitations
- Official use cases: repository/CI coding tasks, everyday office workflows, scheduled automation, remote collaboration via phone/messaging, multimodal creation (documents, PPT, images, audio, video via H3 Max), deep research, websites (docs welcome.md, llms.txt; usage.md).
- Documented limitations: CLI has no Browser/Computer Use (desktop-only); desktop app is macOS/Windows only (no Linux); installer doesn't support Alpine/musl; headless mode can't use "ask" permission mode; install scripts have no uninstall flag; external PRs only from collaborators; Token Plan excludes H3 and some speech special models; GitHub repo has no release tags.

## Conflicts / uncertainty notes
- Branding overlap: "MiniMax Agent" (web product title) vs "MiniMax Code" (desktop+CLI). The agent.minimax.io site serves both; docs only cover "MiniMax Code". The web app and desktop share cloud conversation handoff. Relationship is not explained in a single fetched doc — treat as an ecosystem of surfaces rather than two fully separate products.
- Launch dates: only GitHub repo creation dates are available (minimax-code: 2026-06-01; cli: 2026-03-25). No official press-release dates fetched — minimax.io/news is JS-rendered and web_search/tavily were unavailable this session.
- Default model of MiniMax Code CLI is not documented; web app defaulted to M2.7 in the rendered UI. Avoid asserting a fixed default model.
- GitHub star counts vary slightly between API (1,408) and org HTML page (1,403) — both fetched 2026-09-20.
- MiniMax-Coding-Plan-MCP and "Coding Plan" refer to a Token-Plan-related MCP offering; "Coding Plan" itself as a product is not defined in fetched docs.
- Web-app plan/pricing details (beyond Token Plan) require sign-in and were not retrievable.
