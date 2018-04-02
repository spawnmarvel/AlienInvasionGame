import pygame
from settings import Settings
from player import Player
import game_functions as game_function
from pygame.sprite import Group

def run_game():
    #init and cretat screen object
    pygame.init()
    #pixels 800 x 800, screen is surface for the game
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Ant Invasion")

    hero = Player(game_settings, screen)
    #make agroup of bullets
    bullets = Group()

    #starts the main loop for the game, controll
    while True:
        #watch for keys and mouse
        game_function.check_events(game_settings, screen, hero, bullets)
        hero.update()
        game_function.update_bullets(bullets)
        # redraw the screen during each pass thorugh loop
        game_function.update_screen(game_settings, screen, hero, bullets)
        

run_game()