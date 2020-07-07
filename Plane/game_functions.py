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


def create_enemy_fleet(sets, screen, fighter_tool):
    """创建敌人战机舰队"""
    # 创建一个敌人战机，并计算每一行可容纳的战机个数
    enemy_tool = Enemy(screen)
    number_enemy_x = get_number_enemy_x(sets, enemy_tool)
    number_enemy_rows = get_number_enemy_rows(sets, enemy_tool, fighter_tool)

    # 创建第一行外星人
    for enemy_row in range(number_enemy_rows):
        for enemy_number in range(number_enemy_x):
            create_enemy(sets, screen, enemy_number, enemy_row)
        
        
def get_number_enemy_x(sets, enemy_tool):
    # 计算每一行可容纳的战机个数
    available_space_x = sets.screen_width - 2 * enemy_tool.rect.width
    number_enemy_x = int(available_space_x / (2 * enemy_tool.rect.width))

    return number_enemy_x


def get_number_enemy_rows(sets, enemy_tool, fighter_tool):
    # 计算屏幕可容纳多少行敌人战机
    available_space_y = sets.screen_height - 3 * enemy_tool.rect.height - fighter_tool.rect.height
    number_enemy_rows = int(available_space_y / (2 * enemy_tool.rect.height))

    return number_enemy_rows


def create_enemy(sets, screen, enemy_number, enemy_row):
    new_enemy = Enemy(screen)

    # 设置响应的敌人战机的位置
    x = new_enemy.rect.width + 2 * new_enemy.rect.width * enemy_number
    new_enemy.rect.x = x
    y = new_enemy.rect.height + 2 * new_enemy.rect.height * enemy_row
    new_enemy.rect.y = y

    sets.enemy_list.append(new_enemy)


def blit_enemy_fleet(sets):
    for enemy in sets.enemy_list:
        enemy.blit_img()