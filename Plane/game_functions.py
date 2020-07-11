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


def update_screen(sets, screen, fighter):
    # 绘制背景图
    blit_bg_image(sets, screen)

    # 绘制子弹
    blit_bullets_img(sets)

    # 绘制战斗机
    fighter.blit_img()

    # 绘制敌人舰队
    blit_enemy_fleet_img(sets)

    # 重新绘制游戏窗口
    pygame.display.update()


def blit_bg_image(sets, screen):
    """绘制背景图"""
    screen.blit(sets.bg_img, sets.bg_img_rect)


def fire_bullet(sets, screen, fighter):
    if len(sets.bullet_list) < sets.bullet_max_num:
        new_bullet = Bullet(sets, screen, fighter)
        sets.bullet_list.append(new_bullet)


def update_bullets_coordinate(sets, screen, fighter):
    # 更新子弹的坐标
    for b in sets.bullet_list:
        b.update_coordinate()

    # 删除超出边界的子弹
    for b in sets.bullet_list.copy():
        if b.rect.bottom <= 0:
            sets.bullet_list.remove(b)

    # 响应子弹和敌人战机的碰撞 & 敌人战机全部被击落后，重新创建敌人战机舰队
    check_bullet_enemy_collisions(sets, screen, fighter)


def check_bullet_enemy_collisions(sets, screen, fighter):
    # 检测更新后的子弹是否集中敌人战机，如果有，就删除相应的子弹和敌人战机
    collitions = list_collide(sets)

    # 删除现有的子弹并重新创建敌人战机舰队
    if len(sets.enemy_list) == 0:
        for b in sets.bullet_list.copy():
            sets.bullet_list.remove(b)

        create_enemy_fleet(sets, screen, fighter)


def list_collide(sets):
    """遍历所有的子弹，记录其中和敌机相撞的子弹与敌机"""
    crashed = {}
    for b in sets.bullet_list:
        e = check_bullet_enemy_collide(b, sets)
        if e:
            crashed[b] = e
            sets.bullet_list.remove(b)


def check_bullet_enemy_collide(b, sets):
    """判断子弹是否与敌机相撞(子弹有可能是大口径的，并非只能是单纯的小子弹)"""
    crashed = []

    for e in sets.enemy_list:
        if collided(b, e):
            crashed.append(e)
            sets.enemy_list.remove(e)

    return crashed


def collided(b, e):
    """两个矩形之间的碰撞检测"""
    x1 = b.rect.x
    y1 = b.rect.y
    w1 = b.rect.w
    h1 = b.rect.h

    x2 = e.rect.x
    y2 = e.rect.y
    w2 = e.rect.w
    h2 = e.rect.h

    if (abs((x1 + w1 / 2) - (x2 + w2 / 2)) < abs((w1 + w2) / 2)):
        if abs((y1 + h1 / 2) - (y2 + h2 / 2)) < abs((h1 + h2) / 2):
            return True

    return False


def blit_bullets_img(sets):
    # 绘制子弹
    for b in sets.bullet_list:
        b.blit_img()


def create_enemy_fleet(sets, screen, fighter_tool):
    """创建敌人战机舰队"""
    # 创建一个敌人战机，并计算每一行可容纳的战机个数
    enemy_tool = Enemy(sets, screen)
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
    new_enemy = Enemy(sets, screen)

    # 设置响应的敌人战机的位置
    x = new_enemy.rect.width + 2 * new_enemy.rect.width * enemy_number
    new_enemy.rect.x = x
    y = new_enemy.rect.height + 2 * new_enemy.rect.height * enemy_row
    new_enemy.rect.y = y

    sets.enemy_list.append(new_enemy)


def update_enemy_fleet_coordinate(sets):
    """检测敌人战机是否碰到左右边界"""
    check_fleet_edges(sets)

    # 更新敌人战机的坐标
    for enemy in sets.enemy_list:
        enemy.update_coordinate()


def check_fleet_edges(sets):
    """如果有敌人战机到达边缘后，将采取相应的措施"""
    for enemy in sets.enemy_list:
        if enemy.check_edges():
            change_fleet_direction(sets)
            break


def change_fleet_direction(sets):
    """将所有的敌人战机向下移动，并且调整敌人战机的移动方向"""
    for enemy in sets.enemy_list:
        enemy.rect.y += sets.enemy_drop_speed

    sets.enemy_direction *= (-1)


def blit_enemy_fleet_img(sets):
    for enemy in sets.enemy_list:
        enemy.blit_img()