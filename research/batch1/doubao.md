# Doubao research (fetched 2026-09-20)

## Sources used

1. https://docs.volcengine.com/docs/ark?lang=zh — Ark (火山方舟) docs home (fetched 2026-09-20)
2. https://docs.volcengine.com/docs/ark/model-list?lang=zh — official Ark model list (fetched 2026-09-20)
3. https://docs.volcengine.com/docs/ark/model-pricing?lang=zh — official Ark model pricing (fetched 2026-09-20)
4. https://docs.volcengine.com/docs/ark/product-overview?lang=zh — product overview w/ base URL & auth (fetched 2026-09-20)
5. https://docs.volcengine.com/docs/ark/responses-api-text-generation?lang=zh — Responses API reference (fetched 2026-09-20)
6. https://docs.volcengine.com/docs/ark/chat-api?lang=zh — Chat API reference (fetched 2026-09-20)
7. https://docs.volcengine.com/docs/82379/1159178?lang=zh (redirects to /docs/ark/model-release-announcement) — model release announcements (fetched 2026-09-20)
8. https://github.com/ByteDance-Seed — Seed team GitHub org (via GitHub API, fetched 2026-09-20)
9. https://seed.bytedance.com/ and https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity — Seed 2.1 official release blog, dated 2026-06-23 (fetched 2026-09-20)
10. https://www.doubao.com/ — consumer app site (fetched 2026-09-20)

Note: tavily_search / tavily_extract were out of quota; web_search disabled. All data above came from direct fetches of official pages.

## Company facts

- **Provider**: ByteDance (字节跳动) — listed as the provider (提供方) of the doubao-seed model family on Ark's official model release announcement page [7].
- **API platform**: Volcengine Ark (火山方舟), operated by Beijing Volcano Engine Technology Co., Ltd. (北京火山引擎科技有限公司), ByteDance's cloud arm. Address listed in official footer: 北京市海淀区北三环西路甲18号院大钟寺广场1号楼 [4].
- **Consumer app**: Doubao (豆包), https://www.doubao.com/ — "AI chat/QA assistant; writing, copywriting, translation, programming tools"; official meta description notes Seedance 2.0 video generation is integrated and free with login [10].
- **Docs**: https://docs.volcengine.com/docs/ark (Ark docs, Chinese). Console: https://ark.volcengine.com (region: cn-beijing).
- **Seed team**: GitHub org https://github.com/ByteDance-Seed (created 2025-03-12, 63 public repos, ~3,126 followers); blog https://seed.bytedance.com/; contact seed.feedback@bytedance.com [8]. Notable public repos (GitHub API, 2026-09-20): VeOmni (2,214 stars, "Scaling Any Modality Model Training with Model-Centric Distributed Recipe"), Triton-distributed (1,546 stars) [8]. Seed blog model family page lists: Seed2.1, Seedance 2.5, Seedream 5.0 Pro, SeedRealtime, Seed Audio 1.0, Seed GR-RL [9].
- **Seed 2.1 family**: officially released **2026-06-23** per ByteDance Seed blog; "Doubao and Volcano Engine users can now start to access Doubao Seed 2.1" [9].

## Models

Official Ark model list [2] groups text LLMs into "推荐模型" (recommended) and "往期模型" (previous). All Doubao API models are closed-API (open weights: not publicly disclosed — none of the API models are offered as downloadable weights; the Seed GitHub org hosts tooling/repos such as VeOmni, but no Doubao LLM weights were observed on official sources).

### Recommended (current flagship, fetched 2026-09-20)

| Model ID | Family | Context window | Max output (default) | Max thinking | Capabilities (per official docs) | Rate limit |
|---|---|---|---|---|---|---|
| doubao-seed-2-1-pro-260915 | Doubao Seed 2.1 | 1024k in | 256k (default 4k) | 256k | deep thinking, text gen, multimodal understanding, GUI task handling, tool calling, structured output (json_schema recommended) | 500 RPM / 1,000,000 TPM |
| doubao-seed-evolving | Doubao Seed (rolling, weekly updates via unified ID) | 1024k in | 256k (default 4k) | 256k | deep thinking, text gen, multimodal understanding, GUI task handling, tool calling, structured output (json_schema recommended) | 500 RPM / 1,000,000 TPM |
| doubao-seed-2-1-pro-260628 | Doubao Seed 2.1 | 256k in | 256k (default 4k) | 256k | same as above | 500 RPM / 1,000,000 TPM |
| doubao-seed-2-1-turbo-260628 | Doubao Seed 2.1 Turbo | 256k in | 256k (default 4k) | 256k | same as above | 500 RPM / 1,000,000 TPM |

- doubao-seed-2-1-pro-260915: announced as "新发布" (newly released) in the **202609** section of the official release announcement page; official note: "支持 1M 超长上下文，可用于 Agent 长程任务执行、异步子任务验收、多模态理解、深度调研、工具执行、Office 办公跨应用协同及 Coding 工程实践等场景" (supports 1M ultra-long context) [7].
- doubao-seed-evolving: first released June 2026 ("新发布" in 202606 section), "面向 Agent 与 Coding 场景…每周至少发布一个版本更新" (at least one version update per week), always callable via the single model ID [7]. July 2026 update added 1M context [7].
- Exact release day for 260915 not stated on the announcement page (month 2026-09 only; the ID suffix 260915 suggests a 2026-09-15 version date — derived, not officially stated).
- Featured models on Ark docs home / model list: **Doubao Seedance 2.5** (flagship video generation, "30s ultra-long narrative, all-modal reference expansion"), **Doubao Seedream 5.0 pro** (latest image generation), **Doubao Seed Evolving** (latest coding & agent) [2][4].

### Previous-generation Doubao models (still listed, many marked "即将下线" = about to be discontinued)

- doubao-seed-2-0-pro-260215, doubao-seed-2-0-lite-260215/260428, doubao-seed-2-0-mini-260215/260428, doubao-seed-2-0-code-preview-260215: 256k context (224k in / 128k out / 128k thinking), RPM 30,000 / TPM 5,000,000 [2].
- doubao-seed-character-260628 (128k ctx, 96k in / 32k out) and doubao-seed-character-251128 (text gen + tool calling, no deep thinking) [2].
- doubao-seed-1-8-251228, doubao-seed-1-6-250615/251015, doubao-seed-1-6-flash-250615/250828, doubao-seed-1-6-vision-250815, doubao-seed-code-preview-251028, doubao-1-5-pro-32k-250115, doubao-1-5-lite-32k-250115, doubao-1-5-pro-32k-character-250715 — all flagged "即将下线" [2].
- doubao-seed-translation-250915 — translation-enhanced, tiny context (4k ctx / 1k in / 3k out) [2].
- Capability labels used by official docs: 深度思考 (deep thinking), 文本生成 (text gen), 多模态理解 (multimodal understanding incl. image/video/PDF input), GUI 任务处理 (GUI agent), 工具调用 (tool calling), 结构化输出 (structured output), 翻译增强 (translation), 角色扮演场景增强 (roleplay). Video/image generation are separate dedicated models (Seedance/Seedream), not part of the text LLMs [2][4].
- Third-party models also hosted on Ark (out of scope, listed for context): DeepSeek V4.x, GLM-4.7/5.2/5.3-Flash [2].
- Regions: cn-beijing only, per the API key console path ark.volcengine.com/region:cn-beijing/apikey [4]. International endpoint availability not confirmed from fetched pages (see Conflicts).

## Pricing

Official pricing page [3], all prices in **CNY (元) per 1M tokens**, standard online inference (在线推理（常规）), fetched 2026-09-20. Tiered rows = input-length buckets in thousands of tokens (e.g., "(32,128]" = 32K–128K). Cache storage (context caching) = 0.017 元 per 1M tokens per hour for most listed Doubao models. "-" = not listed.

| Model (official name on pricing page) | Condition | Input (non-audio) | Input (audio) | Cache hit (non-audio) | Cache hit (audio) | Output |
|---|---|---|---|---|---|---|
| doubao-seed-evolving | (0,1024]K | 6.00 | - | 1.20 | - | 30.00 |
| doubao-seed-2.1-pro | (0,1024]K | 6.00 | - | 1.20 | - | 30.00 |
| doubao-seed-2.1-turbo | (0,256]K | 3.00 | - | 0.60 | - | 15.00 |
| doubao-seed-2.0-pro | (0,32] / (32,128] / (128,256] K | 3.2 / 4.8 / 9.6 | - | 0.64 / 0.96 / 1.92 | - | 16.0 / 24.0 / 48.0 |
| doubao-seed-2.0-lite | (0,32] / (32,128] / (128,256] K | 0.6 / 0.9 / 1.8 | 9.0 / 13.5 / 27.0 | 0.12 / 0.18 / 0.36 | 1.8 / 2.7 / 5.4 | 3.6 / 5.4 / 10.8 |
| doubao-seed-2.0-mini | (0,32] / (32,128] / (128,256] K | 0.2 / 0.4 / 0.8 | 3.0 / 6.0 / 12.0 | 0.04 / 0.08 / 0.16 | 0.6 / 1.2 / 2.4 | 2.0 / 4.0 / 8.0 |
| doubao-seed-2.0-code | (0,32] / (32,128] / (128,256] K | 3.2 / 4.8 / 9.6 | - | 0.64 / 0.96 / 1.92 | - | 16.0 / 24.0 / 48.0 |
| doubao-seed-1.8 | (0,32]K & out≤0.2K / (0,32]K & out>0.2K / (32,128] / (128,256] K | 0.80 / 0.80 / 1.20 / 2.40 | - | 0.16 | - | 2.00 / 8.00 / 16.00 / 24.00 |
| doubao-seed-character | (0,32] / (32,128] K | 0.80 / 1.20 | - | 0.16 | - | 2.00 / 6.00 |
| doubao-seed-code | (0,32] / (32,128] / (128,256] K | 1.20 / 1.40 / 2.80 | - | 0.24 | - | 8.00 / 12.00 / 16.00 |
| doubao-seed-1.6 | same tiering as 1.8 | 0.80 / 0.80 / 1.20 / 2.40 | - | 0.16 | - | 2.00 / 8.00 / 16.00 / 24.00 |
| doubao-seed-1.6-lite | same tiering as 1.8 | 0.30 / 0.30 / 0.60 / 1.20 | - | 0.06 | - | 0.60 / 2.40 / 4.00 / 12.00 |
| doubao-seed-1.6-flash | (0,32] / (32,128] / (128,256] K | 0.15 / 0.30 / 0.60 | - | 0.03 | - | 1.50 / 3.00 / 6.00 |
| doubao-seed-1.6-vision | (0,32] / (32,128] / (128,256] K | 0.80 / 1.20 / 2.40 | - | 0.16 | - | 8.00 / 16.00 / 24.00 |
| doubao-seed-translation | - | 1.20 | - | - | - | 3.60 |
| doubao-1.5-pro-32k | - | 0.80 | - | 0.16 | - | 2.00 |
| doubao-1.5-lite-32k | - | 0.30 | - | 0.06 | - | 0.60 |
| doubao-1.5-vision-pro | - | 3.00 | - | - | - | 9.00 |

- Billing: pay-per-token postpaid; formula = input(non-audio) + input(audio) + cache hits + cache storage × time + output [3].
- **Low-latency tier** (在线推理（低延迟）) also exists: e.g., doubao-seed-2.1-turbo 6.00 in / 30.00 out; doubao-seed-2.0-pro 9.6–28.8 in / 48–144 out [3].
- **Low-priority tier** (在线推理（低优）): ~50% of standard prices, e.g., doubao-seed-2.1-pro 3.00 in / 15.00 out, 2.1-turbo 1.50/7.50; implicit caching only, no storage fee [3].
- **Batch inference** (批量推理): same pricing as low-priority for most models [3].
- **TPM guarantee packs** (TPM 保障包): capacity subscription, e.g., doubao-seed-1.8 1.920 元/10K TPM/hour or 23.040 元/10K TPM/day prepaid [3].
- Effective date: no explicit "effective from" date for Doubao rows on the page (the page only marks historical pre-change DeepSeek prices "调整前价格…2026-08-21/08-28 起不适用"). Treat prices as "as of fetch date 2026-09-20" [3].

## API facts

- **Base URL**: `https://ark.cn-beijing.volces.com/api/v3` [4].
- **Endpoints**: Responses API `POST /api/v3/responses` [5]; Chat (对话) API `POST /api/v3/chat/completions` [6].
- **Auth**: Bearer token — `Authorization: Bearer $ARK_API_KEY`; long-term API Key obtained at https://ark.volcengine.com/region:cn-beijing/apikey [4][5][6]. Chat API also documents an optional Access Key (AK/SK) auth method [6].
- **Streaming**: supported. Chat API: `stream` boolean parameter (default false) + `stream_options` [6]. Responses API: `"stream": true` returns SSE events (e.g., `event: response.created`, `data: {"type":"response.created",...}`) [5].
- **Thinking control**: `thinking={"type":"enabled"|"disabled"}`; Chat API `reasoning_effort` string param; docs also mention Responses API `reasoning.effort=minimal` to disable deep thinking [2][5][6].
- **Modalities**: Chat API accepts messages containing text, image, video, audio [6]. Files API for upload/preprocessing of video, image, PDF [4].
- **Other documented params (Chat API)**: max_tokens default 4096, temperature default 1.0, top_p default 0.7, presence/frequency penalty, logprobs, tool_choice, tools, service_tier (default auto) [6].
- **SDKs**: official `arkruntime` Python SDK (`from arkruntime import Ark`); OpenAI-SDK-compatible mode documented [4][6]. Regions: cn-beijing only per API-key path [4].
- Note: doubao-1.5-pro-32k-character-250715 does not support Responses API (must use Chat API) [5].

## Benchmarks (vendor-reported)

From the official ByteDance Seed blog post "Seed2.1 Officially Released" (2026-06-23) [9]. The blog explicitly states "we prioritize model performance in live workflows over static benchmark scores alone". Most claims are qualitative; only one numeric score published:

- **Code Arena: Frontend** — Seed2.1 Preview: rank 8th, score **1539**, top-10 in 5 of 7 frontend subcategories (vendor_reported, 2026-06-23) [9].
- Qualitative claims for Seed2.1 / Seed2.1 Pro (all vendor_reported, 2026-06-23) [9]:
  - "highest score" on: GDPVal; MobileWorld (mobile GUI); CharXiv-RQ and MeasureBench (visual understanding); "top results" on ERQA.
  - "top tier" on Agents' Last Exam (ALE); "standout" on CreativeWork (internal), MMLongBench-128K, OVBench (streaming video).
  - "industry-leading" on TVBench and TOMATO (video understanding); "strong performance" on Video MME and LVBench.
  - "competitive" on OSWorld, ProgramBench, Toolathlon, ClawBench (SeedClawBench — internal), FrontierScience-Research.
  - "performs well" on SciCode and FrontierScience-Olympiad; "steady performance" on xDailyBench and Doubao Multi-Turn Bench; "consistent performance" on Workspace Bench and Agent Startup Bench.
  - RL-guided agent action selection reduces average steps to complete tasks by 16%.
- No benchmark scores are published on the Ark model list [2], pricing [3], or release announcement [7] pages.

## Conflicts / uncertainty notes

1. **Two flagship "pro" models listed simultaneously**: doubao-seed-2-1-pro-260915 (1M context, newest) and doubao-seed-2-1-pro-260628 (256k). Both are "recommended"; docs do not state which replaces which.
2. **doubao-seed-evolving vs versioned models**: Evolving is a rolling weekly-updated model under one ID; its pricing row (6/30 CNY) matches doubao-seed-2.1-pro, but the pricing page does not explicitly state which underlying version Evolving maps to.
3. **Pricing page lists families without version suffixes** (e.g., "doubao-seed-2.1-pro" covers 260628/260915). Assumed family-level pricing; not explicitly documented on the page.
4. **Effective dates**: pricing page has no "effective from" dates for Doubao rows (only DeepSeek historical notes). Prices recorded as-of fetch date.
5. **Release date precision**: official announcement page gives month (202609) for 2-1-pro-260915; exact day not stated. The Seed 2.1 family blog gives an exact date (2026-06-23).
6. **International region unverified**: English docs (lang=en) still served the cn-beijing base URL and Chinese content; no verified international endpoint (e.g., ark.volcengine.com/api/v3) from pages fetched today.
7. **Open weights**: no official statement found on fetched pages that any Doubao API model weights are downloadable; Seed GitHub org exists but hosts tooling (VeOmni, Triton-distributed), not Doubao LLM weights. Marked "not publicly disclosed" rather than "closed".
8. Many legacy models (seed 1.6/1.8, 1.5 series) are flagged "即将下线" (to be discontinued soon) with no dates given; translation/character variants remain listed without deprecation flags.
