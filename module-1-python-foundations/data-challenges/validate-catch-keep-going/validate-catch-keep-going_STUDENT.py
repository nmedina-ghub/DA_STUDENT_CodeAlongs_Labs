#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    fields = row.split(",")

    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))

    request_id, request_type, borough, number, status = fields

    if borough == "":
        return False, "borough is empty"

    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status

    return True, "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1: True, "ok"
#
# Step 1, answer 2: False, "borough is empty"
#


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection

valid = 0

for row in rows:
    ok, reason = validate_request(row)

    if ok:
        valid += 1
    else:
        print(row.split(",")[0], "REJECTED -", reason)


print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1: The number of rows that passed Day 1 validation is 12.
#
# Step 2, answer 2: The number of rows that failed Day 1 validation is 3.
#


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash

total_days = 0
counted = 0

# for row in rows:
#    ok, reason = validate_request(row)
#
#    if not ok:
#        continue
#
#    days_open = int(row.split(",")[3])
#
#    total_days += days_open
#    counted += 1
#
#    print(row.split(",")[0], "days open:", days_open)

#print("average days open:", total_days / counted)

#print("average days open:", total_days / counted)

# Step 3, answer 1: 3 days
#
# Step 3, answer 2: Value error
#
# Step 3, answer 3: Invalid literal for int() with base 10: '3 days'
#


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        return False, "days_open is not a number: " + value

    if days < 0:
        return False, "days_open is negative: " + value

    return True, "ok"

total_days = 0
counted = 0
skipped = 0

for row in rows:
    ok, reason = validate_request(row)

    if ok:
        ok, reason = check_days_open(row.split(",")[3])

    if ok:
        days = int(row.split(",")[3])
        total_days += days
        counted += 1
    else:
        skipped += 1
        print(row.split(",")[0], "SKIPPED -", reason)
  





print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1: 10
#
# Step 4, answer 2: 5
#
# Step 4, answer 3: 8.2
#
