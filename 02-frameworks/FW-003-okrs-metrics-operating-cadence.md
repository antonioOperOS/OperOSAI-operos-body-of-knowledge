---
id: FW-003
version: 0.2.0
status: partial
kind: framework-set
publish_to: [digital_book, executive_workshop, sales_enablement, AI_coach]
dependencies: [FW-001, CONCEPT-RoT]
outputs: [scorecard.executive, workshop.okr_calibration]
source_influences: [John Doerr - Measure What Matters]
confluence: https://operos.atlassian.net/wiki/spaces/TLAC/pages/49381377
jira: https://operos.atlassian.net/browse/OBOS-6
last_updated: 2026-07-21
note: "Confluence source (page 49381377) names six core models (Strategy-to-OKR Cascade, Leading and Lagging Indicator Map, Weekly Business Review, Monthly Operating Review, Quarterly Reset, Executive Scorecard) and a 5-step implementation path, but does not elaborate mechanism. This migration builds the full framework from that skeleton plus Doerr's Measure What Matters (committed vs. aspirational OKRs, CFRs, 0.0-1.0 scoring, sandbagging). Marked partial rather than migrated: each of the six core models likely deserves its own sub-file (FW-003.1-3.6), mirroring the FW-001 pattern, once reviewed."
---

# OKRs, Metrics & Operating Cadence

## Purpose

Translate strategy into measurable execution through objectives, key results, scorecards, and a review rhythm that catches drift while it's still a leading indicator — not at the quarterly post-mortem when it's already a lagging result. Feeds the Executive Scorecard directly and is the operating-cadence layer underneath the Strategy Cascade (FW-001).

## Visual model

```text
Strategy (FW-001 Strategy Cascade)
  -> Strategy-to-OKR Cascade (company -> division -> team -> individual, negotiated bottom-up)
    -> Leading and Lagging Indicator Map (name the leading signal before the lagging result exists)
      -> Weekly Business Review (leading indicators, blockers, no lagging-revenue narrative)
        -> Monthly Operating Review (trend, root cause, reallocation)
          -> Quarterly Reset (score 0.0-1.0, retire, cascade next set)
            -> Executive Scorecard (continuously current, not rebuilt each quarter)
```

## Inputs

- Company strategy and guiding choices (FW-001 output)
- Current OKR set, if one exists, and prior-cycle attainment scores
- CRM, product, and finance data feeds for each proposed key result
- Calendar and attendee list for the weekly/monthly/quarterly review cadence
- Prior review notes and open action items

## Steps

1. **Cascade objectives top-down, negotiate key results bottom-up.** Doerr's core correction to naive cascading: key results should be substantially proposed by the team that owns them, not dictated by the level above. Dictated KRs produce compliance; negotiated KRs produce ownership.
2. **Label every OKR committed or aspirational, explicitly, at the point of setting it** — never after the fact. Conflating the two is the single most common cause of OKR programs collapsing: committed goals treated as stretch goals lose accountability; stretch goals treated as committed goals get quietly sandbagged down to something safe.
3. **For every key result, name the leading indicator before the lagging result exists.** If a KR can only be measured at quarter-end, the team has a scorecard, not an operating cadence — there's nothing to review weekly or monthly.
4. **Run the Weekly Business Review short and leading-indicator-only.** Blockers and the leading signals that moved this week — not a narrative recap of last month's revenue.
5. **Run the Monthly Operating Review for trend and root cause.** Any leading indicator moving the wrong way for two consecutive weeks gets a root-cause discussion and, if warranted, a resource reallocation decision — before it becomes a missed lagging result.
6. **Run the Quarterly Reset with real scoring.** Score each KR 0.0-1.0 (Doerr/Google convention: ~0.7 is a good outcome on a genuine stretch goal). Retire completed OKRs, carry forward what's still live, cascade the next set through the same negotiated process in step 1.
7. **Maintain the Executive Scorecard as a living document, not a quarterly rebuild.** It should be true on the random Tuesday someone opens it, not just true on presentation day.
8. **Run CFRs (Conversations, Feedback, Recognition) alongside the OKR cadence, not as a separate HR ritual.** Doerr's point: OKRs without CFRs become a compliance exercise; recognition needs to reinforce the metrics that actually matter, not attendance or effort.

## Outputs

- Documented, versioned company OKR set with committed/aspirational labels
- Leading/Lagging Indicator Map, one row per key result
- WBR / MOR / Quarterly Reset agenda templates
- Quarterly OKR scorecard with 0.0-1.0 scores and rationale
- CFR log tied to specific KRs, not generic praise
- Continuously current Executive Scorecard

## Metrics

- OKR score distribution: healthy stretch-goal programs show a spread of scores; a cluster near 1.0 across most KRs is a sandbagging signal, not a success signal
- Leading-to-lagging correlation: does the chosen leading indicator actually predict the lagging result it's supposed to forecast, checked retroactively each quarter
- Review cadence adherence: WBR/MOR/Quarterly Reset held on schedule with the right attendees
- Time from leading-indicator drift detected to a documented corrective action
- RoT framing: any key result driven by a governed agentic loop (an AI-assisted workflow, an agent-run process) is not counted as "attained" in the scorecard until its result metric is stated and measured in RoT terms — revenue per token against a holdout — not proxy activity like queries answered or workflows triggered, per the Operating Rule.

## Failure modes

- Every KR scored near 1.0 — the clearest tell that goals were set low enough to guarantee hitting them (Doerr's sandbagging warning)
- Committed and aspirational OKRs conflated, so accountability swings either too harsh (punishing a genuine stretch miss) or too soft (no consequence for missing a committed number)
- Key results with no leading indicator defined, so the team only learns about a problem at the quarterly post-mortem, when it's too late to correct
- Weekly and monthly reviews that recap lagging revenue numbers instead of leading signals — reactive reporting dressed up as an operating cadence
- OKRs cascaded as top-down directives with no negotiation, producing quiet compliance instead of real ownership
- Executive Scorecard rebuilt from scratch each quarter instead of maintained continuously, so it is stale by definition on the day it's presented
- CFRs run as a disconnected HR ritual, recognizing effort or attendance rather than reinforcing the specific KRs that matter

## AI augmentation

OperOS can auto-populate the Executive Scorecard from connected CRM, product, and finance systems so it stays current instead of being manually rebuilt each quarter; draft Weekly and Monthly Business Review agendas from whichever leading indicators moved most since the last review; flag key results with no defined leading indicator; flag scoring patterns consistent with sandbagging across an OKR set; and for any KR driven by a governed agentic loop, surface plainly whether its RoT-against-holdout result has actually been measured yet, or is still a stated intent rather than a proven outcome.

## OperOS implementation path

1. Define company objectives, explicitly labeled committed or aspirational.
2. Cascade measurable key results, negotiated bottom-up from each owning team rather than dictated.
3. Connect metrics to workflows and owners so leading indicators update automatically instead of by manual report.
4. Automate weekly and monthly review preparation (WBR/MOR agendas) from live data.
5. Track decisions, actions, and learning loops through the Quarterly Reset, and hold every RoT-relevant key result to the holdout-proof bar before scoring it as attained.
