import pygame
from pygame.sprite import Sprite
import logging
logger = logging.getLogger("Bullet")


class Bullet(Sprite):
    """ Bullet class 1.0"""

    #must change name for setings parameter
    def __init__(self, s_settings, screen, ant):
        #create a bullet at the current pos
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet rect at 0 0 and then set correct pos
        self.rect = pygame.Rect(0, 0,  s_settings.bullet_width, s_settings.bullet_height)
        self.rect.centerx = ant.rect.centerx
        self.rect.top = ant.rect.top
        #store the bullet pos in decimal val
        self.y = float(self.rect.y)

        self.color = s_settings.bullet_color
        self.speed_factor = s_settings.bullet_speed_factor
        logger.info("Bullet instance")

    def update(self):
        #move the bullet
        self.y -= self.speed_factor
        #update rect
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
