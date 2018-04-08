import sys
import pygame
from bullet import Bullet
import logging
logger = logging.getLogger("Game functions")

amount_of_bullets = 0

def check_events(s_settings, screen, player, bullets):
    """key / mouse pressed"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, s_settings, screen, player, bullets)
            

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
           

def check_keydown_events(event,s_settings, screen, player, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        player.moving_right = True
        logger.info("move right")
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
        logger.info("move left")
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it
        if len(bullets) < s_settings.bullets_allowed:
            new_bullet = Bullet(s_settings, screen, player)
            bullets.add(new_bullet)
            global amount_of_bullets
            amount_of_bullets = amount_of_bullets + 1
            logger.debug("Shoot bullet")
        else:
            logger.info("Only 5 shots for each session")
    elif event.key == pygame.K_UP:
        player.moving_top = True
        logger.info("Move up")
    elif event.key == pygame.K_DOWN:
        player.moving_bottom = True
        logger.info("Move bottom")

def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        logger.debug("stop right")
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
        logger.debug("stop left")
    elif event.key == pygame.K_UP:
        player.moving_top = False
        logger.debug("stop top")
    elif event.key == pygame.K_DOWN:
        player.moving_bottom = False
        logger.debug("stop bottom")
    # just to check all movments
    # player.toString()

    
def update_bullets(bullets):
    bullets.update()
    #remove bullets beacuse they exist outside the screen (would just consumer more and more ram)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            logger.debug("Bullet removed outside screen")
        #print(len(bullets))

def update_screen(s_settings, screen, player, bullets):
    """redraw the screen during each pass in loop"""
    screen.fill(s_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.blitme()
    #make the most recentrly draw screen visible
    pygame.display.flip()

def get_amount_of_bullets():
    global amount_of_bullets
    return amount_of_bullets
