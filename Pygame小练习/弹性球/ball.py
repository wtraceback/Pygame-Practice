import sys
import pygame

class Settings():
    """关于游戏配置项的类"""

    def __init__(self):
        self.width = 600
        self.height = 800
        self.size = (self.width, self.height)
        self.img_path = 'images/ball.bmp'
        self.caption = 'Ball'
        self.bg_color = (246, 246, 246)
        self.speed = [1, 1]


def main():
    """游戏的主函数"""

    settings = Settings()
    # 初始化 pygame 环境
    pygame.init()
    # 设置游戏窗口
    screen = pygame.display.set_mode(settings.size)
    # 设置游戏窗口的标题
    pygame.display.set_caption(settings.caption)

    # 导入皮球图片
    ball = pygame.image.load(settings.img_path)
    rect = ball.get_rect()

    while True:
        # 关闭游戏窗口
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 皮球位置的更新
        rect = rect.move(settings.speed)
        # rect.x = rect.x + settings.speed[0]
        # rect.y = rect.y + settings.speed[1]
        if rect.left < 0 or rect.right > settings.width:
            settings.speed[0] = -settings.speed[0]
        if rect.top < 0 or rect.bottom > settings.height:
            settings.speed[1] = -settings.speed[1]

        screen.fill(settings.bg_color)
        screen.blit(ball, rect)

        # 更新游戏画面
        pygame.display.update()
        # 延迟 5 毫秒，避免球体移动太快
        pygame.time.delay(5)


if __name__ == '__main__':
    main()