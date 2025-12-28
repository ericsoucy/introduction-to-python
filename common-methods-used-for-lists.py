numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]

numbers = [1, 2, 3, 4, 5]
print(numbers.pop(1)) # The number 2 is returned

numbers = [1, 2, 3, 4, 5]
print(numbers.pop()) # The number 5 is returned

numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []

# sort() method. This method is used to sort the elements in place. H
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

# the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# the reverse() method. This method, will reverse a list of elements in place
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

# index method. This is used to find the first index where an element can be found in a list
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # 1

"""
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""