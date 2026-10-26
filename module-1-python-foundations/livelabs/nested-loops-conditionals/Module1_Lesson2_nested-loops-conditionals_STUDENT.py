#!/usr/bin/env python3
"""Day 2 code-along: Nested Loops & Conditionals. Run: python3 <file>"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
# DISCUSS: If both loops used range(2), order: A: 1 0. B: 0 0. C: 1 1. D: 0 1.
# Your answer:
#
print('----- 1. Nested Loop, Live -----')
<<<<<<< HEAD
# TODO: write a nested loop that prints every (row, col)
# pair for row in range(2) and col in range(3)
for row in range(2):
    for col in range(3):
        print(row,col)
=======
# TODO: write a nested loop that prints every (row, col) pair
# TODO: row goes through range(2), col through range(3)
>>>>>>> upstream/main

# PREDICT before you run: Outer range(3), inner range(2): how many lines print?
# Your answer:
<<<<<<< HEAD
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1
# Prediction:
# 0 1
# 1 2
# 2 0
# 3 0
# 0 0
# 0 0
#
# DISCUSS: With range(3) outside and range(2) inside, a classmate's version
#          prints only 3 lines instead of 6. What's the most likely cause?
=======
#
# DISCUSS: A classmate gets 3 lines instead of 6. What's the likely cause?
>>>>>>> upstream/main
# Your answer:
#


# ===== 2. Nested Conditional, Live =====
# Check the operation type first, then if the quantity is positive.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first
# TODO: if it's "ADD", nest a second check that quantity is above 0
operation = "ADD"
quantity = 5

#If the operation == "ADD" and if the quantity > 0 = valid add, invalid quantity
if operation == "ADD":
        if quantity > 0:
                print("valid add")
        else: 
                print("invalid quantity")

# DISCUSS: If the inner quantity check never runs, what do you trace first?
# Your answer:
#


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# Check each line: print whether it is valid, a bad quantity, or a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
<<<<<<< HEAD
# TODO: loop over transactions; for each line, split it into
# operation and quantity, then nest the ADD/quantity check
# from the nested-conditional step inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]

for item in transactions:
        operation,quantity = item.split()
        quantity = int(quantity)
        if operation == "ADD":
                if quantity > 0:
                        print(item, "- valid")
                else:
                        print(item, "- invalid quantity")
        elif operation == "REMOVE":
                print(item, "- processing remove")

# PREDICT before you run: In the Putting It Together code, which check flags
#                         "ADD -5" as invalid: operation == "ADD", amount > 0,
#                         or operation == "REMOVE"?
=======
# TODO: loop over transactions; split each into operation and amount
# TODO: put the nested ADD/quantity check inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]

# PREDICT before you run: Which check flags "ADD -5" as invalid?
>>>>>>> upstream/main
# Your answer:
#
