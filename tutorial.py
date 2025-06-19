import pygame
from sys import exit #to close code
from random import randint

## Functions
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = txt_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,100))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(thing_surf,obstacle_rect)
            else: 
                screen.blit(snake_surf,obstacle_rect)

        #after the obstacles move it checks which ones are off the screen and deletes them
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return 2
    return 1

def player_animation():
    global player_surf, player_index
    player_index += 0.1
    if player_index > len(player_walk): player_index = 0
    player_surf = player_walk[int(player_index)]

pygame.init() #always need this

## Set up the sceen, FPS clock, font and constants
screen = pygame.display.set_mode((800, 400)) #creates 'display surface' with width, height which must be stored in a variable
pygame.display.set_caption('manni game') #changes window title
clock = pygame.time.Clock() #creating the clock (for FPS)
txt_font = pygame.font.Font('assets/Pixeltype.ttf', 50) #Defines a font, needs font type (none, or a ttf file), size
game_active = 0 #game state
start_time = 0 #reset timer
score = 0
obstacle_timer = pygame.USEREVENT + 1 #basically creating a new event type
pygame.time.set_timer(obstacle_timer,1400) #makes the obstacle_timer event happen every 1400 ms
obstacle_rect_list = []

## Import surfaces
sky_surf = pygame.image.load('assets/Sky.png').convert_alpha() #.convert_alpha removes the whitespace from the image.
ground_surf = pygame.image.load('assets/ground.png').convert_alpha()

caption_surf = txt_font.render('manni game', False, 'Black') #needs text, anti aliasing, colour
caption_rect = caption_surf.get_rect(center = (400, 50)) #half of screen size.

start_rect = caption_surf.get_rect(center=(400, 100))

instr_surf = txt_font.render('Press space to jump. Hit any key to start.', False, 'Black')
instr_rect = instr_surf.get_rect(center = (400, 200))

end_surf = txt_font.render('game over, press enter to restart', False, 'Black')
end_rect = end_surf.get_rect(center = (400, 280)) 

thing_surf = pygame.transform.flip(pygame.image.load('assets/thing.png').convert_alpha(), flip_x=True, flip_y=False)
# thing_rect = thing_surf.get_rect(bottomright = (600, 300))
end_thing_surf = pygame.transform.scale_by(thing_surf,3)
end_thing_rect = end_thing_surf.get_rect(center = (400,200))

snake_surf = pygame.transform.flip(pygame.image.load('assets/snake.png').convert_alpha(), flip_x=True, flip_y=False)

player_surf_1 = pygame.image.load('assets/king.png').convert_alpha()
player_surf_2 = pygame.image.load('assets/king2.png').convert_alpha()
player_walk = [player_surf_1, player_surf_2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

start_plyr_surf = pygame.transform.scale_by(player_surf,3)
start_plyr_rect = start_plyr_surf.get_rect(center = (400,300))

## event loop - everything happens in this while loop
while True: #never will be false (i think) as we want the window to stay open indefinitely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this ensures we can quit
            exit() #exits out of code, avoid errors
        if event.type == pygame.KEYDOWN:
            if game_active == 0:
                game_active = 1
                start_time = pygame.time.get_ticks()
            #jump
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -15
            #reset game
            if event.key == pygame.K_RETURN and game_active == 2:
                game_active = 1
                #thing_rect.x = 600
                start_time = pygame.time.get_ticks()
        #if this isn't in event loop it gets triggered too many times
        if event.type == obstacle_timer and game_active == 1:
            if randint(0,2):
                obstacle_rect_list.append(thing_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(snake_surf.get_rect(bottomright = (randint(900,1100),210)))
    if game_active == 0:
        screen.fill((55, 138, 52))
        screen.blit(caption_surf, start_rect)
        screen.blit(instr_surf, instr_rect)
        screen.blit(start_plyr_surf, start_plyr_rect)
    
    if game_active == 1:
        ## draw all static elements
        screen.blit(sky_surf,(0, 0)) #blit is 'block image transfer', puts one surface on another. needs surface, position arguments. 
        screen.blit(ground_surf,(0, 300)) #second surface goes to front
        screen.blit(caption_surf, caption_rect)
        score = display_score() # this still blits the score but it also saves it 

        #thing_rect.x -= 4 #moves thing left 4 x coords every loop
        # if thing_rect.right <= 0: 
        #     thing_rect.left = 800 #loops it once it leaves the screen
        # screen.blit(thing_surf, thing_rect) #moves the thing where the rectangle is drawn

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)

        #collision
        # if thing_rect.colliderect(player_rect):
        #     game_active = 2
        game_active = collisions(player_rect, obstacle_rect_list)
    
    if game_active == 2:
        #end screen
        screen.fill((173, 35, 49))
        score_surf = txt_font.render(f'Your score: {score}', False, 'Black')
        score_rect = score_surf.get_rect(center = (400, 120)) 
        screen.blit(score_surf, score_rect)
        screen.blit(end_thing_surf, end_thing_rect)
        screen.blit(end_surf, end_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)

    ## update everything
    pygame.display.update() #this updates the display surface with the above (everything in the While statement). just need to call it and then can forget
    clock.tick(60) #sets max FPS (can't set min)