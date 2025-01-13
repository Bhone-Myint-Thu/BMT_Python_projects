class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero error"

# Example usage
calc = Calculator(10, 5)
print(calc.add())    # Output: 15
print(calc.minus())  # Output: 5
print(calc.multi())  # Output: 50
print(calc.div())    # Output: 2.0
# Get user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (add, minus, multi, div): ")

# Create Calculator object
calc = Calculator(a, b)

# Perform chosen operation
if operation == "add":
    print(calc.add())
elif operation == "minus":
    print(calc.minus())
elif operation == "multi":
    print(calc.multi())
elif operation == "div":
    print(calc.div())
else:
    print("Invalid operation")
    