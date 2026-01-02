# Exception handling is the process of catching and managing errors that occur during the execution of a program, so your code doesn't crash unexpectedly.
# Python provides the try, except, else, and finally blocks to gracefully handle errors.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else: # : Runs if no exception is raised in the try block.
    print('Division successful:', x)
finally: # Runs no matter what—whether or not an exception occurred
    print('This block always runs.')

try:
    number = int('abc')
    result = 10 / number
    # separate except clauses can make error responses more specific and useful.
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")

try:
    x = 1 / 0
except ZeroDivisionError as e: # e access the actual error message or object for logging or debugging.
    print(f'Error occurred: {e}')

# catch multiple exceptions in a single except clause by specifying the exceptions as a tuple:
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
