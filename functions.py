import pygame
import os
# Blue Character Left / Right Movement Images for animation


def hold(type, t: float):
    pygame.time.set_timer(type, t/1000)