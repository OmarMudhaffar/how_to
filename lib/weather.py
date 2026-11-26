import re
import logging
import requests


def is_valid_city(city):
    return re.fullmatch(r"[A-Za-z ]{2,40}", city) is not None


def get_weather(city):
    try:
        response = requests.get("https://wttr.in/" + city, params={"format": "3"}, timeout=5)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as error:
        logging.error("weather api failed: " + str(error))
        return "Dad could not check the weather right now."
