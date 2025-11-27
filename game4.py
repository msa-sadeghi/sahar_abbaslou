import pygame
pygame.init()
from player import Player

my_player = Player(100, 100, 5, "player1")
player_2 = Player(300, 100, 4 , "player2")

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
running = True
while running == True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")   
    my_player.draw(screen)
    player_2.draw(screen)
    my_player.move(pygame.key.get_pressed(), WIDTH, HEIGHT)
    player_2.move(pygame.key.get_pressed(), WIDTH, HEIGHT)
    if my_player.rect.colliderect(player_2.rect):
        print("collided")
        player_2.image = player_2.lose_image
    else:
        player_2.image = player_2.start_image
   
    pygame.display.update()