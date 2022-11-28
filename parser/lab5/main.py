from grammar import Grammar


class UI:

    def __init__(self):
        self.grammar = None

    def run(self):

        print("Input file(g1 or g2)>>")
        cmd = input()
        if cmd == "g1":
            self.grammar = Grammar.readFile("g1.txt")
        elif cmd == "g2":
            self.grammar = Grammar.readFile("g2.txt")
        else:
            print("Invalid option")
            return

        while True:
            print("1. Print grammar\n2. Print set of productions for a given non-terminal\n3. Check if CFG\nexit\n>>")
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
            elif cmd == "exit":
                break


ui = UI()
ui.run()
