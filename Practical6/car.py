class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        """Return a string representation of a Car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car for a given distance if enough fuel."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self._odometer += distance
        return distance
