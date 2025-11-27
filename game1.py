import pygame
import random
pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello  from pygame")
# screen.fill((0, 123, 255))
# screen.fill("pink")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
current_color = WHITE
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_color = (
                random.randint(0,22),
                random.randint(0,200),
                random.randint(0,100),
            )

            # if current_color == WHITE:
            #     current_color = BLUE
            # elif current_color == BLUE:
            #     current_color = RED
            # elif current_color == RED:
            #     current_color = GREEN
            # else:
            #     current_color = WHITE
    screen.fill(current_color)
    pygame.display.update()