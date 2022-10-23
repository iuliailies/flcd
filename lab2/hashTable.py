from collections import deque


class HashTable:
    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, elem):
        sum = 0
        for chr in elem:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    def add(self, elem):
        if self.contains(elem):
            return self.getPosition(elem)
        self.__items[self.hash(elem)].append(elem)
        return self.getPosition(elem)

    def contains(self, elem):
        return elem in self.__items[self.hash(elem)]

    def remove(self, elem):
        self.__items[self.hash(elem)].remove(elem)

    def __str__(self) -> str:
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "->" + str(self.__items[i]) + "\n"
        return result

    def getPosition(self, elem):
        pos = self.hash(elem)
        hashIndex = 0
        for item in self.__items[pos]:
            if item != elem:
                hashIndex += 1
            else:
                break
        return pos, hashIndex
