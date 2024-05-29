import pygame
import classes, functions

pygame.init() #starts program

win = pygame.display.set_mode((500, 500)) # sets window size.
pygame.display.set_caption("Heyo") # sets window caption

x = 50
y = 50

w = 40
h = 60

v = 5

run = True
while run:
    pygame.time.delay(25) # delays code by 0.05s
    for event in pygame.event.get(): # gets list of events
        if event.type == pygame.QUIT: # event type is 'quit'
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += v
    elif keys[pygame.K_a]:
        x -= v
    elif keys[pygame.K_w]:
        y -= v
    elif keys[pygame.K_s]:
        y += v

    win.fill((0,0,0)) # Reset background -
    pygame.draw.rect(win, (255, 0, 0), (x, y, w, h)) # Parameter 3 -> Rect which is a location, and a size. # Parameter 2 -> RGB # Parameter 1 -> Surface / Layer
    pygame.display.update()

pygame.quit()