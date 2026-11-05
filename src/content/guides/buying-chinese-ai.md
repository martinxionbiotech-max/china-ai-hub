---
title: "Buying Chinese AI: Access, Contracts and Vendor Risk"
description: "Chinese models are easy to try and hard to buy. A procurement pillar on payment rails, contracting entities, licence terms, data residency and vendor risk."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 0
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3
  - kimi-k3
  - qwen3.8-max
sources:
  - source_name: "Z.ai platform documentation"
    source_url: "https://docs.z.ai/"
    source_type: official
  - source_name: "Moonshot AI international platform"
    source_url: "https://platform.moonshot.ai/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
  - source_name: "DeepSeek API documentation"
    source_url: "https://api-docs.deepseek.com/"
    source_type: official
  - source_name: "Cyberspace Administration of China"
    source_url: "https://www.cac.gov.cn/"
    source_type: official
---

**The short version.** A Chinese model can be in production in an afternoon and still be un-procurable six months later. The gap is not technical. It sits in four places — how you pay, who you sign with, what the terms allow, and where the data goes — and each one fails at a different stage of scaling.

This pillar covers those four gates in the order a buyer meets them.

## Why this pillar exists

Every other section of this site answers "which model". This one answers "can I actually buy it, and what am I agreeing to when I do".

The questions are unglamorous and they decide more projects than benchmark scores do:

| Gate | Fails when | Typical symptom |
|---|---|---|
| Payment | The platform bills in CNY to a Chinese entity | Card declined, no invoice, finance blocks the spend |
| Counterparty | The contract is with an affiliate you have not assessed | No recourse, no audit rights, unclear liability |
| Contract | The terms restrict resale or model training | Product launch blocked after engineering is done |
| Data | Personal data crosses the border | Legal review stops the rollout |

Four gates, and the model itself is rarely the reason a deal dies.

## The argument in one paragraph

Chinese AI labs optimise for developer adoption inside China, where payment, invoicing and identity are solved by infrastructure the buyer already has. A foreign buyer arrives without that infrastructure, so the same product becomes a procurement project. Vendors respond by creating international domains, resellers and cloud partnerships — each of which solves access while adding a layer between the buyer and the lab. **The buyer's real task is not finding access; it is choosing which layer to accept, and understanding what that layer costs in recourse, price and data control.**

## The eight chapters

1. [How foreign teams pay for Chinese AI APIs](/guides/paying-for-chinese-ai-apis/) — the payment rails, and why a declined card is a procurement problem, not a bug.
2. [Who you actually sign with](/guides/who-you-sign-with-chinese-ai/) — the entity behind the domain, and why it matters when something goes wrong.
3. [What Chinese AI terms actually restrict](/guides/chinese-ai-terms-of-service/) — distillation, resale, output ownership and the clauses that block products.
4. [Data residency and cross-border transfer](/guides/chinese-ai-data-residency/) — PIPL, hosting regions and the ICP question.
5. [How to spot an API reseller](/guides/spotting-chinese-ai-api-resellers/) — the tells, the legitimate cases, and the risks that transfer to you.
6. [Enterprise onboarding documents](/guides/chinese-ai-enterprise-onboarding/) — what vendors ask for, and what to prepare before the first call.
7. [Self-hosting vs API: a cost model](/guides/self-hosting-vs-api-cost-model/) — the break-even that survives real utilisation.
8. [A vendor risk register](/guides/chinese-ai-vendor-risk-register/) — eight risks, scored, with the mitigations that actually work.

## Our position

**The procurement gap is the most durable moat in Chinese AI — and the least written about.** Model capability converges quarterly; payment rails, contracting entities and licence terms change slowly. A buyer who understands the second set makes better decisions for years, while benchmark-chasing expires in months.

**Cheap access through a reseller is usually the most expensive option.** It solves the payment gate and quietly transfers the counterparty, the data path and the compliance question to an intermediary who may not be able to answer any of them. We treat resellers as a legitimate tool for experimentation and a poor foundation for production.

**"Can I self-host it" is not a licence question alone.** Apache-2.0 and MIT are permissive, but the custom Chinese licences — MiniMax's community licence, several Qwen variants, Kimi's revenue-triggered terms — turn self-hosting into a legal review. The licence text, not the model card summary, decides.

**Most buyers should start with the international domain of a Chinese lab, not a reseller.** It costs more than the domestic price and less than the risk of an unvetted intermediary. Paying a 20–40% premium for a contract you can enforce is a good trade at almost any volume.

## What this pillar does not cover

- Model quality and benchmark interpretation — see [Research](/research/) and the [benchmark pages](/benchmarks/).
- Domestic Chinese procurement for Chinese entities — the invoicing and identity problems largely disappear there.
- Legal advice. Every chapter describes what to check and who to ask; none of it substitutes for counsel in your jurisdiction.

## How to use it

Read chapters 1–4 before the first production deployment. Chapters 5–8 are for the point where spend becomes visible to finance and legal — usually somewhere between the pilot and the second contract.

If you only have ten minutes: read [the payment chapter](/guides/paying-for-chinese-ai-apis/) and [the terms chapter](/guides/chinese-ai-terms-of-service/). Those two decide whether the rest is worth your time.
