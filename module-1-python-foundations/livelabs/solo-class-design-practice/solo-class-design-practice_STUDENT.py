#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer: What the tool is. 
# How many are free to borrow right now.
# Whether it needs a safety check before it goes out again. Power tools need a quick inspection after every use. Most other tools do not.
#
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer: ID_number: to identify the tool in the library
# Name: to identify the tool in the library
# Quantity_available: to know how many are free to borrow right now
# Needs_safety_check: to know if the tool needs a safety check before it goes out again

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

import json

with open("tools_list.json", "r") as file:
    data = json.load(file)

class tool_tracker:

    def __init__(self, ID_number: int, name: str, quantity_available: int, needs_safety_check: bool):
        self.ID_number = ID_number
        self.name = name
        self.quantity_available = quantity_available
        self.needs_safety_check = needs_safety_check

    def needs_inspection(self):
        return self.needs_safety_check

tool_library = []

for item in data:
    tool_library.append(
        tool_tracker(
            item["ID_number"],
            item["name"],
            item["quantity_available"],
            item["needs_safety_check"]
        )
    )

# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

tool1 = tool_tracker(1, "Cordless Drill", 3, True)
tool2 = tool_tracker(2, "Step Ladder", 5, False)

print(tool1.needs_inspection())
print(tool2.needs_inspection())

tool1.quantity_available = 2

print(tool1.needs_inspection())
print(tool2.needs_inspection())


# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer: I chose these attributes because the operations manager needs to know each turbine's name, location, energy production, and operating status.
# I created needs_maintenance() to help identify turbines that may need attention if their energy output is too low or they are not operating.
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
