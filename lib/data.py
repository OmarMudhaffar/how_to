import logging

FILE_PATH = "dad-head/howto.txt"


def read_lines(path):
    """Generator: give back the lines of the file one by one."""
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


def get_data(path=FILE_PATH):
    """Load everything dad knows from the file into a list."""
    try:
        return list(read_lines(path))
    except FileNotFoundError:
        logging.error("file not found: " + path)
        print("Dad lost his memory! (file " + path + " not found)")
        return []


def add_how_to(title, answer, path=FILE_PATH):
    """Save a new how-to at the end of the file."""
    with open(path, "a") as file:
        file.write(title + " | " + answer + "\n")
