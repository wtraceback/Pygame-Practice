import pygame


class Settings():
    """存储关于 打砖块 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 500
        self.size = (self.screen_width, self.screen_height)

        # 背景图
        self.bg_img = pygame.image.load('images/background.jpg')
        self.bg_img_rect = self.bg_img.get_rect()

        # 标题
        self.caption = 'Arkanoid'

        # 挡板的移动速度
        self.baffle_speed_factor = 5

        # 弹球的移动速度
        self.ball_speed_factor = [2, -2]
        self.reverse_direction = -1

        # 砖块组
        self.brick_list = []