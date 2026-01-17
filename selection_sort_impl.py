def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([33, 1, 89, 2, 67, 245])) # should return [1, 2, 33, 67, 89, 245]
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3])) # should return [3, 5, 12, 15, 16, 23, 72, 99, 567]
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # should return [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]
