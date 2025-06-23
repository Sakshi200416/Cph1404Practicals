"""
State Abbreviations
Estimate: 10 minutes
Actual:   X minutes
"""

STATE_ABBREV_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(STATE_ABBREV_TO_NAME)

state_abbrev = input("Enter short state: ").upper()
while state_abbrev != "":
    try:
        print(f"{state_abbrev} is {STATE_ABBREV_TO_NAME[state_abbrev]}")
    except KeyError:
        print("Invalid short state")
    state_abbrev = input("Enter short state: ").upper()

for abbrev, name in STATE_ABBREV_TO_NAME.items():
    print(f"{abbrev:>3} is {name}")
