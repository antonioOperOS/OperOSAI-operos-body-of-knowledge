---
id: FW-005
version: 0.2.0
status: migrated
kind: framework-set
source_influences: [Alex Hormozi - offers/value equation, Brian Tracy - enterprise selling]
publish_to: [digital_book, sales_enablement, AI_coach]
dependencies: [FW-001, FW-003, FW-004]
outputs: [scorecard.revenue_offers_selling, playbook.offer_ladder]
confluence: https://operos.atlassian.net/wiki/spaces/TLAC/pages/48988162
jira: https://operos.atlassian.net/browse/OBOS-8
last_updated: 2026-07-23
note: "Confluence source (page 48988162, v0.2) was substantially developed — four named sub-models (Grand Outcome Offer Architecture, Enterprise Discovery System, Buying Committee Map, Expansion Pathway) each with their own inputs/steps/outputs/metrics/failure modes, plus a sales motion and an offer ladder. This migration synthesizes and normalizes that material into the repo's standard single-file 9-section structure (matching FW-002 through FW-004), rewritten in OperOS's own language rather than copied verbatim, with an explicit RoT-terms result metric added per the Operating Rule (not present in the source page). Directly feeds `05-sales-enablement/SALES-001-sales-enablement.md`."
---

# Revenue, Offers & Selling

## Purpose

Turn the OperOS Method into a repeatable commercial motion: package the work as a business outcome instead of an AI capability, run enterprise sales conversations that surface real pain and a real decision process, manage the multi-stakeholder buying committee that enterprise deals actually run through, and convert a single proven pilot into department- and enterprise-wide expansion.

## Visual model

```text
Ideal customer + economic buyer
  -> Painful, measurable business problem
    -> Grand Outcome Offer (transformation promise, de-risked via diagnostic + phased pilot)
      -> Enterprise Discovery (context, pain, impact, decision map, success criteria)
        -> Buying Committee Map (economic / technical / user buyers, risk-legal, champion, blocker)
          -> Pilot -> Measured Outcome (proof artifact)
            -> Expansion Pathway (pilot workflow -> department -> cross-functional -> enterprise operating layer)
```

## Inputs

- Target customer segment and named economic buyer
- The specific business pain and its current cost of inaction (time, money, risk, or revenue)
- Existing workflows, systems, and AI posture at the account
- Stakeholder list across the buying committee (economic, technical, user, risk/legal, champion, blocker)
- Prior sales notes, discovery call recordings or summaries, and any existing pilot results

## Steps

1. **Package the Grand Outcome Offer.** Define the customer segment and economic buyer first, then name the painful, measurable problem before naming any AI capability — the offer promises a transformation in outcome language, not a feature list. Reduce the buyer's perceived risk with a diagnostic, a roadmap, and a phased pilot; reduce perceived time-to-value with 30/60/90-day implementation packaging; and attach a proof requirement (metrics, case-study format, executive reporting) before the deal closes, not after.
2. **Run Enterprise Discovery as a structured sequence, not a pitch.** Move through company strategy and priorities, where execution or workflow friction is creating cost, the quantified impact of that friction, the systems and stakeholders involved, what a successful pilot would need to prove, and the actual decision process and timeline — in that order. Pitching before this sequence is complete is the single most common way enterprise deals stall.
3. **Map the Buying Committee before the deal advances.** Enterprise purchases are rarely a single decision-maker: the economic buyer needs ROI and risk covered by a business case, the technical buyer needs a reference architecture, the user buyer needs a real pilot experience, risk/legal needs a control model, the champion needs a narrative and internal enablement tools, and the blocker needs their specific objection named and handled — not avoided. Skipping any one role is how a technically-won deal stalls in procurement or security review.
4. **Prove the outcome, then build the Expansion Pathway.** A pilot that hits its measured outcome is the trigger, not the finish line: expansion moves from the single pilot workflow to a department system, then a cross-functional system, then the full enterprise operating layer. The same expansion triggers apply in reverse — an adjacent workflow sharing the same knowledge base, multiple teams running the same manual process, a new governance requirement, or an executive asking for a dashboard are diagnostic signals that expansion is available, not something to wait to be asked for.
5. **Run the full sales motion as one connected line, not four disconnected steps.** Thought leadership generates the executive meeting; the meeting earns the diagnostic; the diagnostic earns the roadmap; the roadmap earns the pilot; the pilot produces the outcome report; the outcome report earns expansion. Each stage's output is the input the next stage requires — a diagnostic run without a prior discovery conversation, or a pilot sold without a defined success metric, breaks the chain downstream.

## Outputs

- Offer definition: name, target customer, core problem, promised outcome, implementation package, proof requirement, pricing logic, expansion path
- Discovery outputs: pain map, quantified impact estimate, stakeholder map, use-case shortlist, success criteria, recommended next step
- Buying committee outputs: stakeholder and influence map, proof plan by role, mutual action plan, risk register
- Expansion outputs: expansion map, next-workflow recommendation, department rollout plan, executive value report, renewal/upsell path
- The Offer Ladder itself: AI Enterprise Diagnostic -> Knowledge Foundation Sprint -> Workflow Automation Pilot -> Operating Cadence Deployment -> Enterprise AI Operating System -> Certification/Enablement

## Metrics

- Conversion at each stage of the motion: meeting-to-diagnostic, diagnostic-to-proposal, proposal-to-close, pilot activation
- Time to first measurable value (the clock the buyer is actually watching, not the clock the seller is watching)
- Stakeholder coverage: percentage of the buying committee roles identified and addressed with role-specific proof before close
- Pilot-to-expansion conversion, number of workflows automated per account, adoption by department, net revenue retention
- Gross margin by implementation package on the Offer Ladder
- **Result metric (RoT terms):** for any AI-assisted step in this motion (discovery-call summarization, offer-variant generation, stakeholder extraction from notes, expansion recommendation), the defined result metric is incremental revenue per token spent on that workflow, measured against a holdout sales process or rep — not proposals generated or calls summarized. No sales automation here is considered Published until this is defined, per the Operating Rule.

## Failure modes

- Selling the AI capability instead of the business outcome — the Grand Outcome Offer collapses back into a feature pitch
- Pitching before discovery is complete, so the offer doesn't match a quantified, agreed-upon problem
- No named economic buyer, or a champion mistaken for one — the deal has energy but no one who can actually approve spend
- Discovery treats curiosity as urgency, or produces no quantified impact estimate, so the business case has nothing to point to
- Buying Committee Map skips a role — most often risk/legal or the blocker — and the deal stalls in a review no one saw coming
- Custom, bespoke delivery replaces productized packaging, so the offer can't scale past the first few deals
- Pilot hits its outcome but no Expansion Pathway conversation follows, so a proven result never becomes account growth
- No proof artifact captured after implementation — the next sale has to start from zero instead of building on the last one

## AI augmentation

OperOS can generate offer variants by persona and industry from the same Grand Outcome Offer core, translate diagnostic findings directly into offer language, draft proposals from reusable modules, and flag missing proof or ROI assumptions before a proposal goes out. On discovery, it can prepare the account brief, generate the question plan, summarize the call and extract commitments, and score opportunity quality against the Buying Committee Map. Post-pilot, it can recommend the specific expansion path from the pilot's actual results rather than a generic upsell script.

## OperOS implementation path

1. Select the target segment and build the Grand Outcome Offer around one quantified business problem, not a capability list.
2. Map that offer to the corresponding diagnostic and implementation playbook (`03-assessments/ASMT-001-assessments-diagnostics.md`, `04-playbooks/PLAY-001-implementation-playbooks.md`).
3. Build sales assets and proposal modules against the Buying Committee's six roles, so every deal has role-specific proof ready before it's asked for.
4. Instrument discovery-call and proposal generation with AI augmentation, and track conversion at every stage of the sales motion.
5. Feed every closed pilot's measured outcome into the Expansion Pathway and into case studies / market positioning (`08-case-studies/PROOF-001-case-studies-proof.md`).
6. Define and instrument the RoT result metric for any AI-assisted step in this motion before calling it Published.

*Confluence source (page 48988162, v0.2) was substantially developed — not a skeleton — with four named sub-models (Grand Outcome Offer Architecture, Enterprise Discovery System, Buying Committee Map, Expansion Pathway), an explicit sales motion, and an offer ladder. This migration synthesizes that material into the repo's standard 9-section structure and OperOS's own language, and adds the RoT-terms result metric the source page did not define. Marked `migrated` rather than `partial`: the source content was complete enough to normalize directly, unlike FW-002 through FW-004, which required drawing on named external source influences to fill gaps.*
