def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def backtrack(row, current_state):
        # Base case: All queens placed
        if row == n:
            solutions.append(list(current_state))
            return

        for col in range(n):
            # Check if placing a queen at (row, col) is valid
            if is_valid(row, col, current_state):
                current_state.append(col)
                backtrack(row + 1, current_state)
                # Backtrack: remove the queen to try the next column
                current_state.pop()

    def is_valid(row, col, state):
        for r, c in enumerate(state):
            # Check column and diagonals
            # Diagonal check: row difference == column difference
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    backtrack(0, [])
    return solutions

print(dfs_n_queens(1)) # should return [[0]].
print(dfs_n_queens(2)) # should return []
print(dfs_n_queens(3)) # should return []
print(dfs_n_queens(4)) # [[1, 3, 0, 2], [2, 0, 3, 1]]
print(dfs_n_queens(5)) # should return [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]
print(len(dfs_n_queens(5))) #  should be 10
print(len(dfs_n_queens(8))) #  should be 92