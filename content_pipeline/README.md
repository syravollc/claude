# Content pipeline (draft -> review -> approve -> schedule)

AI drafts. A human approves. A scheduling tool publishes. Nothing in this folder posts anywhere or touches your accounts.

## Weekly routine (about 30-45 minutes)
1. `python3 pipeline.py generate --week N` (4 drafts: 3 short-video scripts, 1 post/carousel; plus write the weekly email yourself or from a draft)
2. `python3 pipeline.py review`, then read and edit each file in `queue/`.
3. `python3 pipeline.py approve ID ...` for the ones you are happy to put your name on.
4. `python3 pipeline.py export --start YYYY-MM-DD` creates `export/schedule.csv`.
5. Upload to your scheduling tool, record or design the video, post.

## Faceless animated format
- Each video draft is a storyboard: scenes with narration, a simple animated visual, and on-screen text.
- No real people or faces appear. Visuals are illustrated characters, motion graphics, timelines and text cards.
- Trust without a face: use your own recorded voiceover (no camera), show real documents with personal details blurred, and be specific about your story. A synthetic voice works but weakens the personal feel.
- Disclose AI use where platforms require it (rules for AI-generated or synthetic media on YouTube, TikTok and Meta change; check each). Never present an animated character as a real family or invent testimonials.
- Animation tools to compare (unverified; check price, licensing and export limits): Canva animations, CapCut, or an AI video generator. A Canva connector may be available in this workspace, to be confirmed before use.

## Setup
1. Fill `story_facts.md` with true facts (the generator refuses to run until you do). This is the only place personal details come from.
2. Set `ANTHROPIC_API_KEY` and `CONTENT_MODEL` in your own shell. Do not commit keys. `--dry-run` works without them.
3. Test with `python3 pipeline.py generate --week 1 --dry-run` first.

## Safeguards built in
- Drafts that contain guarantees, medical or mental-health words, "proven", or income-hype phrases are flagged and cannot be approved until you edit them and clear the flag yourself.
- The model is told to write `[NEEDS FACT: ...]` instead of inventing details; those drafts are flagged too.
- Each draft ends with an AI-assistance note. Check each platform's current AI-content labelling rules before posting; they change.
- Status is always `draft` until a person approves.

## Where it gets published (unverified, check each before relying on it)
| Channel | Use | Notes |
|---|---|---|
| YouTube Shorts, Instagram Reels, TikTok | Short-video scripts | You record or use a video tool; schedule natively or via a scheduler. Check each platform's AI-disclosure and automation policies |
| Pinterest | Printables and planner previews | Strong for printables; link to the landing page |
| Email (MailerLite, Beehiiv, Kit or similar) | Weekly email, lead magnet delivery | Free tiers exist; verify current limits |
| Homeschool communities (forums, groups) | Answer questions, no link-dropping | Follow each group's rules; helpful answers first, links rarely |
| Store/landing page | Guide and planner | Pick one platform; fees assumed in the workbook |

Scheduler options to check: Buffer, Metricool, Later, or each platform's own scheduler. I have not verified current prices or whether each accepts CSV bulk upload.

## Not automated on purpose
- Recording your voiceover (recommended) and final video assembly/export.
- Replying to comments and DMs.
- Anything about money: ads, refunds, pricing.
