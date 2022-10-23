from hashTable import HashTable


class SymbolTable:

    def __init__(self, size) -> None:
        self.__hashTable = HashTable(size)

    def __str__(self) -> str:
        return str(self.__hashTable)

    def add(self, key):
        return self.__hashTable.add(key)

    def contains(self, key):
        return self.__hashTable.contains(key)

    def remove(self, key):
        self.__hashTable.remove(key)

    def getPosition(self, key):
        return self.__hashTable.getPosition(key)
