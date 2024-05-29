import pygame
import classes, functions

pygame.init() #starts program

win = pygame.display.set_mode((500, 500)) # sets window size.
pygame.display.set_caption("Heyo") # sets window caption


x = 50
y = 50
w = 50
h = 50
c = (255, 0, 0)
#Creating player objects.
player1 = classes.Player(x, y, w, h, c, 1)
player1.draw(win)

player2 = classes.Player(x+150, y, w, h, (0, 255, 0), 2)
player2.draw(win)

run = True
while run:
    pygame.time.delay(25) # delays code by 0.05s
    for event in pygame.event.get(): # gets list of events
        if event.type == pygame.QUIT: # event type is 'quit'
            run = False
    keys = pygame.key.get_pressed()

    player1.move(keys, 10) # Diff move.
    player2.move(keys, 10)


    #!! Window update !!
    win.fill((0,0,0)) # Reset background -
    player1.draw(win) # Printing players.
    player2.draw(win)

    pygame.display.update()

pygame.quit()