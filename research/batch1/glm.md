# Z.ai / GLM research (fetched 2026-09-20)

## Sources used
- https://docs.z.ai/ (Quick Start; docs index at https://docs.z.ai/llms.txt)
- https://docs.z.ai/guides/llm/glm-5.3 (GLM-5.3 model page)
- https://docs.z.ai/guides/vlm/glm-5.3-flash (GLM-5.3-Flash/FlashX model page)
- https://docs.z.ai/guides/overview/pricing (USD pricing, fetched 2026-09-20)
- https://docs.z.ai/release-notes/new-released (official release dates)
- https://docs.z.ai/legal-agreement/privacy-policy (legal entity, last updated 2025-09-29)
- https://chat.z.ai/ (redirect target of z.ai/; title: "Z.ai - Advanced AI Chatbot & Agent powered by GLM-5.3-Flash")
- https://github.com/zai-org (org; repo list via GitHub API, fetched 2026-09-20)
- https://github.com/zai-org/GLM-5 (README, fetched 2026-09-20)
- https://api.github.com/orgs/THUDM/repos (repo list, fetched 2026-09-20)
- https://docs.bigmodel.cn/cn/guide/start/pricing (CNY pricing, fetched 2026-09-20)
- https://bigmodel.cn/pricing (HTML shell; meta author tag only — page is a JS SPA)
- https://www.zhipuai.cn/ and /about (no founding statement found)

## Company facts
- Official names: **Z.ai** (international brand/domain), **Zhipu AI / 智谱 (Zhipu)** (China brand). Chinese platform: **BigModel (open.bigmodel.cn / bigmodel.cn)**. GitHub org: **zai-org** (current model repos); academic-roots org: **THUDM** (Tsinghua KEG; hosts slime RL framework and research repos).
- Legal entities (officially stated):
  - International (Z.ai services): **JINGSHENG HENGXING TECHNOLOGY PTE.LTD**, registered address 10 Anson Road, #26-03, International Plaza, Singapore 0759903. Source: Z.ai Privacy Policy (https://docs.z.ai/legal-agreement/privacy-policy, "Last Update: September 29, 2025").
  - China: **北京智谱华章科技股份有限公司 (Beijing Zhipu Huazhang Technology Co., Ltd.)** — stated as author/copyright of bigmodel.cn. Source: HTML meta tag of https://bigmodel.cn/pricing.
- Founded: **not stated on any official page fetched** (not publicly stated on z.ai, docs.z.ai, zhipuai.cn home/about pages fetched 2026-09-20).
- HQ: China operations in Beijing (bigmodel.cn legal name; zhipuai.cn content references 北京市海淀区 activities). International HQ per privacy policy: Singapore. No single "headquarters" line found on official pages.
- Official websites: https://z.ai/ (international; redirects to https://chat.z.ai/), https://bigmodel.cn/ (China platform), https://open.bigmodel.cn/ (China API platform), https://www.zhipuai.cn/ (Chinese corporate site).
- Docs: https://docs.z.ai/ (international, English), https://docs.bigmodel.cn/ (Chinese).
- GitHub: https://github.com/zai-org (main), https://github.com/THUDM (research).
- International consumer chat app: chat.z.ai, "powered by GLM-5.3-Flash" (page title, 2026-09-20).
- Coding subscription: "GLM Coding Plan" from $18/month, compatible with Claude Code, Cline, etc. (docs.z.ai Quick Start, fetched 2026-09-20; points-based quota, off-peak/weekends at 50% points — GLM-5.3 model page).

## Models
Current flagship API models on Z.ai (per docs.z.ai model cards and pricing page, fetched 2026-09-20):

### GLM-5.3 (flagship, text)
- Official name: GLM-5.3; API model id: `glm-5.3`.
- Release date: **2026-08-18** (docs.z.ai release notes).
- Context window: 1M tokens; max output: 128K tokens. Text-only input. Reasoning always enabled (`low`/`high`/`max`, default `max`); disabling reasoning not supported.
- Same base model as GLM-5.2; all gains from post-training. 50% coding gain over GLM-5.2 on Z.ai Code Bench (vendor claim).
- Open weights: **YES**. Hugging Face `zai-org/GLM-5.3` (744B total / 40B active, FP8) and `GLM-5.3-BF16`; ModelScope mirrors `ZhipuAI/GLM-5.3`. License: Apache-2.0 (GitHub repo metadata for zai-org/GLM-5; README has no separate weights license section). Source: https://github.com/zai-org/GLM-5 README.
- API availability: Z.ai international API + BigModel China. Coding Plan included.

### GLM-5.3-Flash / FlashX (multimodal coding)
- Official name: GLM-5.3-Flash / GLM-5.3-FlashX; API ids: `glm-5.3-flash`, `glm-5.3-flashx`.
- Release date: **2026-08-26** (docs.z.ai release notes); FlashX "now live" per model page (fetch date 2026-09-20).
- Context: 1M; max output: 128K. Input modalities: video / image / text / file; output: text.
- Architecture: 320B total / 18B active params; first open-source frontier model combining sparse + linear attention; mHC hyper-connections; 30T-token multimodal pre-training corpus (model page).
- FlashX: inference speeds of 200 tokens/s (model page).
- Capabilities per official docs: visual coding loop (observe→code→test), computer use (BUA/CUA), browser/GUI agents, office workflows (PPTX/PDF/DOCX/XLSX), video understanding/editing, Blender 3D, Godot game dev, CAD via build123d, financial research. Reasoning always enabled.
- Open weights: **YES**. HF `zai-org/GLM-5.3-Flash` (320B-A18B, FP8) + `GLM-5.3-Flash-BF16`; ModelScope `ZhipuAI/GLM-5.3-Flash`. Apache-2.0 (same repo metadata). Source: zai-org/GLM-5 README.
- API availability: Z.ai international API; FlashX not yet on GLM Coding Plan (model page).
- Was pre-release tested anonymously as "ox-alpha" on OpenCode/OpenRouter; "all traffic served on Chinese AI chips" (model page).

### GLM-5.2 (previous flagship, text)
- Release: **2026-06-16**. 1M context; reasoning `high`/`max` only. Open weights: yes, 744B-A40B (HF `zai-org/GLM-5.2`, BF16/FP8). Still listed on API pricing page at same price as GLM-5.3.

### Other current/notable API models (docs.z.ai pricing page, 2026-09-20)
- GLM-5.1 (2026-04-07), GLM-5 (2026-02-12) — text.
- GLM-OCR (2026-02-03) — OCR; open weights (zai-org/GLM-OCR, Apache-2.0).
- GLM-4.7 / GLM-4.7-FlashX / GLM-4.7-Flash (2025-12-22 / 2026-01-19) — text; GLM-4.6 (2025-09-30), GLM-4.5 series (2025-07-28).
- GLM-4.6V / GLM-4.6V-FlashX / GLM-4.5V — vision (open weights repo zai-org/GLM-V).
- GLM-Image (2026-01-14) — text-to-image, "open-source SOTA" per docs; open weights (zai-org/GLM-Image, Apache-2.0).
- CogVideoX-3 (2025-07-15) — video generation; open weights (zai-org/CogVideo, Apache-2.0).
- GLM-ASR-2512 (2025-12-10) — speech recognition (open weights repo zai-org/GLM-ASR).
- AutoGLM-Phone-Multilingual (2025-12-11) — phone agent; open framework zai-org/Open-AutoGLM (Apache-2.0).
- China (BigModel) additionally lists: GLM-5-Turbo, GLM-5V-Turbo, GLM-4-Plus, GLM-4-Air series, GLM-Z1 series, Embedding-2/3, GLM-TTS, GLM-TTS-Clone, GLM-Realtime-Flash/Air, CodeGeeX-4, Rerank, CogView-4, ViduQ1/Vidu2 (pricing docs).
- GLM-5 tech report: "GLM-5: from Vibe Coding to Agentic Engineering", arXiv:2602.15763 (2026) — cited in zai-org/GLM-5 README.
- Regions: international (Z.ai, Singapore operator) and China (BigModel) are separate platforms; both sell GLM-5.x APIs.

## Pricing
All values as listed on official pricing pages, fetched 2026-09-20. No explicit "effective date" is printed on the pages; treat fetch date as effective.

### International (Z.ai, USD per 1M tokens) — https://docs.z.ai/guides/overview/pricing
Latest models:
- GLM-5.3: input $1.4 | cached input $0.26 | cache storage limited-time free | output $4.4
- GLM-5.2: input $1.4 | cached $0.26 | storage free | output $4.4
- GLM-5.3-Flash: input $0.15 | cached $0.03 | storage free | output $0.50
- GLM-5.3-FlashX: input $0.37 | cached $0.075 | storage free | output $1.25

Selected older (same page): GLM-5.1 $1.4/$0.26/$4.4; GLM-5 $1.0/$0.2/$3.2; GLM-4.7 $0.6/$0.11/$2.2; GLM-4.6 $0.6/$0.11/$2.2; GLM-4.5 $0.6/$0.11/$2.2; GLM-4.5-Air $0.2/$0.03/$1.1; GLM-4.6V $0.3/$0.05/$0.9; GLM-OCR $0.03/$0.03; GLM-4.7-Flash and GLM-4.5-Flash: Free.
- Web Search tool: $0.01/use. GLM-Image $0.015/image; CogView-4 $0.01/image; CogVideoX-3 $0.2/video; GLM-ASR-2512 $0.03/MTok (~$0.0024/min).
- GLM Coding Plan: from $18/month (subscription; docs quick start).

### China (BigModel, CNY per 1M tokens) — https://docs.bigmodel.cn/cn/guide/start/pricing
Flagship:
- GLM-5.3 (1M ctx): input ¥8 | output ¥28 | cached hit ¥2 | cache storage 限时免费 (limited-time free)
- GLM-5.3-Flash (1M ctx, image/video/file/text input): input ¥0.8 | output ¥2.8 | cached ¥0.23
- GLM-5.3-FlashX (1M ctx): input ¥2 | output ¥7 | cached ¥0.57
- GLM-5.2 (1M): ¥8 / ¥28 / cached ¥2
- GLM-5.1: input ¥6 (<32K) / ¥8 (≥32K); output ¥24 / ¥28
- GLM-5-Turbo: input ¥5 / ¥7; output ¥22 / ¥26
- GLM-5: input ¥4 / ¥6; output ¥18 / ¥22
- GLM-Image ¥0.1/image; CogVideoX-3 ¥1/video; CogView-4 ¥0.06/image; GLM-ASR-2512 input ¥16/MTok (~¥0.0002/sec), output free; GLM-TTS ¥2/10k chars; GLM-TTS-Clone ¥6/call; Search tools ¥0.01–0.05/use; Embedding-3/2 ¥0.5/MTok (Batch 50% off).
- Batch API = 50% of standard price for supported models (pricing page note).

## API facts
- Endpoint (OpenAI-compatible chat completions): `POST https://api.z.ai/api/paas/v4/chat/completions` (docs quick start).
- GLM-5.3 also supports: OpenAI Response protocol base `https://api.z.ai/api/v1`; Anthropic Message protocol base `https://api.z.ai/api/anthropic`; coding-plan endpoint `https://api.z.ai/api/coding/paas/v4` (GLM-5.3 model page).
- Auth: `Authorization: Bearer YOUR_API_KEY` (docs quick start).
- Streaming: supported — `"stream": true`; tool streaming via `tool_stream: true` (recommended for Flash). SDKs: zai-sdk (Python, Java), OpenAI SDK compatibility documented.
- China API: BigModel platform (open.bigmodel.cn); docs.bigmodel.cn lists OpenAI-compatible and Claude-compatible API guides.

## Benchmarks (vendor-reported)
All scores are as published on official Z.ai pages (docs/README), not independently verified. No third-party source used.

From https://docs.z.ai/guides/llm/glm-5.3 (fetched 2026-09-20):
- Terminal-Bench 3.0: GLM-5.3 28.3 vs GLM-5.2 4.6
- DeepSWE v1.1: GLM-5.3 66.9 vs GLM-5.2 46.2
- Agents' Last Exam (CLI): GLM-5.3 28.5 vs GLM-5.2 23.8
- Z.ai Code Bench (private, in-house): GLM-5.3 Max effort 34.5% at ~75K output tokens/task vs GLM-5.2 23.4% at ~96K; High effort 31.4% at ~50K vs Claude Opus 4.8 29.5% at ~120K; Claude Fable 5 39.5% at Max
- CyberGym (vuln discovery): GLM-5.3 84.5% vs GLM-5.2 77.2%; Mythos 5 83.8%; GPT-5.6 Sol 83.6%
- ExploitBench: GLM-5.3 54.4% vs GLM-5.2 24.4%; Mythos 5 78.0%; GPT-5.6 Sol 76.5%
- ExploitGym (time-normalized): GLM-5.3 105 tasks/2h, 130/6h vs GLM-5.2 29/39; Mythos 5 181/247
- Real-world security: 2,436 vulnerabilities identified across 269 projects, incl. 1,097 medium/high severity (company claim)

From https://docs.z.ai/guides/vlm/glm-5.3-flash (fetched 2026-09-20):
- Artificial Analysis Intelligence Index v4.1.1: GLM-5.3-Flash score 57 at $0.045/task (discounted)
- DeepSWE v1.1: Flash 63.4 vs GLM-5.2 46.2
- AutomationBench: Flash 48.8 vs GLM-5.2 26.2
- Z.ai Code Bench v1.0 (run on Claude Code 2.1.207): Flash max effort 29.0 vs Claude Opus 4.8 29.5; Flash beats GLM-5.2 at every effort level

From https://docs.z.ai/release-notes/new-released (fetched 2026-09-20):
- GLM-ASR-2512: Character Error Rate 0.0717 (2025-12-10)

From https://github.com/zai-org/GLM-5 README (fetched 2026-09-20):
- Vending Bench 2 (andonlabs.com): GLM-5 #1 among open-source models, final account balance $4,432 over simulated one-year horizon, "approaching Claude Opus 4.5"

## Conflicts / uncertainty notes
- No "effective date" printed on either pricing page; prices are a snapshot as of fetch date 2026-09-20.
- Weights license: GitHub repo metadata for zai-org/GLM-5 says Apache-2.0, but the README contains no separate weights-license section. Recommend verifying per-model HF model cards before reuse.
- GLM-5.3-FlashX pricing exists but FlashX "not yet available" on the GLM Coding Plan (model page) — subscription vs pay-as-you-go availability differs.
- Company founding year: not found on any official page fetched; zhipuai.cn home/about pages carry no founding statement. (Commonly cited 2019 not verified here.)
- bigmodel.cn/pricing is a JS SPA (unscrapable without JS); CNY data was taken from the docs.bigmodel.cn pricing docs page instead — same vendor, likely consistent, but page rendering of the SPA was not verified.
- The Z.ai Privacy Policy names JINGSHENG HENGXING TECHNOLOGY PTE.LTD as the Z.ai operator; the Chinese platform's legal name is 北京智谱华章科技股份有限公司. The exact corporate relationship between the two is not described on the fetched pages.
- Chinese-side pricing lists additional models not present in international docs (GLM-5-Turbo, GLM-5V-Turbo, GLM-4-Plus, GLM-Z1, ViduQ1/Vidu2, GLM-Realtime, GLM-TTS) — the two platforms' catalogs differ.
- Release dates come from Z.ai international release notes; dates for China-side availability may differ slightly.
- web_search and Tavily were unavailable during this research (provider disabled / quota exceeded); all facts above come from direct fetches of official pages.
