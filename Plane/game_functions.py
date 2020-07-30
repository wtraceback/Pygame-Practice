import sys
import pygame
from time import sleep
import json

from bullet import Bullet
from enemy import Enemy


def check_events(sets, screen, stats, score_board, fighter, start_butn):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            set_stored_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sets, screen, stats, fighter)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, fighter)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            check_click_start_butn(sets, screen, stats, score_board, fighter, start_butn, pos)


def check_keydown_events(event, sets, screen, stats, fighter):
    """响应按键"""
    if event.key == pygame.K_LEFT:
        fighter.moving_left = True
    elif event.key == pygame.K_RIGHT:
        fighter.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(sets, screen, fighter)
    elif event.key == pygame.K_q:
        set_stored_high_score(stats)
        sys.exit()


def  check_keyup_events(event, fighter):
    """响应松开"""
    if event.key == pygame.K_LEFT:
        fighter.moving_left = False
    elif event.key == pygame.K_RIGHT:
        fighter.moving_right = False


def check_click_start_butn(sets, screen, stats, score_board, fighter, start_butn, pos):
    """点击了开始按钮后，将开始游戏"""
    butn_clicked = start_butn.rect.collidepoint(pos[0], pos[1])
    if butn_clicked and not stats.game_active:
        # 重置 子弹、敌人战机、战斗机 的移动速度以及 敌人战机 的移动方向
        sets.init_dynamic_sets()

        # 重置统计信息
        stats.game_active = True
        stats.reset_stats()
        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置得分和等级以及剩余战斗机的数目
        score_board.prepare_score_text()
        score_board.prepare_level_text()
        score_board.prepare_fighters()

        # 清空 子弹列表
        for b in sets.bullet_list.copy():
            sets.bullet_list.remove(b)

        # 清空 敌人战机舰队列表
        for e in sets.enemy_list.copy():
            sets.enemy_list.remove(e)

        # 创建新的敌人战机舰队
        create_enemy_fleet(sets, screen, fighter)

        # 将战斗机移动至画面正中央
        fighter.center_fighter()


# def collidepoint(stats, start_butn, pos):
#     mouse_x = pos[0]
#     mouse_y = pos[1]
#
#     if start_butn.rect.x <= mouse_x and mouse_x <= start_butn.rect.x + start_butn.rect.w:
#         if start_butn.rect.y <= mouse_y and mouse_y <= start_butn.rect.y + start_butn.rect.h:
#             stats.game_active = True
#
#     return False


def update_screen(sets, screen, stats, score_board, fighter, start_butn):
    # 绘制背景图
    blit_bg_image(sets, screen)

    # 绘制子弹
    blit_bullets_img(sets)

    # 绘制战斗机
    fighter.blit_img()

    # 绘制敌人舰队
    blit_enemy_fleet_img(sets)

    # 开始游戏前，显示开始按钮
    if not stats.game_active:
        start_butn.draw_butn()

    # 显示得分
    score_board.show_score()

    # 重新绘制游戏窗口
    pygame.display.flip()
    # pygame.display.update()


def blit_bg_image(sets, screen):
    """绘制背景图"""
    screen.blit(sets.bg_img, sets.bg_img_rect)


def fire_bullet(sets, screen, fighter):
    if len(sets.bullet_list) < sets.bullet_max_num:
        new_bullet = Bullet(sets, screen, fighter)
        sets.bullet_list.append(new_bullet)


def update_bullets_coordinate(sets, screen, stats, score_board, fighter):
    # 更新子弹的坐标
    for b in sets.bullet_list:
        b.update_coordinate()

    # 删除超出边界的子弹
    for b in sets.bullet_list.copy():
        if b.rect.bottom <= 0:
            sets.bullet_list.remove(b)

    # 响应子弹和敌人战机的碰撞 & 敌人战机全部被击落后，重新创建敌人战机舰队
    check_bullet_enemy_collisions(sets, screen, stats, score_board, fighter)


def check_bullet_enemy_collisions(sets, screen, stats, score_board, fighter):
    # 检测更新后的子弹是否集中敌人战机，如果有，就删除相应的子弹和敌人战机
    collitions = list_collide(sets)

    # 将每次击中的敌人战机，记入得分中
    if collitions:
        for enemys in collitions.values():
            stats.score += sets.each_enemy_score * len(enemys)
            score_board.prepare_score_text()

        check_high_score(stats, score_board)

    # 删除现有的子弹并重新创建敌人战机舰队
    if len(sets.enemy_list) == 0:
        for b in sets.bullet_list.copy():
            sets.bullet_list.remove(b)

        # 提升游戏的设置
        sets.increase_speed()

        # 提升等级
        stats.level += 1
        score_board.prepare_level_text()

        create_enemy_fleet(sets, screen, fighter)


def list_collide(sets):
    """遍历所有的子弹，记录其中和敌机相撞的子弹与敌机"""
    crashed = {}
    for b in sets.bullet_list:
        e = check_bullet_enemy_collide(b, sets)
        if e:
            crashed[b] = e
            sets.bullet_list.remove(b)

    return crashed


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
    available_space_y = sets.screen_height - 10 * enemy_tool.rect.height - fighter_tool.rect.height
    number_enemy_rows = int(available_space_y / (2 * enemy_tool.rect.height))

    return number_enemy_rows


def create_enemy(sets, screen, enemy_number, enemy_row):
    new_enemy = Enemy(sets, screen)

    # 设置响应的敌人战机的位置
    x = new_enemy.rect.width + 2 * new_enemy.rect.width * enemy_number
    new_enemy.float_x = x
    new_enemy.rect.x = x
    y = 3 * new_enemy.rect.height + 2 * new_enemy.rect.height * enemy_row
    new_enemy.rect.y = y

    sets.enemy_list.append(new_enemy)


def update_enemy_fleet_coordinate(sets, screen, stats, score_board, fighter):
    """检测敌人战机是否碰到左右边界"""
    check_fleet_edges(sets)

    # 更新敌人战机的坐标
    for enemy in sets.enemy_list:
        enemy.update_coordinate()

    # 检测敌人战机和战斗机之间的碰撞
    if check_fighter_enemy_collide(sets, fighter):
        fighter_hit(sets, screen, stats, score_board, fighter)

    # 检测是否有敌人战机到达了屏幕底端
    check_enemy_arrive_bottom(sets, screen, stats, score_board, fighter)


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


def check_fighter_enemy_collide(sets, fighter):
    for e in sets.enemy_list:
        if collided(fighter, e):
            return e

    return None


def fighter_hit(sets, screen, stats, score_board, fighter):
    """响应被敌人战机撞到的战斗机"""
    if stats.fighter_left > 0:
        # 将 战斗机 减一
        stats.fighter_left -= 1
        # 更新左上角的战斗机的显示数目
        # score_board.fighters.pop()
        score_board.prepare_fighters()

        # 清空 子弹列表
        for b in sets.bullet_list.copy():
            sets.bullet_list.remove(b)

        # 清空 敌人战机舰队列表
        for e in sets.enemy_list.copy():
            sets.enemy_list.remove(e)

        # 创建新的敌人战机舰队
        create_enemy_fleet(sets, screen, fighter)

        # 将战斗机移动至画面正中央
        fighter.center_fighter()

        # 暂停半秒，方便玩家反应过来
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_enemy_arrive_bottom(sets, screen, stats, score_board, fighter):
    """检查是否有敌人战机到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for e in sets.enemy_list:
        if e.rect.bottom >= screen_rect.bottom:
            fighter_hit(sets, screen, stats, score_board, fighter)
            break


def blit_enemy_fleet_img(sets):
    for enemy in sets.enemy_list:
        enemy.blit_img()


def check_high_score(stats, score_board):
    """检测当前的分数是否超过最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prepare_high_score_text()


def get_stored_high_score(stats):
    """从 json 文件加载 历史最高分"""
    try:
        # Python 在当前执行的文件所在的目录中查找指定的文件
        filename = 'history_high_score.json'
        with open(filename) as file_obj:
            data = json.load(file_obj)
    except:
        # 如果读取数据失败(文件不存在或格式错误)，则使用默认值
        pass
    else:
        # 防止获取 history_high_score 属性失败
        try:
            # 如果为 0 或者是文件读取错误，则使用默认值
            if data['history_high_score'] > 0:
                stats.high_score = data['history_high_score']
                stats.history_high_score = data['history_high_score']
        except:
            # 文件数据格式没有 history_high_score 属性
            pass


def set_stored_high_score(stats):
    """当前分数超过历史最高分，则将最高分保存至 json 文件中"""
    if stats.high_score > stats.history_high_score:
        data = {
            'history_high_score': int(round(stats.high_score, -1))
        }

        filename = 'history_high_score.json'
        with open(filename, 'w') as file_obj:
            json.dump(data, file_obj)