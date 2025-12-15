#strings
# Uppercase and Lowercase
s = input("Enter a string: ")

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Alphabet or Digit
if s.isalpha():
    print("String contains only letters")
elif s.isdigit():
    print("String contains only digits")
else:
    print("String contains letters and digits or special characters")

# numbers of vowles
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

#Reverse string

print("Reversed string:", s[::-1])

#Palindrome String
#s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Remove Extra Spaces
#s = input("Enter a string with spaces: ")

print("After removing spaces:", s.strip())

# split word
#s = input("Enter a sentence: ")

words = s.split()
print("Words:", words)

#starting and ending string
s = input("Enter a string: ")

print("Starts with 'Py':", s.startswith("Py"))
print("Ends with 'on':", s.endswith("on"))
