# In this example, we have a list of numbers and want to create a new list of even numbers.
# So we pass in a lambda function as one of the arguments to the filter() function to get a new list containing the numbers 2 and 4.
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]