# class Calculator:
#     def __init__(self, add, minus, multi, div, result):
#         self.add = add
#         self.minus = minus
#         self.multi = multi
#         self.div = div
#         self.result = result
    
#     def add(self):
#         result = self.add + self.add
#         print(result)
    
#     def minus(self):
#         result = self.minus - self.minus
#         print(result)
        
#     def multi(self):
#         result = self.multi * self.multi
#         print(result)
    
#     def div(self):
#         result = self.div / self.div
#         print(result)
        
#     def result(self):
#         print(self.result)

# input1 = Calculator(10, 5, 2, 4, 0)
# input1.add()
# input1.minus()
# input1.multi()
# input1.div()
# input1.result()

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