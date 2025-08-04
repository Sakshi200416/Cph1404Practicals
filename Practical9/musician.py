class Musician:
    """Represent a musician who has a name and a list of instruments."""

    def __init__(self, name):
        self.name = name
        self.instruments = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(i) for i in self.instruments)})"

    def add(self, instrument):
        """Add an instrument to this musician."""
        self.instruments.append(instrument)

    def play(self):
        """Print what the musician is playing, or if they need an instrument."""
        if not self.instruments:
            print(f"{self.name} needs an instrument!")
        else:
            print(f"{self.name} is playing: {self.instruments[0]}")
