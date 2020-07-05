import pygame

class Enemy():
    """这是一个敌人战机的类"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/enemy.png')

        # 敌机最开始在屏幕左上角附近
        self.rect = self.img.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blit_img(self):
        """在指定位置绘制敌机"""
        self.screen.blit(self.img, self.rect)