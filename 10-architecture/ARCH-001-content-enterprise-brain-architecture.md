---
id: ARCH-001
version: 0.1
status: drafting
kind: architecture
jira: OBOS-19
---

# OperOS Content & Enterprise Brain Architecture

## Integration workstreams

1. Provision the private GitHub repository and governance controls. **Done** — this repo.
2. Export and normalize existing Confluence source objects into Markdown and YAML. **In progress** — see stub objects throughout this repo linking back to their Confluence source.
3. Establish `MANIFEST.yaml`, object schemas, and cross-link validation. **Done** — see root `MANIFEST.yaml`.
4. Create the Databricks `operos_brain` catalog and schemas. **Blocked** — no Databricks connector currently available to this session; requires manual setup or direct workspace access.
5. Implement approved-release ingestion from GitHub into Delta tables. **Blocked**, depends on #4.
6. Build retrieval indexes with object, version, access and citation metadata. **Blocked**, depends on #4/#5.
7. Establish evaluation datasets, human review, and production promotion gates. **Not started.**
8. Configure Confluence publication and Google Drive artifact distribution. **Not started.**

## Databricks state model (per object, once #4 is live)

Not Ingested -> Parsed -> Indexed -> Evaluated -> Production
