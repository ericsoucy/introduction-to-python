# A map is an ADT that manages collections of key-value pairs and their operations in a very specific and efficient way.

# In a map, every value is associated with a specific key.
# One of the key characteristics of maps is that every key must be unique. This uniqueness allows for direct lookups, which makes the process of retrieving information much more efficient.
# Only keys must be unique, values can be repeated.
# The map Abstract Data Type also defines important operations, such as inserting key-value pairs, getting the value associated with a key, updating the value associated with a key, removing a key-value pair, and checking if a key exists in the map.
# It doesn't actually specify how these operations should be performed, it just lists them as part of the available operations of the data type.

# A hash map, also known as a hash table, is a concrete implementation of the map Abstract Data Type.
# Hash maps use a technique called "hashing" to perform common operations very efficiently.
# Hashing essentially works by generating a hash value for each element using a hash function.
# The hash value is generated based on the key of the key-value pair and it's used to calculate an index in an underlying array, the actual data structure where the key-value pairs are stored.

# What happens if two keys result in the same index?
# Hash maps solve these collisions with clever strategies.
# One option is to use the "chaining" strategy, where each array index points to a linked list (another data structure), where all the elements with the same index are stored.
# Another strategy is to use "open addressing", which involves searching for the next available index in the array based on a predefined search sequence.

# The average case time complexity of hash maps is "Constant Time" O(1) for inserting, retrieving, and deleting key-value pairs.
# The worst case time complexity of these operations is Linear Time O(n), which occurs when there are many hash collisions, so the collision resolution strategy has to be applied multiple times.

# The space complexity of inserting into a hash map is constant O(1) on the average case, a constant amount of memory to store the new pair. However, in the worst case, it can have linear space complexity O(n) due to a resizing operation of the underlying array. In general, removing an element has a constant space complexity O(1).
# This turns the hash table into something similar to a linear data structure where n elements have to be scanned to find the target key. However, this is relatively rare if the hash map is implemented properly.

# Python's dictionaries are implemented as hash maps behind the scenes.
# To create a Python dictionary, you just need to write the key-value pairs within curly brackets and separate them with a comma. Each key should be separated from its corresponding value with a colon.

my_dictionary = {
  "A": 1,
  "B": 2, 
  "C": 3
}
my_dictionary = dict(A="1", B="2", C="3")

my_dictionary["A"]  # 1 Get value associated with key "A"
my_dictionary["A"] = 4 # Update value associated with key "A"

del my_dictionary["A"]  # Remove key-value pair with key "A"
"A" in my_dictionary  # Check if key "A" exists in the dictionary
my_dictionary.keys()
my_dictionary.values()
my_dictionary.items()

# Sets
# Sets are unordered collections of unique elements.
# Sets are unordered. The elements of a set are not stored in any specific order, so you cannot access them through indices.
# Sets only contain unique elements. If you try to add the same value twice, only one copy of the value will be kept.
# They are analogous to sets in mathematics and they implement the same set operations, like intersection, union, and difference.
# One of the main advantages of sets is that they guarantee that the elements will be unique (no duplicates). This is why they are often used to remove duplicates from lists and other data structures.

# The average case time complexity of adding, removing, getting the length of the set, 
#  and checking if an element is in the set is "Constant Time" O(1), which is very efficient.
# Since sets are implemented as hash tables, the worst case time complexity of adding, removing, 
# and checking membership is "Linear Time" O(n). 
# This may occur when there are multiple hash collisions, transforming the hash table into something similar to
# a linear data structure, where n scans are required to find the key.

# In terms of space complexity, in the average case, inserting an element would have constant complexity O(1),
# with a new unique element requiring a constant amount of memory. 
# However, in the worst case, there could be a resizing operation of the underlying array, 
# which could take linear space complexity O(n). In general, removing an element would take constant space complexity O(1).

# Python has a built-in set data structure that you use to work with sets in your programs.
# Behind the scenes, Python sets are implemented using a hash table where only the keys are stored, without any associated values.
# Sets can only store objects of immutable data types because their hash values always remain the same. In contrast, the hash values of mutable objects can change when they are mutated. That's why they cannot be part of sets. If the hash value of an object stored in the set changes,
# the program would not be able to find it anymore.

# To define a set in Python, you just need to surround the elements with curly brackets and separate them with commas:
numbers = {1, 2, 3, 4}
numbers = set()
numbers.add(5)  # Add element 5 to the set
numbers.remove(2)  # Remove element 2 from the set

# The .pop() method returns an arbitrary element from the set, while the .clear() method removes all elements from the set.

# test if an element is in a set with the in operator:
5 in numbers  # True

# Python also support set operations, including union, difference, symmetric difference, and intersection, which you can perform with these methods:
set_a = {1, 2, 3, 4}
set_b = {2, 3, 4, 5, 6}

set_a.union(set_b)
set_a.intersection(set_b)
set_a.symmetric_difference(set_b)
set_a.difference(set_b)
set_a | set_b
set_a & set_b
set_a ^ set_b
set_a - set_b

# The average case time complexity for adding, removing, and testing membership is "Constant Time" O(1).
# The worst case time complexity for these operations is "Linear Time" O(n) because of the hash map's worst case collision scenario.

# You can also check if a set is a subset or superset of another one:
set_a.issubset(set_b)
set_a.issuperset(set_b)

# What is the fundamental difference in the type of data stored by a hash map (or map) compared to a set?
# Hash maps store unique key-value pairs, while Sets store unique individual elements.

# What is the main mechanism that allows hash maps and Sets to achieve average-case O(1) (constant time) performance for operations like insertion and lookup?
# They use a hash function to compute a direct memory location for elements.

# In the context of hash maps and sets, what is a "hash collision"?
# When two different keys or elements produce the same hash value.