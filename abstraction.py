# Abstraction is the process of hiding complex implementation details and showing only the essential features of an object or system.
# Think of it as focusing on what something does rather than how it does it.
# It provides you with a simplified interface to interact with a complex system.
# This module provides the ABC class (standing for “abstract base class”) and the @abstractmethod decorator.
# On the other hand, an abstract method is a method declared in an Abstract Base Class (ABC) using the @abstractmethod decorator.
# It may have no implementation or a basic default one.
# However, any subclass must override it to be considered concrete and instantiable, even if a default implementation is provided.


# In this example:
# We are importing the ABC class and abstractmethod from the abc module.
# We then create an Animal class that inherits from ABC, and create an abstract method make_sound in it that each subclass of Animal must override.
# We create the concrete classes Dog, Cat, and Monkey, which must override the make_sound abstract method.
# We instantiate the concrete classes and call their make_sound method to show how each of them implements the make_sound abstract method in its own way.

from abc import ABC, abstractmethod


class Animal(ABC):  # Inherits from abstract base class
    @abstractmethod  # Abstract method decorator
    def make_sound(self):  # The method subclasses must override
        pass


# Concrete class that will override the abstract method
class Dog(Animal):
    def make_sound(self):
        print("Woof!")


# Another concrete class that will override the abstract method
class Cat(Animal):
    def make_sound(self):
        print("Meow!")


# Another concrete class that will override the abstract method
class Monkey(Animal):
    def make_sound(self):
        print("Ooh ooh aah aah!")


# Create instances of each concrete class
animals = [Dog(), Cat(), Monkey()]

# Loop through the instances to call the make_sound method
for animal in animals:
    animal.make_sound()

# Output:
# Woof!
# Meow!
# Ooh ooh aah aah!

# Here's another example, this time with an instance attribute you can pass to the instances of the concrete methods:
# In this example:
# We have an abstract base class TalkingToy that defines a blueprint for any toy that can speak.
# The subclasses RobotToy, TeddyBearToy, and DinosaurToy implement the speak method in their own way.
# When we create instances of these subclasses and call the speak method, each toy speaks in its own unique way.
from abc import ABC, abstractmethod


# The blueprint for any toy that can speak
class TalkingToy(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class RobotToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says beep boop! I am a robot!")


class TeddyBearToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says hug me! I'm cuddly!")


class DinosaurToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says ROOOOAR!")
# Create toys
rusty = RobotToy("Rusty")
fluffy = TeddyBearToy("Fluffy")
rex = DinosaurToy("Rex")

toys = [rusty, fluffy, rex]
for toy in toys:
    toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!

# What is the primary goal of abstraction in object-oriented programming?
# To hide complex logic and only show essential features

# How does Python implement abstraction through its ABC module?
# By using decorators and inheritance to define abstract methods that subclasses must implement.

# In the car analogy for abstraction, what represents the simplified interface and the complex system?
# The interface is the steering wheel, brakes, and accelerator, and the complex system is the engine, transmission, and braking physics.