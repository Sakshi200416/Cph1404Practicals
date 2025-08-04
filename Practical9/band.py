class Band:
    """Represent a band, which has musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Call the play() method for each musician."""
        for musician in self.musicians:
            musician.play()
