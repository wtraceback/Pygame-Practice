import sys
import pygame

from bullet import Bullet
from enemy import Enemy


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


def blit_bg_image(sets, screen):
    screen.blit(sets.bg_img, sets.bg_img_rect)


def update_screen(sets, screen, fighter):
    # 绘制背景图
    blit_bg_image(sets, screen)

    # 绘制战斗机
    fighter.update_coordinate()
    fighter.blit_img()

    # # 绘制敌人战机
    blit_enemy_fleet(sets)

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
        new_bullet = Bullet(sets, screen, fighter)
        sets.bullet_list.append(new_bullet)


def create_enemy_fleet(sets, screen):
    """创建敌人战机舰队"""
    # 创建一个敌人战机，并计算每一行可容纳的战机个数
    enemy_tool = Enemy(screen)
    available_space_x = sets.screen_width - 2 * enemy_tool.rect.width
    number_enemy_x = int(available_space_x / (2 * enemy_tool.rect.width))

    # 创建第一行外星人
    for enemy_number in range(number_enemy_x):
        new_enemy = Enemy(screen)
        x = new_enemy.rect.width + 2 * new_enemy.rect.width * enemy_number
        new_enemy.rect.x = x
        sets.enemy_list.append(new_enemy)


def blit_enemy_fleet(sets):
    for enemy in sets.enemy_list:
        enemy.blit_img()