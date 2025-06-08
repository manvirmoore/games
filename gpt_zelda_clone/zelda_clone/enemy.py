import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gpt_zelda_clone/zelda_clone/assets/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 3

    def update(self):
        pass

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()