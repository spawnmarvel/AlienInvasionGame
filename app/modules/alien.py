import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, s_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.s_settings = s_settings
        #load image and set rect atr
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        #start each new alien near the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store pos for alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ draw the alien at is cur pos"""
        self.screen.blit(self.image, self.rect)
