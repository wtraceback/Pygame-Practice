import pygame

class Ship():
    """这是一个关于战斗机的类"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.img = pygame.image.load('images/plane.png')

        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_img(self):
        self.screen.blit(self.img, self.rect)