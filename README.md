# Generation of combinatorial objects described by a grammar

## Introduction

This project's goal is to implement combinatorial methods to generate objects via non-contextual grammars.

For example the set of binary trees can be described by the following non-contextual grammar,

    Tree -> Node | Leaf
    Node ->  Tree . Tree

The `.` (dot) operation is the concatenation of 2 elements (also called product), however in order to generate a tree we don't want to concatenate strings
but rather have a constructor BinaryTree(a,b) that takes the two elements and returns a tree (recursive definition of a binary tree). This project
allow us to do that by specifying a bijection for the dot operation.


## Requirements

The requirements are the following,

  * Up to date Python 3
  * Jupyter notebook in order to run the .ipynb files

## Structure

  * `rules.py` contains the combinatorials methods used to generate the objects
  * `examplesgrammars.py` contains grammars written using our grammar classes
  * `tests.py` contains functions used to test the project. We can run it with `python tests.py`
  * `demo.ipynb` is a demonstration notebook used to expose the main features of the project (in french)

## Combinatorials methods

In the following `self` denotes an `AbstractRule` object,

  * self.count(n): returns the number of objects of weight n in the grammar
  * self.list(n): returns the objects of weight n in the grammar as a list
  * self.unrank(n, rank): return the object of index rank (0-based indexing) in the elements list of weight n
  * self.rank(obj): return the rank of obj in the list of elements that are the same size of obj, this needs two additional functions that has to be implemented by the grammar in order to work.

