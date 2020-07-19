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
        self.fighter_max_num = 3

        # 子弹相关配置项
        self.bullet_list = []
        self.bullet_max_num = 10

        # 敌人战机相关配置项(移动速度、向下移动的速度、战机舰队数组)
        self.enemy_drop_speed = 10
        self.enemy_list = []

        # 开始按钮信息
        self.start_butn_text = 'Start'

        # 提升游戏的等级，加快游戏的节奏
        self.spddeup_scale = 1.1
        self.init_dynamic_sets()

    def init_dynamic_sets(self):
        self.fighter_speed_factor = 5
        self.bullet_speed_factor = 3
        self.enemy_speed_factor = 1
        # 舰队移动的方向：右：+1 左：-1
        self.enemy_direction = 1

    def increase_speed(self):
        """提升 子弹、敌人战机、战斗机 的速度"""
        self.fighter_speed_factor += self.spddeup_scale
        self.bullet_speed_factor += self.spddeup_scale
        self.enemy_speed_factor += self.spddeup_scale