import re
import logging
import requests


def is_valid_city(city):
    """A city name can have only letters and spaces (2 to 40 letters)."""
    return re.fullmatch(r"[A-Za-z ]{2,40}", city) is not None


def get_weather(city):
    """Ask the wttr.in API for the weather in a city. Returns one short line."""
    try:
        response = requests.get("https://wttr.in/" + city, params={"format": "3"}, timeout=5)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as error:
        logging.error("weather api failed: " + str(error))
        return "Dad could not check the weather right now."
