import pygame
from settings import PLAYER_SPEED, SWORD_DURATION

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gpt_zelda_clone/zelda_clone/assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.Vector2(0, 0)
        self.last_attack = 0
        self.attacking = False
        self.facing = "down"
        self.sword_hitbox = pygame.Rect(0, 0, 20, 20)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing = "right"
        elif keys[pygame.K_UP]:
            self.direction.y = -1
            self.facing = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.facing = "down"

        if keys[pygame.K_z] and not self.attacking:
            self.attacking = True
            self.last_attack = pygame.time.get_ticks()

    def move(self):
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.rect.y += self.direction.y * PLAYER_SPEED

    def update(self):
        self.input()
        self.move()
        self.update_sword()

    def update_sword(self):
        if self.attacking:
            now = pygame.time.get_ticks()
            if now - self.last_attack > SWORD_DURATION:
                self.attacking = False

            offset = 25
            if self.facing == "up":
                self.sword_hitbox.topleft = (self.rect.centerx - 10, self.rect.top - offset)
            elif self.facing == "down":
                self.sword_hitbox.topleft = (self.rect.centerx - 10, self.rect.bottom)
            elif self.facing == "left":
                self.sword_hitbox.topleft = (self.rect.left - offset, self.rect.centery - 10)
            elif self.facing == "right":
                self.sword_hitbox.topleft = (self.rect.right, self.rect.centery - 10)
        else:
            self.sword_hitbox.topleft = (-100, -100)