import pygame.font


class Button():
    def __init__(self, sets, screen):
        """初始化按钮相关的属性"""
        self.sets = sets
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 设置 Start 按钮的相关属性
        self.width = 200
        self.height = 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的 rect 对象，并设置其默认值
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.butn_color = (112, 128, 134)

        self.prepare_text()

    def prepare_text(self):
        """将 msg 渲染成图像，绘制在矩形框上"""
        self.text_img = self.font.render(self.sets.start_butn_text, True, self.text_color)
        self.text_img_rect = self.text_img.get_rect()
        self.text_img_rect.center = self.rect.center

    def draw_butn(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.butn_color, self.rect)
        self.screen.blit(self.text_img, self.text_img_rect)