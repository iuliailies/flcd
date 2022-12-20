from grammar import Grammar
from customParser import Parser
from recursive_descendent import recursive_descendant
import re


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', token) is not None


def isConstant(token):
    return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^(0|[+-]?[1-9][0-9]*),[0-9]*|^`.`$|^`.*`$', token) is not None


def isStringConstant(token):
    return re.match(r"^'.'$|^'.*'$", token) is not None


def buildSequenceFromPIF(filename):
    sequence = []
    with open(filename, 'r') as file:
        for line in file:
            elem = line.split(":")[0].strip()
            type = line.split(",")[-1].strip()
            if type == '0':
                if isStringConstant(elem):
                    sequence.append('string')
                elif isConstant(elem):
                    sequence.append('integer')
                else:
                    sequence.append('constant')
            elif type == '1':
                sequence.append('identifier')
            else:
                sequence.append(elem)
    print("Sequence from PIF: ", sequence)
    return sequence


class UI:

    def _init_(self):
        self.grammar = None

    def run(self):

        print("Input file(g1, g2 or g3)>>")
        cmd = input()
        if cmd == "g1":
            self.grammar = Grammar.readFile("g1.txt")
        elif cmd == "g2":
            self.grammar = Grammar.readFile("g2.txt")
        elif cmd == "g3":
            self.grammar = Grammar.readFile("g3.txt")
        else:
            print("Invalid option")
            return

        while True:
            print("1. Print grammar\n2. Print set of productions for a given non-terminal\n3. Check if CFG\n4. Apply recursive descendant\nexit\n>>")
            cmd = input()
            if cmd == "1":
                print(self.grammar)
            elif cmd == "2":
                print("Add non-terminal>>")
                nonTerminal = input()
                print(self.grammar.getProductionsFor(nonTerminal))
            elif cmd == "3":
                isCgf = self.grammar.isCFG()
                if isCgf:
                    print("Grammar is CFG")
                else:
                    print("Grammar is NOT CGF")
            elif cmd == "4":
                parser = Parser(self.grammar)
                # sequence = ['1', '1', '0', '0', '0', '1', '1', '1', '0', '0']
                # sequence = buildSequenceFromPIF('pif2.txt')
                sequence = ['a', 'a', 'c', 'b', 'c']
                result, productions = recursive_descendant(self.grammar, sequence, parser.config)
                print(result, productions)

                if result:
                    parser.parse_tree()
                    parser.write_tree_to_file("g3")
            elif cmd == "exit":
                break


ui = UI()
ui.run()

