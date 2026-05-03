class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def has_left(self):
        return self.left is not None

    def set_left(self, node):
        self.left = node

    def get_left(self):
        return self.left

    def has_right(self):
        return self.right is not None

    def set_right(self, node):
        self.right = node

    def get_right(self):
        return self.right

    def is_leaf(self):
        return not self.has_left() and not self.has_right()

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def has(self):
        return self.value is not None
