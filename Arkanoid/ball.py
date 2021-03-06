import pygame


class Ball():
    """这是一个关于 弹球 的类"""
    def __init__(self, sets, screen, baffle):
        """初始化弹球并设置其初始位置"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.sets = sets
        self.baffle = baffle

        # 加载弹球图片
        self.img = pygame.image.load('images/ball.png')
        self.rect = self.img.get_rect()

        self.reset_ball()

    def update(self):
        if not self.is_fire:
            # 弹球跟着挡板移动
            self.rect.centerx = self.baffle.rect.centerx
        else:
            # 弹球自行移动
            self.rect = self.rect.move(self.sets.ball_speed_factor)

    def blit_img(self):
        """绘制弹球"""
        self.screen.blit(self.img, self.rect)

    def reset_ball(self):
        """初始化弹球的位置居中并让其在发射之前跟随着挡板移动"""
        # 设置弹球的最初始的位置
        self.rect.centerx = self.baffle.rect.centerx
        self.rect.bottom = self.baffle.rect.top

        # 弹球的初始状态
        self.is_fire = False