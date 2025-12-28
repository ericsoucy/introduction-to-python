# The range() function is used to generate a sequence of integers. 
# range(start, stop, step)

for num in range(3):
    print(num)

for num in range(1, 5):
    print(num)

# step 2 : count by 2
for num in range(2, 11, 2):
    print(num)

#  generate a sequence of integers in decrementing order, then you can use a negative integer for the step argument
for num in range(40, 0, -10):
    print(num)

# Another thing you can do with the range() function is create a list of integers by using it
# with the list constructor.
# The list constructor is used to convert an iterable into a list.
# Here is an example of generating a list of even integers between 2 and 10
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]