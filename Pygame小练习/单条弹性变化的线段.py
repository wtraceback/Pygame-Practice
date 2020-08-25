import sys
import pygame


class Configuration():
    """配置相关的类"""

    def __init__(self):
        self.size = (480, 700)
        self.caption = 'Draw a line with the mouse'
        self.bg_color = (230, 230, 230)

        # 线段相关
        self.start = (0, 0)
        self.end = (0, 0)
        self.drawing = False
        self.line_color = (255, 0, 0)
        self.line_width = 2


def main():
    configs = Configuration()

    # 游戏的初始化、游戏窗口的设置、游戏窗口标题的设置
    pygame.init()
    screen = pygame.display.set_mode(configs.size)
    pygame.display.set_caption(configs.caption)

    while True:
        for event in pygame.event.get():
            # 关闭游戏窗口
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 确定线段的起点
                configs.start = event.pos
                configs.end = event.pos
                configs.drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                # 确定线段的终点
                configs.end = event.pos
                configs.drawing = False

            elif event.type == pygame.MOUSEMOTION and configs.drawing:
                # 不断变化中的线段
                configs.end = event.pos

        screen.fill(configs.bg_color)
        # 绘制线段
        pygame.draw.line(screen, configs.line_color, configs.start, configs.end, configs.line_width)
        pygame.display.update()


if __name__ == '__main__':
    main()