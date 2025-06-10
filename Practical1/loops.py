# a. Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b. Count in 10s to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# c. Print n stars
stars = int(input("Number of stars: "))
print("*" * stars)

# d. Increasing stars
for i in range(1, stars + 1):
    print("*" * i)
