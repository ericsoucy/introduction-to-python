even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# refactored using list comprehension
# In this refactored example, the even_numbers list is created using a single line of code.
# The list comprehension loops through numbers from 0 to 20, and includes only those that are divisible by 2.
# This approach is more compact and eliminates the need for a separate loop and conditional block.
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

# In this example, we have a list of numbers and want to create a new list of tuples indicating which numbers are even or odd.
# In the first part of the list comprehension, we use an if statement to check if the number is evenly divisible by 2.
# If so, then the result is a tuple of that number followed by the word Even.
# Otherwise, the result is a tuple with the number followed by the word Odd.
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# Another way to create a list starting from an existing iterable is the filter() function.
# Here is an example of creating a new list of just words longer than four characters
# The filter() function is used to select elements from an iterable that meet a specific condition.
# The filter() function accepts a function and an iterable for its arguments.
# In this example, we are passing in an is_long_word function into the filter() function to check if the current word count is greater than 4.
# All words that have a character count greater than 4 are added into a new list and assigned to the long_words variable.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# Another function to be aware of is the map() function, which takes an iterable and applies a function to each of its elements.
# Here is an example of using the map() function to convert a list of temperatures from Celsius to Fahrenheit
# map() accepts a function and an iterable for its arguments.
# The to_fahrenheit function takes a temperature and converts it from Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# The sum() function. This function is used to get the sum from an iterable like a list or tuple.
# Here is an example of using the sum() function
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

# You can also pass in an optional start argument which sets the initial value for the summation. 
# Here is an updated example using the start argument as a positional argument:
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60