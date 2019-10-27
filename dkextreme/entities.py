import pygame as pg
import random

from . import util

SCREENRECT = util.SCREENRECT
GRAVITY = util.GRAVITY

class Platform(pg.sprite.Sprite):
    def __init__(self, speed, direction):
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
class Barrel(pg.sprite.Sprite):

    speed = 4

    def __init__(self, speed, direction, actor):
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.facing = random.choice((-1, 1)) * Barrel.speed
        self.frame = 0
        
    def update(self):
        # Figure out gravity and if they need to fall by dropping them by gravity
        self.rect.y = self.rect.y + GRAVITY
        # Let's scan for platforms
        falling = False
        for platform in pg.sprite.spritecollide(self, platforms, True):
            falling = True
            # For each platform, we should set the bottom of the barrel to the top of it.
            self.rect.top += self.rect.top - platform.rect.top
        if not falling:
            self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        #self.image = self.images[self.frame // self.animcycle % 3]
        