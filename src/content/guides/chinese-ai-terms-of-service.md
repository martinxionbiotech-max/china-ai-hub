---
title: "What Chinese AI Terms Actually Restrict"
description: "Distillation, resale, output ownership and data use: the clauses in Chinese AI terms that block products after launch, and how to read them before you."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 3
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3
  - kimi-k3
  - minimax-m3
sources:
  - source_name: "DeepSeek API documentation"
    source_url: "https://api-docs.deepseek.com/"
    source_type: official
  - source_name: "Z.ai platform documentation"
    source_url: "https://docs.z.ai/"
    source_type: official
  - source_name: "Moonshot AI international platform"
    source_url: "https://platform.moonshot.ai/"
    source_type: official
  - source_name: "MiniMax"
    source_url: "https://www.minimax.io/"
    source_type: official
---

**The short version.** Chinese AI terms are shorter than their Western equivalents and less negotiated, but they contain four restrictions that regularly break products: no training competing models on outputs, limits on resale or white-labelling, unclear output ownership, and broad rights to use your inputs. The first two are the ones that surface after launch.

## The four clauses that matter

| Clause | Typical restriction | Who it breaks |
|---|---|---|
| **No competing-model training** | Outputs may not be used to train a model that competes with the provider | Anyone fine-tuning on model outputs |
| **Resale / white-label** | Reselling raw API access usually needs permission; wrapping it in a product may not | Aggregators, agencies, SaaS resellers |
| **Output ownership** | Provider assigns or licenses outputs to you, sometimes with conditions | Products that need clean IP assignment |
| **Input rights** | Provider may use inputs to improve services unless opted out | Anyone sending confidential or personal data |

None of these is unusual. All of them are easy to miss because they sit in a user agreement that is often only published in Chinese, and because sales teams describe the product, not the contract.

## Clause 1: training on outputs

The most common restriction across Chinese and Western providers alike: you may not use the service to develop a model that competes with it.

For most buyers this is irrelevant. For three groups it is existential:

- Teams **distilling** a small model from a large one.
- Teams **fine-tuning** on generated data at scale.
- Teams building **evaluation datasets** from model outputs and publishing them.

The restriction usually applies to outputs used to train *competing* models, which leaves room for internal, non-competing uses — but "competing" is rarely defined, and the definition is the provider's to make.

**What to do:** if training on outputs is part of the plan, get written confirmation that your use case is permitted, or use a model whose licence explicitly allows it. Open-weight models with permissive licences are often the cleaner path for distillation.

## Clause 2: resale and white-labelling

Two different activities, often conflated:

- **Reselling raw access** — selling API keys or metered access. Almost universally restricted without a reseller agreement.
- **Embedding the model in a product** — your customers use your product, not the API. Usually permitted, sometimes with conditions on disclosure or branding.

The grey zone is the middle: an agency that builds a chatbot for a client and hosts it, or a platform that exposes "model choice" to its own users. Some terms treat that as resale; some do not.

**What to do:** describe your architecture in one paragraph and ask the vendor to confirm in writing that it is permitted. A vendor who will not put it in writing has told you something.

## Clause 3: output ownership

Chinese terms vary more here than Western ones. Three patterns appear:

1. **Assignment** — outputs are yours, with the provider disclaiming any warranty of non-infringement.
2. **Licence** — the provider retains ownership and grants you a broad licence to use outputs.
3. **Conditional** — outputs are yours provided you comply with the acceptable-use policy.

For most products the practical difference is small. It becomes material if you need to represent to your own customers that you own the content, or if you are acquiring IP.

**What to do:** check whether the term is assignment or licence, and whether it survives termination. If your customer contracts promise ownership, your supplier contract must be able to support that promise.

## Clause 4: input rights

The clause foreign buyers read most carefully and Chinese providers write most broadly: the provider may use inputs and outputs to operate, improve and develop its services.

Security teams treat this as a data-processing question. It is also a confidentiality question: a customer's document sent to a model may become training data unless there is an opt-out or an enterprise agreement that excludes it.

**What to do:** ask three questions — is training on my data on by default, can it be turned off, and does the enterprise agreement override the consumer terms? Get the answer for the specific product you are buying, not the platform in general.

## Why these clauses are shorter than Western ones

Chinese AI terms tend to be brief because they were written for a domestic market where the regulatory baseline is set by law rather than by contract — PIPL, the Data Security Law and the generative-AI measures do work that Western contracts do in writing.

That is not a criticism. It does mean a foreign buyer cannot rely on the contract to allocate risk the way they are used to, and should read the regulation alongside it.

## A reading order that saves time

1. **Acceptable use** — what is prohibited outright.
2. **Training on outputs** — the distillation question.
3. **Resale and commercial use** — the white-label question.
4. **Output ownership and termination** — the IP question.
5. **Data use and retention** — the confidentiality question.

Five sections, twenty minutes. Most terms are shorter than a typical SaaS MSA.

## Our view

**The distillation clause is the one that quietly kills products.** A team builds a fine-tune on outputs, ships it, and discovers at due diligence that the terms prohibited exactly that. It is the most common avoidable legal problem in the Chinese-model ecosystem, and it is entirely preventable with one question before the first training run.

**"We can resell it" is a business assumption, not a legal one.** Reseller terms exist at every major Chinese lab, but they are negotiated, not published. Companies that assume embedding equals resale discover the distinction during a customer's procurement review, which is the worst possible time.

**Open weights change the question, not the answer.** An Apache-2.0 model lets you train on outputs and self-host without a service contract — but the *licence* may still restrict certain commercial uses, and the model's own terms can follow the weights. Read the licence, not the marketing page.

**A vendor that answers these four questions in writing is worth a price premium.** The ability to get a clear answer is a proxy for how the vendor will behave when something goes wrong.

## What is uncertain

- Translations of Chinese user agreements are inconsistent; the Chinese text governs.
- "Competing model" is rarely defined with precision.
- Enterprise agreements can override consumer terms in ways that are not public.

## Next

[Data residency and cross-border transfer](/guides/chinese-ai-data-residency/) — where the data goes, and what that requires.
