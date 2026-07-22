---
id: FW-004
version: 0.2.0
status: partial
kind: framework-set
source_influences: [Cardone Ventures, Eliyahu Goldratt - The Goal, The Toyota Way]
publish_to: [digital_book, sales_enablement, AI_coach]
dependencies: [FW-001, FW-002]
outputs: [scorecard.operations_accountability]
confluence: https://operos.atlassian.net/wiki/spaces/TLAC/pages/49414145
jira: https://operos.atlassian.net/browse/OBOS-7
last_updated: 2026-07-22
note: "Confluence source (page 49414145) names five core models (Accountability Map, Process-to-SOP System, Constraint Resolution Loop, Continuous Improvement Flywheel, Weekly Operations Review) and a 5-step implementation path, but does not elaborate mechanism. This migration builds the full framework from that skeleton plus Cardone Ventures' seat-based accountability discipline, Goldratt's Theory of Constraints (The Goal), and Toyota Way standardized work / kaizen. Marked partial rather than migrated: still missing are OperOS-specific worked examples and validation against an actual OperOS operations cycle."
---

# Operations & Accountability

## Purpose

Convert strategic intent into repeatable operating systems: clear seat-based ownership, documented process that matches how work is actually done, a disciplined method for finding and breaking the one constraint limiting system throughput, and a cadence of small improvements that compounds instead of a periodic overhaul that doesn't stick.

## Visual model

```text
Accountability Map (seats, owners, and the one number each seat owns)
  -> Process-to-SOP System (the seat's repeatable work becomes a documented, versioned standard)
    -> Constraint Resolution Loop (find the one constraint holding back system throughput; exploit, subordinate, elevate)
      -> Continuous Improvement Flywheel (standard-owner-led changes to the SOP, tested small, compounding)
        -> Weekly Operations Review (the cadence that checks constraint drift and validates the SOP still matches reality)
```

## Inputs

- Draft accountability chart: seats (not people) mapped to functions, each seat with a defined number it owns
- Current SOP inventory, with owner and last-reviewed date per SOP
- Throughput data across the value stream, or the best available proxy, to locate the binding constraint
- A genchi genbutsu ("go and see") observation of the process as actually run today, not as documented
- Prior Weekly Operations Review notes and open action items

## Steps

1. Build the Accountability Map as seats, not names: every function gets one seat, one owner, and one number that seat is accountable for. A person underperforming in an undefined seat is an accountability-map problem to fix first, not a talent problem to solve second — this is the Cardone Ventures discipline of role clarity before performance conversations.
2. Convert each seat's recurring work into a Process-to-SOP: observe the process as it is actually run before writing anything down, then document the standard, version it, and name a single owner who is allowed to change it.
3. Run the Constraint Resolution Loop — Goldratt's five focusing steps: identify the system's one binding constraint; decide how to exploit it without new investment; subordinate every other process to that decision (stop optimizing non-constraints); elevate the constraint if exploitation alone isn't enough; then repeat, because a resolved constraint reveals the next one.
4. Feed every resolved constraint or process gap into the Continuous Improvement Flywheel: the standard's owner proposes a change, it's tested small, and it's folded into the SOP's next version if it holds or discarded if it doesn't. Improvement authority sits with the person doing the work, not a separate improvement team.
5. Close the loop weekly in the Operations Review: what constraint is currently binding, what each seat owner reported against their number, which SOPs changed and why, and what's queued next.

## Outputs

- Accountability Map (seats, owners, numbers — living document, reviewed quarterly)
- SOP library, versioned per seat, with a named owner and a last-reviewed date
- Constraint log: what's binding now, what's been resolved, and what the resolution actually was
- Weekly Operations Review notes and open action list
- Kaizen log: process changes proposed, tested, and accepted or rejected

## Metrics

- System throughput at the current constraint — the only throughput number that matters until the constraint moves. Goldratt's core claim: local efficiency gains anywhere else don't raise total system output.
- Seat accountability coverage: percentage of functions with a named seat owner and a defined number (should trend to 100%)
- SOP staleness: percentage of SOPs past their review-by date
- Kaizen throughput: process changes tested per month, and the percentage that survive into the standard
- **Result metric (RoT terms):** for any operations workflow OperOS instruments with AI (SOP drift detection, constraint-signal monitoring, accountability reporting), the defined result metric is incremental revenue per token spent on that workflow, measured against a holdout process or team — not SOPs generated or reviews automated. No operations automation here is considered Published until this is defined, per the Operating Rule.

## Failure modes

- Accountability map drawn around current people instead of seats, so it has to be redrawn every time someone leaves
- SOPs written from what the process should be instead of genchi genbutsu observation of what it actually is — documentation nobody follows
- Improving a process that isn't the constraint: raises local efficiency, doesn't raise system throughput, and creates the illusion of progress — the exact trap Goldratt warns against in The Goal
- The Constraint Resolution Loop stops after "exploit" instead of subordinating every other process to it, so the fix gets quietly undone by an unrelated process still optimizing for its own local metric
- Continuous improvement treated as a separate initiative or team rather than the standard-owner's job, so kaizen dies the moment executive attention moves elsewhere
- Weekly Operations Review becomes a status-reporting ritual instead of an actual constraint check

## AI augmentation

OperOS can flag SOPs past their review-by date, surface throughput signals that suggest the binding constraint has shifted before a human notices, draft the Weekly Operations Review agenda from the prior week's constraint log and open kaizen items, and detect when a seat's actual output is drifting from its accountability number early enough to intervene before the quarterly review.

## OperOS implementation path

1. Ingest the org chart and reshape it into seats-and-numbers, independent of current headcount.
2. Instrument SOP versioning and review-by dates through the knowledge graph, seeded from genchi genbutsu observation rather than existing documentation.
3. Build a lightweight throughput model across the value stream to locate the current constraint (start with the most visibly bottlenecked stage if full instrumentation isn't available yet).
4. Run the Constraint Resolution Loop against that model and log exploit/subordinate/elevate decisions explicitly, not just the final fix.
5. Connect the Continuous Improvement Flywheel and Weekly Operations Review outputs to Jira execution and Confluence knowledge so kaizen changes trace to their SOP version and their constraint-log entry.
6. Define and instrument the RoT result metric for any AI-assisted operations workflow before calling it Published.

*Confluence source (page 49414145) provided the purpose statement, the five named core models, and a generic implementation outline, but no worked-out mechanics for any of them. This migration synthesizes the mechanics from the framework's named source influences (Cardone Ventures' seat-based accountability discipline, Goldratt's Theory of Constraints from The Goal, and Toyota Way standardized work and kaizen) rather than copying detail that didn't exist on the page. Status is `partial`: still missing are OperOS-specific worked examples (a real Accountability Map instance, a real constraint log from an actual OperOS process) and validation against an actual OperOS operations cycle — pending a fuller Confluence writeup or a direct session with Antonio.*
