# In this workshop, you are going to build a discount calculator that can apply different discount strategies to products.
# The system will determine the best price for a customer based on multiple discount rules.

from abc import ABC, abstractmethod
from typing import List
class Product:
    def __init__(self, name: str, price: float)-> None:
        self.name = name
        self.price = price
    def __str__(self)-> str:
        return f"{self.name} - ${self.price}"
class DiscountStrategy(ABC):
    """Abstract base class for all discount strategies."""
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass
    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Checks if the discount percent is within the allowed limit (70%)."""
        return self.percent <= 70
    def apply_discount(self, product: Product) -> float:
        """Calculates the price after applying the percentage reduction."""
        return product.price * (1 - self.percent / 100)
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Ensures the fixed discount is not more than 10% of the price."""
        return (product.price * 0.9) > self.amount
    def apply_discount(self, product: Product) -> float:
        """Subtracts the fixed amount from the product price."""
        return product.price - self.amount
class PremiumUserDiscount(DiscountStrategy):
    """A strategy that applies a fixed discount for premium-tier users."""
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Returns True if the user tier is 'premium', regardless of casing."""
        return user_tier.lower() == 'premium'
    def apply_discount(self, product: Product) -> float:
        """Applies a flat 20% discount."""
        return product.price * 0.8
class DiscountEngine:
    """Manages a collection of discount strategies to find the best deal."""
    def __init__(self, strategies: List[DiscountStrategy]) -> None:
        self.strategies = strategies
    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """Determines the lowest price possible after checking all strategies."""
        prices = [product.price]
        # Iterate through all available strategies
        for strategy in self.strategies:
            # Check if the specific strategy can be used
            if strategy.is_applicable(product, user_tier):
                # Calculate the potential new price
                discounted = strategy.apply_discount(product)
                # Add it to our list of options
                prices.append(discounted)
        # Return the lowest price found in the list
        return min(prices)
if __name__ == "__main__":
    # Create the product instance
    product = Product('Wireless Mouse', 50.0)

    # Define the current user context
    user_tier = "Premium"

    # Create a list containing all available discount strategies
    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]
    # 1. Create the engine with your list of strategies
    engine = DiscountEngine(strategies)

    # Calculate the best price
    best_price = engine.calculate_best_price(product, user_tier)

    # Final formatted output
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")
    