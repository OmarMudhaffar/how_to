from .data import get_data
from . import how_to as ht
from .menuside import showmenu



def run():
    lines = get_data()
    showmenu()

    while True:
        question = input("Hi Son what do you want me to teach you?: ")
        if question == "exit":
            break

        if ht.has_special_chars(question):
            print("Son, use only letters and numbers, no special characters.")
            continue

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