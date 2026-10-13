# Dropshipping test plan and kill rule

Status: DRAFT. Nothing here has been run or spent. Written before any data, so the rules cannot be tuned after seeing results.

## 1. Purpose and honesty clause

Answer one question cheaply: can one product in one niche be sold at a cost per purchase below its contribution margin?

- A pass means "earned a second, larger test round." It does not mean "profitable business." About 15 purchases cannot prove a stable edge.
- The expected outcome is failure. Most of the budget is likely lost. That is an acceptable, planned cost.
- Benchmarks (vendor blogs, not independent): net margins 5-20%, ads $8-15 per order.

## 2. Hard limits (set now, do not change mid-test)

| Item | Limit |
|---|---|
| Total cash cap, all costs | **$400** |
| Ad spend cap | $300 |
| Store, domain, tools, one sample order | $100 |
| Duration | 28 days from first ad spend |
| Products tested | 1 (a second only if the first is killed in stage 1) |
| Who approves spend | The human. AI agents never hold a card or ad-account credentials |

Raising any limit requires a written note in the log (section 9) before the money is spent.

## 3. Phase 0: pre-spend gates (days 1-5, spends under $100)

A product must pass **all** gates or it is rejected with no ad spend.

1. Retail price $30-80.
2. Landed cost (product + shipping to customer) gives **gross margin >= 50%** at that price.
3. Supplier ships from a **US warehouse**, with delivery of 2-6 days quoted.
4. Not fragile, not electrical or battery, no health or safety claims, no cosmetics or ingestibles, no brand or trademark conflict.
5. Amazon 1-3 star reviews for the same product show no recurring defect.
6. Google Trends (12 months) is flat or rising for the product term, not a recent one-off spike.
7. Meta Ad Library shows demand but not saturation. Use judgment, and record the advertiser count.
8. One sample ordered and received. Quality and delivery time recorded.
9. Terms checked: store policies (shipping, returns, refunds), business and sales-tax obligations understood for your location.

Niche order from the earlier scoring: pet comfort/enrichment, then WFH ergonomics, then coffee/tea accessories.

## 4. Break-even economics (fill in before spending)

```
price                      P  = $____   (example: $45)
landed cost (COGS+ship)    C  = $____   (example: $18)
payment fees               F  = 2.9% * P + $0.30
refund/chargeback reserve  R  = 5% * P
contribution margin        M  = P - C - F - R
break-even CPA             = M   (cost per purchase at which ad spend wipes out margin)
```

Example with the numbers above: F = $1.61, R = $2.25, M = **$23.14**.

What that requires from the ads: `CPC / conversion_rate <= M`.
At CPC $0.60 you need a click-to-purchase rate of at least 2.6%. At CPC $1.00 you need 4.3%. Typical cold-traffic store conversion is 1-3%, so the test can fail on arithmetic alone. If your numbers show a required rate above 4%, **reject the product before spending.**

## 5. Phase 1: creative test (days 6-12, $100 ad spend)

- One product, 3 creatives (short video, demo, problem/solution), one audience set, equal budget.
- Track per creative: spend, link CTR, add-to-cart, checkout starts, purchases.
- Per-creative kill: spend >= **2x M** with 0 purchases, or link CTR < 0.8% after 1,000 impressions. Pause it.
- Stage kill: all 3 creatives killed, or $100 spent with 0 purchases. Stop the product. Go to the product-switch rule in section 7.

## 6. Phase 2: confirmation (days 13-24, up to $150 ad spend)

Only surviving creatives run. Keep the budget flat, do not scale up on a lucky day.

- Continue while blended CPA over the stage is <= **1.5x M**.
- Pause and review at any time if refund or complaint rate exceeds 8% or any chargeback occurs.

## 7. Kill rules (any one stops the test)

1. Cash spent reaches $400.
2. $150 of ad spend with **0 purchases**.
3. After >= 10 purchases, blended CPA > **1.5x M**.
4. Refund plus chargeback rate > 10%, or a chargeback dispute, payment hold or account warning from the ad platform or payment processor.
5. Supplier stock-out or delivery times above 8 days with no fix.
6. Day 28 reached.

On a kill, stop all ads the same day. Do not "give it one more week."
Product-switch rule: if the first product dies in Phase 1 (rule 2 applied at $100 or all creatives killed), one replacement product may be tried, but total spend still stops at $400.

## 8. Decision on day 28

Compute from the log:

- Purchases n, blended CPA, contribution profit = n * M - ad spend, refund rate.

| Outcome | Condition | Action |
|---|---|---|
| **Pass** | n >= 15, CPA <= 0.7 * M, refund rate < 8%, contribution profit > 0 | Plan a second round at a pre-written higher cap. Do not scale automatically |
| **Inconclusive** | 8 <= n < 15 and CPA <= M | One more capped round of $150, same product, same rules |
| **Fail** | anything else | Stop. Write what you learned. Archive the store |

## 9. What AI automates and what stays human

| Task | AI | Human |
|---|---|---|
| Shortlist products, scrape trends and ad libraries | Yes | Reviews |
| Listings, store copy, ad scripts and variants | Drafts | Approves |
| Support replies | Drafts | Sends or approves |
| Daily report (spend, CPA, margin, refund rate) | Yes | Reads |
| Budget, ad spend, supplier orders, refunds, policy and legal decisions | No | Yes |

## 10. Log (fill daily)

```
date | spend | impressions | link CTR | add-to-cart | purchases | revenue | cost of goods | fees | refunds | CPA | notes
```

Any change to the plan or limits is written here **before** it is applied, with the reason.

## 11. Limits of this plan

- It cannot verify live product demand or supplier prices. Those come from Trends, the Ad Library and supplier quotes.
- Tax, licensing and consumer-protection duties depend on your location and are not covered here.
- Q4 timing is tight: if tested products cannot be delivered before the holidays, expect weaker conversion and more refunds.
