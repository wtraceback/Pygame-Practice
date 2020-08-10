import pygame.font


class Levelboard():
    """显示 关卡 相关的类"""
    def __init__(self, sets, stats, screen):
        """初始化关卡相关的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.sets = sets
        self.stats = stats

        # 字体相关的信息
        self.font = pygame.font.SysFont(None, 32)
        self.text_color = (255, 255, 255)

        self.prepare_level_text()

    def prepare_level_text(self):
        """将关卡字体渲染成图片"""
        level_text = str(self.stats.level)
        self.level_img = self.font.render('Level: ' + level_text, True, self.text_color)

        # 显示的位置
        self.level_rect = self.level_img.get_rect()
        self.level_rect.left = 10
        self.level_rect.top = 10

    def show_level(self):
        # 在屏幕的左上角显示关卡
        self.screen.blit(self.level_img, self.level_rect)