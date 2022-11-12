from linkedList import LinkedList, Node


class PIF:
    def __init__(self):
        self.__content = LinkedList()

    def add(self, token, pos):
        self.__content.appendToEnd(Node((token, pos)))

    def __str__(self):
        result = ""
        val = self.__content.headValue
        while val.next is not None:
            result += val.data[0] + "->" + str(val.data[1]) + "\n"
            val = val.next
        return result
