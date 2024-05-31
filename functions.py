import pygame
import os, math, constants

pygame.font.init()
pygame.mixer.init()
# Blue Character Left / Right Movement Images for animation
bonk = pygame.mixer.Sound('graphics/sound/bonk.mp3')
winm = pygame.mixer.Sound('graphics/sound/winbrass.wav')

def reset(obj1, obj2):
    obj1.x = 80
    obj1.y = 150
    obj2.x = 400
    obj2.y = 150
    obj1.dir = 'rs'
    obj2.dir = 'ls'

def dist(obj1, obj2):
  dist = math.sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
  return dist

def hold(type, t: float):
    pygame.time.set_timer(type, t/1000)

def dam(surf, attacker, victim):
   victim.life -= 1
   bonk.play()
   if victim.life <= 0:
      win(surf, attacker)
wintext = pygame.font.SysFont('Comic Sans MS', 30)
def win(surf, obj):
   if obj.mt == 1:
      x = wintext.render('Player 1 Wins', False, (0, 0, 0))
      surf.blit(x, (100, 100))
   if obj.mt == 2:
      x = wintext.render('Player 2 Wins', False, (0, 0, 0))
      surf.blit(x, (100, 100))
   
   constants.run = False
   winm.play()
            
def playmusic():
   pygame.mixer.music.load('graphics/sound/fight.wav')
   pygame.mixer.music.play(100)
   pygame.mixer.music.set_volume(0.25)

def updateUI(surf, obj1, obj2):
   surf.blit(pygame.image.load(os.path.join('graphics', 'player1.png')), (0, 0))
   pygame.draw.rect(surf, (85,27,27), (20, 20, obj1.life*(100/constants.MAX_LIFE), 20))
   pygame.draw.rect(surf, (247,58,58), (20, 20, obj1.life*(100/constants.MAX_LIFE), 13))
   pygame.draw.rect(surf, (255,255,255), (20, 20, obj1.life*(100/constants.MAX_LIFE), 6))
   pygame.draw.rect(surf, (0,0,0,0), (20, 20, 100, 20), 3)

   surf.blit(pygame.image.load(os.path.join('graphics', 'player2.png')), (0, 32))
   pygame.draw.rect(surf, (85,27,27), (20, 20+32, obj2.life*(100/constants.MAX_LIFE), 20))
   pygame.draw.rect(surf, (247,58,58), (20, 20+32, obj2.life*(100/constants.MAX_LIFE), 13))
   pygame.draw.rect(surf, (255,255,255), (20, 20+32, obj2.life*(100/constants.MAX_LIFE), 6))
   pygame.draw.rect(surf, (0,0,0,0), (20, 20+32, 100, 20), 3)

