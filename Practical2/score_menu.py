"""Score Menu Program"""

import random


def main():
    """Main function to run the score menu."""
    score = get_valid_score()
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice.")


def print_menu():
    """Display menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = -1
    while score < 0 or score > 100:
        try:
            score = float(input("Enter score (0–100): "))
        except ValueError:
            print("Invalid input; enter a number.")
    r
