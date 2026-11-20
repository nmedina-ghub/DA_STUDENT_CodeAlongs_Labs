#!/usr/bin/env python3
"""Lab: Stress-Test Your Code: Timing & Efficiency
GitBook Quest 1.9: Lookups Matter

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 stress-test-timing-practice_STUDENT.py
    Or make it executable once:
        chmod +x stress-test-timing-practice_STUDENT.py
    and from then on run it directly:
        ./stress-test-timing-practice_STUDENT.py
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
    Commit this file (you may rename it stress-test-timing-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Generate Batches of Your Class at Three Sizes (10, 1,000, and 100,000) =====
# Any class works: your own from Day 15's lab, a new one, or the sample
# LibraryTool on today's slides.

import random  # Python's built-in module for random values

class LibraryTool:
    def __init__(self, tool_name, quantity_available, requires_inspection):
        self.tool_name = tool_name
        self.quantity_available = quantity_available
        self.requires_inspection = requires_inspection

    def is_available(self):
        return self.quantity_available > 0

def make_batch(size):
    tools = []
    for i in range(size):
        tools.append(LibraryTool(f"Tool{i}", random.randint(0, 5), random.choice([True, False])))
    return tools

small_batch = make_batch(10)
medium_batch = make_batch(1000)
large_batch = make_batch(100000)
print(len(small_batch), len(medium_batch), len(large_batch))


# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

def find_by_name_linear(batch, name):

    for obj in batch:
        if obj.tool_name == name:
            return obj
    return None


def build_lookup(batch):
    return {obj.tool_name: obj for obj in batch}


lookup = build_lookup(large_batch)

name = "Tool99999"

print(find_by_name_linear(large_batch, name))

print(lookup.get(name))


# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

import time  # Python's built-in module; time.perf_counter() is new

# Prediction: linear_time

size_batch_pairs = [(10, small_batch), (1000, medium_batch), (100000, large_batch)]

print("Size\tLinear Time\tDict Time")

for size, batch in size_batch_pairs:
    lookup = build_lookup(batch)

    start = time.perf_counter()
    find_by_name_linear(batch, "NotThere")
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    lookup.get("NotThere")
    dict_time = time.perf_counter() - start

    print(size, linear_time, dict_time)

# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer: Linear search is O(n) because it takes longer as the number of tools increases, while dictionary lookup is O(1) because its search time stays roughly constant.
#
#

# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Bring your numbers, not a summary of them. Specifically:
# - Your timings at each batch size, for both searches. Everyone tested a
#   different class on a different laptop, so the raw numbers won't match -
#   put yours up anyway.
# - Which column changed as the batch grew, and which one didn't. - The
#   batch size where the difference stopped being something you had to
#   squint at.
# - Whether anything surprised you. A linear scan that looked suspiciously
#   flat is worth raising - say what you found out was going on.
# - If you tried the AI stretch: what it claimed, and whether your own
#   timings actually backed it up. "It was wrong" is a good answer if you
#   can show the number that proves it.
#
# Be ready for "why does that happen?" - the timings are evidence, and the
# explanation is what's being assessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out: I created three different batch sizes to test how search performance changes as the amount of data increases. Linear search gets slower because it checks items one at a time, while dictionary lookup uses a key to find an item much faster.
#
#
