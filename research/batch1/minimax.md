# MiniMax research (fetched 2026-09-20)

## Sources used
- https://www.minimax.io/ (international corporate site, About section)
- https://www.minimax.cn/about (Chinese corporate site)
- https://platform.minimaxi.com/docs/guides/models-intro (CN platform model overview; redirected from platform.minimaxi.com)
- https://platform.minimaxi.com/docs/llms.txt (CN docs index; canonical host platform.minimax.cn)
- https://platform.minimax.io/docs/llms.txt (international docs index)
- https://platform.minimaxi.com/docs/api-reference/text-anthropic-api.md (CN Anthropic-compat API)
- https://platform.minimax.io/docs/api-reference/text-anthropic-api.md (intl Anthropic-compat API)
- https://platform.minimaxi.com/docs/guides/pricing-paygo.md (CN pay-as-you-go pricing)
- https://platform.minimax.io/docs/guides/pricing-paygo.md (intl pay-as-you-go pricing)
- https://platform.minimaxi.com/docs/release-notes/models.md (official model release notes)
- https://www.minimax.cn/models/text/m3 (official M3 model page)
- https://www.minimax.cn/blog/minimax-m3 (official M3 blog post; HTML fetched via curl)
- https://github.com/MiniMax-AI (GitHub org)
- https://github.com/MiniMax-AI/MiniMax-M2 (M2 repo README + LICENSE via raw.githubusercontent)
- https://huggingface.co/MiniMaxAI/MiniMax-M2 (M2 model card; HF API for metadata)
- https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/README.md + LICENSE
- https://huggingface.co/MiniMaxAI/MiniMax-M2.7/raw/main/README.md + LICENSE (via GitHub raw)
- https://huggingface.co/api/models/... for M2, M3, M2.7, Music3, H3
- https://platform.minimax.io/docs/guides/local-deploy.md and local-deploy-m3.md
- https://platform.minimax.cn/protocol/privacy-policy (entity name + HQ address)
- HF API for MiniMaxAI/MiniMax-Music3, MiniMaxAI/MiniMax-H3

## Company facts
- **Official name (EN)**: MiniMax ("A World-Leading General AI Technology Company") — minimax.io
- **Chinese name**: 上海稀宇科技有限公司 (Shanghai Xiyu Technology Co., Ltd.) — official CN privacy policy (platform.minimax.cn/protocol/privacy-policy)
- **Founded**: early 2022 (officially stated: "Founded in early 2022" — minimax.io; "自2022年初成立以来" — minimax.cn/about). Exact date not stated.
- **HQ**: 上海市闵行区古北路1699号1704-1室 (Room 1704-1, No. 1699 Gubei Road, Minhang District, Shanghai) — official privacy policy
- **Mission (official)**: "co-create intelligence with everyone"; pursuing AGI — minimax.io
- **Websites**:
  - International: https://www.minimax.io/ ; API docs: https://platform.minimax.io/
  - China: https://www.minimax.cn/ ; API platform: https://platform.minimaxi.com/ (canonical host platform.minimax.cn)
- **Docs URLs**: https://platform.minimax.io/docs (EN), https://platform.minimaxi.com/docs (CN), full index at /docs/llms.txt (both)
- **GitHub**: https://github.com/MiniMax-AI (key repos: MiniMax-M2, MiniMax-M3, MiniMax-M2.7, MiniMax-Music3, MiniMax-H3, MSA sparse-attention, minimax-code, cli, MiniMax-MCP-JS, MiniMax-Provider-Verifier)
- **Hugging Face**: https://huggingface.co/MiniMaxAI ; ModelScope: https://modelscope.cn/organization/minimax
- **Products (official list, minimax.io)**: MiniMax Code, MiniMax Design, MiniMax Audio, Talkie (intl) / 星野 (CN), plus open platform for enterprises & developers. MiniMax Agent at https://agent.minimax.io/
- **Vendor-claimed scale (minimax.cn/about, fetched 2026-09-20)**: users in 230+ countries/regions; 300M+ individual users; 2M+ enterprise clients & developers across 100+ countries. (International site renders the counters as "0+" due to JS.)

## Models
### Current flagship language models (per official CN models-intro page, 2026-09-20)
**MiniMax-M3** — current flagship
- Family: MiniMax M-series text/multimodal LLM; native multimodal (text, image, video input → text output)
- Release date: 2026-06-01 (official release notes: "2026 年 6 月 1 日, 全新语言模型 MiniMax-M3 正式发布")
- Context window: **1,000,000 tokens** (API docs); official M3 page: "API 最高支持 1M tokens 上下文窗口，保障至少 512K tokens 可用" (guarantees ≥512K usable)
- Max output: not publicly disclosed in fetched official docs
- Architecture: Mixture-of-Experts, **~428B total parameters / ~23B activated** (HF README); MiniMax Sparse Attention (MSA) — claimed 9× prefill and 15× decode speedup vs M2 at 1M context
- Open weights: **Yes** — HF `MiniMaxAI/MiniMax-M3` (~171k downloads), GitHub MiniMax-AI/MiniMax-M3, MXFP8 repo MiniMaxAI/MiniMax-M3-MXFP8; ModelScope mirrors; arXiv 2606.13392
- License: **MiniMax Community License** (custom): free for non-commercial use; commercial use requires prominent attribution "Built with MiniMax M3" + written authorization from MiniMax if >US$20M yearly revenue, otherwise a one-time notice to api@minimax.io
- Capabilities (official docs): agentic reasoning, tool use, coding, long context, image+video input (JPEG/PNG/GIF/WEBP ≤10MB; MP4/AVI/MOV/MKV ≤50MB direct, ≤512MB via Files API); reasoning toggleable (`thinking` param: disabled by default, `adaptive` to enable); auto prompt caching
- API availability: China platform + international platform (both Anthropic- & OpenAI-compatible endpoints)
- Output speed: not published for M3 in API docs (unlike M2.x)

**MiniMax-M2.7 / M2.7-highspeed** — current
- Release date: 2026-03-18 (official release notes)
- Context window: **204,800 tokens** (API docs)
- Positioning: "开启模型的自我迭代" / "first model deeply participating in its own evolution" (recursive self-improvement, agent teams, complex skills, tool search)
- Output speed (vendor): M2.7 ≈60 TPS; M2.7-highspeed ≈100 TPS (same quality, faster)
- Input: text only (no image/video); interleaved thinking is always on (cannot be disabled via API)
- Open weights: **Yes** — HF `MiniMaxAI/MiniMax-M2.7` (~1.46M downloads), GitHub MiniMax-AI/MiniMax-M2.7
- License: **custom NON-COMMERCIAL LICENSE** (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution "Built with MiniMax M2.7" required)
- Parameter count: not found in official README → not publicly disclosed
- Max output: not publicly disclosed

### Legacy / other language models (official docs)
- MiniMax-M2: released 2025-10-27; context 204,800; MoE **230B total / 10B active**; open weights (HF ~264.6k downloads); license = **modified MIT** (must prominently display "MiniMax M2" if used in commercial products with >100M MAU or >US$30M ARR); interleaved thinking with `<think>...</think>` tags; API was free until 2025-11-07 08:00 (launch promo)
- MiniMax-M2.5 / M2.5-highspeed: 2026-02 (day not stated); MiniMax-M2.1 / M2.1-highspeed: 2025-12-22; MiniMax-M1: 2025-06-16; all context 204,800 per API docs
- MiniMax-H3 (video, open-weight): released 2026-07-31; text/image/video/audio → video; 768P/2K, 4–15s; license: MiniMax H3 Community License Agreement; HF ~4.3M downloads
- MiniMax H3 Max: fal.ai post-trained fast video model (480P/768P, 5–15s)
- Speech-2.8-HD / Speech-2.8-Turbo (TTS): released 2026-01-23
- image-01 / image-01-live (image generation)
- MiniMax Music 3 (open-source music model, HF/ModelScope); **Music API: paid endpoints closed to new users since 2026-08-20**, free music endpoints discontinued (official notice)

## Pricing
Pay-as-you-go, per 1M tokens. Fetched 2026-09-20. CNY = China platform (platform.minimax.cn), USD = international platform (platform.minimax.io). No effective-date stamp on the pages beyond today's fetch.

### MiniMax-M3 (standard tier; "Permanent 50% off" shown against strikethrough list prices)
| Tier | Input | Output | Cache read |
|---|---|---|---|
| ≤512k input — CNY | ¥2.10 (list ¥4.20) | ¥8.40 (list ¥16.80) | ¥0.42 (list ¥0.84) |
| >512k input — CNY | ¥4.20 (list ¥8.40) | ¥16.80 (list ¥33.60) | ¥0.84 (list ¥1.68) |
| ≤512k input — USD | $0.30 (list $0.60) | $1.20 (list $2.40) | $0.06 (list $0.12) |
| >512k input — USD | $0.60 (list $1.20) | $2.40 (list $4.80) | $0.12 (list $0.24) |
Priority tier (`service_tier=priority`, 1.5× standard): CNY ¥3.15/¥12.60/¥0.63 (≤512k), ¥6.30/¥25.20/¥1.26 (>512k); USD $0.45/$1.80/$0.09 (≤512k), $0.90/$3.60/$0.18 (>512k).

### MiniMax-M2.7 series (CNY / USD per 1M tokens)
| Model | Input | Output | Cache read | Cache write |
|---|---|---|---|---|
| MiniMax-M2.7 | ¥2.1 / $0.30 | ¥8.4 / $1.20 | ¥0.42 / $0.06 | ¥2.625 / $0.375 |
| MiniMax-M2.7-highspeed | ¥4.2 / $0.60 | ¥16.8 / $2.40 | ¥0.42 / $0.06 | ¥2.625 / $0.375 |
Legacy (M2.5, M2.1, M2): input ¥2.1/$0.30, output ¥8.4/$1.20, cache read ¥0.21/$0.03, cache write ¥2.625/$0.375.

### Other modalities (list prices, both regions)
- TTS: speech-2.8-hd ¥3.50 / $100 per 1M chars; speech-2.8-turbo ¥2.00 / $60 per 1M chars (async same)
- ASR: ¥2.50 / $0.38 per hour
- Voice design ¥9.90 / $3 per voice; rapid voice cloning ¥9.90 / $1.5 per voice (billed on first synthesis use)
- Video (H3): 768P ¥0.50/$0.08 per sec; 2K ¥0.80/$0.13 per sec; H3-Max: 480P ¥0.33/$0.05, 768P ¥0.50/$0.08 per sec
- Image: image-01 ¥0.025 / $0.0035 per image
- Music: Music-3.0 ¥1.0 / $0.15 per song (≤5 min) — discontinued for new users since 2026-08-20
- Pricing page URLs: https://platform.minimaxi.com/docs/guides/pricing-paygo and https://platform.minimax.io/docs/guides/pricing-paygo (Token Plan subscription: /docs/guides/pricing-token-plan)

## API facts
- **Endpoints**: Anthropic-compatible base URL `https://api.minimax.io/anthropic` (intl) / `https://api.minimax.cn/anthropic` (CN) — set `ANTHROPIC_BASE_URL`. OpenAI-compatible Chat Completions + Responses API also supported; plus legacy MiniMax-native endpoints.
- **Auth**: API Key via `ANTHROPIC_API_KEY` env var (Bearer-style); keys from platform console. No other auth schemes mentioned.
- **Streaming**: supported (`stream=True`; thinking streamed as `thinking_delta`, text as `text_delta`)
- **Key params**: `max_tokens`, `temperature` (0–2, recommended 1.0), `top_p`, `thinking` (M3 only: omitted/`disabled` default, `adaptive` enables), `tools`/`tool_choice`, `service_tier` (`standard` | `priority`, priority = 1.5× price)
- **Prompt caching**: automatic caching + explicit Anthropic-style `cache_control` (active caching); cache read/write billed separately
- **Multimodal (M3 only)**: image/video via Anthropic content blocks (URL, base64, or `mm_file://{file_id}`); max 50MB video / 10MB image direct; Files API up to 512MB video; request body ≤64MB
- **Interleaved thinking**: M2.x thinking always on; must echo full assistant content (thinking blocks) back in history

## Benchmarks (vendor-reported)
All scores below are published by MiniMax itself (label: vendor_reported). Fetched 2026-09-20.

### MiniMax-M2 (official GitHub README table, methodology footnotes included there)
Coding/agentic: SWE-bench Verified 69.4; Multi-SWE-Bench 36.2; SWE-bench Multilingual 56.5; Terminal-Bench 46.3; ArtifactsBench 66.8; BrowseComp 44; BrowseComp-zh 48.5; GAIA (text only) 75.7; xbench-DeepSearch 72; HLE (w/ tools) 31.8; τ²-Bench 77.2; FinSearchComp-global 65.5; AgentCompany 36.
Artificial Analysis-aligned: AIME25 78; MMLU-Pro 82; GPQA-Diamond 78; HLE (w/o tools) 12.5; LiveCodeBench 83; SciCode 36; IFBench 72; AA-LCR 61; τ²-Bench-Telecom 87; Terminal-Bench-Hard 24; AA Intelligence index 61. Claim: "#1 among open-source models" on AA composite.
URL: https://github.com/MiniMax-AI/MiniMax-M2

### MiniMax-M2.7 (official HF README)
- GDPval-AA ELO: 1495 — claimed highest among open-weight models, surpassing GPT5.3
- Toolathon accuracy: 46.3% ("global top tier")
- MM Claw end-to-end benchmark: 62.7% ("close to Sonnet 4.6"); 97% skill compliance across 40+ complex skills
URL: https://huggingface.co/MiniMaxAI/MiniMax-M2.7

### MiniMax-M3 (official model page + official blog)
- BrowseComp: 83.5 (vs Opus 4.7 79.3) — minimax.cn/models/text/m3
- PostTrainBench: 37.1 (3rd; behind Opus 4.7 42.4 and GPT-5.5 39.3) — model page; blog states 0.37 vs 0.42/0.39 (same result, different rounding)
- Coding/agent (blog): SWE-Bench Pro 59.0%; Terminal Bench 2.1 66.0%; SWE-fficiency 34.8%; KernelBench Hard 28.8%; MCP Atlas 74.2%
URLs: https://www.minimax.cn/models/text/m3 ; https://www.minimax.cn/blog/minimax-m3

## Conflicts / uncertainty notes
- **Max output tokens**: not published in any fetched official doc for M3, M2.7, or M2 → treated as not publicly disclosed.
- **M2.7 parameter count**: not found in official README/model card → not publicly disclosed.
- **PostTrainBench rounding**: model page says 37.1 (Opus 4.7 = 42.4, GPT-5.5 = 39.3); blog says 0.37 (0.42/0.39). Same result, inconsistent presentation across official pages.
- **M2.5 exact release day**: release notes give only "2026 年 2 月".
- **M3 blog benchmark table** (SWE-Bench Pro etc.) was extracted from HTML source of a JS-rendered page; values are verbatim but the page's full comparison table may contain more rows not captured here.
- **M3 "1M context"**: docs state API supports up to 1M-token context with ≥512K guaranteed usable; pricing tiers split at ≤512k vs >512k input tokens.
- **M2.7 license change vs M2**: M2 = modified MIT (commercial OK with attribution); M2.7 = non-commercial-only without written authorization; M3 = community license with revenue-threshold authorization. Different licenses per model — do not generalize.
- **HF license metadata**: HF API returns `license: None` / tag `license:other` for these repos; actual terms are in each repo's LICENSE file (quoted above).
- **Music API**: officially discontinued for new users since 2026-08-20 (paid + free endpoints); open-source MiniMax Music 3 remains on HF/ModelScope.
- **International site counters** ("0+ countries", "0M+ users") render via JS and were unreadable; CN about page states 230+ countries, 300M+ users, 2M+ enterprise clients/developers (vendor claims).
- **HQ address** is from the official privacy policy of the CN API platform; entity registered name is 上海稀宇科技有限公司. No English legal-entity name was found in fetched sources.
