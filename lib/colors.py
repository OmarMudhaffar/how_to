import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"


def color(text, code):
    """Return the text painted with a color code."""
    return code + text + RESET


def slow_print(text, delay=0.02):
    """Print the text letter by letter, like dad is typing."""
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()
