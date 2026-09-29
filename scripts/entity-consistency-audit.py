#!/usr/bin/env python3
"""SinoAIHub entity-relationship consistency audit (P0 / plan B1).

Cross-checks the six entity types — Company <-> Model <-> Agent <-> API
<-> Pricing <-> Benchmark — between the main site frontmatter and the data
site markdown, using reverse pointers as ground truth.

Exit code 0 = no contradictions; 1 = contradictions found.
"""
import glob
import os
import re
import sys

import yaml

MAIN = "/root/.openclaw/workspace/repos/china-ai-hub"
DATA = "/root/.openclaw/workspace/repos/china-ai-hub-data"

# ---------------------------------------------------------------------------
# Main site frontmatter
# ---------------------------------------------------------------------------

def load_frontmatter(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"):
        return {}
    parts = t.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def load_collection(coll):
    out = {}
    for f in glob.glob(f"{MAIN}/src/content/{coll}/*.md"):
        d = load_frontmatter(f)
        key = d.get(f"{coll.rstrip('s')}_id") or d.get("model_id") or d.get("provider_id") or d.get("company_id") or d.get("slug")
        if key:
            out[key] = d
    return out


# ---------------------------------------------------------------------------
# Data site markdown: extract a `## Section` body and the id links it contains
# ---------------------------------------------------------------------------

def data_sections(path):
    t = open(path, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^## (.+)$", t, re.M):
        name = m.group(1).strip()
        start = m.end()
        nxt = re.search(r"^## ", t[m.end():], re.M)
        end = m.end() + nxt.start() if nxt else len(t)
        out[name] = t[start:end].strip()
    return out


def section_ids(section_text):
    """Return id targets referenced by markdown links in a section."""
    return re.findall(r"\]\(\.\./(?:models|agents|apis|companies)/([a-z0-9.+-]+)\.md\)", section_text or "")


def data_files(coll):
    return [f for f in glob.glob(f"{DATA}/docs/{coll}/*.md") if not f.endswith("index.md")]


# ---------------------------------------------------------------------------
# Contradiction collection
# ---------------------------------------------------------------------------

contradictions = []

def report(pair, face_a, face_b, where):
    contradictions.append({
        "pair": pair,
        "face_a": face_a,
        "face_b": face_b,
        "where": where,
    })


def main():
    models = load_collection("models")
    agents = load_collection("agents")
    apis = load_collection("apis")
    companies = load_collection("companies")
    pricing = load_collection("pricing")
    benchmarks = load_collection("benchmarks")

    # Ground truth reverse pointers
    gt_company_agents = {}
    gt_company_apis = {}
    gt_company_models = {}
    for cid in companies:
        gt_company_agents[cid] = sorted(aid for aid, a in agents.items() if a.get("company") == cid)
        gt_company_apis[cid] = sorted(aid for aid, a in apis.items() if a.get("provider") == cid)
        gt_company_models[cid] = sorted(mid for mid, m in models.items() if m.get("provider") == cid)

    # --- Check 1: main-site company foundation_models / open_models / agents / api ---
    for cid, c in companies.items():
        fm_foundation = sorted(c.get("foundation_models") or [])
        fm_open = sorted(c.get("open_models") or [])
        fm_agents = sorted(c.get("agents") or [])
        fm_api = sorted(c.get("api") or [])

        # 1a. foundation_models + open_models must cover every CURRENT model
        #     (not discontinued, not superseded) whose provider == company, and must
        #     not point at a model of another company. Speed variants (canonical_model
        #     siblings) count as current models and must be listed.
        current_models = sorted(
            mid for mid, m in models.items()
            if m.get("provider") == cid
            and m.get("status") != "discontinued"
            and not m.get("superseded_by")
        )
        listed = sorted(set(fm_foundation + fm_open))
        for mid in fm_foundation + fm_open:
            if models.get(mid, {}).get("provider") != cid:
                report("Company->Model", f"{cid}.foundation/open_models lists {mid}",
                       f"model {mid}.provider = {models.get(mid, {}).get('provider')}",
                       f"{MAIN}/src/content/companies/{cid}.md")
        missing = sorted(set(current_models) - set(listed))
        if missing:
            report("Company->Model", f"{cid} lists {listed}",
                   f"current models with provider={cid}: {current_models} (missing {missing})",
                   f"{MAIN}/src/content/companies/{cid}.md")

        # 1b. agents field == reverse pointers
        if fm_agents != gt_company_agents[cid]:
            report("Company->Agent", f"{cid}.agents = {fm_agents}",
                   f"agents with company={cid}: {gt_company_agents[cid]}",
                   f"{MAIN}/src/content/companies/{cid}.md")

        # 1c. api field == reverse pointers
        if fm_api != gt_company_apis[cid]:
            report("Company->API", f"{cid}.api = {fm_api}",
                   f"apis with provider={cid}: {gt_company_apis[cid]}",
                   f"{MAIN}/src/content/companies/{cid}.md")

    # --- Check 2: forward pointers resolve (no dangling) ---
    model_ids = set(models)
    agent_ids = set(agents)
    api_ids = set(apis)
    company_ids = set(companies)
    pricing_ids = set(pricing)
    for aid, a in agents.items():
        for m in (a.get("underlying_models") or []):
            if m not in model_ids:
                report("Agent->Model", f"agent {aid}.underlying_models={m}", "model id not found", f"{MAIN}/src/content/agents/{aid}.md")
        c = a.get("company")
        if c and c not in company_ids:
            report("Agent->Company", f"agent {aid}.company={c}", "company id not found", f"{MAIN}/src/content/agents/{aid}.md")
    for aid, a in apis.items():
        if a.get("provider") not in company_ids:
            report("API->Company", f"api {aid}.provider={a.get('provider')}", "company id not found", f"{MAIN}/src/content/apis/{aid}.md")
        pr = a.get("pricing_ref")
        if pr and pr not in pricing_ids:
            report("API->Pricing", f"api {aid}.pricing_ref={pr}", "pricing id not found", f"{MAIN}/src/content/apis/{aid}.md")
        for cl in a.get("context_limits", []):
            if cl.get("model") and cl["model"] not in model_ids:
                report("API->Model", f"api {aid}.context_limits.model={cl['model']}", "model id not found", f"{MAIN}/src/content/apis/{aid}.md")
    for mid, m in models.items():
        pr = (m.get("pricing") or {}).get("pricing_ref")
        if pr and pr not in pricing_ids:
            report("Model->Pricing", f"model {mid}.pricing_ref={pr}", "pricing id not found", f"{MAIN}/src/content/models/{mid}.md")
    for pid, p in pricing.items():
        for m in p.get("models", []):
            if m.get("model") and m["model"] not in model_ids:
                report("Pricing->Model", f"pricing {pid}.model={m['model']}", "model id not found", f"{MAIN}/src/content/pricing/{pid}.md")
        if p.get("provider_id") not in company_ids:
            report("Pricing->Company", f"pricing {pid}.provider_id={p.get('provider_id')}", "company id not found", f"{MAIN}/src/content/pricing/{pid}.md")

    # --- Check 3: data-site company pages carry Agents / API / foundation / open sections
    #     matching the main site (and the reverse pointers) ---
    for f in data_files("companies"):
        sid = os.path.basename(f)[:-3]
        secs = data_sections(f)
        # foundation + open models
        ds_fm = sorted(section_ids(secs.get("Foundation Models", "")))
        ds_om = sorted(section_ids(secs.get("Open Models", "")))
        main_fm = sorted((companies.get(sid, {}).get("foundation_models") or []))
        main_om = sorted((companies.get(sid, {}).get("open_models") or []))
        if ds_fm != main_fm:
            report("DataSite Company->Model", f"data {sid} Foundation Models = {ds_fm}",
                   f"main {sid}.foundation_models = {main_fm}", f)
        if ds_om != main_om:
            report("DataSite Company->Model(open)", f"data {sid} Open Models = {ds_om}",
                   f"main {sid}.open_models = {main_om}", f)
        # agents section
        ds_agents = sorted(section_ids(secs.get("Agents", "")))
        if ds_agents != gt_company_agents.get(sid, []):
            report("DataSite Company->Agent", f"data {sid} Agents = {ds_agents}",
                   f"agents with company={sid}: {gt_company_agents.get(sid, [])}", f)
        # api section
        ds_api = sorted(section_ids(secs.get("APIs", "") or secs.get("API", "")))
        if ds_api != gt_company_apis.get(sid, []):
            report("DataSite Company->API", f"data {sid} API = {ds_api}",
                   f"apis with provider={sid}: {gt_company_apis.get(sid, [])}", f)

    # --- Check 4: data-site agent "Company" links match main-site agent.company ---
    for f in data_files("agents"):
        sid = os.path.basename(f)[:-3]
        secs = data_sections(f)
        comp = secs.get("Company", "")
        m = re.search(r"\]\(\.\./companies/([a-z0-9.+-]+)\.md\)", comp)
        ds_company = m.group(1) if m else None
        main_company = agents.get(sid, {}).get("company")
        if ds_company != main_company:
            report("DataSite Agent->Company", f"data {sid}.Company = {ds_company}",
                   f"main {sid}.company = {main_company}", f)

    # --- Check 5: data-site api "Provider" links match main-site api.provider ---
    for f in data_files("apis"):
        sid = os.path.basename(f)[:-3]
        secs = data_sections(f)
        prov = secs.get("Provider", "")
        m = re.search(r"\]\(\.\./companies/([a-z0-9.+-]+)\.md\)", prov)
        ds_provider = m.group(1) if m else None
        main_provider = apis.get(sid, {}).get("provider")
        if ds_provider != main_provider:
            report("DataSite API->Company", f"data {sid}.Provider = {ds_provider}",
                   f"main {sid}.provider = {main_provider}", f)

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------
    if not contradictions:
        print("OK: 0 contradictions")
        return 0

    print(f"{len(contradictions)} contradictions found:\n")
    by_pair = {}
    for c in contradictions:
        by_pair.setdefault(c["pair"], []).append(c)
    for pair, items in sorted(by_pair.items()):
        print(f"## {pair} ({len(items)})")
        for c in items:
            print(f"  - entity: {c['where']}")
            print(f"      face A (declared): {c['face_a']}")
            print(f"      face B (truth):    {c['face_b']}")
        print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
