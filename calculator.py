"""
Simple Calculator Class - Student Implementation Required

Students need to implement all the methods below.
"""


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return float(result)

    def power(self, base, exponent):
        """Raise base to the power of exponent"""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, value):
        """Return the square root of value"""
        if value < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = value ** 0.5
        self.history.append(f"√{value} = {result}")
        return float(result)

    def factorial(self, n):
        """Return n! for non-negative integers"""
        if isinstance(n, float) and not n.is_integer():
            raise ValueError("Factorial is only defined for integers")
        n = int(n)
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.history.append(f"{n}! = {result}")
        return result

    def percentage(self, total, percent):
        """Return percent% of total"""
        result = (total * percent) / 100.0
        self.history.append(f"{percent}% of {total} = {result}")
        return float(result)
    def get_history(self):     
        """Return calculation history"""
        return self.history

    def clear_history(self):
        """Clear calculation history"""
        self.history = []
