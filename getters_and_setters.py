# Getters and setters are methods that let you control how the attributes of a class are accessed and modified. With getters you retrieve a value, and with setters you set a value.
# These actions are done through what's known as properties. They are what connect getters and setters, and allow access to data.
# Properties act like attributes but behave like methods under the hood. Think of them as data you define like methods, but work like attributes. This means you can access properties with dot notation instead of parentheses or round brackets.
# The main thing properties do is that they run extra logic behind the scenes when you get, set, or delete values with them. This makes them the perfect choice when you want to access or manipulate data within objects.

# When you use a method, you always have to call it with parentheses. But with a property, you can access it just like a normal attribute using dot notation. 
# To create a property, you define a method and place the @property decorator above it. This tells Python to treat the method as a property.

# Getters let you retrieve a value or even compute a value on the fly.
# Setters let you modify the values safely by running checks before assignment.
# Properties are what tie these getters and setters together so you can write logic while still using dot notation.
# Deleters let you define what happens when an attribute is deleted.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius

    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26

# To make a setter to create the radius, for example, you have to define another method with the same name and use @<property_name>.setter above it:
class Circle2:
    def __init__(self, radius):
        # always use the underscore-prefixed form
        self._radius = radius

    @property
    def radius(self):  # A getter to get the radius
         # always use the underscore-prefixed form
        return self._radius

    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
         #always use the underscore-prefixed form
        self._radius = value

my_circle = Circle(3)
print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8
my_circle.radius # This will call the getter
my_circle.radius = 4 # This will call the setter

# A deleter runs custom logic when you use the del statement on a property. To create one, you use the @<property_name>.deleter decorator:
class Circle_with_deleter:
    def __init__(self, radius):
        self._radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
# Create circle object with a radius
my_circle = Circle_with_deleter(33)
print("Initial radius:", my_circle.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'
