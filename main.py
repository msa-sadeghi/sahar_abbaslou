import pygame
pygame.init()

WIDTH = 1200
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS  =  60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    CLOCK.tick(FPS)