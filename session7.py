# student = ("sara", "tehran", 20)
# for item in student:
#     print(item)


# def greet(name, family):
#     print("hello", name, family)

# greet("sara", "sabouri")


# def add(a, b, c):
#     return a + b + c

# x = add(1,2,3)
# print(x)

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()

# outer()


# def my():
#     global x
#     x = 10
#     print(x)

# my()
# print(x)


# def average(numbers):
#     return sum(numbers) / len(numbers)

# print(average([1,2,3,4]))

# def validate_national_code(code):
#     return len(code) == 10 and code.isdigit()

# print(validate_national_code("1234567890"))
# print(validate_national_code("12345678a0"))
# print(validate_national_code("12345678"))


# x = "python is good"
# print(len(x.split()))



# def is_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(is_even(12))

# def my(name, age=18):
#     return f"{name} is {age} years old"


# print(my("milad"))
# print(my("sara",  22))
# try:
#     file = open("sample.txt", "w")
#     file.write("hello\nhow are you\ni love python.")
#     file.close()
# except:
#     print("error")

# try:
#     file = open("sample.txt", "r")
#     print(file.readlines())
#     file.close()
# except FileNotFoundError:
#     print("file not found")



# try:
#     file = open("sample.txt", "a")
#     for i in range(4):
#         name = input("enter a name: ")
#         file.write(name+"\n")
#     file.close()
# except:
#     print("error")

# try:
#     with open("sample.txt", "a") as file:
#         for i in range(4):
#             name = input("enter a name: ")
#             file.write(name+"\n")
    
# except:
#     print("error")


try:
    with open("s", "r") as f:
        lines = f.readlines()
        count_of_chars = 0
        for l in lines:
            for c in l:
                if c != "\n":
                    count_of_chars += 1
        print(count_of_chars)
except:
    print()