# Moonshot Kimi research (fetched 2026-09-20)

## Sources used

- https://www.moonshot.cn/ (company site, CN) — fetched 2026-09-20
- https://www.moonshot.cn/about (company profile page) — fetched 2026-09-20
- https://www.moonshot.ai/ (company site, EN) — fetched 2026-09-20
- https://github.com/MoonshotAI (org page) — fetched 2026-09-20
- https://github.com/MoonshotAI/Kimi-K3 (README) — fetched 2026-09-20
- https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE — fetched 2026-09-20
- https://github.com/MoonshotAI/Kimi-K2.5 (README) — fetched 2026-09-20
- https://raw.githubusercontent.com/MoonshotAI/Kimi-K2.5/master/LICENSE — fetched 2026-09-20
- https://www.kimi.com/blog/kimi-k3 (K3 launch tech blog) — fetched 2026-09-20 (dated 2026-07-16 per moonshot.cn research list)
- https://platform.kimi.ai/docs/llms.txt (docs index) — fetched 2026-09-20
- https://platform.kimi.ai/docs/models.md (model list) — fetched 2026-09-20
- https://platform.kimi.ai/docs/pricing/chat (pricing) — fetched 2026-09-20
- https://platform.kimi.ai/docs/api/overview.md (API overview) — fetched 2026-09-20
- https://platform.kimi.ai/docs/api/models-overview.md (parameter reference) — fetched 2026-09-20
- https://platform.kimi.ai/docs/api/chat.md (Chat Completions spec) — fetched 2026-09-20
- https://platform.kimi.ai/docs/guide/kimi-k3-quickstart.md (K3 guide) — fetched 2026-09-20

Note: `platform.moonshot.ai` now redirects to `platform.kimi.ai`; `moonshotai.com` returned no content (see Conflicts).

## Company facts

- Official name (EN): Moonshot AI
- Official name (CN): 月之暗面 ("月之暗面（Moonshot AI）正式成立" — moonshot.cn/about)
- Founded: officially stated as "Spring 2023" (2023年春天) on moonshot.cn/about. Exact day not stated on that page.
- HQ address (official, CN site): 北京市海淀区知春路76号京东科技大厦1栋13层 / 13F, Building 1, JD Technology Building, 76 Zhichun Road, Haidian District, Beijing
- Company websites: https://www.moonshot.ai (EN), https://www.moonshot.cn (CN), product at https://www.kimi.com / https://www.kimi.ai
- API platform: https://platform.kimi.ai (global); CN console linked as https://platform.kimi.com (from moonshot.cn nav)
- Docs: https://platform.kimi.ai/docs (index: /docs/llms.txt)
- GitHub: https://github.com/MoonshotAI
- Hugging Face: https://huggingface.co/moonshotai ; ModelScope: https://modelscope.cn/organization/moonshotai
- Blog: https://www.kimi.com/blog/ ; careers: https://careers.kimi.com
- Contact (official): growth@moonshot.cn, globalpr@moonshot.ai
- Slogan (EN site): "Seeking the optimal conversion from energy to intelligence"
- Developer community: Discord (discord.gg/TYU2fdJykW) and forum.moonshot.ai

## Models

### API models (current, per platform.kimi.ai/docs/models.md, fetched 2026-09-20)

| Model ID | Description (official) |
|---|---|
| `kimi-k3` | Flagship: "Kimi's most capable model to date, with 2.8 trillion parameters, native visual understanding, and a 1M-token context window" — for software engineering, knowledge work, deep reasoning |
| `kimi-k2.7-code` | Dedicated coding model; context 256K; thinking always on |
| `kimi-k2.7-code-highspeed` | Same model as k2.7-code; ~180 tokens/s output, up to 260 tokens/s in short contexts |
| `kimi-k2.6` | Visual + text input; thinking and non-thinking modes; dialogue and agent tasks; context 256K (blog dated 2026-04-20) |

Deprecated (per docs/models.md): `kimi-k2.5` and `moonshot-v1*` discontinued 2026-08-31; `kimi-k2*` series discontinued 2026-05-25; `kimi-latest` 2026-01-28; `kimi-thinking-preview` 2025-11-11.

### Kimi K3 (open-weight flagship)

- Family: Kimi K-series. Exact release date: launch blog 2026-07-16 (per moonshot.cn research listing); weights "released by July 27, 2026" per launch blog.
- Architecture (per GitHub README): MoE; 2.8T total params; 104B activated; 93 layers (1 dense); 896 experts, 16 selected/token + 2 shared; 160K vocab; attention = 69 KDA + 24 Gated MLA layers; hidden dim 7168; SiTU-GLU; vision encoder MoonViT-V2 (401M params); quantization MXFP4 weights / MXFP8 activations (QAT)
- Context window: 1,048,576 tokens (1M)
- Max output (API): `max_completion_tokens` default 131,072, settable up to 1,048,576 (chat.md spec)
- Open weights: YES ("Open Frontier Weights", full weights on HF). License: "Kimi K3 License" (custom — permissive MIT-style, but: Model-as-a-Service operators with >$20M aggregate revenue over any 12 months must sign a separate agreement with Moonshot AI; products with >100M MAU or >$20M monthly revenue must display "Kimi K3" in UI)
- Capabilities (official): always-on thinking with `reasoning_effort` low/high/max (default max); native vision (text + image per arch table; marketing text also says video); long-horizon coding/agentic; tool calling (`tool_choice` auto/none/required); structured output (JSON schema); streaming with reasoning_content. Temperature fixed 1.0, top_p 0.95 (cannot be modified).
- API availability: yes, `kimi-k3` on platform.kimi.ai (unlocked after min $1 top-up); also on kimi.ai app, Kimi Work, Kimi Code. Weights on HF/ModelScope. Region specifics: not stated on fetched pages.
- Audio: not stated for K3 (no audio modality claimed in fetched docs).
- K3 benchmarks: see Benchmarks section.

### Kimi K2.5 (open-source, now deprecated on API)

- Open-source native multimodal agentic model; continual pretraining on ~15T mixed visual+text tokens atop Kimi-K2-Base. 1T total / 32B activated; 256K context; MLA attention; MoonViT (400M) vision encoder. Thinking + Instant modes. License: Modified MIT License (attribution required if product >100M MAU or >$20M monthly revenue).
- API model `kimi-k2.5` officially discontinued 2026-08-31 (use kimi-k3).

### Other official open releases (GitHub org)

- Kimi K2: open-source MoE, 32B activated / 1T total (superseded)
- Kimi K1.5: o1-level multimodal reasoning tech report
- Kimi-Linear, MoBA, Attention Residuals, FlashKDA, MoonEP (architecture/infra)
- Kimi-VL, Kimi-Audio, Kimina-Prover-Preview, Moonlight (Muon) (research)
- kimi-code / kimi-cli: coding agent CLI (~7.5k stars)
- Benchmarks published by Moonshot: WorldVQA, PerceptionBench, CombiBench, Kimi Code Bench 2.0

## Pricing

Source: https://platform.kimi.ai/docs/pricing/chat (fetched 2026-09-20). USD, per 1M tokens (1M = 1,000,000). Prices exclude taxes. Effective date: not stated on page.

### K3 series

| Model | Cache write (TTL 5min) | Cache write (TTL 1h) | Cached input | Input | Output | Context |
|---|---|---|---|---|---|---|
| kimi-k3 | $3.00 | $6.00 | $0.30 | $3.00 | $15.00 | 1,048,576 tokens |

Caching is automatic on repeated prefixes; cache hits billed only at cached-input price.

### K2 series

| Model | Input (cache hit) | Input (cache miss) | Output | Context |
|---|---|---|---|---|
| kimi-k2.7-code | $0.19 | $0.95 | $4.00 | 262,144 tokens |
| kimi-k2.7-code-highspeed | $0.38 | $1.90 | $8.00 | 262,144 tokens |
| kimi-k2.6 | $0.16 | $0.95 | $4.00 | 262,144 tokens |

Notes: pay-as-you-go only, no subscription (docs). File upload/extraction APIs temporarily free. Batch API pricing on separate page (/docs/pricing/batch) — not fetched in detail. K3 access requires min $1 top-up.

## API facts

- Service address: `https://api.moonshot.ai`
- Endpoints (per /docs/api/overview.md):
  - OpenAI Chat Completions: base_url `https://api.moonshot.ai/v1`, POST `/chat/completions`
  - OpenAI Responses: `https://api.moonshot.ai/v1`, POST `/responses`
  - Anthropic Messages: base_url `https://api.moonshot.ai/anthropic`, POST `/anthropic/v1/messages`
  - Others: GET /v1/models; POST /v1/tokenizers/estimate-token-count; GET /v1/users/me/balance; POST /v1/tools/search, /v1/tools/search_pro, /v1/tools/fetch; files (/v1/files); batches (/v1/batches)
- Auth: API key header `Authorization: Bearer $MOONSHOT_API_KEY` (keys managed in platform console)
- Streaming: YES — SSE (`stream=True`), with separate `reasoning_content` and `content` deltas
- Compatible SDKs: official OpenAI and Anthropic SDKs; LangChain, Dify, Coze noted
- Model controls: kimi-k3 uses top-level `reasoning_effort` (low/high/max, default max); kimi-k2.x use `thinking` param; temperature/top_p/n/penalties fixed and must not be passed
- Other capabilities: JSON mode / structured output, partial mode, context caching, web search tools, file upload for text/image/video, batch API

## Benchmarks (vendor-reported)

All below are vendor-published (Moonshot AI), from the respective GitHub READMEs / tech report.

### Kimi K3 (repo README, 2026; reasoning effort=max, temp=1.0)

- GPQA Diamond: 93.5
- HLE-Full: 43.5 (56.0 with tools)
- DeepSWE: 67.5 (67.3 with mini-SWE-agent harness)
- Terminal-Bench 2.1: 88.3
- FrontierSWE: 81.2
- SWE-Marathon: 42.0
- ProgramBench: 77.8
- BrowseComp: 91.2 (90.4 with full 1M context, no compaction)
- DeepSearchQA (F1): 95.0
- MMMU-Pro: 81.6 (83.4 with tools)
- Video-MME (w. sub): 90.0
- ZeroBench (pass@5): 23.0 (41.0 with tools)
- URL: https://github.com/MoonshotAI/Kimi-K3 (some comparison scores cited from Artificial Analysis as of July 23, 2026)

### Kimi K2.5 (repo README; thinking mode)

- HLE-Full: 30.1 (50.2 w/ tools); AIME 2025: 96.1 (avg@32); GPQA-Diamond: 87.6 (avg@8)
- SWE-Bench Verified: 76.8; Terminal-Bench 2.0: 50.8
- MMMU-Pro: 78.5; OCRBench: 92.3; VideoMME: 87.4; MMVU: 80.4
- BrowseComp: 60.6 (74.9 w/ ctx mgmt; 78.4 Agent Swarm)
- Longbench v2: 61.0; AA-LCR: 70.0
- URL: https://github.com/MoonshotAI/Kimi-K2.5

## Conflicts / uncertainty notes

1. **K3 modality**: repo architecture table lists Modality = "Text, Image", while the same README's description and the launch blog say K3 "understands text, images, and video". The API guide does show a video input example for kimi-k3 (video_url / ms:// file ids). Treat video support as officially documented in API but inconsistent in the model card.
2. **Founded date**: official about page says only "Spring 2023"; no exact day/official registration date stated. Do not cite a specific date.
3. **Pricing effective date**: not stated on the pricing page; prices are as fetched on 2026-09-20.
4. **Max output for K2.x**: official chat.md only explicitly documents K3 defaults (131,072 default / 1,048,576 max); K2.x max output not stated in fetched portion — context is 256K but max_completion_tokens ceiling unconfirmed.
5. **Domain migration**: moonshotai.com no longer serves readable content; platform.moonshot.ai redirects to platform.kimi.ai; CN platform is platform.kimi.com. Old "Moonshot" branding persists in API URLs (api.moonshot.ai).
6. **K3 benchmark comparators**: K3 README compares against models including "Claude Fable 5", "GPT-5.6 Sol", "GLM-5.2" etc. Some competitor scores re-evaluated by Moonshot or cited from third parties (Artificial Analysis, Vals AI, official leaderboards) — treat the whole table as vendor-reported.
7. **K2.5 benchmark caveats**: comparisons marked * were re-evaluated by Moonshot; GPT-5.2-xhigh had ~10% failure rate on vision benchmarks (may underestimate).
8. **K3 launch timeline**: blog dated 2026-07-16 (per moonshot.cn listing); weights by 2026-07-27; K3 tech report (PDF in repo) is the authoritative benchmark document.
9. **K3 API pricing vs open weights**: API model `kimi-k3` ($3/$15 per 1M) is the hosted version of the open-weight Kimi K3; open-weight self-hosting costs are not Moonshot's pricing.
