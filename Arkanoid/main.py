import pygame
import sys


def main():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Arkanoid')

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 重绘屏幕对象
        pygame.display.update()


if __name__ == '__main__':
    main()