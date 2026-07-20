---
id: FW-001.5
version: 0.1.0
status: draft
kind: framework
source_influences: [BCG Growth-Share Matrix, BCG Experience Curve]
publish_to: [digital_book, sales_enablement, AI_coach]
dependencies: [FW-001.1, FW-001.2]
---

# Growth-Share & Experience Curve (BCG Method)

## Purpose

Allocate capital and attention across products/segments/clients by growth potential and relative position, and use cumulative-volume cost declines to time when to compete on price versus differentiation.

## Visual model

```text
High Growth | Question Marks   |  Stars
            |------------------|------------------
Low Growth  | Dogs             |  Cash Cows
            |  Low Share            High Share
```

## Inputs
- Market growth rate per segment/product/client tier
- Relative market share or relative position per segment
- Cumulative production/delivery volume and unit cost history

## Steps
1. Plot each product/segment/client tier by growth rate and relative share.
2. Classify: Star, Cash Cow, Question Mark, Dog.
3. Assign capital/attention allocation rules per quadrant.
4. Track unit cost against cumulative volume (experience curve) per offer.
5. Decide, per offer, whether the strategy is cost-down-and-scale or differentiate-and-hold-price.
6. Revisit quarterly as growth/share shifts.

## Outputs
- Portfolio matrix (updated quarterly)
- Capital/attention allocation plan
- Experience-curve cost tracker per offer

## Metrics
- Share and growth trend per quadrant
- Unit cost decline rate vs. cumulative volume
- Capital allocated to Stars/Question Marks vs. Cash Cows/Dogs

## Failure modes
- Treating all "growth" segments as equally worth funding
- Ignoring cost-down discipline on offers meant to scale on price
- Never actually killing or divesting Dogs

## AI augmentation
OperOS can auto-update the matrix from CRM/finance data each quarter and flag offers whose unit economics contradict their assigned quadrant strategy.

## OperOS implementation path
1. Connect CRM and finance data per segment/offer.
2. Auto-generate the quarterly matrix.
3. Flag misaligned capital allocation.
4. Feed results back into FW-001.1 Strategy Cascade review.
