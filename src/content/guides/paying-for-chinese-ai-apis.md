---
title: "How Foreign Teams Pay for Chinese AI APIs"
description: "Card declines, CNY invoicing and prepaid balances: the payment rails behind Chinese AI platforms, the workarounds buyers use, and what each one costs in."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 1
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3
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
---

**The short version.** Chinese AI platforms are built for Chinese buyers: CNY billing, corporate bank transfer, Alipay or WeChat Pay, and a fapiao (增值税发票) issued to a Chinese entity. A foreign company without a Chinese subsidiary sits outside that flow. The international domains, cloud marketplaces and resellers exist to bridge it — and each bridge charges a different toll.

## Why the card fails

A declined card is usually not a fraud block. It is a mismatch between the payment instrument and the billing entity:

- The platform bills in CNY to a mainland entity and cannot issue a fapiao to a foreign company.
- The corporate card is issued outside China and the acquirer does not process the currency.
- The account requires a mainland phone number or identity verification for the billing profile.

None of these is a bug in your card. They are the platform working as designed for its home market.

## The four rails

| Rail | How it works | Cost | Recourse |
|---|---|---|---|
| **International domain** | A separate site with USD pricing and card billing (Z.ai, platform.moonshot.ai, MiniMax's international site, Alibaba Cloud international) | Usually a premium over CNY list | Contract with the international entity |
| **Cloud marketplace** | Buy through Alibaba Cloud, Volcano Engine or a global cloud that resells the model | Marketplace margin, committed-spend terms | The cloud provider's contract, not the lab's |
| **Reseller / aggregator** | A third party sells access to several Chinese models behind one key | 10–50% markup, sometimes more | Whatever the reseller's terms say — often thin |
| **Chinese entity** | A subsidiary, a partner or a Hong Kong company holds the account | Setup and compliance cost | Full domestic terms, fapiao included |

The rails are not ranked. A team doing a two-week evaluation and a company putting an agent into production should choose differently.

## What each rail actually costs

**International domains** price in USD and take international cards. The premium over the domestic CNY list is real but usually smaller than the cost of an hour of legal review. The contractual counterparty is the international affiliate, which is the point: you can read the terms, and there is an entity to serve notice on.

**Cloud marketplaces** are the procurement-friendly route. Your existing cloud contract, security review and billing relationship extend to the model. The trade-off is that the marketplace is the counterparty for billing and support, and the model's own terms still govern use — two contracts, not one.

**Resellers** are the fastest route and the weakest position. You are buying a service from a company that buys from a company. When a model is deprecated, a price changes or a key is rate-limited, you learn about it after the fact. For evaluation, fine. For production, it is a single point of failure with no audit rights.

**A Chinese entity** is the only rail that gets you the domestic price, the fapiao and direct support. It is also the slowest and the most expensive to set up, and it creates its own obligations — bookkeeping, tax registration, and a local presence that may trigger data-residency questions.

## The prepaid trap

Most Chinese platforms run on prepaid balances: you top up, the balance draws down, and there is no invoice until the top-up is consumed.

That model creates two problems for foreign finance teams:

1. **No accounts payable flow.** Prepaid top-ups look like a card charge, not a supplier invoice. Many finance systems cannot book them without a contract.
2. **Balance expiry and refunds.** Unused balances may not be refundable, and expiry terms are often written in the domestic user agreement. Read them before a five-figure top-up.

The practical fix is to treat the top-up as a prepayment against a purchase order, and to agree the refund position in writing before the first payment. Platforms vary; assume nothing.

## Choosing a rail: a decision rule

- **Evaluation (under ~$2,000):** international domain, card, no negotiation. The premium is irrelevant at this size.
- **Pilot, one model, no personal data:** international domain or cloud marketplace, whichever your finance team can book fastest.
- **Production, personal data involved:** cloud marketplace or international entity, plus a data processing agreement. Resellers are out.
- **Volume where price matters:** negotiate direct with the lab's international arm, or revisit the cloud marketplace with committed spend.

## Our view

**Payment is the first filter, and it quietly decides your architecture.** Teams that can only buy through a reseller tend to spread across many models, because switching is one API key. Teams that signed with a lab tend to standardise, because changing suppliers is a contract. Neither is wrong; they produce different systems.

**The international premium is usually worth paying.** A 20–40% markup sounds significant until it is compared with the cost of a contract you cannot enforce. The premium buys a counterparty, a USD invoice and a support channel — three things a reseller cannot give you at any price.

**Prepaid balances are an underwriting decision, not a payment convenience.** Money on deposit with a supplier you have not assessed is unsecured credit. Cap the exposure at what you would lose without a second thought, and treat anything larger as a supplier credit risk.

**A declined card is a useful signal.** It usually means the platform was built for a domestic buyer and the international route is a bolt-on. Ask how the international entity handles support, refunds and data before assuming the bolt-on behaves like the core product.

## What is uncertain

- International pricing changes frequently and is not always publicly listed per model.
- Refund and expiry terms sit in domestic user agreements that are not consistently translated.
- Whether a given marketplace contract covers the model's own acceptable-use terms depends on the contract text.

## Next

[Who you actually sign with](/guides/who-you-sign-with-chinese-ai/) — the entity behind the domain, and why the distinction survives the payment question.
