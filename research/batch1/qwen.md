# Qwen research (fetched 2026-09-20)

## Sources used
- https://qwen.ai/ — official Qwen portal (fetched; JS-rendered, only page title "Qwen" extractable)
- https://www.alibabacloud.com/help/en/model-studio/models — Alibaba Cloud Model Studio: Recommended models
- https://www.alibabacloud.com/help/en/model-studio/text-generation-model — Text generation model list (current + legacy)
- https://www.alibabacloud.com/help/en/model-studio/model-pricing — Model inference pricing (redirect target of /billing; all prices USD)
- https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max — qwen3.8-max model detail (capabilities, context limits, pricing, rate limits, snapshots)
- https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash — qwen3.8-flash model detail
- https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope — OpenAI-compatible API (BASE_URL, auth, streaming)
- https://github.com/QwenLM — GitHub org (pinned repos)
- https://github.com/QwenLM/Qwen3.8 — Qwen3.8 open-model repo README (release log, family overview)
- https://huggingface.co/Qwen — HF org
- https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B — flagship open-weight model card (architecture, context, benchmarks)
- https://huggingface.co/api/models/Qwen/Qwen3.8-2.4T-A95B and .../Qwen/Qwen3.8-27B — HF API metadata (license tags, lastModified)
- https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE — license text

## Company facts
- Team: Qwen team, Alibaba Group (GitHub: "the large language model series developed by Qwen team, Alibaba Group"); HF org: "organization of Qwen, which refers to the large language model family built by Alibaba Cloud."
- Official website: https://qwen.ai/ (portal; body content JS-rendered — not extractable by simple fetch)
- Consumer chat: Qwen Studio / Qwen Chat at https://chat.qwen.ai/
- API/docs: Alibaba Cloud Model Studio (Bailian), https://www.alibabacloud.com/help/en/model-studio/ ; managed API product also at https://www.qwencloud.com
- GitHub: https://github.com/QwenLM
- HuggingFace: https://huggingface.co/Qwen
- ModelScope: https://www.modelscope.cn/organization/Qwen (mirror for China users)
- Related products (per Qwen3.8 README): Qoder (agentic coding, qoder.com), QwenWork (qwenwork.cn), Qwen Code (open-source terminal agent, qwen.ai/qwencode), Qwen Cloud (managed inference, qwencloud.com)
- Naming: official docs sample model reply uses Chinese name 千问 ("我叫千问"); the full "Tongyi Qianwen / 通义千问" branding was NOT explicitly confirmed on the fetched English pages — see conflicts.

## Models

### Current flagship API models (Alibaba Cloud Model Studio, text generation)
- qwen3.8-max — flagship. 2.4T-parameter MoE. Context window 1,000,000 tokens; max input 991,808; max output 131,072; max chain-of-thought 262,144. Input modalities: Image, Text, Video; output: Text. Supports thinking (enable_thinking) and non-thinking modes, function calling, structured outputs, web search, prefix completion, context caching, batch inference (Beijing only). Fine-tuning unsupported. Regions: China (Beijing), Singapore (International scope), Hong Kong, Frankfurt, US (Virginia), Tokyo (Global scope). Snapshot: qwen3.8-max-0902 (alias qwen3.8-max-2026-09-02), upgraded coding/vision snapshot. Source: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max
- qwen3.7-plus — balanced performance/cost, 1M context, thinking, function calling, built-in tools; current snapshot equivalent qwen3.7-plus-2026-05-26. Source: text-generation-model page.
- qwen3.8-flash — lightweight/low-cost, 1M context (max input 991,808, max output 131,072, CoT 262,144); multimodal input (Image/Text/Video), text output; "fully compatible with both OpenAI and Anthropic API protocols". Context caching supported; batch inference unsupported. Source: https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash
- qwen3.7-flash — 1M context; snapshot equivalent qwen3.7-flash-2026-07-15; batch discount 50% (Singapore/Beijing).
- Legacy tiers still listed: qwen-max, qwen-plus, qwen-flash, qwen-turbo (qwen-turbo "will no longer be updated; switch to Qwen-Flash"), qwq-plus, qwen-long (10M context), qwen-mt-* (translation, 16k), qwen3-max / qwen3-235b-a22b / qwen3-32b … (open Qwen3 series served via API), Qwen3-Coder models.

### Flagship open-weight releases (GitHub QwenLM / HF Qwen)
- Qwen3.8-2.4T-A95B — first Qwen-Max-class open release. MoE: 2.4T total / 95B activated, 512 experts, 10 routed + 1 shared activated per token, 92 layers, Gated DeltaNet + Gated Attention hybrid. Text-only; thinking-only (thinking cannot be disabled); reasoning_effort xhigh/medium/low. Native context 262,144 tokens, extensible to 1,010,000. Released 2026-08-12 (HF lastModified 2026-08-12T10:24Z; GitHub announcement). License: "Qwen3.8-Max License" — custom MIT-style license: unrestricted use/copy/modify/sell, but (1) products with >100M MAU or >US$20M/month revenue must display the model name; (2) Model-as-a-Service or AI Work Assistant businesses with >US$50M/12-month aggregate revenue need a separate license from Qwen. Not gated. ~56,249 downloads at fetch time. Sources: HF model card, HF API, LICENSE file.
- Qwen3.8-27B — released 2026-08-14 (HF lastModified 2026-08-14T15:00Z). License: Apache-2.0 (HF API tag license:apache-2.0).
- Qwen3.6-35B-A3B (2026-04-16), Qwen3.6-27B (2026-04-22); Qwen3.5-397B-A17B (2026-02-16), Qwen3.5-122B-A10B / 35B-A3B / 27B (2026-02-24), Qwen3.5-9B/4B/2B/0.8B (2026-03-02); Qwen3-Next-80B-A3B (2025-09-11). All dates from the QwenLM/Qwen3.8 README release log.
- Qwen3.5 family notes (README): unified vision-language foundation, Gated DeltaNet + sparse MoE, RL scaled across million-agent environments, 201 languages/dialects.

## Pricing
All prices USD per 1 million tokens, from https://www.alibabacloud.com/help/en/model-studio/model-pricing (English page shows USD only; CNY values not on this page). Effective date not stated on page (live list). Some models carry limited-time discounts shown in console.

- qwen3.8-max: Singapore (International): input $2 / output $6. Beijing: $1.65 / $4.951 (batch: 50% → $0.825 / $2.475). Hong Kong / Frankfurt / US Virginia / Tokyo (Global): $1.65 / $4.951.
  - Context cache (Beijing/Global): implicit cache hit $0.206; explicit cache creation $2.063; explicit cache read $0.137. Singapore: hit $0.25, creation $2.5, read $0.17.
- qwen3.8-flash: Singapore $0.15 / $0.47. Beijing & all Global regions: $0.113 / $0.382. Cache hits $0.016 (SG) / $0.014 (Beijing/Global); explicit creation $0.2 (SG) / $0.177; read $0.016/$0.014.
- qwen3.7-plus: Singapore: ≤256K $0.4 in / $1.6 out; 256K–1M $1.2 / $4.8 (list prices; limited-time 20% off shown in console). Beijing: ≤256K $0.276 / $1.101; 256K–1M $0.826 / $3.301. Thinking mode billed same as output.
- qwen3.7-flash: Singapore tiered: ≤32K $0.030/$0.130; 32K–256K $0.100/$0.400; 256K–1M $0.200/$0.800. Beijing: $0.028/$0.110; $0.083/$0.330; $0.165/$0.660. Batch 50% (SG & Beijing).
- qwen3.6-plus: SG ≤256K $0.5/$3; 256K–1M $2/$6. qwen3.6-flash: SG ≤256K $0.25/$1.5; 256K–1M $1/$4.
- qwen3-max (legacy flagship): SG tiered ≤32K $1.2/$6; ≤128K $2.4/$12; ≤256K $3/$15. Beijing tiered $0.359/$1.434; $0.574/$2.294; $1.004/$4.014.
- qwen-turbo (legacy, discontinued updates): SG $0.05 in / $0.2 out non-thinking, $0.5 thinking. Beijing $0.044 / $0.087 / $0.431.
- qwq-plus: SG $0.8 / $2.4; Beijing $0.230 / $0.574.
- qwen-long-latest: Beijing $0.072 / $0.287.
- qwen3.8-omni-flash: Singapore $0.15 input / $0.016 cache-hit input / $0.47 output per 1M tokens.
- Free quota: 1 million tokens for many models (incl. qwen3.8-max, qwen3.7-plus, qwen3.8-flash) in Singapore only; valid 90 days from activation/model release/approval, whichever is later.
- General rules: batch inference = 50% of real-time price (input+output) where supported; cache and batch discounts cannot combine; explicit cache creation billed at 125% of standard input price (per page note).

## API facts
- Protocol: OpenAI-compatible Chat Completions (also Responses API; qwen3.8-flash also Anthropic-protocol compatible). Source: compatibility page + qwen3.8-flash page.
- BASE_URL (OpenAI-compatible mode):
  - Singapore: https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1
  - Beijing: https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1 (migration target; page table lists an ap-southeast-1 URL for Beijing — see conflicts)
  - Hong Kong: https://{WorkspaceId}.cn-hongkong.maas.aliyuncs.com/compatible-mode/v1
  - Japan (Tokyo): https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1
  - US (Virginia): https://dashscope-us.aliyuncs.com/compatible-mode/v1
- Full endpoint (HTTP): POST …/compatible-mode/v1/chat/completions
- Auth: API key (env var DASHSCOPE_API_KEY), obtained in Model Studio console; keys are region-bound (key must be created in the same region as the endpoint).
- Streaming: supported (stream=True; stream_options={"include_usage": True} for token usage in stream).
- Thinking mode: enable_thinking parameter (chat_template_kwargs on self-hosted open weights); reasoning.effort in Responses API.
- Rate limits: Beijing/Singapore dynamic (TPM tiered by monthly spend). Frankfurt/US/Tokyo/HK (Global): 30,000 RPM, 5,000,000 TPM for qwen3.8-max and qwen3.8-flash.

## Benchmarks (vendor-reported)
From the official Qwen3.8-2.4T-A95B model card benchmark table (published Aug 2026, Qwen3.8-Max column; scores as stated by vendor — label: vendor_reported). Source: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
- Coding/agent: Terminal Bench 2.1: 86.6 · SWE-bench Pro: 67.7 · DeepSWE 1.1: 56.6 · FrontierSWE: 73.5 · PaperBench: 93.0 · AndroidBench: 75.1 · QwenSWEBench: 80.7 · NL2Repo-Bench: 55.9 · MLS-Bench-Lite: 41.0
- General agent: CoWorkBench: 74.8 · WorkSpaceBench: 67.7 · JobBench: 53.4 · SkillsBench: 70.2 · WideSearch: 81.9 · HLE w/ tools: 56.2 · Automation-Bench (Pass@1): 27.3 · Toolathlon Verified (Pass@1): 72.5
- General capabilities: GPQA Diamond: 92.6 · HLE: 43.6 · IFBench: 82.8 · $OneMillion-Bench (expert): 52.5 · HealthBench: 60.2 · PLawBench: 73.2 · MRCR v2 256K (8-needle): 92.9 · LongBench v2: 66.3
- Comparison columns in the same table: Claude Opus 4.8, Fable 5, GPT 5.6 Sol, Qwen3.7-Max (see model card for full table and footnotes).
No other official benchmark pages were fetched (qwen.ai blog is JS-rendered and unfetchable).

## Conflicts / uncertainty notes
- qwen.ai portal and blog pages are JS-rendered: only the title "Qwen" was extractable; release blog (https://qwen.ai/blog?id=qwen3.8) content could not be verified via fetch. Tavily quota was exhausted and web_search was unavailable, so no fallback search was possible.
- "Tongyi Qianwen / 通义千问" official branding was not explicitly seen on the fetched English pages; docs sample response only shows the Chinese name 千问. Treat the English alias "Tongyi Qianwen" as widely used but unverified in this fetch.
- The OpenAI-compatibility page's BASE_URL table lists an ap-southeast-1 URL for the Beijing region while the migration note says Beijing should use {WorkspaceId}.cn-beijing.maas.aliyuncs.com — inconsistent on the page itself; both recorded above.
- Pricing page shows USD only (English site); CNY list prices would require the Chinese console/pricing page (not fetched). Some prices carry limited-time discounts (e.g., qwen3.7-plus 20% off listed in console); list prices recorded here.
- Exact release date of the qwen3.8-max API model is not stated on the fetched pages; the open-weight Qwen3.8-2.4T-A95B was released 2026-08-12, the 27B on 2026-08-14, and the qwen3.8-max-0902 snapshot is dated 2026-09-02 (per snapshot alias qwen3.8-max-2026-09-02). Blog citation says August 2026.
- Qwen3.8-2.4T-A95B open weights are text-only and thinking-only; vision input, non-thinking mode, and 1M default context are described as Qwen3.8-Max (API) extras on the model card.
- qwen3.8-max page shows "Batch Inference: Supported" only in China (Beijing); other regions list Unsupported.
