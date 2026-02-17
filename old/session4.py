# string = input("enter a string: ")
# print(string.upper())

# number = int(input("enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# string = input("enter a string: ")
# print(string[0:3])
# print(string[:3])
# print(string[3:])
# print(string[3:6])
# print(string[1:4])
# print(string[::2])
# print(string[::-1])


# number = int(input("enter a number: "))
# if number > 0:
#     print(f"{number} is positive")
# elif number < 0:
#     print(f"{number} is negative")
# else:
#     print(f"{number} is zero")


# number1 = float(input("enter a number: "))
# number2 = float(input("enter a number: "))

# op = input("enter ('+' or '-' or '*' or '/'): ")
# if op == "+":
#     print(f"{number1} + {number2} = {number1 + number2}")
# elif op == "-":
#     print(f"{number1} - {number2} = {number1 - number2}")
# elif op == "*":
#     print(f"{number1} * {number2} = {number1 * number2}")
# elif op == "/":
#     print(f"{number1} / {number2} = {number1 / number2}")
from fractions import Fraction

x = Fraction(2,3)
y = Fraction(3,4)

print(x + y)

