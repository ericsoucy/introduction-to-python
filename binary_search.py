# What Is Binary Search and How Does It Differ From Linear Search?
# Binary search is an efficient algorithm for finding an item from a sorted list of items.
# The basic idea behind binary search is to divide the list in half repeatedly until the target item is found or the search space is empty.

# The time complexity of linear search is O(n) because the time it takes to search through the list grows linearly with the size of the list.
# The space complexity of linear search is O(1) because it doesn't require any additional space to search through the list.
# Binary search is a more efficient algorithm for searching through a large list of items. The condition here is that the list must be sorted in ascending order.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
# We start by identifying a low and high index. This represents the range of the list we are searching through.
# We then check the condition of low being less than or equal to high. If low is greater than high, we have searched through the entire list and the target value is not found. In that case we stop the search and return -1.
# If the low index is less than or equal to the high index, we calculate the middle index of the list, mid. We then check if the target value is at the middle index. If it is, we return the middle index.
# Otherwise, we check if the value at the midpoint is less than the target. If it is, we update the low index to be the middle index plus one. This means we will search the right half of the list.
# Lastly, if none of the other conditions are True, we update the high index to be the middle index minus one. This means we will search the left half of the list.
# We continue to repeat this process until we find the target or determine that the target is not in the list.

# The time complexity of binary search is O(log n) because the time it takes to search through the list grows logarithmically with the size of the list.
# The space complexity of binary search is O(1) because it doesn't require any additional space to search through the list.

# What is the main difference between linear search and binary search?
# Binary search requires a sorted list, while linear search does not.

# What is the time complexity of linear search?
# O(n)

# In binary search, what happens if the target value is not found in the list?
# The algorithm returns -1.
