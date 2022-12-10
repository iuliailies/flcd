from grammar import Grammar
from recursive_descendent import recursive_descendant

class UI:

    def __init__(self):
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
                sequence = ['1', '1', '0', '0', '0', '1', '1', '1', '0', '0']
                result, productions = recursive_descendant(self.grammar, sequence)
                print(result, productions)
            elif cmd == "exit":
                break


ui = UI()
ui.run()
