import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
def pages():
    P = []
    P.append(cover("The Family Planner", "a planner that bends to your child",
        "Six printable pages to plan the year, the week, and the month, and to adjust when something isn't working.",
        art_compass(170), pill="PRINTABLE PDF · 7 PAGES",
        extra='<div class="fine" style="max-width:5in;margin:.25in auto 0">How to use: fill in Year at a Glance together, copy the Weekly Planner each week, do the Monthly Check-In on the same day each month, and use the Reset Plan when things feel stuck.</div>'))
    P.append(page(head("start here", "Year at a Glance", "Where you are, where you might go, and the one thing you'll try.") +
        field("Learner (nickname is fine, no personal details needed)", 1) +
        table(["", "Where we are now", "What's working", "What isn't", "One thing we'll try"],
              [[x, "", "", "", ""] for x in ["Learning style<br><span class='fine'>(live instructor, online instructor, reading, hands-on)</span>", "Pace", "Daily structure", "Social life", "Goals<br><span class='fine'>(not just graduation)</span>"]], "tall") +
        field("The route we're considering", 2) + field("What would tell us it's time to slow down?", 2) +
        box("story", "From my experience", "<p>I wasn't a passenger in my own education. Telling my parents what worked and what didn't, and watching them change things, mattered more than any curriculum.</p>"), "Year at a Glance", art=art_sprout(100)))
    P.append(page(head("each week", "Weekly Planner", "Week of ____________ &nbsp; Energy this week (1-5): ____") +
        table(["Day", "Learning block 1", "Learning block 2", "Break / movement", "Friends or activity"], [[d, "", "", "", ""] for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Weekend"]], "tall") +
        field("The protected fun slot", 1) +
        '<div class="two"><div class="fld"><b>Friday review: what worked</b>' + lines(2) + '</div><div class="fld"><b>What to change</b>' + lines(2) + '</div></div>' +
        box("worked", "What worked for me", "<p>My day ran from about 9 to 2, and the rest was free for other activities and things I was curious about. The free time only felt like a gift once I started planning it.</p>"), "Weekly Planner", art=art_book(120, 88)))
    P.append(page(head("each month", "Monthly Check-In", "Sit down together, relaxed. Month of ____________") +
        '<div class="two"><div class="box plain"><p class="t" style="color:var(--navy)">The learner fills in</p>' + field("Something I enjoyed", 2) + field("Something that was hard", 2) + field("Something I want to change", 2) +
        '<p><b>Energy (1-5):</b> 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5</p><p><b>I want to go:</b> faster / slower / the same</p></div>' +
        '<div class="box plain"><p class="t" style="color:var(--navy)">The parent fills in</p>' + field("I noticed they seemed", 2) + field("Something I\'m worried about", 2) + field("Something I\'ll change on my side", 2) + '</div></div>' +
        field("Decision for next month, together", 3) +
        box("try", "A note", "<p>Honest, not for judging. If you see ongoing dread, loss of interest, or changes in sleep or mood, slow down, and talk to a qualified professional if you're worried.</p>"), "Monthly Check-In", art=art_bubbles(170, 80)))
    P.append(page(head("keep it safe", "Records Tracker", "Update this every term. Future you will be grateful.") +
        table(["Item", "Where it's stored", "Last updated", "Needed for"], [[x, "", "", ""] for x in ["Course list", "Official transcripts", "Diploma / graduation records", "Activity log (clubs, groups, volunteering)", "Work samples", "Test results", "Enrollment emails"]], "tall") +
        field("State or district rules to check", 3), "Records Tracker"))
    P.append(page(head("thinking about college early", "College Questions Checklist", "Ask before you commit. Write the answer, the date, and who answered.") +
        table(["Question", "Answer", "Date / who"], [[q, "", ""] for q in ["Age and grade requirements? Any exceptions?", "Which tests, transcripts or interviews are needed?", "What does it cost? Any programs that help?", "Which credits transfer, and where? (Get it in writing.)", "In person, online, or hybrid?", "Who is our contact? Is there an advisor?", "What role do parents have for a minor?", "Effect on financial aid and later admissions?", "Withdrawal policy if it isn't working?"]], "tall"), "College Questions", art=art_stairs(190, 112)))
    P.append(page(head("when things feel stuck", "Reset Plan", "A rough stretch is a signal to adjust, not a failure.") +
        '<div class="two"><div>' + field("What's been hardest", 2) + field("What we're pausing", 2) + field("What we're keeping", 2) + '</div><div>' + field("The one thing we'll change", 2) + field("Who we'll talk to", 2) + field("Review date", 1) + '</div></div>' +
        box("plain", "The steps", "<ol><li>Stop adding new commitments for two weeks.</li><li>Have one honest conversation.</li><li>Protect sleep, play and friends.</li><li>Pick one thing to change.</li><li>Recheck in two weeks.</li><li>Decide together: continue, adjust or pause.</li></ol>") +
        box("didnt", "What didn't work for me", "<p>My first year of online school was hard: no classroom structure, lots of free time I wasn't used to, and missing friends. It got better, but only after we changed things on purpose.</p>") +
        f'<p class="fine">{DISCLAIMER}</p>', "Reset Plan", art=art_compass(90)))
    return P
if __name__ == "__main__":
    for mode in (False, True):
        open(os.path.join(HERE, f"planner{'_print' if mode else ''}.html"), "w").write(build_html(pages(), mode, "The Family Planner"))
