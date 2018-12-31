# python-bst
![coverage.io](https://codecov.io/gh/icaoberg/python-bst/branch/master/graph/badge.svg)
[![Build Status](https://travis-ci.org/icaoberg/python-bst.svg?branch=master)](https://travis-ci.org/icaoberg/python-bst)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-bst)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-bst.svg)](https://github.com/icaoberg/python-bst/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

This repo contains a very simple naive implementation of a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree).

The purpose of this repo is to serve as an example on how to create a `.travis.yml` for [Travis CI](https://travis-ci.org/).

## Example

![BST](https://github.com/icaoberg/python-bst/blob/master/images/bst.png?raw=true)

```
from BST import BST
import random
import graphviz
import os

random.seed( 12345 )

number_of_nodes = 10
tree = BST()
tree.random( number_of_nodes )
tree.tofigure().render('./images/bst', format='png')
```

## Disclaimer
This implementation is based on a homework I did for 15213 Advanced Data Structures and Algorithms in Java many years ago.

As you can tell from the plot below, it is slow

![Insertions](https://github.com/icaoberg/python-bst/blob/master/images/insertion.png?raw=true)

The plot above is showing average time (50 times for each run) from creating a BST.

---
[![CBD](http://www.cbd.cmu.edu/wp-content/uploads/2017/07/wordpress-default.png)](http://www.cbd.cmu.edu)

Copyleft © 2018 [icaoberg](http://www.andrew.cmu.edu/~icaoberg) at the [Computational Biology Department](http://www.cbd.cmu.edu) in [Carnegie Mellon University](http://www.cmu.edu)
