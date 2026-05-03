from Node import Node
from graphviz import Digraph
import random

class BST:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def random(self, number_of_nodes):
        self.root = None
        self.number_of_nodes = 0

        if number_of_nodes <= 0:
            return

        elements = random.sample(range(number_of_nodes), number_of_nodes)
        for e in elements:
            self.insert(e)

    def get_root(self):
        return self.root

    def insert(self, element):
        if self.root is None:
            self.root = Node(element)
            self.number_of_nodes += 1
        else:
            self.__insert(self.root, element)

    def __insert(self, node, element):
        if node.get() > element:
            if not node.has_left():
                node.set_left(Node(element))
                self.number_of_nodes += 1
            else:
                self.__insert(node.get_left(), element)
        else:
            if not node.has_right():
                node.set_right(Node(element))
                self.number_of_nodes += 1
            else:
                self.__insert(node.get_right(), element)

    def is_empty(self):
        return self.number_of_nodes == 0

    def size(self):
        return self.number_of_nodes

    def min(self):
        if self.is_empty():
            return None
        return self.__min(self.root)

    def __min(self, node):
        if not node.has_left():
            return node.get()
        return self.__min(node.get_left())

    def max(self):
        if self.is_empty():
            return None
        return self.__max(self.root)

    def __max(self, node):
        if not node.has_right():
            return node.get()
        return self.__max(node.get_right())

    def inorder(self):
        result = []
        if not self.is_empty():
            self.__inorder(self.root, result)
        return result

    def __inorder(self, node, result):
        if node.has_left():
            self.__inorder(node.get_left(), result)
        result.append(node.get())
        if node.has_right():
            self.__inorder(node.get_right(), result)

    def tofigure(self, debug=False):
        self._invisible = self.number_of_nodes + 1
        dot = Digraph('BST')

        if self.is_empty():
            return dot

        self.__tofigure(self.root, dot)
        return dot

    def __tofigure(self, node, dot):
        if node.has_left():
            dot.edge(str(node.get()), str(node.get_left().get()))
            self.__tofigure(node.get_left(), dot)
        else:
            dot.node(str(self._invisible), label='NULL', shape='square')
            dot.edge(str(node.get()), str(self._invisible))
            self._invisible += 1

        if node.has():
            dot.node(str(node.get()), str(node.get()))

        if node.has_right():
            dot.edge(str(node.get()), str(node.get_right().get()))
            self.__tofigure(node.get_right(), dot)
        else:
            dot.node(str(self._invisible), label='NULL', shape='square')
            dot.edge(str(node.get()), str(self._invisible))
            self._invisible += 1

    def __len__(self):
        return self.number_of_nodes

    def __repr__(self):
        return f"BST(size={self.number_of_nodes}, inorder={self.inorder()})"
