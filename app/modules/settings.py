class Settings():
    """ Settings class 1.0 """

    def __init__(self):
        self.screen_width = 700
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        #ant speed settings
        self.player_speed_factor = 1  # 1.5
        #bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 178, 34, 34
        self.bullets_allowed = 5