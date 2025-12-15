# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function to find power
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Main program
num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))

base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))
print("Power:", power(base, exp))
