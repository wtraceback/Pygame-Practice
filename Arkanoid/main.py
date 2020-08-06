import pygame

from settings import Settings
from baffle import Baffle
import game_functions as gf
from ball import Ball


def main():
    sets = Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一个挡板
    baffle = Baffle(sets, screen)

    # 创建一个弹球
    ball = Ball(sets, screen, baffle)
    
    # 创建砖块组
    gf.create_brick_group(sets, screen, baffle)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(baffle, ball)

        # 更新挡板的坐标
        baffle.update()

        # 更新弹球的坐标
        gf.update_ball(sets, baffle, ball)

        # 更新画面
        gf.update_screen(sets, screen, baffle, ball)


if __name__ == '__main__':
    main()
