def dfs(matrix, start_node):
    # Number of nodes in the graph
    n = len(matrix)

    # Track visited nodes to avoid infinite loops in undirected graphs
    visited = []
    # Use a stack to manage the DFS process (LIFO)
    stack = [start_node]

    while stack:
        # Pop the last node added (going deep)
        current_node = stack.pop()

        if current_node not in visited:
            visited.append(current_node)

            # Check all possible neighbors in the matrix row
            # We iterate backwards (range(n-1, -1, -1)) to maintain
            # a consistent order if you want to visit smaller indices first
            for neighbor in range(n - 1, -1, -1):
                if matrix[current_node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited
print("results:")
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)) # should return a list with 1, 2, 3, and 0.
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3)) # should return a list with 1, 2, 3, and 0.
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3)) # should return [3]
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3)) # should return a list with 3 and 2
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0)) # should return a list with 0 and 1
