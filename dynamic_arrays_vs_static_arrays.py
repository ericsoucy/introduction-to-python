# Static arrays have a fixed size. They store elements in adjacent memory locations.
# The size of a static array is determined when the array is initialized. Once that specific block of memory is allocated, it's fixed, and cannot be changed while the program is running. This is a key characteristic of static arrays.
# Storing elements in adjacent memory locations makes the data retrieval process more efficient because the program can store the location of the first element and then use indices to make simple calculations and find the other elements in memory.
# Thanks to this, accessing the values of a static array takes constant time O(1), which is very efficient.

# You can use a static array when you know the number of elements that will be stored in advance.
# It's also helpful when the values will be accessed very frequently, since the access operation is very efficient.

# Trying to increase the size of a static array would involve creating a new array and copying all the elements from the old array to a new one, which is inefficient. In that case, a dynamic array would be much better because it handles this process automatically.
# Python does not include traditional static arrays as built-in data structures.

# Arrays in Python are dynamic, so let's take a look at those.
# Dynamic arrays are more flexible because they can grow or shrink automatically while the program is running.
# They work through an automatic resizing mechanism that copies the elements into a new array when the original array is full. The process is done efficiently because the size of the new array is chosen in an efficient way that makes these computationally expensive operations less frequent.
# Accessing the elements of a dynamic array takes constant time O(1), so this operation is very efficient.
# Inserting an element in the middle of the array takes linear time O(n) because the elements after it need to be relocated.
# Inserting an element at the end of the array takes constant time O(1) if there is still space available in the dynamic array, but if the array is full and needs resizing, this operation has a O(n) complexity.
# You should use dynamic arrays when you don't know in advance the number of values that you will need to store in the array. They are also helpful when you will be frequently inserting and deleting elements.
# Python's built-in list data structure works as a dynamic array. You can create a list by writing the elements within square brackets, separated by commas.

numbers = [3, 4, 5, 6]

# indices start from 0 for the first element and are incremented by 1 for each subsequent element:
numbers[0]  # 3
numbers[1]  # 4
numbers[2]  # 5
numbers[3]  # 6

#update a value, you just need to reassign it
numbers[2] = 16

# append elements to the list with the .append() method:
numbers.append(7)

# insert elements at a specific index with the .insert() method, passing the index as the first argument and the element itself as the second argument.
numbers.insert(3, 15)

#You can remove an element at a specific index with the .pop() method:
numbers.pop(2)

# What is the main difference in size between a static array and a dynamic array?
# Static arrays have a fixed size, while dynamic arrays can change size during runtime.

# If you need to add more elements to a static array that is already full, what is the typical process involved?
# You must create a new, larger array and copy all existing elements to it.

# In which scenario would a static array typically be a more suitable choice than a dynamic array?
# When the data size is fixed and known at the time the program is written.