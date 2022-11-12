class FiniteAutomata:

    def __init__(self, filename):
        self.filename = filename
        self.readFromFile()

    @staticmethod
    def readLine(line):
        return line.strip().split(' ')[2:]

    def readFromFile(self):
        with open(self.filename) as file:
            self.Q = FiniteAutomata.readLine(file.readline())  # states
            self.E = FiniteAutomata.readLine(file.readline())  # alphabet
            self.q0 = FiniteAutomata.readLine(file.readline())[0]  # initial state: only one element
            self.F = FiniteAutomata.readLine(file.readline())  # final states

            file.readline()

            # Get all transitions
            self.S = {}
            for line in file:
                lhs = line.strip().split('->')[0].strip()
                rhs = line.strip().split('->')[1].strip()
                src = lhs.replace('(', '').replace(')', '').split(',')[0]
                path = lhs.replace('(', '').replace(')', '').split(',')[1]

                if (src, path) in self.S.keys():
                    self.S[(src, path)].append(rhs)
                else:
                    self.S[(src, path)] = [rhs]

            if not self.validate():
                raise Exception("Error while reading input file.")

    def validate(self):
        # initial state should be a part of states
        if self.q0 not in self.Q:
            print('Initial state not in states')
            return False
        # final state(s) should be a part of states
        for f in self.F:
            if f not in self.Q:
                print('Final state not in states')
                return False

        # check for intruder states or alphabet elements
        for key in self.S.keys():
            state = key[0]
            elem = key[1]
            if state not in self.Q:
                print('Usage of invalid state as source')
                return False
            if elem not in self.E:
                print('usage of invalid alphabet element')
                return False
            for dest in self.S[key]:
                if dest not in self.Q:
                    print('Usage of invalid state as destination')
                    return False
        return True

    def isDfa(self):
        for pair in self.S.keys():
            print(self.S[pair])
            if len(self.S[pair]) > 1:  # more than one destination obtained form the same (src, path) pair
                return False
        return True

    def checkSequence(self, sequence):
        if not self.isDfa():
            print("Sequence is not DFA.")
            return
        currentState = self.q0
        for symbol in sequence:
            if (currentState, symbol) in self.S.keys():
                currentState = self.S[(currentState, symbol)][0]  # because it's a dfa, we know we only have one dest
            else:
                return False
        # check if we reached a final state
        if currentState in self.F:
            return True
        else:
            return False
