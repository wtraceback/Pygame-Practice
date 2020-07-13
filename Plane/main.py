import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


def main():
    sets = Settings()

    # pygame 初始化
    # 创建一个屏幕对象（即游戏窗口，用于显示游戏元素）
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(sets)

    # 创建开始按钮
    start_butn = Button(sets, screen)

    # 创建一艘战斗机
    fighter = Ship(sets, screen)

    # 创建敌人战机舰队
    gf.create_enemy_fleet(sets, screen, fighter)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(sets, screen, stats, fighter, start_butn)

        if stats.game_active:
            #更新战斗机的坐标
            fighter.update_coordinate()

            # 更新子弹的坐标，并且进行子弹和敌人战机的碰撞检测
            gf.update_bullets_coordinate(sets, screen, fighter)

            # 检测敌人战机是否到达屏幕边缘、更新敌人战机的坐标
            gf.update_enemy_fleet_coordinate(sets, screen, stats, fighter)

        # 绘制背景图、绘制子弹、绘制战斗机、绘制敌人舰队、重新绘制游戏窗口
        gf.update_screen(sets, screen, stats, fighter, start_butn)


if __name__ == "__main__":
    main()