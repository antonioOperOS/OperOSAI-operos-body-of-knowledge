---
id: FW-002
version: 0.2.0
status: partial
kind: framework
source_influences: [Ben Horowitz - The Hard Thing About Hard Things, Andy Grove - High Output Management, Jocko Willink - Extreme Ownership]
publish_to: [digital_book, sales_enablement, AI_coach]
dependencies: []
outputs: [scorecard.leadership_leverage]
confluence: https://operos.atlassian.net/wiki/spaces/TLAC/pages/49348629
jira: https://operos.atlassian.net/browse/OBOS-5
---

# Leadership & High Output Management

## Purpose

Turn management into a leverage system: better decisions, better meetings, better delegation, better feedback, and higher output per unit of leadership time. A manager's output is not their personal output — it is the output of the team and the adjacent teams under their influence. Every mechanism below exists to raise that ratio, not to make the manager feel busier.

## Visual model

```text
Decision Rights Matrix (who decides what, at what altitude)
  -> Task-Relevant Maturity Map (match delegation style to actual skill x will, per task)
    -> One-on-One Operating System (the recurring channel where maturity is assessed and calibrated)
      -> Manager Leverage System (the multiplier: which activities produce the highest output per hour)
        -> Leadership Feedback Loop (what came of it, fed back into the next cycle)
```

## Inputs

- Org chart and actual (not nominal) decision rights
- Task-Relevant Maturity per direct report, per domain (a person can be high-maturity in one area and low in another)
- Calendar data: meeting mix, 1:1 cadence, prep time
- Delegation backlog and follow-through rate
- Peacetime vs. wartime read on the current company/team stage (Horowitz's distinction between managing for optimization vs. managing for survival)
- Prior 1:1 notes and commitment history

## Steps

1. Build the Decision Rights Matrix first: for each recurring decision type, name who decides, who is consulted, and who is merely informed. Ambiguity here is the single biggest tax on leadership leverage.
2. Map Task-Relevant Maturity per person, per task — not a single "senior/junior" label. Grove's core insight: the right management style (directive, coaching, participative, delegating) is a function of the task, not a fixed trait of the person.
3. Run the One-on-One Operating System: fixed cadence, employee sets the agenda, manager listens for early signals of trouble (this is the highest-leverage activity a manager has, per Grove — a one-hour 1:1 improves the quality of a subordinate's output for two weeks or more).
4. Compute manager leverage explicitly: list the manager's recurring activities and rank by output-per-hour delivered to the team, not personal throughput. Cut or delegate the bottom of the list.
5. Apply Extreme Ownership at the review layer: when an initiative underperforms, the leader who owned it owns the diagnosis first, before any downward blame — this is what keeps the feedback loop honest instead of political.
6. Name whether the current mode is wartime or peacetime for the team in question, and adjust management style accordingly (peacetime optimizes process and consensus; wartime compresses decision cycles and tolerates less debate).
7. Close the Leadership Feedback Loop monthly: what decisions were made, what was delegated and to whom, what broke, what the 1:1s surfaced early enough to prevent a bigger failure.

## Outputs

- Decision Rights Matrix (living document, one per team)
- Task-Relevant Maturity map per direct report
- 1:1 cadence and agenda template
- Manager leverage audit (ranked activity list)
- Monthly leadership feedback brief
- Wartime/peacetime mode designation per team, reviewed quarterly

## Metrics

- Manager leverage ratio: team output change attributable to manager time invested (leading indicator)
- 1:1 completion rate and early-signal catch rate (how often a 1:1 surfaced a problem before it became a fire)
- Decision cycle time on matrixed decisions (should compress, not expand, as the matrix matures)
- Delegation follow-through rate (task-relevant maturity should visibly increase over 2-3 cycles per person)
- **Result metric (RoT terms):** for any leadership workflow OperOS instruments with AI (agenda prep, blocker detection, commitment tracking), the defined result metric is incremental revenue per token spent on that workflow, measured against a holdout team or period — not meetings held or summaries generated. No leadership automation here is considered Published until this is defined, per the Operating Rule.

## Failure modes

- One delegation style applied to every person and every task, ignoring Task-Relevant Maturity
- 1:1s that become status reports instead of the employee's agenda
- Decision rights left implicit, so every decision re-litigates who gets to make it
- Managing in peacetime mode during a wartime moment (or vice versa) — wrong tempo for the actual stage
- Leadership feedback loop that assigns blame downward before the leader owns the miss
- Leverage activities never audited, so a manager's calendar fills with low-output work by default

## AI augmentation

OperOS can prepare 1:1 agendas from prior commitments and current blockers, flag decisions being made outside the Decision Rights Matrix, detect early-warning language in written updates (the kind a good 1:1 would catch), and summarize commitments and follow-through rate per person automatically — surfacing where task-relevant maturity is actually rising or stalling instead of relying on manager memory.

## OperOS implementation path

1. Ingest org chart and decision-log data to draft an initial Decision Rights Matrix.
2. Instrument 1:1 cadence and agenda capture through the knowledge graph.
3. Build the Task-Relevant Maturity map per person, per task category, from delegation and follow-through history.
4. Run the manager leverage audit against real calendar data, not self-report.
5. Connect leadership feedback outputs to Jira execution and Confluence knowledge so commitments trace to outcomes.
6. Define and instrument the RoT result metric for any AI-assisted leadership workflow before calling it Published.

*Confluence source (page 49348629) provided the purpose statement, the five named core models, and a generic implementation outline, but no worked-out mechanics for any of them. This migration synthesizes the mechanics from the framework's named source influences (Grove, Horowitz, Willink) rather than copying detail that didn't exist on the page. Status is `partial`: still missing are OperOS-specific worked examples (real Decision Rights Matrix instances, real 1:1 templates in use) and validation against an actual OperOS leadership cycle — pending a fuller Confluence writeup or a direct session with Antonio.*
