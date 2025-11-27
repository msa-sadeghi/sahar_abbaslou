# x = True
# print(type(x))
# y = False
# print(type(y))

# print(10 > 3)
# print(10 < 3)
# print(10 == 3)
# print(10 != 3)
# print(10 >= 3)
# print(10 <= 3)

# a = int(input("enter a number: "))
# b = int(input("enter a number: "))

# print(a > b)

# print(True and True)
# print(True and False)
# print(False and False)
# print(False and True)

# print(True or True)
# print(True or False)
# print(False or False)
# print(False or True)

# print(not True)
# print(not False)


# age = int(input("enter an age: "))
# if age < 8:
#     print("kid")
# elif age >= 8 and age <=13:
#     print("teenager")
# elif age >= 14 and age < 18:
#     print("junior")
# else:
#     print("adult")


a = float(input("enter a number: "))
b = float(input("enter a number: "))
op = input("+ - * / ?")
if op == "+":
    print("result is:", a + b)
elif op == "-":
    print("result is:", a - b)
elif op == "*":
    print("result is:", a * b)
elif op == "/":
    print("result is:", a / b)