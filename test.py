import re
import random

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.items():
    print(product)

my_set = {1, 2, 3, 4, 5, 6}
my_set.add(5)

print(my_set)

try:
  print(22 / 0)
except ZeroDivisionError:
  print("You can't divide by zero!")