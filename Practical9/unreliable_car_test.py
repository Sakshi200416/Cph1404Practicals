from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    reliable_car = UnreliableCar("Reliable", 100, 100)
    unreliable_car = UnreliableCar("Unreliable", 100, 10)

    print("ReliableCar should always drive:")
    for i in range(5):
        print(f"Attempt {i+1}: drove {reliable_car.drive(20)}km")

    print("\nUnreliableCar may not drive:")
    for i in range(5):
        print(f"Attempt {i+1}: drove {unreliable_car.drive(20)}km")


if __name__ == "__main__":
    main()
