import pytest
from BST import BST

def test_empty():
    tree = BST()
    assert tree.is_empty()
    assert tree.size() == 0
    assert len(tree) == 0

def test_insert():
    tree = BST()
    for i, val in enumerate([5, 3, 7, 1, 4]):
        tree.insert(val)
        assert tree.size() == i + 1
    assert not tree.is_empty()

def test_inorder():
    tree = BST()
    for val in [5, 3, 7, 1, 4]:
        tree.insert(val)
    assert tree.inorder() == [1, 3, 4, 5, 7]

def test_min_max():
    tree = BST()
    random_bst = BST()
    random_bst.random(10)
    assert random_bst.min() == 0
    assert random_bst.max() == 9

def test_min_max_empty():
    tree = BST()
    assert tree.min() is None
    assert tree.max() is None

def test_min_max_single():
    tree = BST()
    tree.insert(42)
    assert tree.min() == 42
    assert tree.max() == 42

def test_random():
    tree = BST()
    tree.random(10)
    assert tree.size() == 10

def test_random_invalid():
    tree = BST()
    tree.random(0)
    assert tree.is_empty()

def test_repr():
    tree = BST()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    assert repr(tree) == "BST(size=3, inorder=[1, 2, 3])"
