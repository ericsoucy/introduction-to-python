# Graphs are data structures used to represent the connections or relationships between objects or entities.
# They consist of nodes (also called vertices) and edges (connections between nodes).
# Nodes, also known as vertices, represent the objects or entities that are part of the network modeled by the graph
# Edges represent the connections or relationships between the nodes in the graph.

# Graphs can be directed or undirected, weighted or unweighted, and can be used to model various real-world systems such as social networks, transportation networks, and communication networks.

# Undirected graphs are graphs where the edges don't have a specific direction
# In undirected graphs, the edges represent a bidirectional relationship between nodes, meaning that if there is an edge between node A and node B, you can traverse from A to B and from B to A without any restrictions.

# Directed graphs, on the other hand, have edges with a specific direction
# In directed graphs, the edges represent a unidirectional relationship between nodes, meaning that if there is an edge from node A to node B, you can only traverse from A to B, but not from B to A unless there is a separate edge in the opposite direction.

# vertex label graph 
# A graph where each vertex (node) is assigned a unique label or identifier.

# cyclic graph
# A graph that contains at least one cycle, which is a path that starts and ends at the same vertex without repeating any edges or vertices (except for the starting/ending vertex).
# In a cyclic graph, you can traverse a sequence of edges and return to the starting vertex

# edge label graph
# A graph where each edge is assigned a unique label or identifier.

# weighted graph
# A graph where each edge has a numerical value (weight) associated with it, representing the cost, distance, or capacity of that edge.

# unweighted graph
# A graph where all edges are considered equal, without any specific weights or values assigned to them.

# Directed Acyclic Graph (DAG)
# A directed graph that does not contain any cycles, meaning there is no way to start at a vertex and follow a sequence of directed edges to return to the same vertex.
# DAGs are often used to represent hierarchical structures or dependencies, such as task scheduling or version control systems.

# disconnected graph
# A graph in which there are at least two vertices that are not connected by a path.
# In a disconnected graph, it is not possible to reach certain vertices from others, resulting in multiple isolated components within the graph.

# What is a graph in computer science?
# A data structure used to represent relationships between objects.

#What are the two main components of a graph?
# Nodes (vertices) and edges (connections between nodes).

# What is a directed graph?
# A graph where edges have a direction.