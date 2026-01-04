import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # 1. Title line: centered name in 30 '*'
        title = f"{self.name:*^30}\n"
        
        # 2. Ledger entries
        items = ""
        for item in self.ledger:
            # Truncate description to 23 chars
            desc = item["description"][:23]
            # Format amount to 2 decimal places, max 7 chars total
            amt = f"{item['amount']:.2f}"
            
            # Left align description (23) and right align amount (7)
            items += f"{desc:<23}{amt:>7}\n"
            
        # 3. Total line
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total
    def deposit(self, amount, description=""):
        """Add a positive amount and description to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Add a negative amount to the ledger if funds are sufficient."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Calculate the total current balance."""
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    def transfer(self, amount, category_instance):
        """
        Withdraws from this category and deposits into another.
        'category_instance' is the object representing the destination.
        """
        if self.check_funds(amount):
            # Withdraw from current category (self)
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            # Deposit into the other category
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Returns False if amount is greater than balance, True otherwise."""
        return amount <= self.get_balance()

# Example of how to instantiate it:
food = Category("Food")
clothing = Category("Clothing")



def create_spend_chart(categories):
    # 1. Calculate withdrawals for each category
    spent_amounts = []
    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_amounts.append(abs(spent))

    total_spent = sum(spent_amounts)
    
    # Calculate percentages rounded down to the nearest 10
    # Formula: (Spent / Total) * 100, then floor to nearest 10
    percentages = []
    for amount in spent_amounts:
        if total_spent > 0:
            val = (amount / total_spent) * 100
            percentages.append(math.floor(val / 10) * 10)
        else:
            percentages.append(0)

    # 2. Build the chart header
    res = "Percentage spent by category\n"

    # 3. Build the y-axis and bars (from 100 down to 0)
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # 4. Add the horizontal line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Build the vertical names
    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += f"{name[i]}  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res