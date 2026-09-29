---
image: "/images/ai/models-glm-5.3.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "Self-Hosting Chinese Open-Weight Models: Licenses, Hardware and Quantization"
description: "A decision guide for self-hosting Chinese open-weight models — matching license obligations, hardware footprint, quantization routes and inference ecosystems to the right open checkpoint."
published_date: "2026-09-29"
updated_date: "2026-09-29"
related_entities:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - glm-5.3
  - glm-5.3-flash
  - glm-5.2
  - kimi-k3
  - minimax-m3
  - minimax-m2.7
  - qwen3.8-2.4t-a95b
  - deepseek-v3-2
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "Hugging Face model card — DeepSeek-V4-Pro"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
    source_type: official
  - source_name: "Z.ai — GLM-5 GitHub repository"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
  - source_name: "MiniMax — M3 Community License"
    source_url: "https://huggingface.co/MiniMaxAI/MiniMax-M3"
    source_type: official
---

**Short answer.** Eleven of the twenty-one tracked models ship open weights, but "open weight" is not one legal category — the database records five license regimes, from DeepSeek's unconditional MIT to MiniMax M2.7's non-commercial-only terms with prior authorization required for any commercial use. Self-hosting is therefore a two-part decision: can you legally deploy the weights (license), and can you practically serve them (hardware + quantization). The least-friction route is a DeepSeek MIT or Zhipu Apache-2.0 checkpoint; the 1M-context open-weight option is currently Zhipu-only (GLM-5.3, GLM-5.3-Flash).

## Decision criteria

| Criteria | Relevance / Notes |
|---|---|
| License regime | MIT (DeepSeek) → Apache-2.0 (Zhipu) → conditional MIT-style with revenue/MAU triggers (Kimi K3, Qwen3.8-2.4T-A95B, MiniMax M3) → non-commercial-only (MiniMax M2.7) |
| Revenue / scale triggers | Kimi K3: MaaS >$20M/yr or >100M MAU; Qwen A95B: >100M MAU or >$50M/12mo MaaS; MiniMax M3: >$20M/yr |
| Total parameters | 1.6T (V4-Pro) to 320B (GLM-5.3-Flash) — total params dictate memory footprint even for sparse MoE |
| Active parameters | 8B–49B — the sparse-MoE inference cost driver |
| Context window (open) | 1M only on GLM-5.3 / GLM-5.3-Flash; Qwen A95B 256K; others below |
| Precision shipped | FP8 (GLM-5.3, GLM-5.3-Flash), BF16/FP8 (GLM-5.2) |
| Quantization route | Standard route for single-GPU serving of 30B-class models; frontier MoE needs clusters |
| Serving ecosystem | vLLM/Ollama via Qwen-Agent; DeepSeek Harness for DeepSeek models |

## The open-weight catalog

| Model | License | Parameters | Context | Notes |
|---|---|---|---|---|
| [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) | MIT | 1.6T / 49B active | 1M | Largest open model; verify HF vs GA checkpoint |
| [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) | MIT | 552B / 8–16B active | 1M | Sparse encoder-decoder; non-trivial to serve |
| [DeepSeek-V3.2](/models/deepseek-v3-2/) | MIT | 61-layer DSA MoE | not stated | Discontinued; historical reference |
| [GLM-5.3](/models/glm-53/) | Apache-2.0 | 744B / 40B active | 1M | Text-only; open 1M option |
| [GLM-5.3-Flash](/models/glm-53-flash/) | Apache-2.0 | 320B / 18B active | 1M | Vision + video + computer use |
| [GLM-5.2](/models/glm-52/) | MIT | 744B / 40B active | 1M | "Pure open, no regional limits" |
| [Kimi K3](/models/kimi-k3/) | Kimi K3 License | not disclosed | 1M / 1M output | Conditional MIT-style |
| [MiniMax-M3](/models/minimax-m3/) | Community License | not disclosed | 1M | Attribution + revenue trigger |
| [MiniMax-M2.7](/models/minimax-m27/) | Non-commercial only | not disclosed | 200K | Strictest terms |
| [Qwen3.8-2.4T-A95B](/models/qwen38-24t-a95b/) | Qwen3.8-Max License | 2.4T / 95B active | 256K | Weights only, no API |

## Entity routing

Route by the license you can clear and the hardware you can field.

| Scenario | Best-documented fit | Why |
|---|---|---|
| Least legal friction, largest open model | [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) | MIT, 1.6T/49B, 1M context |
| Cheapest open flash, 1M context + vision | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) | MIT, 552B/8-16B active |
| Open-weight 1M context, text-only | [GLM-5.3](/models/glm-53/) | Apache-2.0, 744B/40B |
| Open 1M multimodal | [GLM-5.3-Flash](/models/glm-53-flash/) | 320B/18B, vision+video+computer-use |
| MIT "no regional limits" GLM | [GLM-5.2](/models/glm-52/) | Deprecated but MIT; 744B/40B |
| Long-output 1M open model | [Kimi K3](/models/kimi-k3/) | Conditional license, 1M/1M |
| Cheapest open flagship | [MiniMax-M3](/models/minimax-m3/) | Community license, attribution + trigger |
| Scale-triggered open model, no API | [Qwen3.8-2.4T-A95B](/models/qwen38-24t-a95b/) | 256K, weights only |
| Historical MIT reference | [DeepSeek-V3.2](/models/deepseek-v3-2/) | Discontinued, MIT |

## What the evidence shows

The license is a cost and a risk that appears on no pricing page, and it activates precisely when a business starts succeeding. The three conditional licenses share a structure: permissive everyday use with an obligation that scales with revenue, MAU or the Model-as-a-Service business model — differing only in where the line is drawn ($20M/yr MiniMax vs $20M/12mo Kimi MaaS vs $50M/12mo Qwen MaaS) and what is owed (attribution, notice, separate agreement, or prior authorization). MiniMax M2.7 is the strictest — non-commercial only, any commercial use requiring prior written authorization.

The thresholds are low enough to be real, not theoretical. A $20M annual revenue trigger is well within reach of a successful vertical SaaS product built on a Chinese open model. A company that hits the Kimi K3 MaaS trigger or the Qwen $50M/12-month MaaS trigger without having budgeted for a separate license negotiation has created an unplanned commercial dependency. The license, in other words, is part of total cost of ownership.

Hardware is the second filter. A 4-bit-quantized 30B-class open model runs on a single high-memory GPU; frontier-scale open models (744B–1.6T) need clusters even though MoE inference is sparse, because total parameters still dictate memory. Quantization is the standard route, and its quality is the adopter's responsibility to evaluate. The serving ecosystem is thin but real: Qwen-Agent documents vLLM/Ollama connectivity, and DeepSeek Harness is the DeepSeek-native runtime.

China AI Hub analysis indicates the licensing landscape has shifted from a binary to a spectrum: the earlier generation of Chinese open models trended toward straightforward MIT or Apache, but the 2026 database shows the emergence of the *conditional permissive* license — MIT plus a monetization guardrail — which means "open weights" no longer implies "I can build a business on this without ever talking to the lab again."

## Selection procedure

Work through these steps in order.

1. **Clear the license first.** DeepSeek MIT and Zhipu Apache-2.0 are the only regimes a large enterprise can clear without bespoke negotiation. If your revenue or MAU will cross a threshold ($20M/yr for MiniMax M3 and Kimi K3 MaaS, $50M/12mo for Qwen MaaS), the conditional licenses activate an obligation — budget for the conversation before you scale.
2. **Reject the non-commercial trap explicitly.** MiniMax M2.7 is non-commercial only, with prior written authorization required for any commercial use. Do not build a product on it unless you have that authorization in hand.
3. **Size the hardware to total parameters, not active parameters.** Even a sparse MoE must load its total parameters into memory: 1.6T (V4-Pro) is a cluster deployment, 320B (GLM-5.3-Flash) is large but more tractable. Quantization is the standard route, and its quality is yours to evaluate.
4. **If long context is non-negotiable and you must self-host, the field is Zhipu only.** GLM-5.3 and GLM-5.3-Flash are the only open-weight 1M-context models; Alibaba's open A95B is 256K.
5. **Pin the checkpoint before you depend on it.** Verify the HF checkpoint matches the serving checkpoint (DeepSeek-V4-Pro's was last modified 2026-06-22 vs an 0813 GA), and confirm Zhipu's license applies to the actual weight artifacts, not just the repo.

## Limitations

The license is quoted from vendor statements and repository metadata, not legal review — re-check the license file in the specific model repository before any commercial decision. Zhipu's Apache-2.0 is read from GitHub repo metadata rather than a dedicated weights-license file, so a rigorous procurement must confirm it applies to the actual weight artifacts. The DeepSeek-V4-Pro HF checkpoint was last modified 2026-06-22 and it is not documented whether it matches the 0813 GA API checkpoint. Model-level capability flags trace to official pages; a missing flag is recorded as absence, not verified non-capability. Parameter counts are not disclosed for Moonshot and MiniMax models, so hardware planning for those is harder to pin down.

## Sources

- [China AI Hub — Models database](/models/)
- [Hugging Face model card — DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Z.ai — GLM-5 GitHub repository](https://github.com/zai-org/GLM-5)
- [MiniMax — M3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-M3)

*Labels used above: **Official fact** (license text, parameter counts, context windows and precision from primary sources), **Vendor-reported claim** (capability and serving statements published by the vendor), and **China AI Hub analysis** (our synthesis, introduced as such). No third-party evaluation evidence is currently recorded for these open-weight models.*
