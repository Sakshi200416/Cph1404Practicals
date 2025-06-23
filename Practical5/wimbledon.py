FILENAME = "wimbledon.csv"

def main():
    records = get_records(FILENAME)
    champion_to_wins, countries = process_data(records)
    print("Wimbledon Champions:")
    for name, wins in champion_to_wins.items():
        print(f"{name} {wins}")
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_records(filename):
    """Read and return data rows from file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        return [line.strip().split(",") for line in in_file]


def process_data(data):
    champion_to_wins = {}
    countries = set()
    for record in data:
        champion = record[2]
        country = record[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries


if __name__ == "__main__":
    main()
