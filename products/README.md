# Products (PDF)

Five products on one cream design. Each printable also has a `_PRINT` version with a white background to save ink.

| Product | File | Pages | Price to test (hypothesis) |
|---|---|---|---|
| The Family Planner | `Family_Planner.pdf` (+ `_PRINT`) | 7 | $6-12 |
| The Readiness Bundle (10-question check, conversation guide, monthly check-in, slow-down signals) | `Readiness_Bundle.pdf` (+ `_PRINT`) | 8 | $6-12 |
| The Early College Questions Checklist | `Early_College_Checklist.pdf` (+ `_PRINT`) | 7 | $6-12 |
| The First-Year Starter Pack (short guide + planner pages + readiness check) | `First_Year_Starter_Pack.pdf` (+ `_PRINT`) | 13 | $12-19 |
| Early, Not Rushed: the Guide (11 chapters) | `Early_Not_Rushed_Guide.pdf` | 28 | $19-25 |

Prices are guesses to test, not market data.

## Before you sell
- Read every page. All personal facts come from the author's own account; confirm they are exactly right and you're comfortable publishing them.
- Rules and policies (placement tests, dual enrollment, records) change. The products say "check the official source"; keep that.
- AI disclosure: the guide's "About this guide" page says AI helped draft and format parts and the author reviewed it. Etsy and other marketplaces may require you to disclose AI assistance in the listing: check their current rules.
- Fonts (Lora, Nunito, Patrick Hand) are open licensed (SIL OFL). Illustrations are original.
- Selling licence: the pages say "Personal use only." Decide your licence and refund terms before listing.

## Rebuild
```
cd products
python3 build_planner.py; python3 build_readiness.py; python3 build_early_college.py; python3 build_starter.py; python3 build_guide.py
PW_PATH=$(npm root -g)/playwright node render.js $PWD/guide.html $PWD/Early_Not_Rushed_Guide.pdf   # repeat for each .html
```
Needs Python 3, Node with Playwright (Chromium). `check.js` flags pages whose content overflows; `shot.js` makes page previews.
