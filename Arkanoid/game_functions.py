import pygame
import sys


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(sets, screen, baffle):
    """更新屏幕上的图像，并切换到新的屏幕"""
    blit_bg_img(sets, screen)

    # 绘制挡板
    baffle.blit_img()

    # 重绘屏幕对象
    pygame.display.update()


def blit_bg_img(sets, screen):
    # 绘制背景图片
    screen.blit(sets.bg_img, sets.bg_img_rect)