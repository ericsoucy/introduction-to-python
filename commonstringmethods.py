print("upper(): Returns a new string with all characters converted to uppercase.")
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

print("lower(): Returns a new string with all characters converted to lowercase.")
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

print("strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.")
str_with_spaces = '   hello world   '
trimmed_my_str  = str_with_spaces.strip()
print(trimmed_my_str)  # "hello world"

print("replace(old, new): Returns a new string with all occurrences of old replaced by new.")
replaced_my_str = my_str.replace('world', 'Python')
print(replaced_my_str)  # "hello Python"

print("split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.")
split_my_str = my_str.split(' ')
print(split_my_str)  # ['hello', 'world']

print("join(iterable): Joins the elements of an iterable (like a list or tuple) into a single string, with the string as the separator.")
my_list = ['hello', 'world']
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

print("startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.")
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

print("endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.")
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

print("count(substring): Returns the number of times a substring appears in a string.")
o_count = my_str.count('o')
print(o_count)  # 2

print("capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.")
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

print("isupper(): Returns True if all letters in the string are uppercase and False if not.")
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

print("islower(): Returns True if all letters in the string are lowercase and False if not.")
is_all_lower = my_str.islower()
print(is_all_lower)  # True

print("title(): Returns a new string with the first letter of each word capitalized.")
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World