# Arithmetic operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# calculate function
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)

# Testing the function
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calculate(a, b, add))
print("Subtraction:", calculate(a, b, subtract))
print("Multiplication:", calculate(a, b, multiply))
print("Division:", calculate(a, b, divide))
