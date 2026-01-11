# What Is Divide and Conquer, and How Does Merge Sort Work?
# The divide and conquer paradigm in computer science is a technique for recursively breaking down problems
# into smaller sub problems.
# One of the key aspects of this technique is recursion, which happens when a function calls itself repeatedly
# until a base case is reached.
# In this lesson, we will take a look at the merge sort algorithm to better understand how the divide and conquer technique works.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# The time complexity for merge sort would be O(n log n) , divided in half (log n) and then merged together (O(n))
# has a space complexity of O(n)

# What is the divide and conquer paradigm in computer science?
# A technique for recursively breaking down problems into smaller sub problems.

# What is the time complexity for the merge sort algorithm?
# O(n log n)

# What is the space complexity for the merge sort algorithm?
# O(n)