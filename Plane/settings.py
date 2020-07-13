import pygame


class Settings():
    """这是一个关于游戏配置项的类"""

    def __init__(self):
        # 游戏窗口配置项
        self.screen_width = 1000
        self.screen_height = 685
        self.size = (self.screen_width, self.screen_height)
        self.caption = "Plane War"

        # 背景图配置项
        self.bg_img = pygame.image.load('images/background.png')
        self.bg_img_rect = self.bg_img.get_rect()

        # 战斗机的速度
        self.fighter_speed_factor = 5
        self.fighter_max_num = 3

        # 子弹相关配置项
        self.bullet_speed_factor = 3
        self.bullet_list = []
        self.bullet_max_num = 10

        # 敌人战机相关配置项(移动速度、向下移动的速度、舰队移动的方向：右：+1 左：-1、战机舰队数组)
        self.enemy_speed_factor = 1
        self.enemy_drop_speed = 10
        self.enemy_direction = 1
        self.enemy_list = []

        # 开始按钮信息
        self.start_butn_text = 'Start'