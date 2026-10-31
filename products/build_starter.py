import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import build_planner
def pages():
    pl = build_planner.pages(); P = []
    P.append(cover("The First-Year Starter Pack", "your first year, a little easier", "A short guide, a planner, and the check-ins I wish my family had in our first year of online school and homeschooling.", art_sprout(170), pill="PRINTABLE PDF · 13 PAGES"))
    P.append(page(head("welcome", "Hi, I'm Fabian", "And this is the pack I wish we'd had.") +
        "<p>When I was pulled out of in-person school in the middle of third grade, nobody handed my family a map. My first year of online school was rough. This pack is a shortcut through the parts we learned the hard way.</p>" +
        f"<div style='text-align:center'>{art_stairs(360, 208)}</div>" +
        "<p>I finished high school at 13 through FLVS Flex, earned my associate degree at 15 and my bachelor's at 17. But this pack isn't about speed. It's about <span class='hl'>fit</span>: building the first year around the child.</p>" +
        box("plain", "What's inside", "<ol><li>My first year, honestly</li><li>What worked and what didn't</li><li>Plan your days</li><li>Find community on purpose</li><li>The feedback talk</li><li>Five first-year principles</li><li>The planner pages (year, week, month, reset)</li><li>A quick readiness check</li></ol>") +
        f'<p class="fine">{DISCLAIMER}</p>', "Welcome"))
    P.append(page(head("part 1", "My first year, honestly", "What it was really like, in my own words.") +
        "<p>I was pulled out in the middle of the school year, which meant I didn't get to say goodbye to most of my friends. At school, the classroom told me where to be and what to do all day. Online, I had lecture times and assignments, and once they were done I was free for the rest of the day. I wasn't used to that freedom.</p>"
        "<p>I also missed the social side so much that, for a while, I honestly thought homeschool social life didn't exist. It did. My parents just didn't know yet what they could sign me up for. It took about a year of settling in before they found the activities and local groups that filled the gap.</p>" +
        '<div class="quote">I told my parents that I missed being in school and felt like I was missing a piece of my childhood. They didn\'t get defensive.</div>'
        "<p>They understood it was a process they were still learning about too. I'm one of three brothers, and my other two later followed the same path, so in a way I was going in blindly with my parents and paving the way.</p>" +
        box("story", "If your family is in year one", "<p>The hard first stretch is normal. It's not a sign you chose wrong. It's a sign you're adjusting, and adjusting is something you can plan for.</p>"), "My First Year", art=art_compass(90)))
    P.append(page(head("part 2", "What worked, and what didn't") +
        '<div class="two">' + box("worked", "What worked", "<ul><li><b>My own pace,</b> with an online instructor I could turn to</li><li><b>Telling my parents</b> what was and wasn't working, and them listening</li><li><b>Finding community on purpose</b>, even though it took a year</li><li><b>Time for ideas I was curious about</b></li><li><b>Getting used to the freedom</b>, and learning to plan it</li></ul>") +
        box("didnt", "What didn't", "<ul><li><b>Expecting it to feel like school</b> at home</li><li><b>Missing friends</b> and not knowing what to sign up for</li><li><b>Too much open time</b> with no plan for it</li><li><b>Waiting for the hard feelings to pass</b> without saying anything</li></ul>") + '</div>' +
        box("try", "What I wish my parents (and I) had known", "<ol><li>The first year will be the hardest. Plan for it.</li><li>Say how you feel early, even when it's awkward.</li><li>Look for activities before you feel lonely, not after.</li><li>Free time isn't a gap. It's a gift if you plan it.</li></ol>") +
        field("What's working for us so far", 2) + field("What isn't", 2), "What Worked / What Didn't", art=art_bubbles(170, 80)))
    P.append(page(head("part 3", "Plan your days", "A simple shape for a day that leaves room to breathe.") +
        '<div class="two"><div>'
        "<p>My day started at 9 and finished around 2. That left the rest of the afternoon for other school activities and things I was interested in, like a trip to the park.</p>"
        "<p>The schedule itself worked. What I'd change is my <b>outlook</b>: I wasn't used to that much free time, and it took a while to treat it as something to plan around instead of a gap to fill.</p></div>"
        f"<div style='flex:0 0 2.5in'>{art_wheel(250)}</div></div>" +
        box("plain", "My daily shape (yours can look different)", table(["", "What I did", "Your version"], [["9 to ~2", "Lectures, assignments, review", ""], ["After 2", "Free time: activities, interests, friends", ""], ["Evening", "Rest", ""]])) +
        box("try", "Plan the free time", checks(["Pick three things your learner would love to do each week", "Put one on the calendar before the week starts", "Leave one slot completely open", "Ask them: what do you want to do with this time?"])), "Plan Your Days"))
    P.append(page(head("part 4", "Find community on purpose", "It didn't happen automatically for me, and it may not for you.") +
        '<div class="two"><div><h3>Places to look</h3><ul><li>Local clubs and organizations (check each group\'s rules)</li><li>Faith and community groups</li><li>Classes and co-ops</li><li>Volunteering</li><li>Sports and arts</li><li>Friends of different ages</li></ul></div><div><h3>Questions to ask</h3><ul><li>How many regular activities does the week have?</li><li>Does my child have at least one friend to talk to freely?</li><li>Do they invite others and get invited?</li></ul></div></div>' +
        table(["Activity or group", "Contact", "Day / time", "Tried it?", "Notes"], [[""] * 5 for _ in range(4)], "tall") +
        box("story", "From my experience", "<p>Once my parents found local activities, I joined local high school clubs and organizations and church groups, and later college clubs. I had as much social life as anyone, maybe more. But it started with a year of looking.</p>"), "Community", art=art_sprout(100)))
    P.append(page(head("part 5", "The feedback talk", "The habit that changed the most for me.") + f"<div style='text-align:center'>{art_bubbles(280, 130)}</div>" +
        '<div class="two">' + box("try", "For parents, try", "<ul><li>\"What's one thing that's working for you?\"</li><li>\"What's one thing that isn't?\"</li><li>\"If you could change one thing, what would it be?\"</li><li>\"What would make this week better?\"</li></ul><p class='fine'>Listen first. Write it down. Don't defend.</p>") +
        box("story", "For students, try", "<ul><li>\"What works for me is ____.\"</li><li>\"What doesn't is ____.\"</li><li>\"Can we try changing one thing?\"</li><li>\"I miss ____, and I'd like help finding it.\"</li></ul><p class='fine'>It's information, not complaining.</p>") + '</div>' +
        field("This week we agreed to change", 2) + field("We'll check in again on", 1), "The Feedback Talk"))
    P.append(page(head("part 6", "Five first-year principles") +
        "<ol><li><h3 style='margin:0'>Build around the child.</h3><p>Face to face, online with an instructor, or no lectures at all. There's no single right style, only what fits.</p></li>"
        "<li><h3 style='margin:0'>Don't recreate school at home.</h3><p>The same linear, one-sided lessons at the kitchen table aren't the goal. Adapt the experience.</p></li>"
        "<li><h3 style='margin:0'>Ask, listen, change one thing.</h3><p>Check in monthly. Change one thing at a time.</p></li>"
        "<li><h3 style='margin:0'>Plan the social side and the free time.</h3><p>Both took me a year to figure out. You can start sooner.</p></li>"
        "<li><h3 style='margin:0'>Fit before speed.</h3><p>Finishing early was one outcome for me, and not the only good one. Go as fast as fits, and no faster.</p></li></ol>" +
        box("worked", "A reminder", "<p>Every child is different. This is one person's experience, and your family will find its own way.</p>"), "Five Principles", art=art_compass(90)))
    P.extend([pl[1], pl[2], pl[3], pl[6]])
    P.append(page(head("quick check", "A fast readiness check", "Five questions. Circle one answer each.") +
        questions(["Does the learner say what works and what doesn't about how they learn?", "Is at least one adult checking in regularly?", "Are you open to changing the plan when something isn't working?", "Is there a plan for friends and activities?", "Are you clear that finishing early is one outcome, not the goal?"]) +
        box("try", "What's next", "<p>Pick one thing from this pack to try this week. Do the monthly check-in on the same day each month. If the first year feels hard, you're not behind. You're adjusting.</p>") + about_author() + f'<p class="fine">{DISCLAIMER}</p>', "Quick Check", art=art_sprout(100)))
    return P
if __name__ == "__main__":
    for mode in (False, True): open(os.path.join(HERE, f"starter{'_print' if mode else ''}.html"), "w").write(build_html(pages(), mode, "The First-Year Starter Pack"))
