# What is automatic, what is not (honest version)

## One-time setup (you, about 1-2 hours)
1. Make the accounts: Kit, Cal.com, your social accounts, a free scheduler (Metricool, Buffer, or YouTube Studio for Shorts). Paste in the copy from `launch/`.
2. Pick a start date and run: `cd text_posts && python3 schedule_export.py YYYY-MM-DD`. This writes `schedule_singles.csv` (32 posts, Mon/Tue/Thu/Fri at 10:00) and `schedule_threads.csv` (thread parts).
3. Upload the singles CSV to your scheduler if it supports CSV import (check its exact format), or paste posts in by hand. Threads need manual posting in most tools.
4. For videos: run the doodle examples or `make_animated_video.py`, check them, and upload to the scheduler or the app.

## Weekly (you, 30-45 minutes)
- Read the week's posts and edit anything that doesn't sound like you.
- Approve the batch in the scheduler (it posts at the times set).
- Reply to comments and messages. Log questions in the Problems Log.
- Record or render the week's videos.

## What I will NOT do
- Hold your passwords or API keys, or post under your name without your review.
- Fully unattended posting. Platforms restrict automation and AI content, and one bad post can hurt trust in this niche.

## Why that's the right level of "automatic"
The scheduler does the posting. The pipeline does the drafting and exporting. You keep one decision per post: approve or edit.
