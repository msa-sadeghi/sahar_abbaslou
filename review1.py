# for i in range(3):
#     n = int(input("enter a number: "))
#     if n % 2 == 0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")

# i  = 0
# while i < 3:
#     n = int(input("enter a number: "))
#     if n % 2 == 0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
#     i += 1


# name = input("enter your name: ")
# print(len(name))
# for ch in name:
#     print(ch)

# sports = ["football", "basketball"]
# sports.append("baseball")
# print(sports)
# sports.remove("football")
# print(sports)

# sports = ("footbal", "basket")
# for s in sports:
#     print(s)


# favorite_sports = {
#     "mohamad":"football",
#     "sara":"football",
#     "reza":"tennis",
# }

# print(f"mohamad likes {favorite_sports['mohamad']}")
# print(f"sara likes {favorite_sports['sara']}")
# print(f"reza likes {favorite_sports['reza']}")
# del favorite_sports["reza"]
# print(favorite_sports)
# favorite_sports["nikan"] =  "football"
# print(favorite_sports)

# import random

# print(random.randint(1, 100))

# choices = ["r", "p", "s"]

# user_choice = input("enter your choice (r  p  s)  : ")
# print(f"user choice is {user_choice}")
# computer_choice = random.choice(choices)
# print(f"computer choice is {computer_choice}")

# if user_choice == "p" and computer_choice == "r":
#     print("user won")
# elif user_choice == "r" and computer_choice == "p":
#     print("computer won")


import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightblue")
    pygame.display.update()
    CLOCK.tick(FPS)