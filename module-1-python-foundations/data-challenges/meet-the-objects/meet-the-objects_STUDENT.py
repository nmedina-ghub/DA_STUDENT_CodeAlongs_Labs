#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations

names = []
bikes = []

for station in stations:
    names.append(station["name"])

    bikes.append(station["bikes_available"])
names.pop(2)

print("stations in the file:", len(stations))
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1: I created two empty lists to store the station names and bike counts.
#
#
# Step 1, answer 2: I removed the third station name from the names list using pop(2).
#
# Step 1, answer 3: The lists no longer match because I removed a name but did not remove the bike count from the same position.
#


# Step 2: Define the Station Class and Prove Two Instances Are Independent

class Station:
    def __init__(self, name: str, capacity: int, bikes_available: int):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

fleet = []

for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"]))

busy = fleet[0]
quiet = fleet[1]

print(busy.needs_restock())
print(quiet.needs_restock())

busy.bikes_available = 0

print(busy.needs_restock())
print(quiet.needs_restock())

# Step 2, answer 1: I created a Station class to store each station's name, capacity, and available bikes.

#
# Step 2, answer 2: I used __init__ to give each station its own information when it is created.
#
# Step 2, answer 3: I added needs_restock() to check if a station has less than one-fourth of its capacity in bikes.
#
# Step 2, answer 4: I changed the number of bikes at one station and saw that the other station stayed the same because each object is independent.
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])

class Station:
    def __init__(self, name: str, capacity: int, bikes_available: int):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

fleet = []

for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"]))

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1: I added __str__ to make the station information easier to read by showing the station name, available bikes, and total capacity.
#
# Step 3, answer 2: Printing fleet[0] uses __str__ to show the station information.
# Printing fleet[:2] still shows the object addresses because it is a list.


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher

class Station:
    def __init__(self, name: str, capacity: int, bikes_available: int):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"

fleet = []

for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"]))

van_list = []

for station in fleet:
    if station.needs_restock():
        van_list.append(station)

print(van_list)

for station in van_list:
    print(station)


# Step 4, answer 1: I added __repr__ to show a simple representation of each Station object.
#
# Step 4, answer 2: I created van_list to store only the stations that need restocking.

#
# Step 4, answer 3: Printing van_list uses __repr__, while printing each station separately uses __str__ to show the station information.
#
