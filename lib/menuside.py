from .colors import color, YELLOW, CYAN, BLUE

MENU = {
    "1": "Ask dad how to do something",
    "2": "Ask AI dad (when dad does not know)",
    "3": "Check the weather in a city",
    "4": "Teach dad something new",
    "5": "Show my last questions",
    "6": "Clear my questions history",
    "exit": "Close the app",
}

DAD_PICTURE = r"""
      ______
     /      \
    |  o  o  |
    |   __   |   "Ask me anything, son!"
     \______/
       |  |
"""


def show_banner(weather_text):
    """Show the welcome picture and today's weather."""
    print(color("*" * 50, YELLOW))
    print(color(DAD_PICTURE, CYAN))
    print(color("   Welcome to the How To app!", YELLOW))
    print(color("   Weather: " + weather_text, BLUE))
    print(color("*" * 50, YELLOW))


def show_menu():
    """Print all the menu options."""
    print()
    for key, text in MENU.items():
        print(color(" [" + key + "] ", YELLOW) + text)
    print()
