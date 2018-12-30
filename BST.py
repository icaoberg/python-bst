from Node import Node

class BST:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

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
        if self.isEmpty():
            return
        else:
            self.__inorder(self.root)

    def __inorder(self, node):
        if node.hasLeft():
            self.__inorder(node.getLeft())

        print(node.get(), ' ')

        if node.hasRight():
            self.__inorder(node.getRight())
