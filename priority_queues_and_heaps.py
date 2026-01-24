# A priority queue is an abstract data type (ADT) that works similarly to a queue or stack, but with one key difference.
# In a priority queue, each element has a "priority" associated with it.
# Elements with higher priority are served before elements with lower priority.

# A heap is a tree data structure with a very specific property called the heap property.
# This property determines the relationship between each node and its children, based on the type of heap.

# There are two primary types of heaps:
# Max-heap
# Min-heap
# In a max-heap, the value of each node is greater than or equal to the value of its children.
# In a min-heap, the value of each node is less than or equal to the value of its children.

# Python has a heapq built-in module that you can use to work with an implementation of a min-heap.

import heapq
# Example of using heapq to create a min-heap priority queue
my_heap = []
heapq.heappush(my_heap, 9)
heapq.heappop(my_heap)

heapq.heappushpop(my_heap, 15)

heapq.heapify(my_heap)

my_heap = []
# if we want to sort them by their "priority" instead?
# You could do this by storing tuples with this structure: (priority, element)
heapq.heappush(my_heap, (3, "A"))
heapq.heappush(my_heap, (2, "B"))
heapq.heappush(my_heap, (1, "C"))

# The average and worst case time complexities for inserting and 
# extracting the minimum or maximum value from a heap (depending on the type of heap) are logarithmic, O(log n),
# because the number of swaps required is usually proportional to the height of the heap, which is log(n).

# The average and worst case time complexity for the "peek" operation is constant time, O(1). 
# Peeking involves getting the minimum or maximum value (depending on the type of heap) without removing it.

# The "heapify" operation, where the heap is built from an unsorted list, has linear time complexity, O(n), in the average and worst cases.

# The space complexity of the heap is linear, O(n)

# What is the primary characteristic that distinguishes a priority queue from a standard queue or stack?
# Each element has an associated priority, and elements with higher priority are served first.
# It retrieves elements based on an assigned priority.

# Which of the following is a common real-world application where a priority queue would be helpful?
# Scheduling tasks in an operating system where some tasks are more urgent.

# What is the main reason why heaps are typically implemented as arrays in practice, despite being conceptualized as trees?
# They provide efficient memory usage and cache performance.
# Arrays simplify the logic for accessing parent and child nodes using mathematical formulas.