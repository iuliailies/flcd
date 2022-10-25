from linkedList import LinkedList, Node

reservedWords = []
separators = []
operators = []

tokensTable = {
    'constants': 0,
    'identifiers': 1
}


def parseFile():
    index = 2
    with open('tokens.in', 'r') as f:
        for i in range(18):
            token = f.readline().strip()
            operators.append(token)
            tokensTable[token] = index
            index += 1
        for i in range(13):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)
            tokensTable[separator] = index
            index += 1
        for i in range(16):
            reservedWord = f.readline().strip()
            reservedWords.append(reservedWord)
            tokensTable[reservedWord] = index
            index += 1