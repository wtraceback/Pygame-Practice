import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def main():
    sets = Settings()

    # pygame 初始化   创建一个屏幕对象（即游戏窗口，用于显示游戏元素）
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一艘战斗机
    fighter = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(sets, screen, fighter)
        gf.update_screen(screen, sets, fighter)


if __name__ == "__main__":
    main()