# A tuple is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types
# Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.
# When might you use a tuple over a list?
#If you need a dynamic collection of elements where you can add, remove and update elements, then you should use a list. If you know that you are working with a fixed and immutable collection of data, then you should use a tuple.

"""
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'


Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""

developer = ('Alice', 34, 'Rust Developer')
print(developer[1]) # 34

numbers = (1, 2, 3, 4, 5)
print(numbers[-2]) # 4

# Another way to create a tuple is by using the tuple() constructor
developer = 'Jessica'
print(tuple(developer)) # ('J', 'e', 's', 's', 'i', 'c', 'a')

programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages) # False

# unpack items from a tuple
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# slice operator on a tuple to extract a portion of it
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3]) # ('pie', 'cookies')