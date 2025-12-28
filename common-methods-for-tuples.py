programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust')) # 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('JavaScript')) # 0

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.index('Java')) # 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3)) # 5

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # 2

# sorted() function can be used on any iterable including tuples
# The sorted() function will always create a new list of the sorted values.
# This differs from the sort() method which sorts the elements of a list in place and does not return a new list.

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers)) # [2, 3, 7, 13, 18, 45, 67, 78]

# customize the sorting behavior for an iterable, you can use the optional reverse and key arguments. 
# Here is an example of using key argument to sort items in a tuple by length:
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# to create a new list of values in reverse order, then you can use the reverse argument 
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']