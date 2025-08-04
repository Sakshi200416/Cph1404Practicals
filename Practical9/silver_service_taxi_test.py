from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare and string representation."""
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(f"Fare: ${fancy_taxi.get_fare():.2f}")
    assert round(fancy_taxi.get_fare(), 2) == 48.80, "Fare should be $48.80"


if __name__ == "__main__":
    main()
