# Kit copy (paste-ready)

I have not seen Kit's current screens, so field names may differ slightly. Match each block to the closest setting. Free plan; check its current limits and whether forms, landing pages and file delivery are included.

## Account
**Sender name:** [NAME]
**Reply-to email:** [your business email]
**Physical/mailing address in footer:** email laws may require one (check requirements where you live; use a P.O. box if you prefer not to use your home address).

## Form
**Form name:** Readiness Check signup
**Headline:** Is this the right fit? The free 10-Question Readiness Check
**Subhead:** Two pages and a short conversation guide for you and your learner.
**Field:** Email only (first name optional)
**Button text:** Send me the checklist
**Consent line under the button:** By signing up you agree to get emails from [NAME]. Unsubscribe any time.
**Success message:** Thanks! Check your inbox for the checklist (look in spam or promotions if you don't see it).

## Automation
**Trigger:** subscribes to the Readiness Check form
**Step 1:** send Email 1 immediately
**Step 2:** wait 3 days, send Email 2
**Step 3:** wait 4 days, send Email 3 (day 7)
**Stop** if they book a chat or reply (do this manually if the free plan can't).

## Email 1: send immediately
**Subject:** Your Readiness Check (and a quick hello)
**Preview text:** Plus one thing to try this week.
**Body:**
Hi {{ subscriber.first_name | default: "there" }},

Thanks for grabbing the Readiness Check: [CHECKLIST LINK]

A quick hello: I'm [NAME]. I left in-person school in 3rd grade because it wasn't working for me, and homeschooling let me work at my own pace. I finished high school at 13 through FLVS Flex, earned my associate degree at 15 and my bachelor's at 17, and I'm now working on a master's.

I'll share what worked, what was hard, and what I'd do differently.

Try this first: sit down with your learner and talk through questions 2 and 3 on the checklist. What's one thing that works for them? What's one thing that doesn't?

Reply and tell me what stood out. I read every message.

[NAME]

P.S. This is my experience, not professional advice.

## Email 2: day 3
**Subject:** Homeschool shouldn't feel like school at home
**Preview text:** One question that changed my education.
**Body:**
Hi {{ subscriber.first_name | default: "there" }},

One of the biggest things I noticed: some families run homeschool exactly like in-person school, with the same linear, one-sided lessons, just at the kitchen table. It's understandable. It's what we know.

What helped me: my parents asked for feedback. What worked? What didn't? And we changed things. Face to face with an instructor, online with one, or no lectures at all. There's no single right style, only what fits the learner.

Try this week: ask your child to name one thing to keep and one thing to change.

[NAME]

## Email 3: day 7
**Subject:** The socialization question
**Preview text:** My honest answer.
**Body:**
Hi {{ subscriber.first_name | default: "there" }},

If you're worried about socialization, you're not alone. I hear it a lot.

I'll be honest: at first I thought homeschool social life didn't exist. I was pulled out mid-year and didn't get to say goodbye to most of my friends, and my parents didn't yet know what they could sign me up for. It took about a year to find the activities and groups that filled the gap. After that, I was part of local high school clubs and organizations and church groups, and I had as much of a social life as anyone, maybe more. It didn't happen by accident. We made room for it.

If you'd like to talk through your family's situation, I offer a free 30-minute chat: [BOOKING LINK]. No pitch, no pressure.

[NAME]

## Footer (all emails)
[NAME] · [mailing address] · Unsubscribe link (automatic) · Privacy: [PRIVACY LINK]
General information from personal experience. Not educational, psychological, medical or legal advice.

## Checks before going live
- [ ] Sign up with a second email and confirm all three emails arrive and links work.
- [ ] Confirm the checklist file or link opens.
- [ ] Fill in [NAME], links, and the mailing address.
- [ ] Check Kit's free plan limits and whether {{ subscriber.first_name }} personalization works on your plan.
