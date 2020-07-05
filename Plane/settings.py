import pygame


class Settings():
    """这是一个关于游戏配置项的类"""

    def __init__(self):
        # 游戏窗口配置项
        self.screen_width = 1000
        self.screen_height = 685
        self.size = (self.screen_width, self.screen_height)
        self.caption = "Plane War"

        # 背景图配置项
        self.bg_img = pygame.image.load('images/background.png')
        self.bg_img_rect = self.bg_img.get_rect()

        # 战斗机的速度
        self.fighter_speed_factor = 5

        # 子弹相关配置项
        self.bullet_speed_factor = 3
        self.bullet_list = []
        self.bullet_max_num = 5

        # 敌人战机相关配置项
        self.enemy_list = []