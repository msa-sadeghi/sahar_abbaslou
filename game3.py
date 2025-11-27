import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
x = 100
y = 100


clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys =  pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= 10
    elif keys[pygame.K_DOWN]:
        y += 10
    if keys[pygame.K_RIGHT]:
        x += 10
    elif keys[pygame.K_LEFT]:
        x -= 10
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    
    pygame.display.update()