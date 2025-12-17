from arithmetic import add, multiply
from string import reverse_string,count_vowels

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
text = input("Enter a string: ")

print("Addition: ",add(a, b))
print("Multiplication: ",multiply(a, b))
print("Reversed string: ",reverse_string(text))
print("vowel count: ",count_vowels(text))


