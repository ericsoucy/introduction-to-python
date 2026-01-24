# Adjacency Matrices and Lists Representation of Graphs
# An adjacency matrix is a two-dimensional list in which the rows and columns represent the graph's vertices.
# The values in the matrix represent the edges or connections between the nodes.

# For example, if you have a matrix stored in a variable named matrix, the value stored at matrix[i][j], where i is the row and j is the column, represents the edge or connection between nodes i and node j.
# The values may have different meanings depending on whether the graph is weighted or unweighted:
# If the graph is unweighted, a value of 1 means that there is an edge connecting these nodes, while a value of 0 means there is no edge between them.
# If the graph is weighted, the value would represent the weight of the edge that connects the nodes.

# One of the great advantages of using an adjacency matrix is that checking if there is an edge between two nodes takes constant time O(1). This is because the program only needs to find that particular value in the 2D list.
# Adjacency matrices have a large quadratic space requirement O(V²), where V is the number of nodes in the graph.

# Adjacency matrices are also inefficient for finding a node's neighbors because the program has to iterate over the entire row or column to find the 0s and 1s that represent the edges.
# In the worst case, this process can take O(V) time, where V is the number of nodes in the graph.

adjacency_matrix = [
#    A  B  C  D
    [0, 1, 1, 1],  # A The neighbors of A are B, C, and D
    [1, 0, 0, 1],  # B The neighbors of B are A and D
    [1, 0, 0, 0],  # C The only neighbor of C is A
    [1, 1, 0, 0]   # D The neighbors of D are A and B
]
# An adjacency list is a collection of lists or arrays that represent the neighbors of each node in the graph.
# An adjacency list is an array or dictionary that stores all the neighbors of each node.

# There are two ways to implement adjacency lists:
# As an array, where each index represents a node and the list stored at that index contains its neighbors.
# As a dictionary, where each key represents a node and the value associated to that key (a list) contains its neighbors.

# Adjacency lists are more efficient than adjacency matrices in terms of space requirements.
# They have a O(V + E) space complexity, where V is the number of vertices (nodes) and E is the number of edges.
# Adjacency lists are less efficient than adjacency matrices for determining if there is an edge between two nodes.

adjacency_list = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['A', 'B']
}

adjacency_list = [
    ['B', 'C', 'D'],  # Neighbors of A (index 0)
    ['A', 'D'],       # Neighbors of B (index 1)
    ['A'],            # Neighbors of C (index 2)
    ['A', 'B']        # Neighbors of D (index 3)
]

# Notice that even if this 2D list may look similar to the adjacency matrix, they are quite different.
# The adjacency matrix stores 0s, 1s, or other values that represent the edges or weights of the edges in the graph.
# The adjacency list stores the actual list of all the neighbors of each node.

# For which of the following scenarios is an adjacency matrix the most efficient choice for representing a graph?
# A dense graph where every node is connected to most other nodes.

# When would it be more efficient to use an adjacency list over an adjacency matrix?
# When the graph is sparse, with a high number of vertices and a low number of edges.

# Which of the following operations is faster in an adjacency matrix compared to an adjacency list?
# Checking if a direct edge exists between two specific nodes.