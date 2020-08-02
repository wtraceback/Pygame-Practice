import pygame


class Baffle():
    """这是一个关于 挡板 的类"""
    def __init__(self, screen):
        """初始化挡板并设置其初始位置"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 加载挡板图片
        self.img = pygame.image.load('images/baffle.png')
        self.rect = self.img.get_rect()

        # 设置挡板的最初始的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20

    def blit_img(self):
        """绘制挡板"""
        self.screen.blit(self.img, self.rect)