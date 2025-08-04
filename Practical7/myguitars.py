from guitar import Guitar


FILENAME = "guitars.csv"


def load_guitars():
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(guitars):
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def main():
    guitars = load_guitars()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    print("\nAdd new guitars")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    guitars.sort()
    print("\nSorted guitars:")
    for guitar in guitars:
        print(guitar)

    save_guitars(guitars)


if __name__ == '__main__':
    main()
