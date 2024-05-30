import pygame
import os
import constants

cga_r = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-splice', 'row-2-column-' + str(i)) + '.png'), 1.5) for i in range(1,5)]
cga_l = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-splice', 'row-4-column-' + str(i)) + '.png'), 1.5) for i in range(1,5)]
# Still Images
cgs_r = pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-splice', 'row-2-column-1.png')), 1.5)
cgs_l = pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-splice', 'row-4-column-1.png')), 1.5)
# Green Character Left / Right Movement Images for animation
cba_r = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-2-column-' + str(i)) + '.png'), 1.5) for i in range(1,5)]
cba_l = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-4-column-' + str(i)) + '.png'), 1.5) for i in range(1,5)]
# Still Images
cbs_r = pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-2-column-1.png')), 1.5)
cbs_l = pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-4-column-1.png')), 1.5)
# Player class is to create moveable player objects.
# Attack animations
cgat_l = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-attack-splice', 'row-4-column-' + str(i) + '.png')), 1.5) for i in range(1,5)]
cgat_r = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cg/cg-attack-splice', 'row-3-column-' + str(i) + '.png')), 1.5) for i in range(1,5)]

cbat_l = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-4-column-' + str(i) + '.png')), 1.5) for i in range(1,5)]
cbat_r = [pygame.transform.smoothscale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-3-column-' + str(i) + '.png')), 1.5) for i in range(1,5)]

class Player():
  def __init__(self, x, y, h, w, c, t):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = c
    self.dir = 0
    self.mt = t #movement type: differing keyboard inputs.
  def anim(self, win, type, direction):
    ticks = pygame.time.get_ticks()
    x = ticks % 4 
    if type == 1:
      # Direction is facing left or right
      if direction == 'r':
        win.blit(cga_r[x], (self.x, self.y))
      elif direction == 'l':
        win.blit(cga_l[x], (self.x, self.y)) 
      elif direction == 'rs':
        win.blit(cgs_r, (self.x, self.y))
      elif direction == 'ls':
        win.blit(cgs_l, (self.x, self.y))
    # Type = Object 1 or 2
    elif type == 2:
      if direction == 'l':
        win.blit(cba_l[x], (self.x, self.y))
      elif direction == 'r':    
        win.blit(cba_r[x], (self.x, self.y))
      elif direction == 'rs':
        win.blit(cbs_r, (self.x, self.y))
      elif direction == 'ls':
        win.blit(cbs_l, (self.x, self.y))

    # Attack
    if type == 3:
      if direction == 'r' or 'rs':
        pass
      elif direction == 'l' or 'ls':
        pass
    elif type == 4:
      if direction == 'r' or 'rs':
        pass
      elif direction == 'l' or 'ls':
        pass




  def draw(self, win):
    #obj = (self.x, self.y, self.w, self.h)
    #c = self.color
    #pygame.draw.rect(win, c, obj) # Parameter 3 -> Rect which is a location, and a size. # Parameter 2 -> RGB # Parameter 1 -> Surface / Layer
    #Drawing Character
    self.anim(win, self.mt, self.dir)


  def move(self, keys, v): # Defines different game object movements.
    if self.mt == 1:
      if keys[pygame.K_d] and self.x + v <= constants.RIGHT_LIMIT - self.w*0.75:
          self.x += v
          self.dir = 'r'
      elif keys[pygame.K_a] and self.x - v >= constants.LEFT_LIMIT:
          self.x -= v
          self.dir = 'l'
      elif keys[pygame.K_w] and self.y - v >= constants.UPPER_LIMIT:
          self.y -= v
      elif keys[pygame.K_s] and self.y + v <= constants.LOWER_LIMIT - 0.5*self.h:
          self.y += v
      else:
        if self.dir == 'l':
          self.dir = "ls"
        elif self.dir == 'r':
          self.dir = "rs"
    elif self.mt == 2:
      if keys[pygame.K_RIGHT] and self.x + v <= constants.RIGHT_LIMIT - self.w*0.75:
          self.x += v
          self.dir = 'r'
      elif keys[pygame.K_LEFT] and self.x - v >= constants.LEFT_LIMIT:
          self.x -= v
          self.dir = 'l'
      elif keys[pygame.K_UP] and self.y - v >= constants.UPPER_LIMIT:
          self.y -= v
      elif keys[pygame.K_DOWN] and self.y + v <= constants.LOWER_LIMIT - 0.5*self.h:
          self.y += v
      else:
        if self.dir == 'l':
          self.dir = "ls"
        elif self.dir == 'r':
          self.dir = "rs"