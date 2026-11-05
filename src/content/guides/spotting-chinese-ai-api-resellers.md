---
title: "How to Spot a Chinese AI API Reseller"
description: "Below-list prices, shared keys and missing entities: the tells of a grey-market API reseller, the legitimate resale routes, and the risks that transfer to."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 5
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3
  - qwen3.8-max
sources:
  - source_name: "DeepSeek API documentation"
    source_url: "https://api-docs.deepseek.com/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
  - source_name: "Moonshot AI international platform"
    source_url: "https://platform.moonshot.ai/"
    source_type: official
---

**The short version.** A reseller is anyone between you and the lab. Some are legitimate — cloud marketplaces, regional distributors, enterprise partners. Many are not: they buy domestic access, expose it behind a compatible API, and sell below list. The price is real; the recourse, the data path and the compliance position are not.

## The legitimate structures first

Before the tells, three arrangements that are normal and defensible:

1. **Cloud marketplace.** Alibaba Cloud, Volcano Engine or a global cloud resells model access under its own contract. You are buying from a company you already vet.
2. **Regional distributor.** An authorised partner sells and supports the platform in a territory. Verify the authorisation in writing.
3. **Enterprise reseller.** A systems integrator bundles model access into a managed service. The integrator is the supplier; the lab's terms still govern use.

The distinguishing feature of all three: they will name their authorisation, their entity and their data path without being pushed.

## Ten tells of a grey-market reseller

| Tell | What you see | Why it matters |
|---|---|---|
| **Price below official list** | 30–70% under the vendor's published rate | Someone is subsidising; usually the margin or the compliance |
| **No named entity** | A website, a Telegram contact, no registered company | No counterparty, no recourse |
| **Shared or pooled keys** | Rate limits that fluctuate with other customers | Your availability depends on strangers |
| **Model version lag** | "GLM-5.3" that behaves like an older snapshot | You cannot verify what you are calling |
| **No DPA, no security page** | Requests for a data agreement go unanswered | Personal data has no lawful route |
| **Compatible-but-not-identical API** | Slight differences in headers, errors, tokenisation | Silent behaviour changes in production |
| **Payment only by crypto or transfer** | No invoice, no card, no marketplace | Unbookable spend, no refund path |
| **Vanishing documentation** | Docs hosted on a personal site | No versioning, no SLA |
| **"Unlimited" plans** | Flat fee for unlimited tokens | Economically impossible; expect throttling or shutdown |
| **Sudden deprecation** | A model disappears with a week's notice | Your product inherits the outage |

Any one of these is a question. Three together is a business model.

## The economics of below-list pricing

A reseller buying at domestic CNY rates and selling in USD below the international list can look cheap for two reasons:

- **Currency and regional arbitrage** — the domestic price is genuinely lower, and the reseller captures part of the gap.
- **Subsidy** — the reseller is buying market share with venture money or with a free tier from the lab.

The first is sustainable until the vendor closes the gap. The second ends when the funding does. Neither gives you a contract with the party that makes the model.

## What actually transfers to you

When you buy through an unvetted reseller, four things move:

1. **The counterparty** — from the lab to an intermediary with unknown balance sheet.
2. **The data path** — your prompts now pass through an additional party, often undisclosed.
3. **The compliance position** — the reseller's jurisdiction and practices become your processing chain.
4. **The failure mode** — when access is cut, you have no service credit and no escalation.

None of this appears in a benchmark. All of it appears in an incident review.

## How to vet a reseller in one call

Ask for, in writing:

- The legal entity, registration number and jurisdiction.
- The authorisation from the lab, or the marketplace listing that establishes the resale.
- A data processing agreement and the list of sub-processors.
- The exact model identifier and version they serve, with a method to verify it.
- The notice period for price changes and model deprecations.

Five items. A legitimate reseller has them ready. A grey-market one has a story.

## Why buyers still use them

Because the alternative is a procurement project. A reseller takes a card, delivers a key in ten minutes and speaks the buyer's language. For a two-week evaluation that is worth the risk, and pretending otherwise ignores how engineering actually happens.

The mistake is not starting with a reseller. It is staying with one after the pilot works.

## Our view

**Below-list pricing is a signal about the supplier's business model, not a discount.** Someone is paying the difference: the vendor through a subsidy, the reseller through burn, or you through the absence of a contract. Ask which.

**The most dangerous resellers are the competent ones.** A crude operation is easy to spot. A well-run aggregator with clean docs, a decent status page and a real company behind it can run for years — and still leave you without recourse when the upstream key is cut.

**Model identity is the tell that matters most.** If you cannot verify which snapshot you are calling — by version string, by behaviour, by the vendor's own endpoint — you cannot reproduce your own results. That is a research-integrity problem as much as a procurement one.

**Aggregators solve a real problem and should be used deliberately.** One key, many models, fast comparison: that is a legitimate evaluation tool. Use it to decide; sign with the lab to ship.

## A note on aggregators

Multi-model aggregators deserve their own category. They add value by normalising APIs and billing, and some are substantial companies. The test is the same: do they disclose the upstream provider, the entity, the data path and the version? If yes, they are a supplier you can assess. If no, they are a convenience with an unknown dependency.

## What is uncertain

- Authorisation claims are rarely verifiable independently.
- Reseller pricing changes faster than any published list.
- Some resellers are formally appointed and simply do not publish it.

## Next

[Enterprise onboarding documents](/guides/chinese-ai-enterprise-onboarding/) — what to prepare before the vendor's first questionnaire.
