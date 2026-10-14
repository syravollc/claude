# Dropshipping product shortlist (DRAFT, pre-research)

Status: nothing run, nothing spent. Written 2026-10-14 under the rules in `DROPSHIPPING_TEST_PLAN.md`.

## 0. How to read this

- These are **product types**, chosen by my judgment. They are not data-backed picks. I have no Google Trends, Meta Ad Library, supplier or Amazon data from this environment.
- Every price and cost below is an **assumed placeholder** used only to show whether the arithmetic could work. The user's real supplier quotes replace them. A candidate that fails once real numbers are in is rejected, per the plan.
- Niche scores (22/30 etc.) are earlier judgment, not measurements.

## 1. The three candidates

| # | Niche | Product type | Assumed retail | Assumed landed cost | Gross margin | M (contribution) | Required click-to-purchase rate at CPC $0.60 / $1.00 |
|---|---|---|---|---|---|---|---|
| A | Pet comfort (22/30) | Calming donut/orthopedic pet bed, medium, washable cover | $49 | $22 | 55% | $22.83 | 2.6% / 4.4% |
| B | WFH ergonomics (22/30) | Adjustable under-desk footrest (non-electric, foam or mesh) | $39 | $16 | 59% | $19.62 | 3.1% / 5.1% |
| C | Coffee/tea (21/30) | Manual hand coffee grinder, stainless body | $42 | $20 | 52% | $18.38 | 3.3% / 5.4% |

M uses the plan formula: `M = P - C - (2.9% * P + $0.30) - 5% * P`.

Honest read of the arithmetic:

- **A** is the only one that clears the plan's 4% required-rate gate at CPC $1.00 without being rejected outright (4.4% would fail it; at $0.60 it passes). It has the most margin cushion, but bulky shipping may push real landed cost above $22.
- **B** passes at CPC $0.60 only. At $1.00 it fails the 4% gate.
- **C** is borderline on margin (52%) and passes the 4% gate only at CPC $0.60. Any cost overrun drops it below the 50% gate.
- All three need cold-traffic conversion of roughly 2.6-3.3% even with cheap clicks. Typical cold-traffic is 1-3%. **Expect each to fail on arithmetic if real CPC is above about $0.60.** That is a real possibility, not a footnote.

Known risks per candidate:

- **A, pet bed:** sizing returns, bulky shipping cost, very crowded on Amazon with low prices (customers will compare to a $30 Amazon bed). Pet "calming" claims must be avoided in ad copy (plan gate 4: no health claims). Use "plush, washable, soft," not "reduces anxiety."
- **B, footrest:** Amazon price anchor is often $20-30, which is below the $30 gate. Comfort is subjective, which can raise refunds. Avoid any posture or health claims.
- **C, grinder:** quality variance (burr type, wobble) drives reviews. Crowded niche with strong Amazon brands. Check trademark/lookalike issues. Low-cost imports often have a recurring defect, which is exactly what gate 5 checks.

## 2. What the user must verify (I cannot)

Record each result in `dropshipping_break_even.xlsx` (Test Log tab) before any spend. A candidate failing any item is rejected.

### Supplier (per candidate)
1. Exact unit cost at quantity 1.
2. Exact shipping fee to a customer for 1 unit.
3. Warehouse location: confirm **US** warehouse, not a "US shipping" claim from overseas.
4. Quoted delivery time to a few distant US zip codes (plan gate: 2-6 days).
5. Stock level and whether the supplier will notify you of stock-outs.
6. Return and defect policy, and who pays return shipping.
7. Whether the supplier ships with branded invoices or packing slips from you.
8. Enter the real numbers into the break-even sheet. Confirm margin >= 50%, price $30-80, required conversion <= 4%.

### Google Trends (12 months, United States)
1. Search the product term (for example "calming dog bed", "under desk footrest", "manual coffee grinder").
2. Record: flat, rising, falling, or one recent spike. Reject a one-off spike.
3. Note seasonality, especially the Q4 pattern.
4. Screenshot or note the date checked.

### Meta Ad Library (United States, all ads)
1. Search the product term and 2-3 close variants.
2. Record the number of active advertisers.
3. Record whether any single ad has run for 60+ days (a sign somebody is profitable) and how many near-identical ads exist (saturation).
4. Save links to 3 representative ads.
5. Judgment call required: demand but not saturation. Write your reasoning down.

### Amazon 1-3 star reviews (3 top comparable listings per candidate)
1. Note the Amazon price of each. If they sell near or below your price, you cannot win on price.
2. Read the 1-3 star reviews. Record any **recurring** defect (same complaint in several reviews: fit, smell, breakage, wobble).
3. Reject if a defect recurs and cannot be fixed by choosing a different supplier.

### Sample and terms (only after the above pass, under the $100 pre-spend allowance)
1. Order one sample only with an explicit yes from the user at the exact cost.
2. Record received quality and real delivery time.
3. Check store policies, sales-tax and business obligations for the user's location.

## 3. Recommended order if the user has little time

Verification order that wastes the least effort: supplier quote (kills most candidates fastest) -> Amazon price anchor -> Google Trends -> Meta Ad Library -> Amazon negative reviews -> sample.

## 4. Open question for the user

Which niche to pursue first: **pet comfort (A)**, **WFH ergonomics (B)**, or **coffee/tea (C)**? Only one product is tested at a time under the plan (a second only if the first is killed in stage 1).

My lean, stated as judgment and not evidence: **A**, because the margin cushion is largest, but it has the highest crowding and the highest shipping-cost uncertainty. If the user prefers lower return risk, **B**. I would test C last.

## 5. Q4 timing note

Today is 2026-10-14. A 5-day gate phase plus sample plus a 28-day test runs into late November. Delivery cutoffs and holiday ad costs raise CPC, so the gate-pass CPC assumptions above are optimistic for this window. The plan's section 11 already flags this. A test that fails in Q4 may not say much about the product in a normal quarter.
