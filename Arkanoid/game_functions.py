import pygame
import sys


def check_events(baffle):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, baffle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, baffle)


def check_keydown_events(event, baffle):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        baffle.moving_right = True
    elif event.key == pygame.K_LEFT:
        baffle.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, baffle):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        baffle.moving_right = False
    elif event.key == pygame.K_LEFT:
        baffle.moving_left = False


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