"""Expected time:35min
   Actual time:32min
"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing  # "Dynamic" or "Static"
        self.reflection = reflection  # True/False
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
