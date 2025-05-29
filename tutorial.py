import pygame
from sys import exit #to close code

pygame.init() #always need this

## Set up the sceen, FPS clock and font
screen = pygame.display.set_mode((800, 400)) #creates 'display surface' with width, height which must be stored in a variable
pygame.display.set_caption('Runner') #changes window title
clock = pygame.time.Clock() #creating the clock (for FPS)
test_font = pygame.font.Font('PyGame/Pixeltype.ttf', 50) #Defines a font, needs font type (none, or a ttf file), size

#test_surf = pygame.Surface((100,200)) #also needs width, height. This creates a surface of specified size (just a box)
#test_surf.fill('Red') #pygame recognises lots of colours. colours the whole rectangle.

## Import surfaces (i.e. images)
sky_surf = pygame.image.load('PyGame/Sky.png').convert_alpha() #.convert_alpha removes the whitespace from the image.
ground_surf = pygame.image.load('PyGame/ground.png').convert_alpha()
text_surf = test_font.render('manni game', False, 'Black') #needs text, anti aliasing, colour
text_rect = text_surf.get_rect(center = (400, 50)) #half of screen size.

thing_surf = pygame.transform.flip(pygame.image.load('PyGame/thing.png').convert_alpha(), flip_x=True, flip_y=False)
thing_rect = thing_surf.get_rect(bottomright = (600, 300))

## creating a rectangle for player
king_surf = pygame.image.load('PyGame/king.png').convert_alpha()
king_rect = king_surf.get_rect(midbottom = (80,300))

## event loop - everything happens in this while loop
while True: #never will be false (i think) as we want the window to stay open indefinitely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this ensures we can quit by checking for the 'event loop'
            exit() #exits out of code, avoid errors
    
    ## draw all static elements
    screen.blit(sky_surf,(0, 0)) #blit is 'block image transfer', puts one surface on another. needs surface, position arguments. 
    screen.blit(ground_surf,(0, 300)) #second surface goes to front
    screen.blit(text_surf, text_rect)
    
    #thing movement- thing_x tries to move thing -3 places unless it leaves the screen. Then it draws this.
    thing_rect.x -= 4 #moves thing left 4 x coords every loop
    
    if thing_rect.right <= 0: 
        thing_rect.left = 800 #loops it once it leaves the screen
    
    screen.blit(thing_surf, thing_rect) #moves the thing where the rectangle is drawn

    screen.blit(king_surf,king_rect)

    pygame.draw.line(screen, 'Black', (0,0),(800,400))
    ## Collisions
    # if king_rect.colliderect(thing_rect):   # returns 1 (True) when collision (each loop). so multiple collision events. 
    #     print('ouch') 

    #if king_rect.collidepoint(pygame.mouse.get_pos()): print('ouchie') #prints the thing every time the mouse hits the king
    
    ## update everything
    pygame.display.update() #this updates the display surface with the above. just need to call it and then can forget
    clock.tick(60) #sets max FPS (can't set min)