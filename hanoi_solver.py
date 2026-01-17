def hanoi_solver(n):
    # Initialize the rods: Rod A has disks, B and C are empty
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    # List to store the string representation of rods after each move
    history = []

    def get_state_string():
        # Returns a string like "[3, 2, 1] [] []"
        return f"{rods['A']} {rods['B']} {rods['C']}"

    # Record the starting arrangement
    history.append(get_state_string())

    def move_disks(n, source, target, auxiliary):
        if n > 0:
            # Move n-1 disks from source to auxiliary
            move_disks(n - 1, source, auxiliary, target)

            # Move the actual disk
            disk = rods[source].pop()
            rods[target].append(disk)

            # Record the state after the move
            history.append(get_state_string())

            # Move n-1 disks from auxiliary to target
            move_disks(n - 1, auxiliary, target, source)

    # Start the recursion: Move n disks from A to C using B as helper
    move_disks(n, 'A', 'C', 'B')

    # Join all states with newlines into a single string
    return "\n".join(history)

print(hanoi_solver(3)) # should return "[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]"
print("-----------")
print(hanoi_solver(2)) # should return "[2, 1] [] []\n[2] [1] []\n[] [1] [2]\n [] [] [2, 1]
print("-----------")
print(hanoi_solver(4)) # should return [4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1]
print("-----------")
print(hanoi_solver(5)) # "[5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1]"