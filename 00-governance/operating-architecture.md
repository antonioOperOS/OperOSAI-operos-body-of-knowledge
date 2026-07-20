---
id: SYS-000
version: 0.2
kind: system
status: drafting
---

# Operating Architecture

Central index for every OperOS Method object, framework, asset, automation, Jira work item, and release.

## System of Record

| Layer | Platform | Authority |
|---|---|---|
| Canonical IP | GitHub | Approved Method source, schemas, ontology, prompts, agent specifications, release tags |
| Human Knowledge Portal | Confluence | Navigation, collaboration, training, implementation guidance |
| Execution | Jira | Work packages, owners, approvals, dependencies, release readiness |
| Enterprise Brain | Databricks (planned) | Governed ingestion, structured objects, retrieval, evaluation, agents, telemetry |
| Publications & Assets | Google Drive | PDF, DOCX, presentations, media, legal, client delivery |

## Source-of-Truth Rule

GitHub defines what the approved OperOS Method is. Confluence presents it to humans. Databricks represents, retrieves, evaluates, and improves it. Jira controls the work required to change and release it. Google Drive distributes approved artifacts.

## Release Container

- Release: OperOS Method v1.0
- Jira Epic: [OBOS-1](https://operos.atlassian.net/browse/OBOS-1)
- Confluence Home: [OperOS Method - OBOS](https://operos.atlassian.net/wiki/spaces/TLAC)
- Release Target: July 26, 2026
