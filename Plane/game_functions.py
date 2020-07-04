import sys
import pygame

from bullet import Bullet


def check_events(sets, screen, fighter):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sets, screen, fighter)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, fighter)


def check_keydown_events(event, sets, screen, fighter):
    """响应按键"""
    if event.key == pygame.K_LEFT:
        fighter.moving_left = True
    elif event.key == pygame.K_RIGHT:
        fighter.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(sets, screen, fighter)
    elif event.key == pygame.K_q:
        sys.exit()


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

    # 更新子弹的坐标以及绘制子弹
    update_bullets(sets)

    # 重新绘制游戏窗口
    pygame.display.update()


def update_bullets(sets):
    # 更新子弹的坐标以及绘制子弹
    for b in sets.bullet_list:
        b.update_coordinate()
        if b.rect.bottom < 0:
            sets.bullet_list.remove(b)
        else:
            b.blit_img()


def fire_bullet(sets, screen, fighter):
    if len(sets.bullet_list) < sets.bullet_max_num:
        new_bullet = Bullet(screen, fighter)
        sets.bullet_list.append(new_bullet)