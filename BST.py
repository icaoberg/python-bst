from Node import Node
from graphviz import Digraph
import random

class BST:
    traversal = None
    dot = None
    list_of_nodes = set()
    list_of_edges = set()
    
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def random(self, number_of_nodes):
        self.root = None
        self.number_of_nodes = 0

        elements = range(number_of_nodes)
        elements = random.sample(elements, len(elements))

        for e in elements:
            self.insert(e)

    def getRoot(self):
        return self.root

    def __insert(self, node, element):        
        if node.get() > element:
            #add to the left
            if not node.hasLeft():
                #if left child is nonexistent
                node.setLeft( Node(element) )
                self.number_of_nodes = self.number_of_nodes + 1
            else:
                self.__insert(node.getLeft(), element)

            return
        else:
            #add to the right
            if not node.hasRight():
                #if right child is nonexistent
                node.setRight( Node(element) )
                self.number_of_nodes = self.number_of_nodes + 1
            else:
                self.__insert(node.getRight(), element)

            return

    def insert(self, element):
        if self.root is None:
            self.root = Node( element )
            self.number_of_nodes = self.number_of_nodes + 1
        else:
            self.__insert(self.root, element)

    def isEmpty(self):
        if self.number_of_nodes == 0:
            return True
        else:
            return False

    def size(self):
        return self.number_of_nodes

    def min(self):
        if self.isEmpty():
            return None
        else:
            if self.root.isLeaf() or not self.root.hasLeft():
                return self.root.get()
            else:
                return self.__min(self.root.getLeft())

    def __min(self,node):
        if node.isLeaf():
            return node.get()
        else:
            self.__min(node.getLeft())

    def max(self):
        if self.isEmpty():
            return None
        else:
            if self.root.isLeaf() or not self.root.hasRight():
                return self.root.get()
            else:
                return self.__max(self.root.getRight())

    def __max(self,node):
        if node.isLeaf():
            return node.get()
        else:
            self.__max(node.getRight())

    def inorder(self):
        self.traversal = []
        if self.isEmpty():
            return
        else:
            self.__inorder(self.root)
            
        return self.traversal

    def __inorder(self, node):
        if node.hasLeft():
            self.__inorder(node.getLeft())

        self.traversal.append(node.get())

        if node.hasRight():
            self.__inorder(node.getRight())
            
    def tofigure(self, debug=False):
        if debug:
            print('Creating empty digraph')
            
        self.dot = Digraph('BST')
            
        if self.isEmpty():
            if debug:
                print('BST is empty')
            return self.dot
        else:
            if debug:
                print('Adding root node to digraph with value ' + str(self.root.get()) )
            #self.dot.node(str(self.root.get()))
            self.__tofigure(self.root)

        return self.dot

    def __tofigure(self, node):            
        if node.hasLeft():
            self.dot.edges([str(node.get())+str(node.getLeft().get())])
            self.__tofigure(node.getLeft())

        if node.has():
            self.dot.node(str(node.get()),str(node.get()))

        if node.hasRight():
            self.dot.edges([str(node.get())+str(node.getRight().get())])
            self.__tofigure(node.getRight())