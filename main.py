import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tiger_image = pygame.image.load("tiger.png")
tiger_image = pygame.transform.scale_by(tiger_image, 0.7)

tiger_rect = tiger_image.get_rect(midbottom=(500, 640))

meat_image = pygame.image.load("meat.png")
meat_image = pygame.transform.scale_by(meat_image, 0.08)
meat_rect = meat_image.get_rect(midtop=(500, 0))

bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale_by(bomb_image, 0.8)
bomb_rect = bomb_image.get_rect(midtop=(500, 0))

myfont = pygame.font.Font("f.ttf", 28)
meat_counts = 0
meat_text = myfont.render(f"meat {meat_counts}", True, "green")
lives = 5
lives_text = myfont.render(f"lives {lives}", True, "red")

FPS = 60
CLOCK = pygame.time.Clock()
running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tiger_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        tiger_rect.x += 5  

    meat_rect.y += 5  
    bomb_rect.y += 5  
    if tiger_rect.colliderect(meat_rect):
        random_x = random.randint(80, 920)
        meat_rect.x = random_x
        meat_rect.y = 0
        meat_counts += 1
        
    if meat_rect.bottom >= 640:
        random_x = random.randint(80, 920)
        meat_rect.x = random_x
        meat_rect.y = 0

    if tiger_rect.colliderect(bomb_rect):
        random_x = random.randint(80, 920)
        bomb_rect.x = random_x
        bomb_rect.y = 0
        lives -= 1

    if bomb_rect.bottom >= 640:
        random_x = random.randint(80, 920)
        bomb_rect.x = random_x
        bomb_rect.y = 0

    meat_text = myfont.render(f"meat {meat_counts}", True, "green")
    lives_text = myfont.render(f"lives {lives}", True, "red")
    screen.fill("pink")
    screen.blit(tiger_image, tiger_rect)
    screen.blit(meat_image, meat_rect)
    screen.blit(bomb_image, bomb_rect)
    screen.blit(meat_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    pygame.display.update()