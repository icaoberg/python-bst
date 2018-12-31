from BST import BST
import random

def test_empty():
	tree = BST()
	assert tree.isEmpty()
	assert tree.size() == 0

def test_it():
	tree = BST()
	random.seed( 12345 )
	number_of_nodes = 10
	tree.random( number_of_nodes )
	assert tree.min() == 0
	assert tree.max() == 9
