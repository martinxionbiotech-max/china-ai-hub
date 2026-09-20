# ARCHITECTURE_AUDIT.md — China AI Hub (Phase 0)

**Audit date:** 2026-09-20
**Auditor:** OpenClaw agent (main session)
**Scope:** Local workspace, GitHub (martinxionbiotech-max), remote OpenCode server (43.130.37.37)

## 1. Audit Question

Does any existing repository, codebase, or session already exist for China AI Hub (chinaaihub.com)?

## 2. Findings

| Location | Check performed | Result |
|---|---|---|
| Local workspace (`~/.openclaw/workspace`, `projects/`) | Directory search for `*chinaai*`, `*ai-hub*`, `*aihub*` | ❌ Nothing found. No prior local repo. |
| GitHub account `martinxionbiotech-max` | `gh repo list --limit 100` | ❌ No repo matching `chinaaihub` / `China-AI-Hub` / `AI-Hub`. 100 repos listed; no AI-hub entity. |
| Remote OpenCode server (43.130.37.37:4096) | Session list scan (100 sessions) for "ai hub / chinaai / aihub / china ai" titles | ❌ No matching sessions. Server healthy (v1.18.30). |
| Memory (`MEMORY.md`, `memory/*.md`) | Semantic search "China AI Hub chinaaihub.com" | ❌ Only tangential hits (China Manufacturing Intelligence, unrelated). |

## 3. Conclusion

**This is a GREENFIELD project.** There is no existing architecture to preserve, audit, or migrate.

Implications:

1. No Phase-0 "do not break existing things" constraint applies.
2. Architecture decisions can be made fresh, but must follow the master prompt (single primary domain, stable IDs, layered IA, evidence system).
3. The user's established conventions apply (see below).

## 4. Established Conventions to Reuse (from user's prior projects)

| Concern | Convention |
|---|---|
| Stack | Astro (5.x) + Tailwind v4 (+ `@tailwindcss/typography`), static export |
| Hosting | Cloudflare Pages (build `npm install && npm run build`, output `dist/`) |
| Repo | Public under `martinxionbiotech-max/…`, main branch |
| Delivery | User pushes to GitHub (or agent pushes to existing repo); Cloudflare auto-builds |
| Image tooling | Seedream image agent (available at workspace `image-agent/`) |
| Writing skill | `deep-research-writer` v2.1.0 + `quality-gate` v1.0.0 for editorial content |
| Source research | `source-verification`, `chinese-web-research`, `competitor-intelligence` skills |
| Build discipline | Verify with `npm run build` after every batch; 1–2 files first, then scale |
| Data honesty | Never fabricate; live-fetch official sources before writing any factual claim |

## 5. Phase 0 Deliverables

- [x] This audit document
- [x] Confirmation of greenfield status (reported to user)

## 6. Next Steps (Phase 1)

Proceed to architecture documentation (see `ARCHITECTURE.md`, `DATA_SCHEMA.md`, etc. in this folder), then scaffold the Astro site with empty content collections, verify the build, and only then start Phase 2 entity research.
