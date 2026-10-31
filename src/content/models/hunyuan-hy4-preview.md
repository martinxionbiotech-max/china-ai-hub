---
model_id: hunyuan-hy4-preview
model_name: Hunyuan Hy4 preview
provider: tencent
model_family: Hunyuan Hy
version: preview
release_date: "2026-08-28"
status: preview
architecture: "Mixture-of-Experts: 770B total / 49B active (6.4%), 78 layers (1 dense FFN + 77 MoE), 256 routed + 1 shared expert per layer, top-8 routing, Gated DeepSeek Sparse Attention with IndexCache, plus one native MTP layer (10B total / 0.7B active) for speculative decoding"
parameter_information:
  total_parameters: "770B"
  active_parameters: "49B"
  parameter_precision: "BF16 open weights; separate FP8 quantized release"
context_window: 1000000
maximum_output: null
capabilities:
  reasoning: true
  coding: true
  math: true
  chinese: true
  english: true
  multilingual: true
  vision: false
  audio: false
  video: false
  tool_calling: true
  function_calling: true
  agent_capability: true
open_weight: true
license: "Apache-2.0"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.834
  output_price_per_1m: 2.501
  currency: USD
  effective_date: "2026-08-28"
  pricing_ref: tencent
official_api: true
cloud_providers:
  - Tencent Cloud TokenHub
  - OpenRouter
regions:
  - china
  - international
benchmark_results:
  - benchmark: Tencent internal blind evaluation (163 experts, 203 engineering tasks)
    score: 2.99
    metric: mean rating out of 4.00
    date: "2026-08-28"
    source_type: vendor_reported
    source_url: https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/
known_limitations:
  - Tencent states the preview over-reasons on complex tasks and tends to over-verify its own work
  - Early preview — Tencent says both pre-training and post-training have headroom left
  - Maximum output length is not published
  - Text-only in the preview; visual understanding was announced for the next Hy4 generation, not this one
  - No independent suite is recorded here — the only published comparative result is Tencent's own internal blind evaluation
last_verified: "2026-10-31"
sources:
  - source_name: Tencent — Tencent Releases and Open-Sources Tencent Hy4 preview
    source_url: https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/
    source_type: official
    published_date: "2026-08-28"
    last_verified: "2026-10-31"
    confidence: high
  - source_name: Hy4 preview model card (Hugging Face, tencent/Hy4-preview)
    source_url: https://huggingface.co/tencent/Hy4-preview
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: Hy4 preview model card — Chinese version (README_CN)
    source_url: https://huggingface.co/tencent/Hy4-preview/blob/main/README_CN.md
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: Tencent Hy research site — Hy4
    source_url: https://hy.tencent.com/research/hy4-preview
    source_type: official
    last_verified: "2026-10-31"
    confidence: medium
  - source_name: 智东西 — 汤道生预告混元Hy4，首次加入视觉理解 (via 腾讯新闻)
    source_url: https://news.qq.com/rain/a/20261030A0000M00
    source_type: industry_media
    published_date: "2026-10-30"
    last_verified: "2026-10-31"
    confidence: medium
  - source_name: 财联社 — Hy4 preview开源，下一版模型近期上线
    source_url: https://cls.cn/detail/2467904
    source_type: industry_media
    published_date: "2026-08-28"
    last_verified: "2026-10-31"
    confidence: medium
---

**What it is.** Hunyuan Hy4 preview (2026-08-28) is Tencent's flagship text model: a 770B-total / 49B-active open-weight MoE with a 1M-token context, released under Apache-2.0 in BF16 and FP8. **Why it matters.** It is Tencent's first open-weight model in this database and its first entry in the 1M-context class, and it is priced at roughly 60% of GLM-5.3's input rate — the group is competing on price per token rather than on exclusivity. **Key characteristics.** 78 layers, top-8 routing over 256 experts, Gated Sparse Attention, a native MTP layer for speculative decoding, and a model card that names DeepSeek and GLM as architectural influences. **What a professional should know.** The only published comparative result is Tencent's own internal blind evaluation, in which the company's experts rated Tencent's model against two competitors; it is not an independent benchmark, and no maximum output length is published.

## Architecture and parameters

Hy4 preview is a 770B-total / 49B-active MoE — **6.4% activation**, a conventional frontier ratio, comparable to GLM-5.3's 744B/40B (5.4%) but at a larger absolute scale. The backbone is 78 layers: the first uses a standard dense FFN, and the remaining 77 replace it with MoE blocks carrying 256 routed experts plus one shared expert, activating the top eight routing choices plus the shared one per token. A separate native MTP (multi-token prediction) layer of 10B total / 0.7B active is built in for speculative decoding, which is a serving optimisation as much as an architectural one.

Two details in the model card are worth more than the parameter count. First, the attention module is Gated DeepSeek Sparse Attention with IndexCache, and Tencent's own card says it was "inspired by DeepSeek and GLM". That is unusual candour: a frontier lab naming two domestic competitors as the source of its attention design. China AI Hub analysis indicates the interesting fact is not that architectures converge but that the convergence is now stated openly, which shortens the distance between "different model" and "different training run" considerably.

Second, the MTP layer and the 4-stream residual pathway (iHC) are both inference-efficiency choices. The card claims the model autonomously analysed bottlenecks in its own inference system and optimised operator fusion and communication, lifting end-to-end throughput **31.8%** against baseline. That number is vendor-reported and unverifiable from outside — treat it as a product claim, not a measurement you can audit.

## What the context window actually means

1M tokens, matching the current frontier standard, and with open weights. That combination is rare: until now this database recorded GLM-5.3 and GLM-5.3-Flash as its only open-weight 1M-context models, and Hy4 preview makes a third.

Maximum output length is **not published** on the card or the press release. That matters because the practical shape of a long-context model depends on the input/output split: a 1M window with a modest output cap is a long-document reader; a 1M window with a large output cap is a different product. Without the output figure, the second half of that sentence is unknown, and this record leaves the field empty rather than guessing.

## Pricing implications

USD **0.834** per million input tokens, **2.501** per million output, and **0.042** per million cached input. Three observations follow.

The input-to-output ratio is 3.0x, in line with the market. More important is the cache price: at 5% of the input rate it is one of the most aggressive cache discounts recorded here (GLM-5.3's cached rate is about 18% of its input price). China AI Hub analysis indicates that a cache price this low is aimed squarely at agent loops that re-read the same context many times per task — the same workload WorkBuddy and CodeBuddy generate. The pricing and the product are designed together.

At $0.834 input, Hy4 preview undercuts GLM-5.3 ($1.40) by roughly 40% and sits far below the flagship tier of most Western models. Tencent's framing in the accompanying coverage was explicitly about cost efficiency and resisting the industry-wide price increases of the year — a positioning claim, but one the published rates support arithmetically.

## API, coding, and agent implications

The model is available through Tencent Cloud TokenHub and OpenRouter, and it is the default-class model inside WorkBuddy and CodeBuddy, where it shipped free for two weeks at launch. That vertical integration is the point: Tencent can price the API aggressively because the same weights also drive two first-party products.

The card positions the model for coding, office work, scientific research and game prototyping, and claims it contributed to its own development — proposing changes to training methods, data strategy, evaluation frameworks and low-level operators, running the experiments and iterating. If accurate, that is an early recursive-improvement loop; it is also a claim no external party can verify, since none of the internal experiments are published.

## Open weights and license

Apache-2.0, with weights on Hugging Face, ModelScope, GitCode and CNB, plus a separate FP8 quantized release. This is the permissive end of the range: no custom licence, no acceptable-use rider recorded, no gating described. For enterprises that need to self-host for data reasons, Apache-2.0 removes the legal review that a bespoke Chinese model licence usually demands.

The practical caveat is hardware. A 770B-parameter model in BF16 needs roughly 1.5 TB of weights before any KV cache; the FP8 release halves that but remains a multi-node proposition. Open weights here means "legally permitted", not "runs on your workstation".

## Benchmark interpretation

This record carries exactly one benchmark row, and it is a deliberately unusual one: Tencent's **internal blind evaluation**, in which 163 of the company's experts rated 203 engineering tasks. Hy4 preview scored **2.99 out of 4.00**, ahead of GLM-5.3 at 2.92 and Kimi K3 at 2.94.

Three things have to be said about that number. It is small-margin — the gap to Kimi K3 is 0.05 on a four-point scale, inside any plausible noise band for expert ratings. It is **not comparable** to any public benchmark in this database, because the task set is not published. And it was run by the vendor, on the vendor's tasks, with the vendor's experts, comparing the vendor's model to two competitors. That does not make it dishonest; it makes it a marketing artefact until someone reproduces it.

The Hugging Face card also surfaces third-party leaderboard entries across several public evaluations. Those are not transcribed here, because the scores are presented in a widget without enough context to confirm which protocol version produced each figure, and a recorded number with the wrong protocol is worse than a blank.

## What the benchmarks do not prove

They do not prove Hy4 preview leads the field, because the only comparison is internal. They do not prove it is better than Hy3, because no head-to-head was published. They do not measure cost-per-completed-task, which is the number that actually decides adoption at 0.834/2.501 per million tokens. And they do not cover the workload where the model is most likely to be used — multi-step office and agent tasks inside WorkBuddy — because the evaluation used engineering tasks.

## Suitable and less suitable workloads

**Well-suited:** long-context analysis with self-hosting requirements, coding and agentic engineering work, Chinese-English bilingual production, and cost-sensitive agent loops that benefit from aggressive cache pricing.

**Less suited:** vision or multimodal input — the preview is text-only, and visual understanding was announced for the next Hy4 generation, not this one. Also less suited to workloads needing independently verified benchmark standing before procurement, and to low-latency chat where the model's stated tendency to over-reason becomes a cost rather than a benefit.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis (1M) | High |
| Coding and software engineering | High |
| Agent orchestration / tool use | High |
| Chinese-language production | High |
| Cost-sensitive high-volume inference | High |
| Self-hosted deployment | Moderate (Apache-2.0 permits it; 770B makes it a cluster project) |
| Vision / multimodal input | None in this preview |
| Low-latency non-reasoning chat | Low (vendor notes over-reasoning as a known issue) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## What is uncertain

- **Max output tokens** — not published anywhere located.
- **Hy3 comparison** — third-party coverage puts Hy3 at 295B total parameters, but no official specification page was located to confirm the figure or the activation ratio.
- **The 31.8% inference-throughput claim** — vendor-reported, with no baseline published.
- **The self-improvement claim** — no experiment logs, no ablation, no external reproduction.
- **Whether the next Hy4 generation supersedes this preview** — Tencent says the next batch is "expected to roll out soon" and has announced a flash variant and first-time visual understanding; this record will need a `superseded_by` link when that ships.
- **Third-party leaderboard scores** — present on the model card, deliberately not transcribed here for protocol reasons.

## China AI Hub analysis

Three readings are worth recording. **First**, Tencent is pricing for share, not for margin: at 0.834 input with a 0.042 cache rate, Hy4 preview is engineered for agent workloads that Tencent itself generates through WorkBuddy and CodeBuddy, which turns the model into a loss-leader for the workbench rather than a standalone product. **Second**, the open weights plus Apache-2.0 are a distribution instrument aimed at the self-hosting segment that GLM and Qwen already serve; Tencent is entering a market its competitors built. **Third**, the architecture section naming DeepSeek and GLM is the most consequential detail in the card: it suggests the Chinese frontier has converged on a shared MoE-plus-sparse-attention recipe, so differentiation is migrating from architecture to data, post-training and — as the self-improvement claim hints — to how much of the training loop the model can run itself.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-hy4-1 | Tencent — Hy4 preview release announcement | https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/ | Official | 2026-08-28 | 2026-10-31 | high | — |
| src-models-hy4-2 | Hy4 preview model card (Hugging Face) | https://huggingface.co/tencent/Hy4-preview | Official | — | 2026-10-31 | high | — |
| src-models-hy4-3 | Hy4 preview model card — Chinese (README_CN) | https://huggingface.co/tencent/Hy4-preview/blob/main/README_CN.md | Official | — | 2026-10-31 | high | — |
| src-models-hy4-4 | Tencent Hy research site — Hy4 | https://hy.tencent.com/research/hy4-preview | Official | — | 2026-10-31 | medium | Page did not render for extraction; cited for existence only |
| src-models-hy4-5 | 智东西 — 汤道生预告混元Hy4，首次加入视觉理解 | https://news.qq.com/rain/a/20261030A0000M00 | Industry media | 2026-10-30 | 2026-10-31 | medium | Vision and flash variant described as forthcoming, not shipped |
| src-models-hy4-6 | 财联社 — Hy4 preview 开源，下一版模型近期上线 | https://cls.cn/detail/2467904 | Industry media | 2026-08-28 | 2026-10-31 | medium | — |

*Labels used above: **Official fact** (Tencent press release and the model card), **Vendor-reported claim** (throughput gain, self-improvement account, internal blind evaluation), **Third-party** (Hy3 parameter figure, forthcoming vision and flash variants), and **China AI Hub analysis** (our synthesis, always introduced as such).*
