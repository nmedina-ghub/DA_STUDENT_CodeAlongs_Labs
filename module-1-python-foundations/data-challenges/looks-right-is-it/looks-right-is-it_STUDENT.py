#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause

def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Step 1, answer 1: The error happened because Python was trying to add an integer and a string.
#
# Step 1, answer 2: I used print(repr(hours)) and discovered it was reading 'Mon' instead of the number of hours.
#
# Step 1, answer 3: I changed parts[2] to parts[3] and used int() to convert the hours into a number.
#


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List

def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days

staff = []

for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)

print("employees in the file:", len(staff))

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1: E103 was the last employee printed before the error. E106 caused the error because it was not in the CSV.
#
# Step 2, answer 2: My staff list had E106 instead of E104. E104 was missing from the list.
#
# Step 2, answer 3: I created an empty staff list and looped through the CSV to add each employee ID only once.
#


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong

records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

for emp in employee_ids:
    total = 0
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Step 3, answer 1: Rosa has 40 hours and Mei has 32 hours.
#
# Step 3, answer 2: The total was outside the outer loop, so hours kept adding together across employees.
#
# Step 3, answer 3: I moved total = 0 inside the outer loop so each employee starts with a fresh total.
#


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week

def weekly_pay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        return regular_pay + overtime_pay
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1: Rosa earns $960.00, Darnell earns $1,543.50, and Mei earns $896.00.
#
# Step 4, answer 2: I changed weekly_pay so the first 40 hours receive regular pay and only extra hours receive time-and-a-half.
#
# Step 4, answer 3: I changed >= 40 to > 40 because overtime only applies to hours over 40.
#
