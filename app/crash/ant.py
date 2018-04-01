import pygame
#https://www.pygame.org/docs/ref/rect.html
#pygame object for storing rectangular coordinate
class Ant():

    def __init__(self, ant_settings, screen):
        # init ant and pos
        self.screen = screen
        self.ant_settings = ant_settings
        # load ant image and get its rect
        self.image = pygame.image.load("images/heroant.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # starte each ant at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #store a decimal value for the ants center
        self.center = float(self.rect.centerx)
        #movment flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ant pos based on movement flag"""
        #not move out to the right of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ant_settings.ant_speed_factor
        #not move out to the left of the screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ant_settings.ant_speed_factor
        #update rect object from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
