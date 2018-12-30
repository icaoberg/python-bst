from BST import BST
import random

def test_empty():
	tree = BST()
	assert tree.isEmpty()
	assert tree.size() == 0

def test_it():
	tree = BST()
	tree.insert(1)
	tree.insert(5)
	tree.insert(3)
	tree.insert(4)
	assert tree.min() == 1
	assert tree.max() == 5
