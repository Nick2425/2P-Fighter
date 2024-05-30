import pygame
import os
import constants, functions
import math

cga_r = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cg/cg-splice', 'row-2-column-' + str(i)) +
            '.png'), 1.5) for i in range(1, 5)
]
cga_l = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cg/cg-splice', 'row-4-column-' + str(i)) +
            '.png'), 1.5) for i in range(1, 5)
]
# Still Images
cgs_r = pygame.transform.smoothscale_by(
    pygame.image.load(
        os.path.join('graphics/cg/cg-splice', 'row-2-column-1.png')), 1.5)
cgs_l = pygame.transform.smoothscale_by(
    pygame.image.load(
        os.path.join('graphics/cg/cg-splice', 'row-4-column-1.png')), 1.5)
# Green Character Left / Right Movement Images for animation
cba_r = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cb/cb-splice', 'row-2-column-' + str(i)) +
            '.png'), 1.5) for i in range(1, 5)
]
cba_l = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cb/cb-splice', 'row-4-column-' + str(i)) +
            '.png'), 1.5) for i in range(1, 5)
]
# Still Images
cbs_r = pygame.transform.smoothscale_by(
    pygame.image.load(
        os.path.join('graphics/cb/cb-splice', 'row-2-column-1.png')), 1.5)
cbs_l = pygame.transform.smoothscale_by(
    pygame.image.load(
        os.path.join('graphics/cb/cb-splice', 'row-4-column-1.png')), 1.5)
# Player class is to create moveable player objects.
# Attack animations
cgat_l = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cg/cg-attack-splice',
                         'row-4-column-' + str(i) + '.png')), 1.5)
    for i in range(1, 5)
]
cgat_r = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cg/cg-attack-splice',
                         'row-3-column-' + str(i) + '.png')), 1.5)
    for i in range(1, 5)
]

cbat_l = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cb/cb-attack-splice',
                         'row-4-column-' + str(i) + '.png')), 1.5)
    for i in range(1, 5)
]
cbat_r = [
    pygame.transform.smoothscale_by(
        pygame.image.load(
            os.path.join('graphics/cb/cb-attack-splice',
                         'row-3-column-' + str(i) + '.png')), 1.5)
    for i in range(1, 5)
]

animation_const = 0

class Player():

  def __init__(self, x, y, h, w, c, t):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = c
    self.dir = 0
    self.mt = t  #movement type: differing keyboard inputs.
    self.ac = 0
    self.attack = False
    self.life = constants.MAX_LIFE

  def anim(self, win, type, direction, obj1, obj2):
    x = animation_const % 4
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

    # Attack animation.
    if type == 3:
      if self.dir == "rs":
        win.blit(cgat_r[self.ac], (self.x, self.y))
      elif self.dir == 'r':
        win.blit(cgat_r[self.ac], (self.x, self.y))
      elif self.dir == "ls":
        win.blit(cgat_l[self.ac], (self.x, self.y))
      elif self.dir == 'l':
        win.blit(cgat_l[self.ac], (self.x, self.y))
      if functions.dist(obj1, obj2) < 30:
        functions.dam(win, obj1, obj2)
        functions.reset(obj1,obj2)
    elif type == 4:
      if self.dir == "rs":
        win.blit(cbat_r[self.ac], (self.x, self.y))
      elif self.dir == 'r':
        win.blit(cbat_r[self.ac], (self.x, self.y))
      elif self.dir == "ls":
        win.blit(cbat_l[self.ac], (self.x, self.y))
      elif self.dir == 'l':
        win.blit(cbat_l[self.ac], (self.x, self.y))
      if functions.dist(obj1, obj2) < 30:
        functions.dam(win, obj2, obj1)
        functions.reset(obj1,obj2)

  def draw(self, win, obj1, obj2):
    #obj = (self.x, self.y, self.w, self.h)
    #c = self.color
    #pygame.draw.rect(win, c, obj) # Parameter 3 -> Rect which is a location, and a size. # Parameter 2 -> RGB # Parameter 1 -> Surface / Layer
    #Drawing Character
    if self.attack == False:
      self.anim(win, self.mt, self.dir, obj1, obj2)
    elif self.attack:
      self.anim(win, self.mt + 2, self.dir, obj1, obj2)

  def move(self, keys, v):  # Defines different game object movements.
    if self.attack != True:
      if self.mt == 1:
        if keys[pygame.K_q]:
          self.attack = True
          self.ac = 0
        elif keys[pygame.
                  K_d] and self.x + v <= constants.RIGHT_LIMIT - self.w * 0.75:
          self.x += v
          self.dir = 'r'
        elif keys[pygame.K_a] and self.x - v >= constants.LEFT_LIMIT:
          self.x -= v
          self.dir = 'l'
        elif keys[pygame.K_w] and self.y - v >= constants.UPPER_LIMIT:
          self.y -= v
        elif keys[
            pygame.K_s] and self.y + v <= constants.LOWER_LIMIT - 0.5 * self.h:
          self.y += v
        else:
          if self.dir == 'l':
            self.dir = "ls"
          elif self.dir == 'r':
            self.dir = "rs"
      elif self.mt == 2:
        if keys[pygame.K_RSHIFT]:
          self.attack = True
          self.ac = 0
        elif keys[
            pygame.
            K_RIGHT] and self.x + v <= constants.RIGHT_LIMIT - self.w * 0.75:
          self.x += v
          self.dir = 'r'
        elif keys[pygame.K_LEFT] and self.x - v >= constants.LEFT_LIMIT:
          self.x -= v
          self.dir = 'l'
        elif keys[pygame.K_UP] and self.y - v >= constants.UPPER_LIMIT:
          self.y -= v
        elif keys[
            pygame.
            K_DOWN] and self.y + v <= constants.LOWER_LIMIT - 0.5 * self.h:
          self.y += v
        else:
          if self.dir == 'l':
            self.dir = "ls"
          elif self.dir == 'r':
            self.dir = "rs"
