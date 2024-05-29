import pygame
# Player class is to create moveable player objects.
class Player():
  def __init__(self, x, y, h, w, c, t):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = c
    self.mt = t #movement type: differing keyboard inputs.

  def draw(self, win):
    obj = (self.x, self.y, self.w, self.h)
    c = self.color
    pygame.draw.rect(win, c, obj) # Parameter 3 -> Rect which is a location, and a size. # Parameter 2 -> RGB # Parameter 1 -> Surface / Layer
  def move(self, keys, v): # Defines different game object movements.
    if self.mt == 1:
      if keys[pygame.K_d]:
          self.x += v
      elif keys[pygame.K_a]:
          self.x -= v
      elif keys[pygame.K_w]:
          self.y -= v
      elif keys[pygame.K_s]:
          self.y += v

    elif self.mt == 2:
      if keys[pygame.K_RIGHT]:
          self.x += v
      elif keys[pygame.K_LEFT]:
          self.x -= v
      elif keys[pygame.K_UP]:
          self.y -= v
      elif keys[pygame.K_DOWN]:
          self.y += v