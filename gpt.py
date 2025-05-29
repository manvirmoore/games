import pygame
import sys
import time

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Management Game")

# Fonts
FONT = pygame.font.SysFont("arial", 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
GRAY = (180, 180, 180)

# Game variables
money = 100
income_rate = 1  # $ per second
workers = 0
worker_cost = 50
last_income_time = time.time()

# Button setup
button_rect = pygame.Rect(200, 300, 200, 50)

def draw_ui():
    screen.fill(WHITE)

    money_text = FONT.render(f"Money: ${money}", True, BLACK)
    rate_text = FONT.render(f"Income Rate: ${income_rate}/sec", True, BLACK)
    workers_text = FONT.render(f"Workers: {workers}", True, BLACK)

    screen.blit(money_text, (20, 20))
    screen.blit(rate_text, (20, 60))
    screen.blit(workers_text, (20, 100))

    pygame.draw.rect(screen, GREEN if money >= worker_cost else GRAY, button_rect)
    button_text = FONT.render("Hire Worker ($50)", True, WHITE)
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))

    pygame.display.flip()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # 60 FPS

    # Income tick
    current_time = time.time()
    if current_time - last_income_time >= 1:
        money += income_rate
        last_income_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and money >= worker_cost:
                money -= worker_cost
                workers += 1
                income_rate += 1

    draw_ui()

pygame.quit()
sys.exit()
