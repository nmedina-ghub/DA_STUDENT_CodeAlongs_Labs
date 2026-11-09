#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

from importlib.resources import path
import json

DATA_FILE = "pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """Validates a donation record for correct format and data."""
    parts = record.split(",")
    if len(parts) != 5:
        return False, "wrong field count"
    if parts[2].strip() == "":
        return False, "missing category"
    try:
        float(parts[3])
    except ValueError:
        return False, "pounds is not a number"
    return True, ""

records = read_donations(DATA_FILE)
valid = []
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("rejected", record.split(",")[0] + ":", reason)
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1: 17
#
# Step 1, answer 2: 20
#


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """Summarizes donation records by category."""
    by_category = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        category = parts[2]
        pounds = float(parts[3])
        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds
    return {"records": len(valid_records), "total_pounds": total_pounds,
            "by_category": by_category}


summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1: This function goes through the valid donations and groups them by category.
# It counts how many donations are in each category and adds up the pounds donated for each one.


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):

    """Exports the donation summary to a JSON file."""

    with open(path, "w") as file:
        json.dump(summary, file, indent=2)

    return path

def run_pipeline(in_path, out_path, summarize):
    
    """Runs the donation processing pipeline."""

    kept = []
    for record in read_donations(in_path):
       
        if validate_donation(record)[0]:
            kept.append(record)
    
    return export_summary(summarize(kept), out_path)


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1: This function saves the donation summary into a JSON file so the information can be stored and viewed later.
#
# Step 3, answer 2: This function puts everything together by reading the donations, checking which ones are valid, summarizing them, and saving the results.
#


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Summarizes donations by day."""
    by_day = {}
    total_pounds = 0.0

    for record in valid_records:
        parts = record.split(",")
        day = parts[4]
        pounds = float(parts[3])

        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}

        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds

    return {
        "records": len(valid_records),
        "total_pounds": total_pounds,
        "by_day": by_day
    }

run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)

reloaded = json.load(open("donation_summary.json"))

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1: I changed the summary function to group donations by date instead of grouping them by category.

#
# Step 4, answer 2: I reused the pipeline to save the daily summary as a JSON file and then loaded the file back to display the results.
#
