def adjacency_list_to_matrix(adj_list):
    # Determine the number of nodes (assuming nodes are 0 to n-1)
    n = len(adj_list)

    # Initialize an n x n matrix filled with 0s
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix based on the adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row for visibility
    for row in matrix:
        print(row)

    return matrix
print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}))
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [1, 1, 0, 1]
# [0, 1, 1, 0]
# [[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
