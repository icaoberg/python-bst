class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def hasLeft(self):
        if self.left is None:
            return False
        else:
            return True

    def setLeft(self, node):
        self.left = node

    def getLeft(self):
        return self.left

    def hasRight(self):
        if self.right is None:
            return False
        else:
            return True

    def setRight(self, node):
        self.right = node

    def getRight(self):
        return self.right

    def isLeaf(self):
        if not self.hasLeft() and not self.hasRight():
            return True
        else:
            return False

    def get(self):
        return self.value

    def has(self):
        if self.value is not None:
            return True
        else:
            return False

    def set(self,value):
        self.value = value
