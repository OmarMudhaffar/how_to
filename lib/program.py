import os
import logging
from dotenv import load_dotenv

from .data import get_data, add_how_to
from .how_to import has_special_chars, is_valid_title
from .people import Dad
from .menuside import show_banner, show_menu
from .weather import get_weather, is_valid_city
from .history import save_question, get_history, clear_history
from .ai import ask_ai
from .logger import setup_logging, log_call
from .colors import color, RED, YELLOW


@log_call
def ask_dad(dad):
    """Ask dad a question and show his 3 best answers."""
    question = input("What do you want me to teach you?: ").strip()
    if question == "" or has_special_chars(question):
        print(color("Son, use only letters and numbers, no special characters.", RED))
        return

    save_question(question)
    answers = dad.teach(question)
    if len(answers) == 0:
        dad.say("Sorry son, I don't know this one. Try [2] to ask AI dad.")
        return

    number = 1
    for score, line in answers:
        title, answer = line.split("|", 1)
        print(color(str(number) + " - " + title.strip(), YELLOW))
        dad.say(answer.strip())
        number = number + 1


@log_call
def ask_ai_dad(dad):
    """Send the question to the AI and show the answer."""
    question = input("Ask AI dad anything: ").strip()
    if question == "":
        return
    save_question(question)
    print("AI dad is thinking...")
    dad.say(ask_ai(question))


@log_call
def show_weather(dad):
    """Ask for a city and show its weather."""
    city = input("Which city?: ").strip()
    if not is_valid_city(city):
        print(color("City name can have only letters.", RED))
        return
    dad.say(get_weather(city))


@log_call
def teach_dad(dad):
    """Let the user add a new how-to that is saved in the file."""
    title = input("Title (must start with 'how to'): ").strip().lower()
    if not is_valid_title(title):
        print(color("Title must look like: how to make coffee", RED))
        return
    answer = input("How to do it: ").strip()
    if answer == "":
        print(color("The answer can not be empty.", RED))
        return
    add_how_to(title, answer)
    dad.learn(title, answer)
    dad.say("Thanks son, now I know " + title + "!")


@log_call
def show_history(dad):
    """Show the last questions from the database."""
    rows = get_history()
    if len(rows) == 0:
        dad.say("You did not ask me anything yet.")
        return
    for question, time in rows:
        print(color(time, YELLOW) + "  " + question)


@log_call
def clear_my_history(dad):
    """Delete all questions from the database."""
    clear_history()
    dad.say("Done, I forgot all your questions.")


ACTIONS = {
    "1": ask_dad,
    "2": ask_ai_dad,
    "3": show_weather,
    "4": teach_dad,
    "5": show_history,
    "6": clear_my_history,
}


def run():
    """Start the app and keep showing the menu until the user types exit."""
    load_dotenv()
    setup_logging()
    logging.info("app started")

    dad = Dad(get_data())
    show_banner(get_weather(os.getenv("CITY", "Barcelona")))

    try:
        while True:
            show_menu()
            choice = input("Choose an option: ").strip().lower()
            if choice == "exit":
                break
            action = ACTIONS.get(choice)
            if action is None:
                print(color("Wrong choice, try again.", RED))
                continue
            action(dad)
    except (KeyboardInterrupt, EOFError):
        print()

    dad.say("Bye son, come back anytime!")
    logging.info("app closed")
