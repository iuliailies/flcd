reservedWords = []
separators = []
operators = []


def parseFile():
    with open('tokens.in', 'r') as f:
        for i in range(18):
            operators.append(f.readline().strip())
        for i in range(13):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)
        for i in range(16):
            reservedWords.append(f.readline().strip())