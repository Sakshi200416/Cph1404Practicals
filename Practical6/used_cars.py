from car import Car

def main():
    """Run tests for Car class."""
    limo = Car("Limo", 100)
    limo.add(20)             # Add 20 more fuel
    print(f"Fuel after adding: {limo.fuel}")
    distance_driven = limo.drive(115)  # Try to drive 115 km
    print(f"Distance driven: {distance_driven}")
    print(limo)
main()
