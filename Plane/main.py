import sys
import pygame


def main():
    # pygame 初始化   创建一个屏幕对象（即游戏窗口，用于显示游戏元素）
    pygame.init()
    screen = pygame.display.set_mode((480, 852))
    pygame.display.set_caption("Plane")

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 重新绘制游戏窗口
        pygame.display.update()


if __name__ == "__main__":
    main()