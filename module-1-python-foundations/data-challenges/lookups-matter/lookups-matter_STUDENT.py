#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0

    for row in members:
        comparisons += 1

        if row["member_id"] == member_id:
            return row, comparisons

    return None, comparisons


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1: The linear search checked 150 members before finding Tomas Park. This shows that linear search checks records one at a time until it finds a match.
#


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
with open(CHECKINS_FILE, "r") as f:
    swipes = f.read().splitlines()

linear_total = 0
not_members = 0

for member_id in swipes:
    row, comparisons = find_linear(members, member_id)

    if row:
        print(member_id, "|", row["name"], "| comparisons:", comparisons)
    else:
        print(member_id, "| NOT A MEMBER", "| comparisons:", comparisons)
        not_members += 1

    linear_total += comparisons

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1: The program checked 20 swipes and found 2 IDs that were not members.
#
# Step 2, answer 2: Linear search performed 2,924 total comparisons. It takes more comparisons when a member is near the end of the list or when an ID is not found.
#


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
members_by_id = {}
build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1
for member_id in swipes:
   linear_running = 0
dict_running = build_steps

pays_off_at = None
swipe_number = 0

for member_id in swipes:
    swipe_number += 1

    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)

    linear_running += linear_count
    dict_running += dict_count

    print(swipe_number, member_id, 
          "| linear:", linear_running, 
          "| dict:", dict_running)

    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1: A dictionary stores member information using member IDs as keys, making it faster to find a member.
#
# Step 3, answer 2: The dictionary pays off at swipe 6 because the total cost becomes lower than linear search.
#
# Step 3, answer 3: The dictionary is more efficient because it only takes one lookup per swipe instead of checking members one at a time.
#


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict

ai_claim = "The dictionary search was more efficient than linear search. Although building the dictionary required 312 steps, it paid off at swipe 6. The dictionary required only 332 total steps compared to 2,924 comparisons for linear search."
print("AI CLAIM:", ai_claim)

_, front_count = find_linear(members, swipes[0])

_, absent_count = find_linear(members, "M1313")

ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

verdict = "The AI claim was correct. Dictionary search was faster overall, but it required an initial cost to build the dictionary."
print("VERDICT:", verdict)

# Step 4, answer 1: The AI claim was supported by the results. The dictionary took 332 total steps compared to 2,924 for linear search.
#
# Step 4, answer 2: Linear search can be fast when a member is near the beginning, but it takes longer when a member is near the end or is not found. Dictionary search takes one lookup per ID after the dictionary is built.
#
