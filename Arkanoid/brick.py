import pygame


class Brick():
    """这是一个关于 砖块 的类"""
    def __init__(self, sets, screen):
        """初始化砖块并设置其初始位置"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.sets = sets

        # 加载砖块图片
        self.img = pygame.image.load('images/brick.png')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.rect.height

    def blit_img(self):
        """在指定位置绘制砖块"""
        self.screen.blit(self.img, self.rect)
