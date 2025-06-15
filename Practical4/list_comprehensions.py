numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print("Squares:", squares)

# TODO: Make a list of even numbers from 1 to 20 (inclusive)
evens = [i for i in range(1, 21) if i % 2 == 0]
print("Evens:", evens)

# TODO: Make a list of numbers from 1 to 100 that are divisible by 10
div_by_10 = [i for i in range(1, 101) if i % 10 == 0]
print("Divisible by 10:", div_by_10)
