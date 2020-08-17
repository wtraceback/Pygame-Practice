import pygame


class Settings():
    """存储关于 打砖块 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 500
        self.size = (self.screen_width, self.screen_height)

        # 背景图
        self.bg_img = pygame.image.load('images/background.jpg')
        self.bg_img_rect = self.bg_img.get_rect()

        # 标题
        self.caption = 'Arkanoid'

        # 挡板的移动速度
        self.baffle_speed_factor = 5
        self.life_limit = 3

        # 弹球方向的取反
        self.reverse_direction = -1

        # 砖块组 and 砖块关卡
        self.brick_list = []
        self.brick_level_group = {
            'level_1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'level_2': [10, 8, 6, 4, 2, 4, 6, 8, 10],
            'level_3': [2, 4, 6, 8, 10, 8, 6, 4, 2],
        }

        # retry 按钮信息
        self.retry_text = 'Retry'

        self.init_dynamic_sets()

        # 音效相关
        self.bg_music_name = 'music/bg_music.mp3'
        self.baffle_music_name = 'music/collid_baffle.wav'
        self.brick_music_name = 'music/collid_brick.wav'
        self.game_over = 'music/game_over.wav'

    def init_dynamic_sets(self):
        # 弹球的移动速度
        self.ball_speed_factor = [2, -2]
