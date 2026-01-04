# In this workshop, you are going to build a salary tracking system for employees.

class Employee:
    # Class attribute: shared by all instances
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000
    }
    def __init__(self, name, level):
         # Validation: Check if both name and level are strings
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        # 2. Value Validation (Check if level exists in the dictionary)
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name
        self._level = level
        # 3. Set the _salary attribute using the dictionary lookup
        self._salary = Employee._base_salaries[level]
    def __str__(self):
        # Returns the formatted string whenever the object is printed
        return f"{self.name}: {self.level}"
    @property
    def name(self):
        """Getter method for the name property."""
        return self._name
    @name.setter
    def name(self, new_name):
        """Allows the name to be changed after the object is created."""
        # Validation: Ensure the new name is a string
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self._name}'.")
    @property
    def level(self):
        """Getter method for the level property."""
        return self._level
    @level.setter
    def level(self, new_level):
        """Allows the level to be updated after the object is created."""
        # Validation: Check if the new rank exists in our dictionary
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        # 2. Validation: Check if the level is actually changing
        if new_level == self._level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        # 3. Validation: Is it a lower salary (demotion)?
        if Employee._base_salaries[new_level] < Employee._base_salaries[self._level]:
            raise ValueError("Cannot change to lower level.")
        # Print the promotion announcement
        print(f"'{self.name}' promoted to '{new_level}'.")
        # Update the salary to match the new level
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level
    @property
    def salary(self):
        """Getter for the salary attribute."""
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        """Allows for manual salary updates."""
        # Validation: Ensure the input is a number
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        # 2. Value Validation: Check against the base salary for the current level
        min_salary = Employee._base_salaries[self.level]
        if new_salary < min_salary:
            raise ValueError(f"Salary must be higher than minimum salary ${min_salary}.")
        self._salary = new_salary
        print(f"Salary updated to ${self._salary}.")
    # The __repr__ method is a special method that is supposed to return a string representation of the object that can be used to instantiate it.
    def __repr__(self):
        # Returns a string like: Employee('Charlie Brown', 'trainee')
        return f"Employee('{self.name}', '{self.level}')"
charlie_brown = Employee("Charlie Brown", "trainee")
print(charlie_brown)
print(f"Base salary: ${charlie_brown.salary}") # Base salary: $1000
#print(repr(charlie_brown))
charlie_brown.name = "Charles Brown2"
charlie_brown.name = "Charles Brown"
charlie_brown.level = "junior"
s