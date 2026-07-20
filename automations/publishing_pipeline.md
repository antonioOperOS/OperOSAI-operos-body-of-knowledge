---
id: AUT-002
version: 0.1.0
status: draft
kind: automation
publish_to: [internal_ops, platform_design]
---

# Publishing Pipeline

## Purpose

Automate conversion of OperOS source objects into market-facing and implementation-ready assets.

## Pipeline

```mermaid
flowchart LR
  A[Markdown Source] --> B[Validate Frontmatter]
  B --> C[Update Manifest]
  C --> D[Generate Digital Book]
  C --> E[Generate Sales Assets]
  C --> F[Generate Workshop Materials]
  C --> G[Generate AI Coach Objects]
  D --> H[Static Site]
  E --> I[PDF/DOCX/PPTX]
  F --> I
  G --> J[Vector/RAG Index]
```

## Validation checks

- object ID exists
- version exists
- status valid
- dependencies exist
- required framework sections present
- no unsupported claims
- no copied source material
- publishing targets defined

## Release process

1. Draft object.
2. Validate schema.
3. Update manifest.
4. Generate outputs.
5. QA outputs.
6. Create release bundle.
7. Publish.
8. Capture feedback.
9. Update source.
