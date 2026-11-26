import logging

FILE_PATH = "dad-head/howto.txt"


def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


def get_data(path=FILE_PATH):
    try:
        return list(read_lines(path))
    except FileNotFoundError:
        logging.error("file not found: " + path)
        print("Dad lost his memory! (file " + path + " not found)")
        return []


def add_how_to(title, answer, path=FILE_PATH):
    with open(path, "a") as file:
        file.write(title + " | " + answer + "\n")
