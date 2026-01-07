# a single underscore is a convention that means the attribute is meant for internal use in the class and should not be directly accessed from outside the class.
# Double underscore, on the other hand, prevents that attribute from being accessed directly from outside the class.

class Example:
    def __init__(self):
        self._internal = 'I can be accessed from outside the class, but should not'
        self.__private = 'You cannot access me directly from outside the class'

obj = Example()

print(obj._internal) # I can be accessed from outside the class, but should not
print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'

# Prefixing an attribute with a double underscore triggers Python's name mangling process,
# in which Python internally renames the attribute by adding an underscore and the class name as a prefix, turning __attribute into _ClassName__attribute

class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__)
# {
#   '_internal': 'I can be accessed from outside the class, but should not',
#   '_Example__private': 'I cannot be accessed directly from outside the class'
# }

# The main purpose of name mangling is to prevent accidental attribute and method overriding when you use inheritance.
# Here's an example that makes that clear:
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

# So, which should you use to prefix attributes between single underscore (_) and double underscore (__)? 
# It depends. If an attribute is only meant for internal use within the class, stick with a single underscore.
# But if you're working with a class that will be inherited, you should use a double underscore
# so the attribute from the parent doesn't get overridden.

# What is the difference between a single underscore and a double underscore?
# A single underscore is just a convention, while a double underscore triggers name mangling.

# What is name mangling?
# A process in which Python changes __attribute into _ClassName__attribute to avoid accidental overriding in subclasses.

# What happens when you don't prefix attributes in a parent and child classes with a double underscore?
# The child class completely overrides the parent class attribute, and the parent's data is lost.

