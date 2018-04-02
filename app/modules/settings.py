class Settings():
    """ class for all settings"""

    def __init__(self):
        self.screen_width = 700
        self.screen_height = 700
        self.bg_color = (240, 255, 255)
        #ant speed settings
        self.player_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100