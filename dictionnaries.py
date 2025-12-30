# In Python, dictionaries are built-in data structures that store collections of key-value pairs.
# With Python dictionaries, you use a key to find its corresponding value.
# You should use dictionaries when you need to associate values to unique keys.
# This is helpful when you need to find a value fast based on the key, and when you need to represent structured data.
# Each key is associated with a value, so you can use the key to access that value.
# After each value, except the last one, there's a comma to separate the different key-value pairs.
# Keys must be unique in the dictionary, and they must be an immutable data type.
# However, the values can be repeated, and they can be of any data type.

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# using dict constructor
# pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

print (pizza['name'])  # 'Margherita Pizza'
pizza['name'] = 'Margherita'
print(pizza['name'])  # 'Margherita'

# The .get() method retrieves the value associated with a key.
# It's similar to the bracket notation that we just used, but its advantage is that you can set a default value, so you won't get an error if the key doesn't exist
print(pizza.get('toppings', [])) # ['mozzarella', 'basil']
print(pizza.get('size', 'Medium'))  # 'Medium'

# The .keys() and .values() methods return a view object with all the keys and values in the dictionary, respectively:
print(pizza.keys())   # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
print(pizza.values()) # dict_values(['Margherita', 8.9,

# The .items() method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:
print(pizza.items())  # dict_items([('name', 'Margherita'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# The .clear() method removes all the key-value pairs from the dictionary:
#pizza.clear()

# The .pop() method removes the key-value pair with the key that you specify as the first argument and returns its value.
# If the key doesn't exist, it returns the default value that you specify as the second argument. If the key doesn't exist and you don't pass a default value, a KeyError is raised:
print (pizza.pop('price', 10))
# pizza.pop('total_price') # KeyError

# The .popitem() method removes and returns the last key-value pair added to the dictionary as a tuple.
print(pizza.popitem())  # ('toppings', ['mozzarella', 'basil'])

# The .update() method updates the key-value pairs with the key-value pairs of another dictionary.
# If they have keys in common, their values are overwritten.
pizza.update({ 'price': 15, 'total_time': 25 })