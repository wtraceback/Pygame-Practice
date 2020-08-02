import pygame
import sys

from settings import Settings
from baffle import Baffle


def main():
    sets = Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一个挡板
    baffle = Baffle(screen)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 绘制背景图片
        screen.blit(sets.bg_img, sets.bg_img_rect)

        # 绘制挡板
        baffle.blit_img()

        # 重绘屏幕对象
        pygame.display.update()


if __name__ == '__main__':
    main()