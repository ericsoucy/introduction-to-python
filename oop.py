# While a single underscore prefix is just a convention, prefixing attributes and methods with a double underscore
# effectively prevents them to be accessed from the outside of their class, making those attributes and methods private.

class Wallet:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # Add to the balance safely

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # Remove from the balance safely

account = Wallet(500)
print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

# To get the current value of __balance, you can define a get_balance method
class Wallet2:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance


acct_one = Wallet2(100)
acct_one.deposit(50)
print(acct_one.get_balance()) # 150

acct_two = Wallet2(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # 422

acct_two.deposit(150)
print(acct_two.get_balance()) # 572

# You can also define a private __validate method to check if every deposit or withdrawal amount is a positive number:
# the __validate method is private, and runs behind the scenes in the deposit() and withdraw() public methods to make sure the amount is always valid.

class Wallet_with_validation:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet_with_validation()
acct_one.deposit(4) # ValueError('Amount must be positive')
print(acct_one.get_balance()) # 0

acct_one.deposit(50)
print(acct_one.get_balance()) # 50
acct_one.withdraw(-8) # ValueError('Amount must be positive')
acct_one.withdraw(58) # ValueError('Insufficient funds')
