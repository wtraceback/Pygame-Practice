import pygame


class Bullet():
    """初始化子弹并设置其初始位置"""
    def __init__(self, sets, screen, fighter):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sets = sets

        # 加载子弹的图像并获取其外接矩形
        self.img = pygame.image.load('images/bullet.png')
        self.rect = self.img.get_rect()

        # 设置子弹的初始位置：在飞机的最顶部的中央
        self.rect.centerx = fighter.rect.centerx
        self.rect.centery = fighter.rect.top

        # 子弹的飞行速度
        self.speed_factor = self.sets.bullet_speed_factor

    def blit_img(self):
        """在指定位置绘制子弹"""
        self.screen.blit(self.img, self.rect)

    def update_coordinate(self):
        self.rect.centery -= self.speed_factor