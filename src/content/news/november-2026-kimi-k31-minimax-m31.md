---
title: "Kimi K3.1 Pro and MiniMax M3.1-Flash Arrive as K2 Retires"
author: "SinoAI Hub Research Team"
description: "Moonshot ships a 3T-class open-weight flagship and closes its K2 series; MiniMax adds a $0.15 flash tier. What changed, and what it means for buyers mid-contract."
published_date: "2026-11-05"
type: model_release
trigger_updates:
  - kimi-k3
  - minimax-m3
sources:
  - source_name: "Kimi API Platform — K3.1 Pro quickstart"
    source_url: "https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart.md"
    source_type: official
    published_date: "2026-11-05"
    confidence: high
  - source_name: "Kimi API Platform — model inference pricing"
    source_url: "https://platform.kimi.ai/docs/pricing/chat.md"
    source_type: official
    published_date: "2026-11-05"
    confidence: high
  - source_name: "MiniMax API platform — pay-as-you-go pricing"
    source_url: "https://platform.minimax.io/docs/guides/pricing-paygo.md"
    source_type: official
    published_date: "2026-11-05"
    confidence: high
---

Two changes landed in the same week, and they point in opposite directions: Moonshot moved its flagship forward and closed its previous generation, while MiniMax extended its price ladder downward.

## Kimi K3.1 Pro

Moonshot describes K3.1 Pro as the first model in a new K3.1 series and its "most capable 3T-class open-weight model to date", with a 1,048,576-token context window and vision input. It is a post-trained version of Kimi K3 with substantially larger post-training compute, and it ships with a `highspeed` variant.

Pricing is flat pay-as-you-go with no context-length tiering. The documentation lists cache writes (5-minute and 1-hour TTL), cache-hit input and output as separate billable items, and batch inference at 60% of the standard price for `kimi-k3.1-pro` and `kimi-k3`.

The pricing table on the documentation page renders client-side and could not be read as text, so this database records the model's specifications and status without a price. That is deliberate: an unverified number is worse than a blank one.

## K2 is closing

The same page carries a notice that from 2026-10-31 the K2 series is no longer available to newly registered users, and that all K2 models are scheduled for retirement by the end of December 2026. Existing users are unaffected until then.

For anyone running K2.7 Code or K2.6 in production, that is a migration deadline with roughly eight weeks on it — short enough that the work should be scheduled now, long enough that panic is optional.

## MiniMax M3.1-Flash

MiniMax added M3.1-Flash at $0.15 input / $0.60 output per 1M tokens, with prompt-cache reads at $0.015. M3's tiers are unchanged: $0.30/$1.20 below 512K input, $0.60/$2.40 above, after the permanent 50% discount.

The new model's announcement also implies a repositioning: the flash tier now sits at the market's $0.15 floor, while the M3 flagship holds its price. MiniMax is competing on the cheap tier rather than cutting the flagship.

## What it means

**Two vendors, two strategies.** Moonshot is consolidating around a single flagship family and retiring the tier below it; MiniMax is widening its ladder downward. A buyer standardising on one vendor is choosing between concentration and optionality, not just between models.

**The K2 retirement is the urgent item.** Migration work has a deadline, and the replacement is more expensive: K3.1 Pro is a 3T-class flagship, not a mid-tier coding model. Teams that relied on K2.7 Code's price will need to re-run their unit economics, not just swap a model ID.

**A missing price is a data point.** The database now lists K3.1 Pro with specifications and no price because the published table could not be verified. We would rather show the gap than import a number from a reseller page.
