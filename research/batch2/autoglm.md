# Zhipu AI (智谱) — AutoGLM, GLM Coding Plan, GLM-PC Research Notes

Fetched: 2026-09-20 (Asia/Shanghai). All facts below come from official sources only (GitHub API / raw READMEs, Hugging Face API, docs.bigmodel.cn, bigmodel.cn, autoglm.z.ai, docs.z.ai, autoglm.zhipuai.cn). Anything not found in these sources is marked "not publicly disclosed".

## Sources used

- `https://api.github.com/search/repositories?q=AutoGLM+in:name&sort=stars&order=desc` — repo discovery
- `https://api.github.com/repos/zai-org/Open-AutoGLM` (via search result) — repo metadata (created_at, license, stars)
- `https://raw.githubusercontent.com/zai-org/Open-AutoGLM/main/README.md` — full Chinese README
- `https://api.github.com/orgs/zai-org/repos?per_page=100&sort=created` — full official org repo list (55 repos; no PC/computer-use repo)
- `https://api.github.com/repos/THUDM/AutoGLM` — 404, repo does not exist (zai-org/AutoGLM also 404)
- `https://api.github.com/search/repositories?q=GLM-PC+OR+autoglm-pc+in:name` — only 3 unrelated third-party repos
- `https://api.github.com/search/repositories?q=org:zai-org+pc&per_page=30` — 0 results
- `https://api.github.com/repos/zai-org/Open-AutoGLM/releases` — `[]` (no GitHub releases)
- `https://api.github.com/repos/zai-org/Synapse` — related repo metadata
- `https://autoglm.z.ai/blog` — official open-source announcement blog (rendered via browser; "AutoGLM Goes Open Source", December 8, 2025)
- `https://huggingface.co/api/models?author=zai-org&limit=200` — full zai-org model list (no GLM-PC; confirms AutoGLM-Phone-9B, SWE-Dev series, WebVIA-Agent)
- `https://huggingface.co/api/models/zai-org/AutoGLM-Phone-9B` — model metadata (license MIT, base model GLM-4.1V-9B-Base, tags)
- `https://huggingface.co/api/models?search=GLM-PC` — no official GLM-PC model
- `https://bigmodel.cn/glm-coding` — GLM Coding Plan landing page (JS SPA; rendered via browser, incl. team-plan tab `?plantype=team`)
- `https://docs.bigmodel.cn/llms.txt` — BigModel docs index (no AutoGLM/computer-use page; Coding Plan + Managed Agents sections)
- `https://docs.bigmodel.cn/cn/coding-plan/overview.md` — Coding Plan quotas, credit math, models, tools
- `https://docs.bigmodel.cn/cn/guide/start/pricing.md` — CN API pay-as-you-go pricing
- `https://docs.bigmodel.cn/cn/guide/start/model-overview.md` — model catalog incl. AutoGLM-Phone
- `https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md` — AutoGLM-Phone API model page
- `https://docs.bigmodel.cn/cn/api/introduction` — API endpoint confirmation
- `https://docs.z.ai/llms.txt` — Z.AI international docs index (no computer-use agent)
- `https://docs.z.ai/devpack/overview.md` — international Coding Plan ("from 18 USD/month")
- `https://docs.z.ai/guides/overview/pricing.md` — international USD API pricing
- `https://raw.githubusercontent.com/zai-org/GLM-5/main/README.md` — GLM-5/5.1/5.2/5.3 model facts
- `https://autoglm.zhipuai.cn/autotyper/` — consumer "智谱AI输入法" (AutoTyper) product page

---

## Product facts

### 1. AutoGLM — phone-use autonomous agent (open source)

- **Official repo**: `zai-org/Open-AutoGLM` — description: "An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone". URL: https://github.com/zai-org/Open-AutoGLM (source: GitHub search API, fetched 2026-09-20).
- **agent_type**: phone agent (phone-use agent). Controls Android phones via ADB, HarmonyOS NEXT devices via HDC, and iOS via WebDriverAgent (iOS config in `docs/ios_setup/ios_setup.md`).
- **Repo metadata** (GitHub API, 2026-09-20): created **2025-12-08T09:23:44Z**; last push 2026-03-06; language Python; topics `agent`, `phone-use-agent`; 26,266 stars; 4,032 forks; 261 open issues; homepage https://autoglm.z.ai/blog; no GitHub releases.
- **Timeline** (from official blog "AutoGLM Goes Open Source", autoglm.z.ai/blog, dated December 8, 2025):
  - Project started **April 2023** (32 months of development before open source).
  - **October 25, 2024**: first AutoGLM capable of stably completing a full operation chain on a real device — "regarded by the industry as the world's first AI Agent with true Phone Use capabilities".
  - **November 2024**: first AI-automated WeChat "Red Packet" (digital cash gift) sent by seeing the screen and clicking through the banking UI.
  - **2025**: AutoGLM 2.0 — moved to cloud virtual phones ("a safer sandbox"; every action replayable/auditable/intervenable; sensitive data isolated); validated RL scaling via **MobileRL, ComputerRL, AgentRL** algorithms.
  - **December 8, 2025**: open sourced (models + code + demos for 50+ Chinese apps).
- **Research papers cited in README**: "AutoGLM: Autonomous Foundation Agents for GUIs" (arXiv:2411.00820, 2024) and "MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents" (arXiv:2509.18119, 2025).
- **Commercial deployments mentioned in official sources**: AutoGLM 2.0 cloud phone product; 智谱 AI 输入法 (AutoTyper) voice-input product (https://autoglm.zhipuai.cn/autotyper/, "用嘴发指令"); AutoGLM-Phone API on BigModel.
- THUDM/AutoGLM and zai-org/AutoGLM repos **do not exist** (404) — the public repo is Open-AutoGLM.

### 2. GLM Coding Plan — Zhipu coding-agent subscription

- **Official page**: https://bigmodel.cn/glm-coding (bigmodel.cn, fetched via browser 2026-09-20). Positioning: "你的全能搭档，搞定复杂工作与编码" / "告别多工具订阅，一个套餐，畅用多种 Agent 工具" (one subscription covering multiple agent tools).
- **agent_type**: coding agent subscription (brings GLM models to third-party coding agents + Zhipu's own ZCode client).
- **Officially listed tools** (landing page): ZCode (Zhipu's own coding client), AutoClaw (Zhipu office agent), Claude Code, Codex, WorkBuddy, TraeWork, CodeBuddy, TraeCode, OpenCode, Cursor, OpenClaw — plus "支持 ZCode、Claude Code 等 20+ 编程工具". Docs overview also names Claude Code, Kilo Code, OpenClaw, OpenCode, TRAE, CodeBuddy.
  - Note: OpenClaw is supported but with "次级调度与尽力交付策略" (secondary scheduling / best-effort; coding-agent tasks have preemption priority; high load triggers queueing/rate limits) (docs.bigmodel.cn/cn/coding-plan/overview).
- **Launch date**: not publicly disclosed in fetched sources. Reference point: plan revision dated **2026-07-30** ("老用户权益说明", docs.bigmodel.cn/cn/coding-plan/notice/usage-revision).
- International counterpart: "GLM Coding Plan" on Z.AI, "Plans from $18/month" (docs.z.ai/llms.txt description; docs.z.ai/devpack/overview).

### 3. GLM-PC / computer-use agent — NOT FOUND in official public sources

- No official product, repo, or model named GLM-PC or computer-use was found as of 2026-09-20:
  - zai-org GitHub org (all 55 public repos listed): no PC/computer-use repo. Repos include research agents (CogAgent, Vision2Web, WebVIA-Agent model) but no desktop computer-use product.
  - zai-org Hugging Face org (all models listed): no GLM-PC / computer-use model. AutoGLM-Phone-9B is phone-only.
  - docs.bigmodel.cn/llms.txt and docs.z.ai/llms.txt: no computer-use pages (Z.AI "Agents" pages are Slide/Poster, Translation, Video Template only).
  - GitHub search "GLM-PC OR autoglm-pc in:name": only unrelated third-party repos.
- **Closest official evidence of computer-use work**: the AutoGLM open-source blog states that in 2025 AutoGLM 2.0 validated "MobileRL, ComputerRL, and AgentRL" RL algorithms — i.e., a ComputerRL (computer-use) training algorithm exists internally, but no public computer-use agent product is disclosed.
- Conclusion: **GLM-PC as a public product = not publicly disclosed / no official public release found**.

---

## Features & capabilities

### AutoGLM (Open-AutoGLM)
- Multimodal screen understanding: screenshot → VLM understands UI → plans next action → executes via ADB/HDC → loop.
- **Actions** (10): `Launch`, `Tap`, `Type`, `Swipe`, `Back`, `Home`, `Long Press`, `Double Tap`, `Wait`, `Take_over` (human takeover for login/captcha).
- **Safety mechanisms**: sensitive-operation confirmation callback (`confirmation_callback`); human takeover callback (`takeover_callback`); automatic takeover on sensitive pages — "截图失败(黑屏)… 应用正在显示敏感页面(支付、密码、银行类应用)。Agent 会自动检测并请求人工接管" (screenshots fail/black on payment/password/bank pages; agent auto-detects and requests human takeover). Project restricted to "研究和学习使用" (research/learning), with usage terms (`resources/privacy_policy.txt`).
- **Planning**: model outputs `<think>…</think>` chain-of-thought + structured `<answer>do(action=…)</answer>` actions; natural-language command decomposed into stable, replayable operation sequences (blog).
- **Apps supported**: 50+ mainstream Chinese apps on Android (WeChat, QQ, Taobao, JD, Pinduoduo, Meituan, Ele.me, Ctrip, 12306, bilibili, Douyin, iQiyi, NetEase Music, Xiaohongshu, Zhihu, Douban, Amap, Baidu Maps…); 60+ HarmonyOS native/system apps.
- **Connectivity**: local USB ADB; remote ADB over WiFi/network (`adb connect IP:5555`); HDC for HarmonyOS; multi-device via `--device-id`.
- **Config**: `PHONE_AGENT_MAX_STEPS` default 100 steps/task; `--lang cn|en` system prompts; ModelConfig (temperature 0.1, freq penalty 0.2, max_tokens 3000 defaults); Python API (`PhoneAgent`) and CLI; Midscene.js integration for iOS/Android; examples dir (basic usage, single-step debug, batch tasks, custom callbacks).
- **Memory**: no persistent-memory feature documented in the README — not publicly disclosed (none mentioned).
- **iOS**: via WebDriverAgent (separate setup doc in repo).
- Text input on Android requires ADB Keyboard app.

### GLM Coding Plan
- **Positioning**: covers requirement understanding, code generation, debugging/repair, codebase Q&A, automated task handling ("需求理解、代码生成、调试修复、代码库问答与自动化任务处理", docs overview).
- **1M context** for long tasks: "一次任务即可完成'从需求到多端可部署产物'的完整开发链路" (landing page).
- **Planning/engineering**: "引领开发模式从 Vibe Coding 迈向 Agentic Engineering，构建'规划-实现-迭代'的工程闭环"; claims coding open-source SOTA; 50% coding improvement vs previous gen (GLM-5.3); 10,000+ verifiable task environments across 9 programming languages (landing page).
- **Included MCP tools**: visual understanding MCP, web search MCP, web reader MCP, open-source repo (Zread) MCP; GLM in Excel (Beta) perk.
- **Official clients**: ZCode (coding software; subscribers get 150% quota, free idle-time tasks, professional data MCP); AutoClaw (office/work agent for CoWork: deep research, business data analysis, brainstorming, task automation; 150% quota for subscribers).
- **Team features**: seat management, team usage/effectiveness dashboards, IP whitelist, "数据默认不用于模型训练" (data not used for model training by default), centralized billing/invoices, max 5 API keys per seat, 1 seat = 1 member (no sharing; sharing triggers risk control).
- **Night campaign (limited time)**: 23:00–09:00 daily, GLM-5.3-Flash unlimited via ZCode + doubled quota in other agents.
- **Limits**: per-5-hour quota + weekly quota; when exhausted, wait for refresh (system does not bill other resource packs); plan quota usable only in officially supported tools (not for self-built apps/SaaS — those need standard API).
- **Coding-plan docs for learning**: "Coding Agent 工作原理", "Agentic 扩展组件", "记忆机制" (memory mechanism doc exists for coding agents), "最佳实践".

---

## Underlying models

### AutoGLM
- **AutoGLM-Phone-9B** (Chinese apps optimized) and **AutoGLM-Phone-9B-Multilingual** (English scenarios): Hugging Face `zai-org/AutoGLM-Phone-9B` (+ Multilingual), ModelScope `ZhipuAI/AutoGLM-Phone-9B` (README model table).
- Architecture: same structure as **GLM-4.1V-9B-Thinking** (README); HF tags: base_model = `zai-org/GLM-4.1V-9B-Base`, arch `Glm4vForConditionalGeneration`, pipeline image-text-to-text.
- Cloud API: BigModel model id **`autoglm-phone`** (endpoint `https://open.bigmodel.cn/api/paas/v4`), 20K context, max output 2048, language 中文, Android phones (docs model page). Also callable via ModelScope inference (`ZhipuAI/AutoGLM-Phone-9B`).
- Local serving: vLLM or SGLang; README's AI deployment guide recommends NVIDIA GPU 24GB+ VRAM and ~20GB model files for local deployment.

### GLM flagship series (context for Coding Plan)
- GLM-5: 744B params / 40B active (vs GLM-4.5's 355B/32B), 28.5T tokens pretraining, DeepSeek Sparse Attention (DSA) — purpose-built for complex systems engineering and long-horizon agentic tasks (zai-org/GLM-5 README).
- GLM-5.1: agentic engineering flagship; SWE-Bench Pro SOTA; sustains optimization over hundreds of rounds/thousands of tool calls.
- GLM-5.2: 1M-token context; IndexShare architecture; Terminal-Bench 2.1 = 81.0; SWE-bench Pro 62.1.
- GLM-5.3 & GLM-5.3-Flash: GLM-5.3 uses same base as 5.2, all gains from post-training; "+50% over GLM-5.2 on in-house Z.ai Code Bench"; open-source SOTA on Terminal Bench 3.0 / Agents' Last Exam; emergent cyber capability (CyberGym). GLM-5.3-Flash: new base, hybrid sparse+linear attention, Manifold-Constrained Hyper-Connections (mHC), 320B-A18B, FP8; internal beta codename **"OX Alpha"** (bigmodel.cn FAQ: "OX Alpha 是 GLM-5.3-Flash 在内测阶段使用的内部代号").
- **Coding Plan runs on**: GLM-5.3 and GLM-5.3-Flash for all plans; legacy requests auto-routed (GLM-5.2/GLM-5.1 → GLM-5.3; GLM-5-Turbo/GLM-4.7 → GLM-5.3-Flash) (docs coding-plan overview).

---

## Pricing

### GLM Coding Plan — China (bigmodel.cn/glm-coding, 2026-09-20)
Personal plans (list price / 连续包季 8折 shown on page; 连续包年 7折 also offered):
| Tier | List price | Quarterly (8折) | 5h credits | Weekly credits |
|---|---|---|---|---|
| Lite (日常使用) | ¥118/月 | ¥94.4/月 | 2,000 | 10,000 |
| Pro (高频使用, 最受欢迎) | ¥538/月 | ¥430.4/月 | 12,000 | 60,000 (6× Lite) |
| Max (深度使用) | ¥1078/月 | ¥862.4/月 | 28,000 | 140,000 (14× Lite) |

Team plans (per seat):
| Tier | Price | Weekly credits | Notes |
|---|---|---|---|
| 标准席位 (高频使用) | ¥598/月, 年付9折 → ¥538.2/月 | 66,000 | seat/permission mgmt, dashboards, overage pay-as-you-go + budget control, IP whitelist, centralized billing, no training on data |
| 高级席位 (深度使用) | ¥1198/月, 年付9折 → ¥1078.2/月 | 155,000 | standard benefits + first access to latest flagship models/features + peak-hour dedicated resource priority |

Credit mechanics (docs overview): model credits = (input×6.9 + cached×1.7 + output×24)/10,000 for GLM-5.3; Flash multipliers 2.3/0.56/8; MCP tools 1.2 credits/call. Off-peak = 50% credit rate; peak = Mon–Fri 14:00–18:00 (UTC+8). 5-hour credits refresh dynamically 5h after consumption; weekly credits refresh every 7 days from subscription. Estimated weekly tokens (GLM-5.3, 95–98% cache hit): Lite 48–104M; Pro 290–627M; Max 676–1,463M. "最高可节省 92% 成本" vs pay-as-you-go GLM-5.3 when using off-peak.

International: **from $18/month** (docs.z.ai; Lite/Pro/Max with same credit scheme 2,000/12,000/28,000 per 5h and 10,000/60,000/140,000 weekly).

### API pay-as-you-go (BigModel, docs.bigmodel.cn/cn/guide/start/pricing.md, ¥/million tokens)
- GLM-5.3: input 8 / output 28 (1M ctx); GLM-5.3-Flash: 0.8 / 2.8 (1M, multimodal); GLM-5.3-FlashX: 2 / 7.
- GLM-5.2: 8 / 28; GLM-5.1: 6 / 24 (<32K) or 8 / 28 (≥32K); GLM-5-Turbo 5/22–7/26; GLM-5: 4/18–6/22.
- AutoGLM-Phone API: **not listed in the pricing table**; the model page states "新模型上线，限时免费！" (new model, limited-time free).
- Batch API = 50% of standard for supported models.

### Z.AI international API (docs.z.ai/guides/overview/pricing.md, USD/million tokens)
- GLM-5.3: $1.4 / $4.4; GLM-5.3-Flash: $0.15 / $0.50; GLM-5.3-FlashX: $0.37 / $1.25; GLM-5.2: $1.4 / $4.4; GLM-5.1: $1.4 / $4.4; GLM-5: $1 / $3.2.

---

## Deployment / open source

### AutoGLM (Open-AutoGLM)
- **License**: code **Apache-2.0** (repo license field); models **MIT** (blog: "The models are released under the MIT License, and all code is under the Apache-2.0 License"; HF cardData license: mit).
- **Repo URL**: https://github.com/zai-org/Open-AutoGLM ; models: https://huggingface.co/zai-org/AutoGLM-Phone-9B , https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual , https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B .
- **Deployment options** (README): (A) third-party hosted inference — BigModel API (`autoglm-phone`) or ModelScope inference; (B) self-host — vLLM 0.12.0 or SGLang v0.5.6.post1 with exact launch params (e.g., `--mm-processor-kwargs {"max_pixels":5000000}`, context 25480), OpenAI-compatible `/v1` endpoint; recommended NVIDIA GPU 24GB+.
- Local vs cloud: the open framework runs locally on user's computer controlling a physical phone; AutoGLM 2.0 commercial product runs agents in **cloud virtual phones** (blog).
- Ecosystem: Midscene.js adaptation for AutoGLM; WeChat community; "AutoGLM 实战派" developer incentive campaign with cash prizes; deployment guide designed for AI assistants (e.g., Claude Code via GLM Coding Plan) to install it.
- Related open source: `zai-org/GLM-V` (deployment guide for GLM-V models), `zai-org/Synapse` ("Self-hosted AI workspace with shareable AI teammates, shared conversations, memory, and governed access to plugins, MCP tools, and local devices").

### GLM Coding Plan
- Cloud subscription; requires configuring dedicated Coding endpoint (not the standard API endpoint) in supported tools (docs coding-plan quick start / api introduction warning).
- Plan quota is independent from standard API balance; only valid inside officially supported coding tools/products; OpenClaw supported at secondary priority.
- Enterprise: IP whitelist, data not used for training by default.

---

## Use cases & limitations

### AutoGLM use cases (docs model page "推荐场景")
- Food delivery ordering ("在淘宝上的闪购帮我查找库迪咖啡的经典拿铁并下单"; "用美团再点一单最近的外卖"); product purchase & price comparison ("对比一下32K显示器哪个购物平台便宜，找一个最便宜的下单"); travel (route planning, flights/train tickets, hotels); news/media (search/play songs, audiobooks, like/comment on bilibili); house rental search; WeChat red packet (blog); cloud-phone batch operations: notifications/likes/comments, sales/customer-service/attendance workflows (blog).
- Business scenarios per blog: sales, customer service, attendance workflows; AI-native phone building; research on GUI agents.

### AutoGLM limitations (README/FAQ + blog)
- Research/learning use only; prohibited for illegal information gathering or unlawful activities.
- Sensitive pages (payment, password, banking) cannot be screenshotted — agent auto-detects and requires human takeover.
- Android 7.0+ device with developer mode + USB debugging (some devices also need "USB 调试(安全设置)") required; ADB Keyboard required for Android text input; data-capable USB cable needed.
- "The current AutoGLM is not a perfect answer. It hasn't seen all the phones and apps in the real world yet" (blog).
- iOS support requires WebDriverAgent configuration (extra setup).
- Local deployment needs ~24GB+ VRAM GPU.

### GLM Coding Plan limitations
- Quota caps (5-hour + weekly) with refresh waiting; no spillover billing to other balances.
- Usable only in officially supported tools (not for self-built apps/websites/SaaS — must use standard API).
- Team: no mixed standard+advanced purchase; no standard→advanced upgrade (both "暂未上线"); 1 seat per member; 5 API keys per seat.
- Peak-hour limits (Mon–Fri 14:00–18:00) cost 2× credits; OpenClaw tasks deprioritized vs coding-agent tasks under load.

---

## Conflicts / uncertainty notes

1. **AutoGLM base model**: README says "该模型结构与 GLM-4.1V-9B-Thinking 相同" (same architecture as GLM-4.1V-9B-Thinking), while HF metadata tags base_model = `zai-org/GLM-4.1V-9B-Base`. Both are official statements; treat "GLM-4.1V-9B family" as the underlying base and note the discrepancy.
2. **AutoGLM-Phone API price**: model doc says limited-time free; the standard pricing table has no entry. Actual paid price after the promotion is not publicly disclosed.
3. **Coding Plan launch date**: not stated in fetched sources; only the 2026-07-30 plan revision is dated.
4. **Lite annual price**: landing page displays ¥94.4/月 (quarterly 8折) and offers 连续包年 7折 (would be ¥82.6, not shown). Only displayed values are recorded here.
5. **GLM-PC / computer-use**: could not be confirmed to exist publicly; only "ComputerRL" (training algorithm, mentioned in AutoGLM blog) indicates internal computer-use research. Status should be "not publicly disclosed" until an official release appears.
6. **Tool list for Coding Plan**: landing page lists 11 named tools incl. Cursor/Codex/OpenClaw; docs list a slightly different set (Claude Code, Kilo Code, Cline, OpenCode, TRAE, CodeBuddy, OpenClaw). Both official; exact supported-tool registry is in docs (tool/others page, not fully fetched).
7. **GLM-5.3 release date**: HF model page createdAt = 2026-08-25 (used here); blog date not fetched.
8. Open-AutoGLM repo shows last push 2026-03-06 but the README top banner promotes an ongoing developer incentive campaign — repo activity vs campaign timing unverified beyond fetched data.
