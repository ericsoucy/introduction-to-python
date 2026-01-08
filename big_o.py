# O(1) is known as "Constant Time Complexity". When an algorithm has constant time complexity,
# it takes the same amount of time to run, regardless of input size.
# For example, checking if a number is even or odd will always take the same amount of time, regardless of the number itself.
def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# O(log n) is known as "Logarithmic Time Complexity".
# This means that the time required by the algorithm increases slowly as the input size grows.
# This is common in problems in which the size of the problem is repeatedly reduced by a constant fraction
# For example, a popular search algorithm called Binary Search has O(log n) worst-case time complexity.
# This is because it eliminates half of the remaining elements in each comparison, which makes it more efficient overall.

# O(n) is known as "Linear Time Complexity". The running time of algorithms with this time complexity increases proportionally to the input size.

# For example, a for loop that iterates over all the elements of a list will perform more iterations as the number of list elements increases.
# If the list is doubled in size, the number of operations will approximately double as well.
grades = [85, 90, 78, 92, 88]
for grade in grades:  # grades is a list.
    print(grade)

# O(n log n) is known as "Log-Linear Time Complexity".
# This is a common time complexity of efficient sorting algorithms, like Merge Sort and Quick Sort.

# O(n²) is known as "Quadratic Time Complexity".
# The running time of these algorithms increases quadratically relative to the input size, which is generally not efficient for real-world problems.
# Nested loops are a common example of quadratic time complexity.
# The inner loop will perform n iterations for each one of the n iterations of the outer loop, resulting in n squared iterations.
n = 5
for i in range(n):
    for j in range(n):
        print("Hello, World!")

# Other time complexities include "Exponential Time Complexity", denoted as O(2^n), and "Factorial Time Complexity", denoted as O(n!).
# Both are inefficient for real-world scenarios.