import pygame


class Ship():
    """这是一个关于战斗机的类"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.img = pygame.image.load('images/fighter.png')

        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_left = False
        self.moving_right = False

        self.fighter_speed_factor = 2

    def blit_img(self):
        self.screen.blit(self.img, self.rect)

    def update_coordinate(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.fighter_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.fighter_speed_factor