import pygame
pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello  from pygame")


robot = pygame.image.load("robot.png")
robot_rect = robot.get_rect(center = (WIDTH/2, HEIGHT/2))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(robot, robot_rect)
    pygame.display.update()