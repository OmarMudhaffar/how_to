lines = []

def get_data():
    file = open("dad-head/howto.txt", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines