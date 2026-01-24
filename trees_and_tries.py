# A tree is a specific type of graph.
# For a graph to be classified as a tree, it must:
# Have no loops or cycles (paths where the start and end nodes are the same).
# Be connected (every node can be reached from every other node).

# The root node is the very top of a tree. It's the only node in the tree without a parent node.
# This is the node where you will start traversing the entire data structure,
# usually with algorithms like breadth-first search (BFS) or depth-first search (DFS).

# A parent node is a node that is immediately connected to other nodes below it
# A child node is a node that is immediately connected to a node above it

# A leaf is a node that has no child nodes

# Tree nodes also have important properties:
# Depth: the length of the path from the root to that node.
# Height: the length of the path from that node down to a leaf.
# Degree: the number of child nodes each node has.
# The height of a tree is the height of its root node.

# Binary Trees and Binary Search Trees
# A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
# A binary search tree is a more specific version of a binary tree, with a very particular ordering property.
# The ordering property of binary search trees (BST) establishes that for every node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value.

# A balanced tree is a tree in which the heights of the left and right subtrees of any node are very similar to make sure that operations remain efficient.

# Tries
# Tries are tree data structures used to store a set of strings.
# A trie, also known as a prefix tree, is a specialized tree data structure used to store a dynamic set or associative array where the keys are usually strings.
# The worst-case time complexity for the search operation is O(L), where L is the length of the string that you are looking for.
# Each node in a trie represents a single character of a string.
# This efficiency makes tries perfect for implementing features like autocomplete and spell checkers.
# However, tries are not efficient for all sets of strings. They can be inefficient if the set of strings has many unique characters. This would require storing many unique characters as individual nodes. These nodes would have to be traversed to find the words, which would not be optimal.

# Which of the following statements about a Binary Search Tree (BST) is always true?
# All values in the left subtree of a node are less than the node's value.

# For which of the following tasks is a trie, or prefix tree most effective?
# Implementing an autocomplete feature for a search bar.

# What is the fundamental difference between a general tree and a Binary Tree?
# A Binary Tree restricts each node to have at most two children, while a general tree allows nodes to have any number of children.