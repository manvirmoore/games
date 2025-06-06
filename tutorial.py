import pygame
from sys import exit #to close code

pygame.init() #always need this

## Set up the sceen, FPS clock and font
screen = pygame.display.set_mode((800, 400)) #creates 'display surface' with width, height which must be stored in a variable
pygame.display.set_caption('manni game') #changes window title
clock = pygame.time.Clock() #creating the clock (for FPS)
test_font = pygame.font.Font('assets/Pixeltype.ttf', 50) #Defines a font, needs font type (none, or a ttf file), size
game_active = True

#test_surf = pygame.Surface((100,200)) #also needs width, height. This creates a surface of specified size (just a box)
#test_surf.fill('Red') #pygame recognises lots of colours. colours the whole rectangle.

## Import surfaces (i.e. images)
sky_surf = pygame.image.load('assets/Sky.png').convert_alpha() #.convert_alpha removes the whitespace from the image.
ground_surf = pygame.image.load('assets/ground.png').convert_alpha()
text_surf = test_font.render('manni game', False, 'Black') #needs text, anti aliasing, colour
text_rect = text_surf.get_rect(center = (400, 50)) #half of screen size.

end_surf = test_font.render('game over, space to restart', False, 'Black')
end_rect = end_surf.get_rect(center = (400, 200)) 

thing_surf = pygame.transform.flip(pygame.image.load('assets/thing.png').convert_alpha(), flip_x=True, flip_y=False)
thing_rect = thing_surf.get_rect(bottomright = (600, 300))

## creating a rectangle for player
player_surf = pygame.image.load('assets/king.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

## event loop - everything happens in this while loop
while True: #never will be false (i think) as we want the window to stay open indefinitely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this ensures we can quit by checking for the 'event loop'
            exit() #exits out of code, avoid errors
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                thing_rect.x = 600
    
    if game_active:
        ## draw all static elements
        screen.blit(sky_surf,(0, 0)) #blit is 'block image transfer', puts one surface on another. needs surface, position arguments. 
        screen.blit(ground_surf,(0, 300)) #second surface goes to front
        screen.blit(text_surf, text_rect)

        #thing movement- thing_x tries to move thing -3 places unless it leaves the screen. Then it draws this.
        thing_rect.x -= 4 #moves thing left 4 x coords every loop

        if thing_rect.right <= 0: 
            thing_rect.left = 800 #loops it once it leaves the screen

        screen.blit(thing_surf, thing_rect) #moves the thing where the rectangle is drawn

        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300

        screen.blit(player_surf,player_rect)

        #collision
        if thing_rect.colliderect(player_rect):
            game_active = False
    
    else:
        #end screen
        screen.fill('Red')
        screen.blit(end_surf, end_rect)

    ## update everything
    pygame.display.update() #this updates the display surface with the above. just need to call it and then can forget
    clock.tick(60) #sets max FPS (can't set min)