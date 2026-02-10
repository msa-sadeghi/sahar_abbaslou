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
lives_text = myfont.render(f"lives {lives}", True, "black")

game_over_text = myfont.render("Game Over Please press Space to play  again", True, "black")
game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))

FPS = 60
CLOCK = pygame.time.Clock()
playing_mode = True

hit_sound =  pygame.mixer.Sound("hit.wav")
bomp_sound =  pygame.mixer.Sound("zap.wav")


running = True
while running:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if lives <= 0:
        playing_mode = False
    if playing_mode:

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
            hit_sound.play()

        if meat_rect.bottom >= 640:
            random_x = random.randint(80, 920)
            meat_rect.x = random_x
            meat_rect.y = 0

        if tiger_rect.colliderect(bomb_rect):
            random_x = random.randint(80, 920)
            bomb_rect.x = random_x
            bomb_rect.y = 0
            lives -= 1
            bomp_sound.play()

        if bomb_rect.bottom >= 640:
            random_x = random.randint(80, 920)
            bomb_rect.x = random_x
            bomb_rect.y = 0

    meat_text = myfont.render(f"meat {meat_counts}", True, "green")
    lives_text = myfont.render(f"lives {lives}", True, "black")
    if playing_mode:
        screen.fill("pink")
    else:
        screen.fill("red")
        screen.blit(game_over_text, game_over_rect)
        if keys[pygame.K_SPACE]:
            playing_mode = True
            lives  = 5
            meat_counts = 0
    if playing_mode:
        screen.blit(tiger_image, tiger_rect)
        screen.blit(meat_image, meat_rect)
        screen.blit(bomb_image, bomb_rect)
    screen.blit(meat_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    pygame.display.update()