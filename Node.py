class Node:
    def __init__(self, value):
        '''
        Default constructor
        :param value: node value
        :type value: numeric
        '''

        self.left = None
        self.right = None
        self.value = value

    def hasLeft(self):
        '''
        Returns true if node has a left child
        '''

        if self.left is None:
            return False
        else:
            return True

    def setLeft(self, node):
        '''
        Set or replace left child
        '''

        self.left = node

    def getLeft(self):
        '''
        Get left child
        '''

        return self.left

    def hasRight(self):
        '''
        Returns true if node has a right child
        '''

        if self.right is None:
            return False
        else:
            return True

    def setRight(self, node):
        '''
        Set or replace right child
        '''

        self.right = node

    def getRight(self):
        '''
        Get right child
        '''

        return self.right

    def isLeaf(self):
        '''
        Returns true if node has no children
        '''

        if not self.hasLeft() and not self.hasRight():
            return True
        else:
            return False

    def get(self):
        '''
        Returns the value of the node
        '''

        return self.value

    def has(self):
        if self.value is not None:
            return True
        else:
            return False

    def set(self,value):
        '''
        Sets the value of the node
        '''

        self.value = value
