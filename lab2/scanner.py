import re

from tokenListParser import *


class Scanner:

    def __init__(self) -> None:
        self.cases = ["=+", "<+", ">+", "<=+", ">=+", "==+", "!=+", "=-", "<-", ">-", "<=-", ">=-", "==-", "!=-"]
        self.numberSignCases = ["=", "(", "<", ">"]

    @staticmethod
    def isIdentifier(token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', token) is not None

    @staticmethod
    def isConstant(token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^`.`$|^`.*`$', token) is not None

    @staticmethod
    def getStringToken(line, index):
        tokens = []
        token = ''
        quotes = 0
        idSeparators = 0

        while index < len(line) and quotes < 2:
            if line[index] == '$':
                idSeparators += 1
            else:
                token += line[index]
            if line[index] == '`':
                quotes += 1
            if (line[index] == '`' and quotes == 2) or line[index] == '$':
                if idSeparators % 2:
                    token += '`'
                    tokens.append(token)
                    token = ''
                else:
                    tokens.append(token)
                    token = '`'

            index += 1

        return tokens, index

    @staticmethod
    def isPartOfOperator(char):
        for op in operators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''  # reset

            elif line[index] == '`':
                if token:
                    tokens.append(token)
                resTokens, index = self.getStringToken(line, index)
                for token in resTokens:
                    tokens.append(token)
                token = ''  # reset

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''  # reset

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens
