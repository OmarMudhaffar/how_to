from .colors import color, slow_print, GREEN, CYAN
from .how_to import best_three


class Person:
    def __init__(self, name, text_color=CYAN):
        self.name = name
        self.text_color = text_color

    def say(self, text):
        slow_print(color(self.name + ": ", self.text_color) + text)


class Dad(Person):
    def __init__(self, knowledge):
        super().__init__("Dad", GREEN)
        self.knowledge = knowledge

    def teach(self, question):
        return best_three(question, self.knowledge)

    def learn(self, title, answer):
        self.knowledge.append(title + " | " + answer)
