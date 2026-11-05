---
title: "Who You Actually Sign With at Chinese AI Labs"
description: "The domain, the operating company and the invoicing entity are rarely the same. How to identify your real counterparty at a Chinese AI lab, and why it."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 2
related_entities:
  - glm-5.3
  - kimi-k3
  - qwen3.8-max
  - deepseek-v4-pro
sources:
  - source_name: "Zhipu AI"
    source_url: "https://www.zhipuai.cn/"
    source_type: official
  - source_name: "Moonshot AI"
    source_url: "https://www.moonshot.cn/"
    source_type: official
  - source_name: "Moonshot AI international platform"
    source_url: "https://platform.moonshot.ai/"
    source_type: official
  - source_name: "MiniMax"
    source_url: "https://www.minimax.io/"
    source_type: official
  - source_name: "DeepSeek"
    source_url: "https://www.deepseek.com/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
---

**The short version.** You will find three names in any Chinese AI purchase: the brand on the website, the operating company that runs the platform, and the entity that issues the invoice. They are often different legal persons. The one that matters is the one on the contract — because that is the only one you can serve notice on.

## The three-name problem

A typical purchase looks like this:

| Layer | Example shape | Where you see it |
|---|---|---|
| Brand | The model family name | Marketing site, model card, docs |
| Platform operator | The entity running the API console | Terms of service, order form |
| Invoicing entity | The entity issuing the fapiao or the international invoice | Invoice, payment receipt |
| Contracting affiliate | An offshore or regional entity you sign with | Master agreement, order form |

Four layers, and buyers routinely check only the first.

This is not a Chinese peculiarity. It is how most large software vendors are structured. What makes it sharper in this market is that the domestic and international businesses are often run by different entities with different prices, different terms and different support organisations.

## What to extract from each document

**From the order form or master agreement:** the legal name, registration jurisdiction and address of the counterparty. If the order form is issued by an entity you have never seen in the docs, that entity is your supplier.

**From the invoice:** the seller's tax identifier. If it does not match the contracting entity, ask why before paying.

**From the terms of service:** the entity named as "we" or "us". This is the party that disclaims liability, and it is frequently not the entity that signs the order form.

**From the support channel:** which organisation answers. A support desk in a different entity is a signal that the commercial relationship is intermediated.

## The domestic / international split

Most large Chinese labs operate two commercial surfaces:

- A **domestic platform** with CNY pricing, fapiao, mainland identity verification and the full model line-up.
- An **international platform or affiliate** with USD pricing, card billing and a narrower catalogue.

The international surface is usually the right starting point for a foreign buyer — but it is a different product in three ways worth checking:

1. **Model coverage.** The newest or largest models sometimes appear on the domestic platform first.
2. **Terms.** The international terms are typically shorter and more permissive on data use, but they also drop commitments the domestic agreement makes.
3. **Support.** International support is often a smaller team with a longer response time.

If your architecture depends on a model that only exists domestically, you have a structural problem, not a payment problem.

## Affiliates, distributors and "authorised partners"

Chinese AI vendors sell through three additional structures that complicate the counterparty question:

- **Regional affiliates** (Hong Kong, Singapore) that contract with foreign buyers but are not the mainland operating company.
- **Cloud distributors** that resell model access under their own contract — the cloud is your supplier, and the lab's terms still bind your use.
- **Authorised partners** whose authorisation is real but whose liability is entirely their own.

None of these is illegitimate. All of them change who you sue, who owes you a service credit, and who can answer a security questionnaire.

## A counterparty check in ten minutes

1. Open the terms of service and search for the legal entity name. Write it down.
2. Open the order form or quote. Compare the entity name.
3. Check the invoice or receipt. Compare the tax identifier.
4. Search the entity in your own jurisdiction's company registry if it is an offshore affiliate.
5. Ask the sales contact, in writing: "Which entity will be the counterparty on the order form, and which entity issues the invoice?"

Five steps, and the answer is usually clean. When it is not, the answer is itself the finding.

## Our view

**Counterparty clarity is worth more than a price concession.** A 15% discount from an intermediary who cannot produce an enforceable contract is a bad trade. Buyers negotiate hard on price and rarely ask who the contracting party is — which is backwards, because price is recoverable and recourse is not.

**The domestic/international split is the most under-appreciated risk in Chinese AI procurement.** Teams evaluate a model on the international docs, then discover that the feature they need — a specific context length, a vision variant, a fine-tuning endpoint — exists only on the domestic platform. Check model parity before architecture.

**An offshore affiliate is not a red flag; an undisclosed one is.** Labs legitimately structure for international sales. The problem is when the buyer believes they are contracting with the lab and finds an affiliate's name on the order form after legal review.

**Cloud marketplaces are the cleanest counterparty for most foreign buyers.** You already have a contract, a security review and a billing relationship. The model's terms still apply to use, but the commercial relationship is one you have already vetted.

## What is uncertain

- Entity structures change, and a name that was correct last year may be a subsidiary now.
- International catalogues lag domestic ones by an amount that varies by vendor and quarter.
- Distributor arrangements are rarely published, so the route from buyer to lab is often reconstructed rather than read.

## Next

[What Chinese AI terms actually restrict](/guides/chinese-ai-terms-of-service/) — the clauses that decide whether your product can ship.
