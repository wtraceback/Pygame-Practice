import pygame


class Enemy():
    """这是一个敌人战机的类"""
    def __init__(self, sets, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sets = sets

        self.img = pygame.image.load('images/enemy.png')

        # 敌机最开始在屏幕左上角附近
        self.rect = self.img.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储坐标的小数
        self.float_x = float(self.rect.x)

    def blit_img(self):
        """在指定位置绘制敌机"""
        self.screen.blit(self.img, self.rect)

    def update_coordinate(self):
        """敌人战机向右或向左移动"""
        self.float_x += (self.sets.enemy_speed_factor * self.sets.enemy_direction)
        self.rect.x = self.float_x

    def check_edges(self):
        """如果到达屏幕的最右边或者是最左边的边缘，则返回 True"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True