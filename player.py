import pygame
class Player:
    def __init__(self, x,y, velocity,name):
        self.image = pygame.image.load("player2.png")
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.lose_image = pygame.image.load("robot.png")
        self.lose_image = pygame.transform.scale_by(self.lose_image, 0.3)
        self.start_image = self.image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.velocity = velocity
        self.direction = "right"
        self.name = name

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.direction == "left", False)
        screen.blit(img, self.rect)
    def move(self, keys, window_width, window_height):
        if self.name == "player1":
            if keys[pygame.K_UP] and self.rect.top >= 0:
                self.rect.y -= self.velocity
            if keys[pygame.K_DOWN] and self.rect.bottom <= window_height:
                self.rect.y += self.velocity
            if keys[pygame.K_LEFT] and self.rect.left >= 0:
                self.rect.x -= self.velocity
                self.direction = "left"
            if keys[pygame.K_RIGHT] and self.rect.right <= window_width:
                self.direction = "right"
                self.rect.x += self.velocity

        elif self.name == "player2":
            if keys[pygame.K_w] and self.rect.top >= 0:
                self.rect.y -= self.velocity
            if keys[pygame.K_s] and self.rect.bottom <= window_height:
                self.rect.y += self.velocity
            if keys[pygame.K_a] and self.rect.left >= 0:
                self.rect.x -= self.velocity
                self.direction = "left"
            if keys[pygame.K_d] and self.rect.right <= window_width:
                self.direction = "right"
                self.rect.x += self.velocity
