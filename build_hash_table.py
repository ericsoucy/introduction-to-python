# in this lab, you will build a hash table from scratch.
# A hash table is a data structure that stores key-value pairs.
# A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.
# For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key.
# The hash value will then be used as the actual key to store the associated value.
# The same hash value would also be used to retrieve and delete the value associated with the key.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

class HashTable:
    def __init__(self):
        # The main storage for our hashed data
        self.collection = {}

    def hash(self, string):
        hashed_value = 0
        for char in string:
            # ord() gets the Unicode integer for a character
            hashed_value += ord(char)
        return hashed_value
    def add(self, key, value):
        hash_key = self.hash(key)
        # If the hash isn't in our collection yet, create a new bucket
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        # Store the key-value pair in the bucket
        self.collection[hash_key][key] = value
    def lookup(self, key):
        hash_key = self.hash(key)
        # Check if the bucket exists and if the key is inside it
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None
    def remove(self, key):
        hash_key = self.hash(key)
        # Only attempt removal if the key actually exists
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            # Optional cleanup: if the bucket is now empty, remove the bucket itself
            if not self.collection[hash_key]:
                del self.collection[hash_key]

table = HashTable()
print(table.hash('golf'))  # Should return 424
table.add('golf', 'sport')
print(table.collection)# {424: {'golf': 'sport'}}
table.add('dear', 'friend')
print((table.collection))  # {424: {'golf': 'sport'}, 412: {'dear': 'friend'}}
table.add('read', 'book')
print((table.collection))  # {424: {'golf': 'sport'}, 412: {'dear': 'friend', 'read': 'book'}}
print(table.lookup('golf'))  # Should return 'sport'
table.add('rose', 'flower')
print((table.collection))  # {424: {'golf': 'sport'}, 412: {'dear': 'friend', 'read': 'book'}, 441: {'rose': 'flower'}}
table.remove('golf')
print(table.lookup('golf'))  # Should return None
print((table.collection))
table.add('fcc','chemical')
table.add('cfc','chemical')
print((table.collection)) # {412: {'dear': 'friend', 'read': 'book'}, 441: {'rose': 'flower'}, 300: {'fcc': 'chemical', 'cfc': 'chemical'}}