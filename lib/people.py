from .colors import color, slow_print, GREEN, CYAN
from .how_to import best_three


class Person:
    """A simple person with a name who can talk."""

    def __init__(self, name, text_color=CYAN):
        self.name = name
        self.text_color = text_color

    def say(self, text):
        """Print what the person says, slowly and with color."""
        slow_print(color(self.name + ": ", self.text_color) + text)


class Dad(Person):
    """Dad is a Person (inherits) who knows how to do many things."""

    def __init__(self, knowledge):
        super().__init__("Dad", GREEN)
        self.knowledge = knowledge

    def teach(self, question):
        """Find the 3 best answers for the question."""
        return best_three(question, self.knowledge)

    def learn(self, title, answer):
        """Remember a new how-to."""
        self.knowledge.append(title + " | " + answer)
