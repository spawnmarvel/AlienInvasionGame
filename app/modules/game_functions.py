import sys
import pygame
from bullet import Bullet


def check_events(s_settings, screen, ant, bullets):
    """key / mouse pressed"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, s_settings, screen, ant, bullets)
            

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ant)
           

def check_keydown_events(event,s_settings, screen, ant, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ant.moving_right = True
        print("move right")
    elif event.key == pygame.K_LEFT:
        ant.moving_left = True
        print("move left")
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it
        if len(bullets) < s_settings.bullets_allowed:
            new_bullet = Bullet(s_settings, screen, ant)
            bullets.add(new_bullet)
            print("Shoot bullet")
        else:
            print("Only 5 shots for each session")

def check_keyup_events(event, ant):
    if event.key == pygame.K_RIGHT:
        ant.moving_right = False
        print("stop right")
    elif event.key == pygame.K_LEFT:
        ant.moving_left = False
        print("stop left")

    
def update_bullets(bullets):
    bullets.update()
    #remove bullets beacuse they exist outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)   
        #print(len(bullets))

def update_screen(ant_settings, screen, ant, bullets):
    """redraw the screen during each pass in loop"""
    screen.fill(ant_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ant.blitme()
    #make the most recentrly draw screen visible
    pygame.display.flip()