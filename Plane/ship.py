import pygame


class Ship():
    """这是一个关于战斗机的类"""

    def __init__(self, sets, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.sets = sets

        self.img = pygame.image.load('images/fighter.png')

        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 存储坐标的小数
        self.float_center_x = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False

    def blit_img(self):
        """在指定位置绘制战斗机"""
        self.screen.blit(self.img, self.rect)

    def update_coordinate(self):
        """更新战斗机的坐标，且限制其运动的边界"""
        if self.moving_left and self.rect.left > 0:
            self.float_center_x -= self.sets.fighter_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.float_center_x += self.sets.fighter_speed_factor

        self.rect.centerx = self.float_center_x

    def center_fighter(self):
        """将战斗机的位置设置为居中"""
        self.float_center_x = self.screen_rect.centerx