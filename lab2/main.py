from scanner import *
from symbolTable import SymbolTable


class Main:

    def __init__(self):
        self.idST = SymbolTable(17)
        self.constST = SymbolTable(17)
        self.scanner = Scanner()

    def run(self):
        parseFile()
        exceptions = []

        with open("p1.txt", 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.tokenize(line.strip())
                print(tokens)
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords+separators+operators:
                        if tokens[i] == ' ':
                            continue
                        # separate between "-" as operator and "-" as part of negative number
                        if tokens[i] in ['+', '-']:
                            temp = i - 1
                            while tokens[temp] == ' ':
                                temp -= 1
                            if temp == -1 or tokens[temp] in self.scanner.numberSignCases:
                                extra = tokens[i]
                                continue
                    elif tokens[i] in self.scanner.concatenationCases and i < len(tokens)-1:
                        if re.match("[1-9]", tokens[i+1]):
                            extra = tokens[i][-1]
                            continue
                        else:
                            exceptions.append('1. Lexical error at token ' + tokens[i] + ', at line ' + str(lineCounter) + "\n")
                    elif self.scanner.isIdentifier(tokens[i]):
                        self.idST.add(tokens[i])
                    elif self.scanner.isConstant(tokens[i]):
                        self.constST.add(extra+tokens[i])
                        extra = ''
                    else:
                        exceptions.append('2. Lexical error at token ' + tokens[i] + ', at line ' + str(lineCounter) + "\n")

        print("ids\n")
        print(self.idST)
        print("constants\n")
        print(self.constST)

        with open('idsST.out', 'w') as writer:
            writer.write(str(self.idST))

        with open('constantsST.out', 'w') as writer:
            writer.write(str(self.constST))

        if not len(exceptions):
            print("Lexically correct")
        else:
            for exception in exceptions:
                print(exception)


main = Main()
main.run()
