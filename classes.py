class ClassName:
    # Special method automatically called when a new object is created.
    # It initializes the attributes of the objects that will be created with the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):
        print(self.name.upper())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!
