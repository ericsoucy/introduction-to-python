def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    while low <= high:
    # Calculate the middle index
        mid = (low + high) // 2
        # Access the element at the middle index
        value_at_middle = search_list[mid]
        # Track the value we are currently inspecting
        path_to_target.append(value_at_middle)
        # Check if we found the target
        if value == value_at_middle:
            # Return both the path and the formatted message
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle:
            # Shift the bottom boundary up
            low = mid + 1
        else:
            # If value is smaller than value_at_middle
            high = mid - 1
   # Updated return statement for when the search fails
    return [], "Value not found"
# Testing a successful search (Target 3 is at the middle of this list)
print(binary_search([1, 2, 3, 4, 5], 3))

# Testing a search that would currently fail or loop (Target 4 is not at the initial middle)
print(binary_search([1, 2, 3, 4, 5, 9], 4))
# Testing with a value that does not exist in the list
print(binary_search([1, 3, 5, 9, 14, 22], 10))