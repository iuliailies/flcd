class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, headValue = None):
        self.headValue = headValue
        self.lastValue = headValue

    def appendToEnd(self, value):
        if self.headValue is None:
            self.headValue = value
        else:
            self.lastValue.next = value
        self.lastValue = value

