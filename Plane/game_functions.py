import sys
import pygame

def check_events(fighter):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, fighter)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, fighter)


def check_keydown_events(event, fighter):
    """响应按键"""
    if event.key == pygame.K_LEFT:
        fighter.moving_left = True
    elif event.key == pygame.K_RIGHT:
        fighter.moving_right = True


def  check_keyup_events(event, fighter):
    """响应松开"""
    if event.key == pygame.K_LEFT:
        fighter.moving_left = False
    elif event.key == pygame.K_RIGHT:
        fighter.moving_right = False


def blit_bg_image(screen, sets):
    screen.blit(sets.bg_img, sets.bg_img_rect)


def update_screen(screen, sets, fighter):
    # 绘制背景图
    blit_bg_image(screen, sets)

    # 绘制战斗机
    fighter.update_coordinate()
    fighter.blit_img()

    # 重新绘制游戏窗口
    pygame.display.update()