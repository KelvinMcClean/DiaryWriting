import random


def main():
    lines = []
    files = ['myself', 'my_area', 'news', 'politics']
    filename = ""
    continueToken = False
    attemptToken = 0
    while len(lines) == 0 or not continueToken:
        attemptToken += 1
        if attemptToken > 1000:
            return "Couldn't get anything to print"
        filename = random.choice(files)
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        for num, i in enumerate(lines, start=0):
            if num != 0 and not i.startswith("--"):
                continueToken = True
                break

    print("CATEGORY:", lines[0].strip())
    choice = lines[0]
    index = 0
    while choice.startswith("--") or choice == lines[0]:
        choice = random.choice(lines)
        index = lines.index(choice)

    print("PROMPT:", choice.strip())

    if filename != 'news':
        lines[index] = "--" + choice

    file = open(filename, 'w')
    file.writelines(lines)
    file.close()


if __name__ == '__main__':
    main()
