# Free-only mode ($0 spend)

Rule: nothing in this mode costs money. Anything that would is marked and skipped.

| Need | Free option | Skip / watch for |
|---|---|---|
| Email list + welcome emails | Kit free plan | Don't upgrade; check the free subscriber limit |
| Booking for free chats | Cal.com free plan, **no payment step** | Don't connect Stripe until you charge |
| Taking payment later | Stripe has no monthly fee, only a per-sale fee (verify) | Add only when you start charging |
| Selling the guide | Payhip free plan (fee only per sale, reported 5%) | Wait until the guide is final |
| Landing page | Payhip/Kit page, or the HTML preview hosted free (verify a free host) | No paid domain |
| Scheduling posts | YouTube Studio (free) + Metricool free | Don't upgrade |
| Animated videos | `make_animated_video.py` (free: ffmpeg, Pillow, edge-tts) | Voice service must be reachable on your computer |
| Editing face videos | `edit_video.py` (free: ffmpeg, optional faster-whisper) | Phone camera, no extra gear |
| Writing scripts | Written by hand/with this chat. The `pipeline.py generate` command **uses a paid API key, so skip it** | |

## How the plan changes
- **Sessions become free conversations first** (15-30 min), no payment. Use them to learn and to earn permission-based testimonials. Charge later once people ask for more.
- **Guide:** finish it first, then decide whether to sell or give it away as the email signup bonus.
- **Domain:** none. Use the free store/landing page URLs.
- **Time is the real cost:** about 5-8 hours a week.

## Honest trade-offs
- Free plans have limits and branding. Check them at signup.
- Free conversations bring feedback, not income. Day-60/90 income gates in `COACHING_BUSINESS_PLAN.md` will be missed until you charge. Decide a date to start charging (suggestion: after 5 free conversations).
