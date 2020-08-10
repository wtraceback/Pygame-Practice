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
        self.prepare_lifes()

    def prepare_level_text(self):
        """将关卡字体渲染成图片"""
        level_text = str(self.stats.level)
        self.level_img = self.font.render('Level: ' + level_text, True, self.text_color)

        # 显示的位置
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 10

    def prepare_lifes(self):
        """显示剩余的生命数"""
        self.lifes = []
        for star_num in range(self.stats.life_left):
            life = LifeStar(self.screen)
            life.rect.x = 10 + star_num * life.rect.width
            life.rect.y = 10
            self.lifes.append(life)

    def show_level(self):
        # 在屏幕的左上角显示关卡
        self.screen.blit(self.level_img, self.level_rect)

        for life in self.lifes:
            life.blit_img()


class LifeStar():
    """显示 生命数 相关的类"""
    def __init__(self, screen):
        """初始化生命数相关的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 加载星星图片
        self.img = pygame.image.load('images/star.png')
        self.rect = self.img.get_rect()

    def blit_img(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.img, self.rect)