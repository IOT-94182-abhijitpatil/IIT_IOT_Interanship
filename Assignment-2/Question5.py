# print a number in binary format using a function

def to_binary(n):
    print(bin(n)[2:])

num = int(input("Enter a number: "))
to_binary(num)
