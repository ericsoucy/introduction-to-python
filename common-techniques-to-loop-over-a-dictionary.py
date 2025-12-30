products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

for product in products.items():
    print(product)

for product, price in products.items():
    print(product, price)

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products) #{'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

for product in enumerate(products):
    print(product)

for index, product in enumerate(products):
    print(index, product)


for price in enumerate(products.values()):
    print(price)

for index, price in enumerate(products.values()):
    print(index, price)

for index, product in enumerate(products.items()):
    print(index, product)

for index, product in enumerate(products.items(), 1):
    print(index, product)