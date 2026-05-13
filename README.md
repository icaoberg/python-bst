# python-bst

> [!WARNING]
> This implementation is inspired by a homework assignment from [15-213](https://www.cs.cmu.edu/~213/) at Carnegie Mellon University. It is intended for educational purposes only and is not suitable for production use.

[![CI](https://github.com/icaoberg/python-bst/actions/workflows/ci.yml/badge.svg)](https://github.com/icaoberg/python-bst/actions/workflows/ci.yml)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-bst)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

A simple naive implementation of a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree) in Python.

The purpose of this repo is to serve as an example of how to set up a GitHub Actions workflow.

## Definition

> A binary tree where each internal node x stores a key such that the key stored in any node in the left subtree of x is less than the key stored in x, and the key stored in any node in the right subtree of x is greater than the key stored in x.

— Paul E. Black, *[binary search tree](https://xlinux.nist.gov/dads/HTML/binarySearchTree.html)*, Dictionary of Algorithms and Data Structures [online], NIST.

## When to Use

A binary search tree is the right structure when you need ordered data with efficient search, insert, and delete operations (O(log n) on average):

- **Symbol tables** — compilers store variable and function names in a BST for fast lookup during parsing and code generation.
- **Database indexing** — BSTs underpin many index structures, enabling range queries and sorted iteration over records.
- **Autocomplete** — prefix-based search and suggestion engines traverse a BST to find all keys in a given range efficiently.
- **Priority queues** — a BST can serve as an ordered set where the minimum or maximum is always accessible at the root's leftmost or rightmost node.
- **Sorting** — inserting n elements and reading back with an inorder traversal produces a sorted list in O(n log n) time.

Note: An unbalanced BST degrades to O(n) in the worst case. For guaranteed performance, prefer a self-balancing variant such as a red-black tree.

## Example

![BST](https://github.com/icaoberg/python-bst/blob/master/images/bst.png?raw=true)

```python
from BST import BST

tree = BST()
tree.random(10)
tree.tofigure().render('./images/bst', format='png')
```

## Requirements

- Python 3.6+
- graphviz (system package) for `tofigure()`

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/icaoberg/python-bst.git
cd python-bst
pip install -r requirements.txt
```

## Usage

```python
from BST import BST

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print(tree.size())     # 5
print(tree.min())      # 1
print(tree.max())      # 7
print(tree.inorder())  # [1, 3, 4, 5, 7]
print(tree.is_empty()) # False
print(len(tree))       # 5
```

### Methods

| Method | Description |
|--------|-------------|
| `insert(element)` | Insert an element into the BST |
| `random(n)` | Populate the BST with `n` random integers |
| `min()` | Return the minimum value |
| `max()` | Return the maximum value |
| `inorder()` | Return elements in sorted order as a list |
| `is_empty()` | Return `True` if the BST has no nodes |
| `size()` | Return the number of nodes |
| `get_root()` | Return the root node |
| `tofigure()` | Return a `graphviz.Digraph` visualization |

## Testing

```bash
pytest tests.py
```

## Support
If you found this project helpful, consider buying me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/icaoberg)

Copyright © [icaoberg](https://github.com/icaoberg) at [Carnegie Mellon University](https://www.cmu.edu). All rights reserved.
