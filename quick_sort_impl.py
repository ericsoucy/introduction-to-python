def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([20, 3, 14, 1, 5])) #should return [1, 3, 5, 14, 20]
print(quick_sort([83, 4, 24, 2])) #should return [2, 4, 24, 83]
print(quick_sort([4, 42, 16, 23, 15, 8])) #should return [4, 8, 15, 16, 23, 42]
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])) #should return [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]