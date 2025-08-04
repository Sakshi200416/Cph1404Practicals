class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if enough fuel, or drive until fuel runs out."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance
