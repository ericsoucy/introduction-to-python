# For the Child class to inherit from the Parent class, you have to pass the Parent to the Child.
# This style is called single inheritance, since a child class inherits from exactly one parent class.
class Parent:
    # Parent attributes and methods
    pass
class Child(Parent):
    pass
    # Child inherits, extends, and/or overrides where necessary

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound
print(jack.bark)  # woof! woof!! woof!!!

# Let's override the sound() method from the parent Animal class in the child Dog class so we can have sound() use the bark class variable:
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound.'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Override sound() to use bark class variable
    def sound(self):
        return f'{self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack barks woof! woof!! woof!!!

# If you want to keep the return value of sound() and add the bark class variable later, you can extend sound() by using the super() function:
# In this example, base is the result of calling the sound() method from the Animal class, and then we append the Dog class's specific sound to it.
# This way, you can extend the functionality of the parent Animal class while still keeping its original behavior.
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Call Animal.sound(), then append bark
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!

# There's also multiple inheritance, where a child class can inherit from more than one parent class.
# Here's the basic syntax of multiple inheritance:
class Parent:
    # Attributes and methods for Parent
    pass
class Child:
    # Attributes and methods for Child
    pass
class GrandChild(Parent, Child):
    # GrandChild inherits from both Parent and Child
    # GrandChild can combine or override behavior from each
    pass

# A simple way to demonstrate multiple inheritance is with a frog, which can both walk on land and swim in water:
class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce()) # Output: I'm Freddy the frog. I can walk on land and I can swim in water.