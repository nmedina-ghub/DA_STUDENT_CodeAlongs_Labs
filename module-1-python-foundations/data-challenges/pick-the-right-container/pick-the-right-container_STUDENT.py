#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs

def scan_for(tap_id, records):
    comparisons = 0

    for row in records:
        comparisons += 1

        if row[0] == tap_id:
            return comparisons

    return comparisons


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1: A linear search checks each record one at a time until it finds the matching tap ID.
#
# Step 1, answer 2: If the ID is not found, Python checks every row in the dataset.
#\

# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size, "| worst-case comparisons:", worst)
    
pairs = 0

for row in taps:
    for other_row in taps:
        pairs += 1

print("rows:", len(taps), "| pair comparisons:", pairs)

big = len(taps) * 10

print("scan comparisons on", big, "rows:", big)
print("pair comparisons on", big, "rows:", big * big)

# Step 2, answer 1: A linear search has O(n) time complexity because the number of
# comparisons increases in proportion to the number of rows.
#
# Step 2, answer 2:  A nested loop has O(n²) time complexity because each row is
# compared against every other row. The number of comparisons
# increases much faster as the dataset grows.

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons

card_ids = []
tap_counts = []
comparisons = 0

for row in taps:
    card = row[1]
    found = False

    for i in range(len(card_ids)):
        comparisons += 1

        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break

    if not found:
        card_ids.append(card)
        tap_counts.append(1)

busiest = tap_counts.index(max(tap_counts))

print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")


# Step 3, answer 1:
# Parallel lists store card IDs and their tap counts in matching positions.
# Each card ID has a corresponding count in the tap_counts list.


# Step 3, answer 2:
# Parallel lists require searching through the existing card IDs
# to find a matching card. This increases the number of comparisons
# as the number of distinct cards grows.

# ===== Day 2 =====

# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set

taps_by_card = {}
lookups = 0

for row in taps:
    lookups += 1
    card = row[1]

    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1

stations = set()

for row in taps:
    stations.add(row[2])

repeat_riders = 0

for card in taps_by_card:
    if taps_by_card[card] > 1:
        repeat_riders += 1


print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])


# Step 4, answer 1:
# A dictionary stores card IDs as keys and tap counts as values.


# Step 4, answer 2:
# A dictionary generally provides faster lookups than searching
# through parallel lists because it uses keys to access values.


# Step 4, answer 3:
# A set stores unique station names and automatically removes duplicates.


# Step 4, answer 4:
# Repeat riders are cards that have tapped more than once.



# ===== Day 3 =====


# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes

summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")

# Run these two lines first to observe the TypeError:
# text = json.dumps(summary, indent=2)
# print(text)


# Step 5, answer 1:
# The error occurred because Python sets are not supported by JSON serialization.
# JSON supports lists and dictionaries, but not sets.

# Step 5, answer 2:
# Convert the set into a list using sorted(stations) before saving it as JSON.

# Step 5, answer 3:
# The TypeError occurred because the stations variable is a set.
# Python requires the set to be converted into a JSON-supported data type.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived

summary["stations"] = sorted(stations)

with open("tap_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

with open("tap_summary.json", "r") as f:
    reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)


# Step 6, answer 1:
# The JSON file saves the summary data using json.dump()
# and loads it back into Python using json.load().


# Step 6, answer 2:
# The dictionary comes back as a dictionary, but the stations
# set comes back as a list because we converted it before saving.
# The tap counts remain identical after reloading.

