import sys
import pygame


class Configuration():
    """配置相关的类"""

    def __init__(self):
        self.size = (480, 700)
        self.caption = 'Draw a rectangle with the mouse'
        self.bg_color = (230, 230, 230)

        # 矩形相关
        self.start = (0, 0)
        self.end = (0, 0)
        self.rect_size = (0, 0)
        self.drawing = False
        self.rect_color = (255, 0, 0)
        self.border_width = 2


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
                # 确定矩形的起点
                configs.start = event.pos
                configs.rect_size = 0, 0
                configs.drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # 确定矩形的尺寸大小
                configs.end = event.pos
                configs.rect_size = configs.end[0] - configs.start[0], configs.end[1] - configs.start[1]
                configs.drawing = False
            elif event.type == pygame.MOUSEMOTION and configs.drawing:
                # 不断变化中的矩形形状
                configs.end = event.pos
                configs.rect_size = configs.end[0] - configs.start[0], configs.end[1] - configs.start[1]

        screen.fill(configs.bg_color)
        # 画矩形框
        pygame.draw.rect(screen, configs.rect_color, (configs.start, configs.rect_size), configs.border_width)
        pygame.display.update()


if __name__ == '__main__':
    main()