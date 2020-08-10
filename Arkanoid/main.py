import pygame

from settings import Settings
from baffle import Baffle
import game_functions as gf
from ball import Ball
from game_stats import GameStats
from button import Button
from levelboard import Levelboard


def main():
    sets = Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(sets)

    # 创建关卡相关信息
    level_board = Levelboard(sets, stats, screen)

    # 创建 Retry 按钮
    retry_butn = Button(sets, screen)

    # 创建一个挡板
    baffle = Baffle(sets, screen)

    # 创建一个弹球
    ball = Ball(sets, screen, baffle)
    
    # 创建砖块组
    gf.create_brick_group(sets, stats, screen)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(sets, stats, screen, baffle, ball, retry_butn, level_board)

        if stats.game_active:
            # 更新挡板的坐标
            baffle.update()

            # 更新弹球的坐标
            gf.update_ball(sets, stats, screen, baffle, ball, level_board)

        # 更新画面
        gf.update_screen(sets, stats, screen, baffle, ball, retry_butn, level_board)


if __name__ == '__main__':
    main()
