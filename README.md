# OperOS Method — Body of Knowledge (OBOS)

**RoT — Return on Tokens.** Revenue generated per token spent, proven against a holdout. That's the one metric every asset in this repository must ultimately serve. See `core-concepts/RoT-return-on-tokens.md`.

## The AI Native Playbook

This repo is being written in public, in parallel with the actual business it describes. Antonio is writing the execution plan, the methodology, and the big-picture narrative here — in the open, as it happens. Rafael and the team are building the real infrastructure behind it at the same time (the GTM Engine's agents, HubSpot instrumentation, the Databricks catalog). Neither waits for the other to finish. The result, once both sides catch up to each other, is the AI Native Playbook: not a retrospective case study, but a document written live while the company it describes was still being built.

## What this is

This repository is the canonical source of the OperOS Business Operating System (OBOS) — a complete, teachable, self-improving methodology for building, running, and scaling an AI-native company. It synthesizes (not copies) the strongest thinking on founder discipline, strategy, product, sales, operations, leadership, execution, adaptation, finance, and AI transformation into one internally-consistent system, plus OperOS's own six proprietary pillars: Knowledge, Governance, Reasoning, Execution, Measurement, Optimization.

**Core rule, inherited from the original v0.1 source system: source once, publish everywhere.** Every object here — framework, template, prompt, concept — has an ID, a version, a status, and a dependency map, so it can become a digital-book chapter, a sales one-pager, a workshop module, a certification lesson, an AI coach object, or a build-in-public post without being rewritten from scratch.

## System of record

| Layer | Platform | Authority |
|---|---|---|
| Canonical IP | **GitHub (this repo)** | Approved Method source, frameworks, ontology, prompts |
| Human Knowledge Portal | Confluence (`operos.atlassian.net`, space TLAC) | Navigation, collaboration, interim canonical source until an object is migrated here |
| Execution | Jira (epic OBOS-1) | Work packages, owners, release readiness |
| Enterprise Brain | Databricks (planned) | Ingestion, retrieval, evaluation, agents |
| Publications & Assets | Google Drive | Finished PDF/DOCX/PPTX/media |

Until an object below is marked `status: migrated`, its Confluence page remains the interim canonical source — see `MANIFEST.yaml` for the authoritative registry and links.

## Structure

- `00-governance/` — operating architecture, the 12-point productization rule
- `01-source-system/` — manifesto, category narrative, master ontology
- `02-frameworks/` — FW-001 through FW-008, mapped 1:1 to the Confluence Master Manifest / Jira OBOS-1 backlog
- `03-assessments/` `04-playbooks/` `05-sales-enablement/` `06-thought-leadership/` `07-certifications/` `08-case-studies/` `09-releases/` — the remaining tracked source object sets
- `10-architecture/` — the Content & Enterprise Brain Architecture (ARCH-001)
- `core-concepts/` — RoT and other load-bearing concepts referenced everywhere
- `templates/` `automations/` — reusable schemas and the publishing pipeline

## Who owns what

Antonio and Rafael co-build this IP. **GTM execution (outbound, agents, LinkedIn cadence, partner program) is owned by Rafael's GTM Engine** (private Confluence draft, being aligned separately) — this repo does not duplicate that. What this repo produces — frameworks, the RoT concept, real build milestones — is raw material for that engine's content channel, drafted as build-in-public posts in `automations/build-in-public-log.md`.

## Status

v0.2.0 — structural bootstrap. Frameworks FW-001.1–FW-001.3 have full content (migrated from the original v0.1 source system package). Everything else is a stub pointing to its live Confluence page until migrated. See `CHANGELOG.md`.
