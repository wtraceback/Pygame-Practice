import pygame


class SoundEffect():
    """这是一个关于 游戏音效 的类"""
    def __init__(self, sets):
        self.sets = sets

        self.init_setting()

        # 准备音效(Sound 模块不能加载 mp3，必须将 mp3 转为 wav 格式)
        self.collid_baffle = pygame.mixer.Sound(self.sets.baffle_music_name)
        self.collid_brick = pygame.mixer.Sound(self.sets.brick_music_name)
        self.game_over = pygame.mixer.Sound(self.sets.game_over)

    def init_setting(self):
        pygame.mixer.init()

        # 背景音乐、设置背景音乐的音量、无限循环播放背景音乐
        pygame.mixer.music.load(self.sets.bg_music_name)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)