import pygame
import logging
logger = logging.getLogger("Player")


class Player():
    """ Player class 1.0"""

    def __init__(self, player_settings, screen):
        # init ant and pos
        self.screen = screen
        self.player_settings = player_settings
        # load ant image and get its rect
        self.image = pygame.image.load("images/transparent_ant.gif")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # starte each ant at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #store a decimal value for the ants center
        self.center_x = float(self.rect.centerx)
        
        #movment flag
        self.moving_right = False
        self.moving_left = False

        # 
        self.rect.centery = self.screen_rect.centery
        self.center_y = float(self.rect.centery)
        self.moving_top = False
        self.moving_bottom = False
        logger.info("Player instance")

    def toString(self):
        print("bool bottom " +format(self.moving_bottom))
        print("bool top " +format(self.moving_top))
        print("bool left " +format(self.moving_left))
        print("bool right " +format(self.moving_right))

    def update(self):
        """update ant pos based on movement flag"""
        # print("bool bottom " +format(self.moving_bottom))
        # print("bool top " +format(self.moving_top))
        # print("bool left " +format(self.moving_left))
        # print("bool right " +format(self.moving_right))
        #not move out to the right of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            logger.debug(format(self.rect.right) + " self right, screen right " + format(self.screen_rect.right))
            self.center_x += self.player_settings.player_speed_factor
            # print(format(self.moving_right))
        #not move out to the left of the screen
        elif self.moving_left and self.rect.left > 0:
            logger.debug(format(self.rect.left) + " self left, screen left " + format(self.screen_rect.left))
            self.center_x -= self.player_settings.player_speed_factor
        # not move passed bottom
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            logger.debug(format(self.rect.bottom) + " self bot, screen bot " + format(self.screen_rect.bottom))
            self.center_y += self.player_settings.player_speed_factor
        # not move beyond top
        elif self.moving_top and self.rect.top > 0:
            logger.debug(format(self.rect.top) + " self top, screen top " + format(self.screen_rect.top))
            self.center_y -= self.player_settings.player_speed_factor
        
        
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
        
    

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
