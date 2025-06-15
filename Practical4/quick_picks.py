import random

NUMBER_OF_PICKS = int(input("How many quick picks? "))
NUMBERS_PER_PICK = 6
LOWEST = 1
HIGHEST = 45

for _ in range(NUMBER_OF_PICKS):
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        number = random.randint(LOWEST, HIGHEST)
        if number not in pick:
            pick.append(number)
    pick.sort()
    print(" ".join(f"{num:2}" for num in pick))
