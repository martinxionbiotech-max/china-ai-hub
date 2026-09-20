# DeepSeek research (fetched 2026-09-20)

## Sources used
- https://api-docs.deepseek.com/ — API docs home
- https://api-docs.deepseek.com/quick_start/pricing — Models & Pricing page
- https://api-docs.deepseek.com/updates — official Change Log
- https://api-docs.deepseek.com/news/news260910 — V4.1-Flash announcement
- https://www.deepseek.com/ — official site (zh)
- https://www.deepseek.com/en/ — official site (en)
- https://www.deepseek.com/en/transparency/ — Transparency Center
- https://www.deepseek.com/en/news/v4-preview/ — V4 Preview release
- https://www.deepseek.com/en/news/deepseek-v4-1-flash/ — V4.1-Flash release
- https://www.deepseek.com/en/news/deepseek-v3-2/ — V3.2 release
- https://www.deepseek.com/en/news/r1-0528/ — R1-0528 release
- https://github.com/deepseek-ai — GitHub org
- https://api.github.com/orgs/deepseek-ai/repos — GitHub API repo list
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash — HF model card
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro — HF model card
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash — HF model card
- https://huggingface.co/deepseek-ai/DeepSeek-V3.2 — HF model card
- https://huggingface.co/api/models?author=deepseek-ai — HF API model list

## Company facts
- Official English name: **DeepSeek** (site title "DeepSeek | 深度求索") — https://www.deepseek.com/en/
- Chinese name/alias: **深度求索** — https://www.deepseek.com/
- Registered company name: **杭州深度求索人工智能基础技术研究有限公司** (shown in official site footer copyright) — https://www.deepseek.com/
- Founded: not publicly disclosed on official pages fetched (no official about page states it)
- Headquarters: Hangzhou — not printed verbatim on fetched pages, but the official footer company name includes 杭州 (Hangzhou), and the site carries Zhejiang ICP filing 浙ICP备2023025841号 and Hangzhou public-security filing 浙公网安备33010502011812号 — https://www.deepseek.com/
- Official website: https://www.deepseek.com/ (EN: https://www.deepseek.com/en/)
- API docs: https://api-docs.deepseek.com/
- API platform (keys/console): https://platform.deepseek.com/
- GitHub org: https://github.com/deepseek-ai
- Hugging Face org: https://huggingface.co/deepseek-ai
- Products: web chat (https://chat.deepseek.com/), mobile apps, API platform, DeepSeek Harness (developer preview) — https://api-docs.deepseek.com/
- Official accounts: Twitter @deepseek_ai, Discord (links in API docs footer) — https://api-docs.deepseek.com/
- Transparency Center lists released models with release dates: V4.0 "DeepSeek-V4 New" April 24, 2026; V3.2 December 1, 2025 — https://www.deepseek.com/en/transparency/

## Models

### deepseek-flash (DeepSeek-V4.1-Flash) — current API model
- Exact API model name: `deepseek-flash`; model version DeepSeek-V4.1-Flash — https://api-docs.deepseek.com/quick_start/pricing
- Family: DeepSeek-V4.1 (smallest of new "asymmetric architecture" family) — https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- Release date: 2026-09-10 (announcement; pricing effective 04:00 UTC same day) — https://api-docs.deepseek.com/updates
- Architecture: 552B-parameter MoE; Causal Encoder–Decoder; 8B active params (input) / 16B (output) — https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- Context window: 1M tokens — https://api-docs.deepseek.com/quick_start/pricing
- Max output tokens: maximum 384K — https://api-docs.deepseek.com/quick_start/pricing
- Open weights: yes — https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash (announced in https://api-docs.deepseek.com/news/news260910)
- License: MIT — https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
- Capabilities (per official docs): thinking (default) + non-thinking modes; native multimodal/vision understanding; JSON output; tool calls; Responses API; Anthropic API; Chat Prefix Completion (Beta); FIM (Beta, non-thinking only) — https://api-docs.deepseek.com/quick_start/pricing
- API availability: yes as `deepseek-flash`; legacy names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` still accepted but retired, routed to V4.1-Flash and billed at Flash price — https://api-docs.deepseek.com/quick_start/pricing
- KV cache vs previous generation: 1/4 the HBM, 1/8 the SSD storage (vendor claim) — https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- Regions: not stated in API docs; HF repo tagged `region:us` — https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

### deepseek-v4-pro (DeepSeek-V4-Pro-0813) — current API model (deprecation announced)
- Exact API model name: `deepseek-v4-pro`; model version DeepSeek-V4-Pro-0813 — https://api-docs.deepseek.com/quick_start/pricing
- Family: DeepSeek-V4; 1.6T total / 49B active params — https://www.deepseek.com/en/news/v4-preview/
- Release date: V4 Preview open-sourced & live on API 2026-04-24; GA update (V4-Pro-0813) rolled out on App/Web/API 2026-08-13 — https://www.deepseek.com/en/news/v4-preview/ and https://api-docs.deepseek.com/updates
- Context window: 1M tokens — https://api-docs.deepseek.com/quick_start/pricing
- Max output tokens: maximum 384K — https://api-docs.deepseek.com/quick_start/pricing
- Open weights: yes — https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (weights last modified 2026-06-22)
- License: MIT — https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Capabilities (per official docs): thinking (default) + non-thinking modes; JSON output; tool calls; Responses API; Anthropic API; Chat Prefix Completion (Beta); FIM (Beta, non-thinking only); vision NOT supported — https://api-docs.deepseek.com/quick_start/pricing
- Thinking effort levels: low / high / max (V4-Pro and V4-Flash) — https://api-docs.deepseek.com/updates (2026-08-13 entry)
- API availability: yes; per Change Log 2026-09-10, "we have decided to continue providing API services for DeepSeek V4 Pro after September 14, 2026, with the billing method remaining unchanged" — https://api-docs.deepseek.com/updates
- Regions: not stated in API docs; HF repo tagged `region:us` — https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Vendor positioning: "open-source SOTA in Agentic Coding benchmarks; leads all current open models in world knowledge, trailing only Gemini-3.1-Pro; beats all current open models in Math/STEM/Coding" — https://www.deepseek.com/en/news/v4-preview/

### DeepSeek-V4-Flash (retired from API 2026-09-10; open weights remain)
- Family: DeepSeek-V4; 284B total / 13B active params — https://www.deepseek.com/en/news/v4-preview/
- Release: 2026-04-24 (V4 Preview); API public beta update 2026-07-31; retired 2026-09-10 (name routes to V4.1-Flash) — https://api-docs.deepseek.com/updates
- Open weights: yes, MIT — https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
- Context: 1M (V4 family standard) — https://www.deepseek.com/en/news/v4-preview/

### DeepSeek-V4-Flash-Vision-Exp (experimental multimodal, retired 2026-09-10)
- Release: 2026-08-21 on API (`deepseek-v4-flash-vision-exp`), experimental; retired 2026-09-10, requests route to V4.1-Flash — https://api-docs.deepseek.com/updates
- Vendor claim: multimodal agent capabilities "close to Opus-4.8"; pure-text on par with V4-Flash — https://api-docs.deepseek.com/updates

### DeepSeek-V3.2 (flagship open-weight; replaced on API by V4 family)
- Release date: 2025-12-01 — https://www.deepseek.com/en/news/deepseek-v3-2/ and https://www.deepseek.com/en/transparency/
- Open weights: yes; license MIT — https://huggingface.co/deepseek-ai/DeepSeek-V3.2
- Vendor claims: "GPT-5 level performance" (V3.2); V3.2-Speciale rivals Gemini-3.0-Pro and attained gold-medal results in IMO, CMO, ICPC World Finals & IOI 2025 (no numeric scores on release page) — https://www.deepseek.com/en/news/deepseek-v3-2/
- Context window: not stated on fetched pages
- Note: V3.2-Speciale was API-only, no tool calls, temporary endpoint expired 2025-12-15 — https://www.deepseek.com/en/news/deepseek-v3-2/

### DeepSeek-R1-0528
- Release date: 2025-05-28 — https://www.deepseek.com/en/news/r1-0528/
- Open weights: yes — https://www.deepseek.com/en/news/r1-0528/ (links to HF); R1 family GitHub repo license MIT — https://github.com/deepseek-ai (repo list API)
- Features stated: JSON output & function calling support — https://www.deepseek.com/en/news/r1-0528/
- Context window: not stated on fetched pages

### Other open releases (from official GitHub org, one line each)
- DeepSeek-V3.2-Exp: 2025-09-29, MIT, introduced DeepSeek Sparse Attention (DSA), API prices cut 50%+ — https://api-docs.deepseek.com/updates + https://api.github.com/orgs/deepseek-ai/repos
- DeepSeek-V3: MIT — https://api.github.com/orgs/deepseek-ai/repos
- DeepSeek-R1: MIT — https://api.github.com/orgs/deepseek-ai/repos
- DeepSeek-Math-V2: Apache-2.0 — https://api.github.com/orgs/deepseek-ai/repos
- DeepSeek-OCR: MIT; DeepSeek-OCR-2: Apache-2.0 — https://api.github.com/orgs/deepseek-ai/repos
- Infra/kernel libs: DeepEP, FlashMLA, DeepGEMM, DeepSelect, DualPipe, 3FS, smallpond, EPLB, DeepSpec, deepseek-recipe — MIT — https://api.github.com/orgs/deepseek-ai/repos
- GitHub org hosts NO DeepSeek-V4 repo; V4 family weights are on Hugging Face only — https://github.com/deepseek-ai

## Pricing
Source: https://api-docs.deepseek.com/quick_start/pricing — USD, per 1M tokens. Current pricing effective 04:00 UTC 2026-09-10 (https://www.deepseek.com/en/news/deepseek-v4-1-flash/); peak/off-peak scheme introduced effective 16:00 UTC 2026-08-16 (https://api-docs.deepseek.com/updates, 2026-08-13 entry).

### deepseek-flash
- Input (cache miss): $0.15 off-peak / $0.30 peak
- Input (cache hit / cached): $0.003 off-peak / $0.006 peak
- Output: $0.60 off-peak / $1.20 peak
- Concurrency limit: 2500

### deepseek-v4-pro
- Input (cache miss): $0.66 off-peak / $1.32 peak
- Input (cache hit / cached): $0.022 off-peak / $0.044 peak
- Output: $1.98 off-peak / $3.96 peak
- Concurrency limit: 500

### Notes
- Off-peak rates are 50% of peak rates. Peak hours: 01:00–04:00 and 06:00–10:00 UTC, Monday–Friday, excluding Chinese public holidays; all other hours (incl. weekends and Chinese public holidays in full) are off-peak — https://api-docs.deepseek.com/quick_start/pricing
- Batch pricing: none listed on the pricing page
- Deduction: billed by tokens × price, deducted from topped-up or granted balance (granted first) — https://api-docs.deepseek.com/quick_start/pricing
- Legacy names `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` are billed at the Flash price — https://api-docs.deepseek.com/quick_start/pricing

## API facts
- Endpoint base URL (OpenAI-compatible): https://api.deepseek.com — https://api-docs.deepseek.com/
- Endpoint base URL (Anthropic-compatible): https://api.deepseek.com/anthropic — https://api-docs.deepseek.com/
- Auth: Bearer token API key; keys created at https://platform.deepseek.com/api_keys — https://api-docs.deepseek.com/
- Streaming: yes — "set the stream parameter to true to get stream response" — https://api-docs.deepseek.com/
- Formats/features: Chat Completions, native Responses API (adapted for Codex), Anthropic API, JSON mode, tool calls, Files API, context caching (KV cache), FIM (Beta, non-thinking only), Chat Prefix Completion (Beta) — https://api-docs.deepseek.com/ and https://api-docs.deepseek.com/quick_start/pricing
- Thinking mode: both current models support non-thinking and thinking; thinking is default; `reasoning_effort` low/high/max on V4-Pro/V4-Flash — https://api-docs.deepseek.com/quick_start/pricing and https://api-docs.deepseek.com/updates
- Rate limits & concurrency: see pricing table above; details at /quick_start/rate_limit — https://api-docs.deepseek.com/quick_start/pricing

## Benchmarks (vendor-reported)
All from the official API docs Change Log (https://api-docs.deepseek.com/updates). Label: vendor_reported; dates = changelog entry dates; metric = score as published.

DeepSeek-V4.1-Flash (entry 2026-09-10):
- GPQA Diamond: 90.9
- HLE: 36.8 (39.1 on pure-text subset only*)
- Codeforces (Rating): 3471
- MathArena Apex: 65.6
- Terminal-Bench 2.1: 90.6
- Terminal-Bench 3.0: 30.0
- Terminal-Bench 4.0: 31.2
- DeepSWE v1.1: 74.2
- ProgramBench: 20.3
- NL2Repo-Bench: 65.4
- CyberGym: 88.1
- SEC-Bench Pro: 62.8
- ExploitGym: 15.3
- HLE (w/tools): 63.9
- Automation-Bench: 54.8
- Agents' Last Exam: 31.8
- Chartography (w/tools): 78.9
- BabyVision (w/tools): 89.6
- ZeroBench-main (w/tools): 49.0

DeepSeek-V4-Pro GA / 0813 (entry 2026-08-13):
- HLE (without/with tools): 42.7 / 60.0
- Terminal-Bench 2.1: 87.9
- NL2Repo: 61.5
- Cybergym: 83.3
- DeepSWE: 62.7
- Toolathlon-Verified: 74.1
- Agents' Last Exam: 25.7
- AutomationBench (Public): 31.8
- DSBench-FullStack (internal): 71.1
- DSBench-Hard (internal): 67.2

DeepSeek-V4-Flash (entry 2026-07-31):
- Terminal-Bench 2.1: 82.7
- NL2Repo: 54.2
- Cybergym: 76.7
- DeepSWE: 54.4
- Toolathlon verified: 70.3
- Agent Last Exam: 25.2
- Automation Bench (Public): 25.1
- DSBench-FullStack (internal): 68.7
- DSBench-Hard (internal): 59.6

DeepSeek-V4-Flash-Vision-Exp (entry 2026-08-21):
- Terminal-Bench 2.1: 83.9
- NL2Repo: 57.7
- DeepSWE: 59.3
- DSBench-Hard: 63.6
- AutomationBench (Public): 25.7
- ApexBench (Pass@1): 36.5
- Agents' Last Exam: 27.3
- Chartography: 64.3
- ZeroBench (Pass@5): 35.0

DeepSeek-V3.2 / R1-0528: no numeric benchmark scores on official release pages; qualitative claims only (see Models section).

## Conflicts / uncertainty notes
1. **V4-Pro retirement conflict**: news260910 says "Starting 04:00 UTC Sept 14, 2026, all deepseek-v4-pro requests will route to V4.1-Flash at V4.1-Flash rates, until V4.1-Pro launches". But the Change Log (2026-09-10, same release) says DeepSeek decided to *continue* V4 Pro API service after Sept 14 with unchanged billing. The pricing page still lists separate pro pricing. Treat changelog/pricing as the operative policy; the routing statement appears superseded.
2. HF DeepSeek-V4-Pro weights were last modified 2026-06-22 — unclear whether they correspond to the 0813 GA checkpoint; docs don't clarify.
3. HQ: no page states "Hangzhou" verbatim; it is derived from the official footer company name (杭州深度求索…有限公司) and Chinese filings (Zhejiang ICP + 330105 Hangzhou police filing).
4. Max output: pricing page lists a single "MAXIMUM: 384K" value spanning both models; per-model limits not broken out.
5. Context: pricing page shows "CONTEXT LENGTH 1M" for both current API models; V3.1 was 128K (mentioned in R1-0528 page); V3.2/R1-0528 context not stated on fetched pages.
6. Vendor benchmark notes: V4.1-Flash HLE tested on pure-text subset (*); V4 family code-agent benchmarks used DeepSeek Harness minimal mode, max effort, topp=0.95, temp=1.0; DSBench-FullStack/Hard are internal test sets. All benchmark figures are vendor-reported and not independently verified.
7. No batch API or batch pricing found in docs; if exists, not on the pricing page fetched.
8. DeepSeek Harness is in "developer preview" per API docs home; official guide is at deepseek-harness.github.io.
