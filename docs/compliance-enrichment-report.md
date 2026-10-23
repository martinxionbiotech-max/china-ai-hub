# Compliance Enrichment Report — sinoaihub.com

**Batch:** `compliance-enrich` · **Date:** 2026-10-23 · **Repo:** china-ai-hub (main site)

Enriched the site's legal/governance pages to clause-level (1500–2200 words/page), added the
missing **Disclaimer** and **Contact** pages, and aligned all disclosures with the site's actual
operating practices. Zero-fabrication: no invented entity, DPO, qualification, cookie, arbitration
body, or jurisdiction.

## 1 · Audit (before → after)

| Page | Before (words) | After (words) | Change |
|---|---|---|---|
| `about.astro` | 333 | 1,555 | +1,222 |
| `privacy.astro` | 314 | 1,848 | +1,534 |
| `terms.astro` | 315 | 1,583 | +1,268 |
| `cookies.astro` | 203 | 1,554 | +1,351 |
| `disclaimer.astro` | **missing** | 1,585 | **new** |
| `contact.astro` | **missing** | 338 | **new** |

Word counts are body text with HTML tags stripped (the site's standard measure; source-file
`wc -w` would over-count frontmatter/markup).

## 2 · New pages

- **`/disclaimer/`** — information-nature statement (independent, not an official source, not
  vendor-affiliated); layered not-professional-advice (not investment / not procurement / not
  legal-technical-security / not endorsement); **AI-generated content disclosure**; accuracy &
  timeliness limits; per-content-type disclaimers (pricing = listed estimates not quotations,
  benchmarks = source-attributed, licenses = not legal advice); third-party information;
  no-warranty; liability limit; correction channel; cross-links.
- **`/contact/`** — existing contact facts (email `admin@sinoaihub.com`, WhatsApp
  `wa.me/8613323237275`), no contact form, public GitHub issue tracker for corrections, response
  expectations, and a note that the site gives no professional advice.

## 3 · AI-content disclosure (as-built facts)

- **AI-generated illustrations** — entity pages carry `image_credit: "AI-generated illustration
  (Seedream)"`; disclosed in Disclaimer, Privacy, Terms, About.
- **Automated verification tooling** — the methodology's "an agent re-fetches the primary source"
  step; disclosed as tooling (not authoring) in Disclaimer, Privacy, Terms, About.
- **Editorial text/analysis** — attributed to the SinoAI Hub Research Team; labeled "China AI Hub
  analysis"; not claimed as AI-generated.

No AI-generated rankings or analysis are claimed; the four claim labels keep sourced fact separate
from interpretation.

## 4 · Zero-fabrication verification

| Item | Result |
|---|---|
| Legal entity name / registration / address | **Not invented** — pages state the project publishes no corporate name, registration, or office |
| DPO | **Not invented** — explicitly "no appointed Data Protection Officer" |
| Arbitration body | **Not invented** — terms state "designates no arbitration body" |
| Governing-law forum | **Not invented** — no disclosed jurisdiction, no forum selected |
| Cookies | **Not invented** — no tracking scripts found (`grep` = 0 hits); only Cloudflare `__cf_bm` / email-protection (real host) |
| Tracking/analytics | **None** — no gtag/GA/Pixel/Hotjar/Clarity/Plausible/Fathom/Matomo/PostHog |
| Contact forms | **None** — site has no forms; pages say "no forms" |
| Individual author personas | **None** — team byline only (matches `/authors/`) |
| Dataset license | **Not CC-BY** — stated as project IP, short-quote-with-attribution, permission for bulk reuse |

## 5 · Consistency

- Date: all six pages `Last updated: 2026-10-23`.
- Entity: "China AI Hub project" / team byline "SinoAI Hub Research Team" (matches Organization
  JSON-LD in `BaseLayout` and `/authors/` Organization schema).
- Contact: `Martin.W — admin@sinoaihub.com` + WhatsApp `wa.me/8613323237275` identical across pages
  and footer.
- Scope: `sinoaihub.com` + `data.sinoaihub.com` stated consistently.
- Cross-links: Disclaimer/Terms/Privacy/Cookies/About interlink; Disclaimer↔disclosure/methodology/
  editorial-standards/data-policy relationship stated.
- Footer nav: added `/disclaimer/` and `/contact/`; `llms.txt.ts` Core pages extended with Contact,
  Disclaimer, Privacy, Terms, Cookies.

## 6 · Build & delivery

- `npm run build` → **180 pages**, exit 0 (prebuild `generate-hubs.mjs` + build-llms run).
- Render verified: h1 + "Last updated: 2026-10-23" present on all six pages; footer links present;
  `/contact/` and `/disclaimer/` present in `sitemap-0.xml` and `dist/llms.txt`.
- Commit: `compliance-enrich` · pushed · `git rev-list --left-right --count HEAD...origin/main` = `0 0`.
