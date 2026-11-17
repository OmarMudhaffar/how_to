lines = []
file = open("howto.txt", "r")
for line in file:
    lines.append(line.strip())
file.close()

def best_three(question, lines):
    question_words = question.lower().replace("?", "").split()
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
    print(results[:3])
    return results[:3]


while True:
    question = input("\nAsk me (or type exit): ")
    if question == "exit":
        break

    answers = best_three(question, lines)

    if len(answers) == 0:
        print("Sorry, I did not find anything.")
    else:
        number = 1
        for answer in answers:
            parts = answer[1].split("|")
            print(number, "-", parts[0].strip())
            print("   ", parts[1].strip())
            number = number + 1

