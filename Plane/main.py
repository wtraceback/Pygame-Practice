import sys
import pygame

import settings
import ship


def main():
    sets = settings.Settings()

    # pygame 初始化   创建一个屏幕对象（即游戏窗口，用于显示游戏元素）
    pygame.init()
    screen = pygame.display.set_mode(sets.size)
    pygame.display.set_caption(sets.caption)

    fighter = ship.Ship(screen)
    bg_img = pygame.image.load('images/background.png')

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 绘制背景图
        screen.blit(bg_img, bg_img.get_rect())

        # 绘制战斗机
        fighter.blit_img()

        # 重新绘制游戏窗口
        pygame.display.update()


if __name__ == "__main__":
    main()