# The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# The enumerate() function also accepts an optional start argument that specifies the starting value for the count
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

# To iterate over multiple iterables in parallel? Well, you can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

#  example of using the zip() function with a for loop to iterate over developers and ids
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')