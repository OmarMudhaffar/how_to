from .data import get_data
from . import how_to as ht

def run():
    lines = get_data()

    while True:
        question = input("\nHi Son what do you want me to teach you?: ")
        if question == "exit":
            break

        answers = ht.best_three(question, lines)

        if len(answers) == 0:
            print("Sorry, I did not find anything.")
        else:
            number = 1
            for answer in answers:
                parts = answer[1].split("|")
                print(number, "-", parts[0].strip())
                print("   ", parts[1].strip())
                number = number + 1