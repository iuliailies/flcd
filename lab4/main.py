from finitaAutomata import FiniteAutomata


def displayMenu():
    print("1.Read FA from file")
    print("2.Display FA states")
    print("3.Display FA alphabet")
    print("4.Display FA transitions")
    print("5.Display FA initial states")
    print("6.Display FA final states")
    print("7.Check accepted sequence")
    print("exit")


class UI:
    def __readFA(self):
        self.fa = FiniteAutomata('finitaAutomata.in')

    def __displayAll(self):
        print(self.fa)

    def __displayStates(self):
        print(self.fa.Q)

    def __displayAlphabet(self):
        print(self.fa.E)

    def __displayTransitions(self):
        print(self.fa.S)

    def __displayInitialStates(self):
        print(self.fa.q0)

    def __displayFinalStates(self):
        print(self.fa.F)

    def __checkAcceptedSequence(self):

        seq = input("Add the sequence, will be checked char by char: ")
        print(self.fa.checkSequence(seq))

    def run(self):
        functionBindings = {'1': self.__readFA,
                            '2': self.__displayStates,
                            '3': self.__displayAlphabet,
                            '4': self.__displayTransitions,
                            '5': self.__displayInitialStates,
                            '6': self.__displayFinalStates,
                            '7': self.__checkAcceptedSequence}
        stop = False
        while not stop:
            displayMenu()
            print("Enter your choice:")
            option = input()
            if option in functionBindings.keys():
                functionBindings[option]()
            elif option == "exit":
                stop = True


ui = UI()
ui.run()