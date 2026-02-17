# for i in range(10):
#     print("hello")

# for i in range(10):
#     print(i)

# print("----------------------")
# for i in range(1, 10):
#     print(i)
# print("----------------------")
# for i in range(1, 10, 2):
#     print(i)
# print("----------------------")
# for i in range(2, 10, 2):
#     print(i)


# for i in range(5):
#     number = int(input("enter a number: "))
#     if number > 0:
#         print(number, "is positive")
#     elif number < 0:
#         print(number, "is negative")
#     else:
#         print(number, "is zero")

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()


# for i in range(1,6):
#     print("*" * i)

# import math
# print(math.factorial(5))

# n = int(input("enter a number: "))
# for i in range(1, n + 1, 2):
#     print(' ' *((n - i)//2) + '*' * i)
# for i in range(n-2, 0, -2):
#     print(' '*((n - i)//2)  + '*' * i)

# x = 12
# y = 13

# z = x
# x = y
# y = z
# print(x,y)

# x = 12
# y = 13

# y,x = x,y
# print(x,y)


# a = 0
# b = 1
# n = []

# for i in range(20):
#     n.append(a)
#     a,b = b, a+b

# print(n)


# while True:
#     print("hi")
#     if input("do you want to exit y or n: ") == "y":
#         break

# i = 0
# while i < 3:
#     print("hello")
#     i += 1
  


import turtle
turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("green")
turtle.pensize(2)

# for i in range(3):
#     turtle.forward(100)
#     turtle.left(120)
i = 0
while i < 3:
    turtle.forward(100)
    turtle.left(120)
    i += 1


turtle.done()