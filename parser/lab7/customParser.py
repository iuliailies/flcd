from recursive_descendent import Configuration


class Node:
    def __init__(self, value, index):
        self.index = index
        self.father = -1
        self.sibling = -1
        self.value = value
        self.production = -1

    def __str__(self):
        return str(self.value) + " " + str(self.father) + " " + str(self.sibling)


class Parser:

    def __init__(self, grammar):
        self.grammar = grammar
        self.config = Configuration(grammar.S)
        self.iteration = 0
        self.tree = []
        self.words = []

    def parse_tree(self):
        fathers = [-1]

        for pos in range(0, len(self.config.work_stack)):
            if type(self.config.work_stack[pos]) == tuple:  # non terminal with production
                self.tree.append(Node(self.config.work_stack[pos][0], pos))
                self.tree[pos].production = self.config.work_stack[pos][1]
            else:
                self.tree.append(Node(self.config.work_stack[pos], pos))  # terminal

        for pos in range(0, len(self.config.work_stack)):
            if type(self.config.work_stack[pos]) == tuple:
                self.tree[pos].father = fathers[0]
                fathers = fathers[1:]
                len_production = len(self.config.work_stack[pos][1])
                child_indexes = []
                for i in range(0, len_production):
                    child_indexes.append(pos + i + 1)
                    fathers.insert(0, pos)
                for i in range(0, len_production):
                    if self.tree[child_indexes[i]].production != -1:
                        offset = self.get_production_depth_offset(child_indexes[i])
                        for j in range(i + 1, len_production):
                            child_indexes[j] += offset
                for i in range(0, len_production - 1):
                    self.tree[child_indexes[i]].sibling = child_indexes[i + 1]
            else:
                self.tree[pos].father = fathers[0]
                fathers = fathers[1:]

    def get_production_depth_offset(self, index):
        prod_rhs = self.config.work_stack[index][1]
        len_production = len(prod_rhs)
        offset = len_production
        for i in range(1, len_production + 1):
            if type(self.config.work_stack[index + i]) == tuple:
                offset += self.get_production_depth_offset(index + i)
        return offset

    def write_tree_to_file(self, filename):
        file = open(filename + ".out", "w")
        file.write("index | value | father | sibling\n")

        for pos in range(0, len(self.config.work_stack)):
            node = self.tree[pos]
            file.write(str(pos) + " " + str(node) + "\n")
        file.close()
