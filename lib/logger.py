import logging


def setup_logging():
    """Save all logs in the app.log file."""
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def log_call(func):
    """Decorator: write in the log every time this function is used."""
    def wrapper(*args, **kwargs):
        logging.info("user used: " + func.__name__)
        return func(*args, **kwargs)
    return wrapper
