import pygame.font


class Scoreboard():
    """显示得分信息相关的类"""
    def __init__(self, sets, screen, stats):
        """初始化得分相关属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.sets = sets
        self.stats = stats

        # 得分信息字体相关的信息
        self.font = pygame.font.SysFont(None, 32)
        self.text_color = (30, 30, 30)

        self.prepare_score_text()
        self.prepare_level_text()

    def prepare_score_text(self):
        """将分数文本渲染成图像，绘制在右上角"""
        score_text = str(self.stats.score)
        self.score_img = self.font.render('Score: ' + score_text, True, self.text_color)

        # 显示得分的位置：右上角
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_level_text(self):
        """将等级文本渲染成图像，绘制在正上方"""
        level_text = str(self.stats.level)
        self.level_img = self.font.render('Level: ' + level_text, True, self.text_color)

        # 显示等级的位置：正上方
        self.level_rect = self.level_img.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = 20

    def show_score(self):
        """在屏幕上右上角显示得分"""
        self.screen.blit(self.score_img, self.score_rect)
        # 在屏幕的正上方显示游戏等级
        self.screen.blit(self.level_img, self.level_rect)
