---
title: "Enterprise Onboarding at Chinese AI Vendors"
description: "What Chinese AI vendors ask for before a contract: entity documents, security questionnaires, DPAs and use-case review, and what to prepare before the."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 6
related_entities:
  - glm-5.3
  - qwen3.8-max
  - kimi-k3
sources:
  - source_name: "Z.ai platform documentation"
    source_url: "https://docs.z.ai/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
  - source_name: "Moonshot AI international platform"
    source_url: "https://platform.moonshot.ai/"
    source_type: official
---

**The short version.** Enterprise onboarding at a Chinese AI vendor is shorter than at a Western one and hits different walls. Expect questions about your entity and use case, a security review that may have no SOC 2 to point at, and a DPA negotiation that decides whether personal data can be involved at all. Prepare four documents and the first call becomes a commercial conversation.

## What they ask for, and why

| Request | What it establishes | Who asks |
|---|---|---|
| Company registration | You are a real entity that can contract | Sales ops, finance |
| Use-case description | Whether your application is permitted under the terms | Compliance |
| Data types processed | Whether personal or sensitive data is involved | Legal / security |
| Expected volume | Pricing tier, rate limits, capacity planning | Sales engineering |
| Security questionnaire | Your own controls, for joint risk | Enterprise security |
| DPA / data processing terms | Lawful basis and sub-processor list | Legal |

Six items. The first four are quick; the last two are where deals slow down.

## The four documents to prepare

1. **A one-page company and entity summary** — legal name, registration number, jurisdiction, ultimate parent, signatory. This prevents the counterparty confusion described in [the entity chapter](/guides/who-you-sign-with-chinese-ai/).
2. **A one-page use-case description** — what the model does, who the users are, what data goes in, what comes out, and whether outputs reach end customers. Vague descriptions get escalated to compliance, which adds weeks.
3. **A data map** — categories of data, whether personal data is involved, where it is stored, retention, and which sub-processors touch it. If personal data is in scope, the endpoint question in [the residency chapter](/guides/chinese-ai-data-residency/) becomes the deciding one.
4. **Your security posture summary** — certifications you hold, encryption, logging, access control, incident process. Chinese vendors often cannot supply a SOC 2; yours may be the only audited document in the room.

## The security questionnaire gap

Western buyers expect a vendor security package: SOC 2 Type II, ISO 27001, pen-test summary, sub-processor list, uptime history.

Chinese AI vendors vary widely. The large cloud-affiliated platforms usually have ISO 27001 and a mature security organisation. Younger labs may have neither a SOC 2 nor a public trust centre, and will answer a questionnaire in prose.

That is not automatically disqualifying, but it changes the risk allocation: if the vendor cannot evidence controls, your contract needs to carry more of the weight — notification obligations, audit rights, breach timelines.

## The DPA conversation

Three questions decide whether a DPA is achievable:

1. **Will they sign your DPA, or only theirs?** Most Chinese vendors offer their own; some will negotiate a mutual addendum.
2. **Who are the sub-processors?** Cloud provider, logging, support tooling. An incomplete list is a compliance problem, not a paperwork one.
3. **Is training on customer data off by default?** If not, can it be switched off contractually, and does the enterprise agreement override the consumer terms?

If the answer to (3) is no at any tier, the product cannot process confidential data, and the architecture has to change.

## The use-case review

Chinese platforms screen applications more explicitly than most Western APIs, because the domestic regulatory framework requires it. Expect questions about:

- Whether the application generates content for public consumption.
- Whether it involves minors, medical, legal or financial advice.
- Whether it could be used for impersonation or fraud.
- Whether the outputs are resold or white-labelled.

Answering these precisely speeds the review. Answering vaguely triggers escalation.

## A timeline that reflects reality

| Week | What happens |
|---|---|
| 1 | Intro call, use case, volume estimate, pricing indication |
| 1–2 | Entity documents exchanged, NDA signed |
| 2–3 | Security questionnaire and DPA negotiation (the long pole) |
| 3–5 | Contract, order form, prepayment or invoicing setup |
| 5–6 | Technical onboarding, key issuance, rate-limit confirmation |

Four to six weeks is normal for an enterprise contract with personal data. A two-week timeline is realistic only for card-paid, international-domain, no-personal-data usage.

## Our view

**The DPA is the real gate, not the contract.** Price and SLA get negotiated in days; the data processing terms decide whether the project is lawful. Start there, and let the commercial terms follow.

**A vendor without a security package is not necessarily unsafe — but it is uninsured.** If they cannot evidence controls, you are relying on their good intentions and your contract. Price that into the decision rather than discovering it in an incident.

**Write the use-case description yourself.** Vendors write vague ones from a sales template, then compliance asks the same questions again. A precise page saves a week per review cycle.

**Treat onboarding as a product decision.** A six-week onboarding means you cannot switch models quickly, which means the first vendor's roadmap matters more than its benchmark score. That is a strategic fact disguised as an administrative one.

## What is uncertain

- Certification coverage varies by entity, not by brand.
- DPA negotiation outcomes differ by deal size and region.
- Timelines assume an engaged vendor; unresponsive ones add weeks silently.

## Next

[Self-hosting vs API: a cost model](/guides/self-hosting-vs-api-cost-model/) — the alternative to all of the above.
