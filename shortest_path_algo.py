INF = float('inf')
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1
        for node_no in range(n):
            # Check if node is unvisited and has a distance smaller than current minimum
            if not visited[node_no] and distances[node_no] < min_distance:
                # Update the minimum distance and record the node index
                min_distance = distances[node_no]
                current = node_no
        # If no unvisited node was found with a distance less than INF, exit the loop
        if current == -1:
            break
        visited[current] = True
        for node_no in range(n):
            distance = matrix[current][node_no]
            # Check if an edge exists and the neighbor isn't already finalized
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                # Check if this new path is actually a shortcut
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    # Update the path to node_no by appending it to the path of 'current'
                    paths[node_no] = paths[current] + [node_no]
    # Define which targets to report results for
    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        # Skip the starting node and unreachable nodes
        if node_no == start_node or distances[node_no] == INF:
            continue
        # Create a generator to convert node integers to strings
        string_path = (str(n) for n in paths[node_no])
        # Join the strings with arrows to show the route
        path = ' -> '.join(string_path)
        # Display the final results for this specific destination
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')
        # Return the final computed data
    return distances, paths

# Calling the function with a start node of 0 and a target node of 5
shortest_path(adj_matrix, 0, 5)
