import re

def best_three(question, lines):
    question_words = question.lower().split()
    results = []

    for line in lines:
        title = line.split("|")[0]
        title_words = title.lower().split()

        score = 0
        for word in question_words:
            if word in title_words:
                score = score + 1

        if score > 0:
            results.append([score, line])

    results.sort(reverse=True)
    return results[:3]

def has_special_chars(question):
    return re.search(r"[^a-zA-Z0-9 ]", question) is not None
