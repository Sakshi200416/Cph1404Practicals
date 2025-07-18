class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
