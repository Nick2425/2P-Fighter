import pygame
import classes, functions
import os

pygame.init() #starts program

win = pygame.display.set_mode((480, 270)) # sets window size.
pygame.display.set_caption("Heyo") # sets window caption

# Images
bg = pygame.image.load(os.path.join('graphics', 'bg.png'))


clock = pygame.time.Clock()


x = 50
y = 50
w = 50
h = 50
c = (255, 0, 0)
#Creating player objects.
player1 = classes.Player(x+80, y+150, w, h, c, 1)
player1.draw(win)
player1.dir = 'rs'
player2 = classes.Player(x+300, y+150, w, h, (0, 255, 0), 2)
player2.draw(win)
player2.dir = 'ls'

run = True
while run:
    clock.tick() # 40 ticks per second
    pygame.time.delay(25) # delays code by 0.025s
    for event in pygame.event.get(): # gets list of events
        if event.type == pygame.QUIT: # event type is 'quit'
            run = False
    keys = pygame.key.get_pressed()
    player1.move(keys, 3) # Diff move.
    player2.move(keys, 3)

    #!! Window update !!
    win.blit(bg, (0,0)) # Reset background -
    player1.draw(win) # Printing players.
    player2.draw(win)

    pygame.display.update()

pygame.quit()