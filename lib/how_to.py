import re

COMMON_WORDS = {"how", "to", "a", "an", "the", "my", "i", "do", "can", "you", "me", "on", "in", "of"}


def unique_words(text):
    """Return a set of the words in the text, without common words like 'how' and 'to'."""
    return set(text.lower().split()) - COMMON_WORDS


def best_three(question, lines):
    """Give back the 3 lines whose title matches the question the most."""
    question_words = unique_words(question)
    results = []

    for line in lines:
        title = line.split("|")[0]
        title_words = unique_words(title)

        score = len(question_words & title_words)
        if score > 0:
            results.append((score, line))

    results.sort(key=lambda item: item[0], reverse=True)
    return results[:3]


def has_special_chars(question):
    """True if the text has anything that is not a letter, number or space."""
    return re.search(r"[^a-zA-Z0-9 ]", question) is not None


def is_valid_title(title):
    """A new how-to title must start with 'how to' and have only letters."""
    return re.fullmatch(r"how to [a-z ]+", title.lower()) is not None
