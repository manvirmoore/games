import pygame
from player import Player
from enemy import Enemy
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(100, 100)
enemies = pygame.sprite.Group(Enemy(200, 200), Enemy(300, 250))
all_sprites = pygame.sprite.Group(player, *enemies)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Combat detection
    for enemy in enemies:
        if player.attacking and player.sword_hitbox.colliderect(enemy.rect):
            enemy.take_damage()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)

    # Draw sword hitbox (debug)
    if player.attacking:
        pygame.draw.rect(screen, (255, 0, 0), player.sword_hitbox)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()