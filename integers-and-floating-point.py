my_int_1 = 56
my_int_2 = -4

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>

my_int_1 = 56
my_int_2 = 12

print("perform an addition operation with integers")
sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68

print("perform a subtraction with integers")
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44

print("multiplication operation with integers")
my_int_1 = 12
my_int_2 = 4

# Multiplication
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48

print("division operation with integers")
my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667

# Floats are positive or negative numbers with decimal points, like 3.14, -0.5, or 0.0.

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

print("addition operation with floats")
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4

print("multiplication operation with floats")
float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001

print("division operation with floats")
float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222

print("If you add an integer and a float, the result is automatically converted to a float:")
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

print("The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right:")
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulus:', mod_ints) # Integer Modulus: 8
print('Float Modulus:', mod_floats) # Float Modulus: 1.1999999999999993

print("Floor division divides two numbers and returns the greatest integer less than or equal to the result")
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

print("Exponentiation raises a number to the power of another")
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

print("converting either numeric data or strings into integers or floats")
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>

print("the int() function to convert a float into an integer")
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>

print("same built-in functions to convert a string into either a float or integer")
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>

print("round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer")
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

print("abs(): returns the absolute value of a number")
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

print (""" bin(): converts an integer to its binary representation as a string.
           oct(): converts an integer to its octal representation as a string.
           hex(): converts an integer to its hexadecimal representation as a string.
       """)
my_int = 56

binary_representation = bin(my_int)
print(binary_representation)  # 0b111000

octal_representation = oct(my_int)
print(octal_representation) # 0o70

hex_representation = hex(my_int)
print(hex_representation) # 0x38

print("pow(): raises a number to the power of another or performs modular exponentiation.")
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3