# main.py - Simple Calculator Application

class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent


def greet_user():
    """Simple greeting function."""
    return "Welcome to the Simple Calculator!"


def main():
    """Main function to demonstrate the calculator."""
    print(greet_user())
    print("=" * 40)
    
    calc = Calculator()
    
    # Demo calculations
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 3 = {calc.subtract(10, 3)}")
    print(f"Multiplication: 4 * 7 = {calc.multiply(4, 7)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")
    print(f"Power: 2^3 = {calc.power(2, 3)}")
    
    print("=" * 40)
    print("Calculator demo completed successfully!")


if __name__ == "__main__":
    main()
