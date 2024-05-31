import pygame
import classes, functions, constants
import os

pygame.init()  #starts program

win = pygame.display.set_mode((480, 270))  # sets window size.
pygame.display.set_caption("Heyo")  # sets window caption

# Images
bg = pygame.image.load(os.path.join('graphics', 'bg.png'))

clock = pygame.time.Clock()

c = 0
h = 0
w = 0

#Creating player objects.
player1 = classes.Player(80, 100, w, h, c, 1)
player2 = classes.Player(400, 170, w, h, (0, 255, 0), 2)

player1.draw(win, player1, player2)
player1.dir = 'rs'
player2.draw(win, player1, player2)
player2.dir = 'ls'

functions.reset(player1, player2)

# Custom Event to make a coroutine.
C_E = pygame.event.custom_type()

constants.run = True
pygame.time.set_timer(C_E, 250)
functions.playmusic()
while constants.run:
    clock.tick()  # 40 ticks per second
    pygame.time.delay(25)  # delays code by 0.025s

    keys = pygame.key.get_pressed()
    player1.move(keys, 3)  # Diff move.
    player2.move(keys, 3)

    #!! Window update !!
    win.blit(bg, (0, 0))  # Reset background -
    player1.draw(win, player1, player2)  # Printing players.
    player2.draw(win, player1, player2)
    
    functions.updateUI(win, player1, player2)

    pygame.display.update()
    for event in pygame.event.get():  # gets list of events
        if event.type == pygame.QUIT:  # event type is 'quit'
            run = False
        # Called every 0.5s / 20 ticks.
        if event.type == C_E:
            classes.animation_const += 1

            if player1.ac == 3:
                player1.ac = 0
                player1.attack = False
            if player2.ac == 3:
                player2.ac = 0
                player2.attack = False

            if player1.attack:
                player1.ac += 1

            if player2.attack:
                player2.ac += 1

pygame.time.delay(2500)
pygame.quit()
