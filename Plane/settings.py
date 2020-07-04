import pygame


class Settings():
    """这是一个关于游戏配置项的类"""

    def __init__(self):
        self.width = 480
        self.height = 700
        self.size = (self.width, self.height)

        self.caption = "Plane War"

        self.bg_img = pygame.image.load('images/background.png')
        self.bg_img_rect = self.bg_img.get_rect()
        self.bullet_list = []
        self.bullet_max_num = 5
