---
id: FW-001.4
version: 0.1.0
status: draft
kind: framework
source_influences: [McKinsey structured problem-solving]
publish_to: [digital_book, sales_enablement, AI_coach]
dependencies: [FW-001.1]
---

# MECE Issue Trees (McKinsey Method)

## Purpose

Decompose ambiguous, high-stakes problems into mutually exclusive, collectively exhaustive branches so the real driver of an issue — not just its symptoms — gets found and acted on.

## Visual model

```text
Core Question
  -> Hypothesis
    -> Issue Tree (MECE branches)
      -> Data required per branch
        -> Analysis
          -> Synthesis ("so what")
            -> Recommendation
```

## Inputs
- The core business question or decision
- Working hypothesis (not a blank-slate brainstorm)
- Available data sources per branch

## Steps
1. State the core question precisely.
2. Form an initial hypothesis (not proof — a testable answer).
3. Break the hypothesis into MECE branches (no overlap, no gaps).
4. Identify what data would prove or kill each branch.
5. Analyze in parallel; kill branches fast when disproven.
6. Synthesize into a "so what," not a data dump.
7. Recommend one clear action, with the tradeoffs named.

## Outputs
- Issue tree diagram
- One-page hypothesis-to-recommendation brief
- Analysis backlog per branch

## Metrics
- Time from question to recommendation
- % of branches killed vs. pursued (should be most branches killed fast)
- Recommendation adoption rate

## Failure modes
- Branches that overlap or leave gaps (not actually MECE)
- Boiling the ocean instead of hypothesis-driven analysis
- Presenting data instead of a "so what"

## AI augmentation
OperOS can draft candidate issue trees from a stated problem, flag non-MECE branches, and pull the data needed per branch from connected sources automatically.

## OperOS implementation path
1. Capture the core question as a knowledge object.
2. Generate a draft issue tree via AI, human-reviewed for MECE-ness.
3. Route data-gathering tasks per branch to agents/humans.
4. Auto-draft the synthesis brief once branches are resolved.
