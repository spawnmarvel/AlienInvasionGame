import sys
import pygame
from bullet import Bullet


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
        print("move right")
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
        print("move left")
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it
        if len(bullets) < s_settings.bullets_allowed:
            new_bullet = Bullet(s_settings, screen, player)
            bullets.add(new_bullet)
            print("Shoot bullet")
        else:
            print("Only 5 shots for each session")

    # elif event.key == pygame.K_UP:
    #    player.moving_top = True
    #   print("Move top")

def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        print("stop right")
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
        print("stop left")
    elif event.key == pygame.K_UP:
        player.moving_up = False
        print("stop up")

    
def update_bullets(bullets):
    bullets.update()
    #remove bullets beacuse they exist outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)   
        #print(len(bullets))

def update_screen(ant_settings, screen, player, bullets):
    """redraw the screen during each pass in loop"""
    screen.fill(ant_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.blitme()
    #make the most recentrly draw screen visible
    pygame.display.flip()