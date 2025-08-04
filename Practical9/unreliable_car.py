import random
from car import Car


class UnreliableCar(Car):
    """An UnreliableCar that may not drive all the time, based on reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car. It only drives if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
