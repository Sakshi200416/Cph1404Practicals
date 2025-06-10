# String formatting with f-string
name = "Gibson L-5 CES"
year = 1922
cost = 16035.99
print(f"{year} {name} for about ${cost:,.0f}!")

# Loop for power of 2 table
for i in range(0, 11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
