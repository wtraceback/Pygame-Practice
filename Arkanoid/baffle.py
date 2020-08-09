import pygame


class Baffle():
    """这是一个关于 挡板 的类"""
    def __init__(self, sets, screen):
        """初始化挡板并设置其初始位置"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.sets = sets

        # 加载挡板图片
        self.img = pygame.image.load('images/baffle.png')
        self.rect = self.img.get_rect()

        # 设置挡板的最初始的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整挡板的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.sets.baffle_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.sets.baffle_speed_factor

    def blit_img(self):
        """绘制挡板"""
        self.screen.blit(self.img, self.rect)

    def center_baffle(self):
        """初始化挡板的位置居中"""
        self.rect.centerx = self.screen_rect.centerx