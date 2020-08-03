import pygame

from settings import Settings
from baffle import Baffle
import game_functions as gf


def main():
    sets = Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一个挡板
    baffle = Baffle(sets, screen)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(baffle)

        # 更新挡板的坐标
        baffle.update()

        # 更新画面
        gf.update_screen(sets, screen, baffle)


if __name__ == '__main__':
    main()