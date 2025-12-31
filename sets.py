# One of the core characteristics of sets is that they don't store duplicate values.
# If you try to add a duplicate value to a set, only one of them will be stored.
# Sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use indices or keys to access them.
# They can only contain values of immutable data types like numbers, strings, and tuples. 
# And they support mathematical set operations, including union, intersection, difference, and symmetric difference.

my_set = {1, 2, 3, 4, 5}
set() # Set
{}    # Dictionary
print(my_set) # {1, 2, 3, 4, 5, 6}
# add an element to a set with the .add() method, and pass in the new element as argument:
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}
# if you try to add an element that is already in the set, only one will be kept
my_set.add(5) # duplicate value
print(my_set) # {1, 2, 3, 4, 5, 6}

# use the .remove() method or the .discard() method, and pass in the element that you want to remove as argument.
my_set.remove(4)
#my_set.discard(4) # no error if element not found
print(my_set) # {1, 2, 3, 5, 6}

# The .clear() method removes all the elements from the set
my_set.clear()
print(my_set) # set()

# .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common
print(my_set.isdisjoint(your_set)) # False

# The union operator | returns a new set with all the elements from both sets:
combined_set = my_set | your_set
print(combined_set) # {1, 2, 3, 4, 5, 6}

# The intersection operator & returns a new set with only the elements that the sets have in common:
common_elements = my_set & your_set
print(common_elements) # {2, 3, 4}

# The difference operator - returns a new set with the elements of the first set that are not in the other sets
unique_to_my_set = my_set - your_set
print(unique_to_my_set) # {1, 5}

# The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both
symmetric_difference = my_set ^ your_set
print(symmetric_difference) # {1, 5, 6}

# Each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it. These operators automatically assign the resulting set to the first set in the expression:
my_set -= your_set
print(my_set) # {1, 5}

# You can check if an element is in a set or not with the in operator
print(5 in my_set)
