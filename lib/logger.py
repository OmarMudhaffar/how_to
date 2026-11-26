import logging


def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def log_call(func):
    def wrapper(*args, **kwargs):
        logging.info("user used: " + func.__name__)
        return func(*args, **kwargs)
    return wrapper
