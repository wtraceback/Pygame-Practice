import pygame
import sys
from time import sleep

from brick import Brick


def check_events(sets, stats, screen, baffle, ball, retry_butn, level_board):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, baffle, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, baffle)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_click_retry_butn(sets, stats, screen, baffle, ball, retry_butn, level_board, mouse_x, mouse_y)


def check_keydown_events(event, baffle, ball):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        baffle.moving_right = True
    elif event.key == pygame.K_LEFT:
        baffle.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        ball.is_fire = True


def check_keyup_events(event, baffle):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        baffle.moving_right = False
    elif event.key == pygame.K_LEFT:
        baffle.moving_left = False


def check_click_retry_butn(sets, stats, screen, baffle, ball, retry_butn, level_board, mouse_x, mouse_y):
    """点击了 retry 按钮，则重新开始游戏"""
    butn_clicked = retry_butn.rect.collidepoint(mouse_x, mouse_y)
    if butn_clicked and not stats.game_active:
        # 恢复弹球最开始的移动方向
        sets.init_dynamic_sets()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 清空原有的砖块
        for brick in sets.brick_list.copy():
            sets.brick_list.remove(brick)

        # 初始化挡板和弹球的位置
        baffle.center_baffle()
        ball.reset_ball()

        # 重置统计信息(必须放在后面；由于上次结束时，小球依然在屏幕外，因此 game_active 放在最前面的话，会立即执行生命数减一操作)
        stats.reset_stats()
        stats.game_active = True

        # 重置关卡信息、生命数
        level_board.prepare_level_text()
        level_board.prepare_lifes()

        # 创建新的敌人战机舰队
        create_brick_group(sets, stats, screen)


def update_screen(sets, stats, screen, baffle, ball, retry_butn, level_board):
    """更新屏幕上的图像，并切换到新的屏幕"""
    blit_bg_img(sets, screen)

    if stats.game_active:
        # 绘制挡板
        baffle.blit_img()

        # 绘制弹球
        ball.blit_img()

        # 绘制砖块
        for brick in sets.brick_list:
            brick.blit_img()

        # 显示关卡
        level_board.show_level()
    else:
        # 绘制重玩点击按钮
        retry_butn.draw_butn()

    # 重绘屏幕对象
    pygame.display.update()


def blit_bg_img(sets, screen):
    # 绘制背景图片
    screen.blit(sets.bg_img, sets.bg_img_rect)


def update_ball(sets, stats, screen, baffle, ball, level_board, music):
    # 更新弹球的坐标
    ball.update()

    # 检测弹球碰到左右墙壁以及顶上的墙壁
    if ball.rect.left < 0 or ball.rect.right > sets.screen_width:
        sets.ball_speed_factor[0] *= sets.reverse_direction
    if ball.rect.top < 0:
        sets.ball_speed_factor[1] *= sets.reverse_direction

    # 弹球出界后，重置游戏
    if ball.rect.top > sets.screen_height:
        ball_out_of_game(stats, baffle, ball, level_board, music)

    # 检测弹球与挡板的碰撞
    if collided(ball, baffle):
        sets.ball_speed_factor[1] *= sets.reverse_direction
        music.collid_baffle.play()

    # 检测弹球与砖块的碰撞
    collisions = check_ball_brick_collide(sets, ball)
    if collisions:
        sets.ball_speed_factor[1] *= sets.reverse_direction
        music.collid_brick.play()

    if len(sets.brick_list) == 0:
        # 创建新的砖块组（升级）
        start_new_level(sets, stats, screen, baffle, ball, level_board)


def start_new_level(sets, stats, screen, baffle, ball, level_board):
    """提升关卡"""
    # 初始化挡板和弹球的位置
    baffle.center_baffle()
    ball.reset_ball()

    # 提升等级
    stats.level += 1
    level_board.prepare_level_text()

    # 创建新的砖块组
    create_brick_group(sets, stats, screen)


def ball_out_of_game(stats, baffle, ball, level_board, music):
    """弹球出界后，重置游戏"""
    if stats.life_left > 0:
        # 游戏可用的生命数减一
        stats.life_left -= 1
        level_board.prepare_lifes()

        # 初始化挡板和弹球的位置
        baffle.center_baffle()
        ball.reset_ball()

        # 暂停 0.5 秒
        sleep(0.5)
    else:
        # 显示 retry 按钮且显示光标
        stats.game_active = False
        # game_over 音效
        music.game_over.play()
        sleep(1)
        pygame.mouse.set_visible(True)


def check_ball_brick_collide(sets, ball):
    """判断弹球是否与砖块相撞"""
    crashed = []

    for brick in sets.brick_list.copy():
        if collided(ball, brick):
            crashed.append(brick)
            sets.brick_list.remove(brick)

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


def create_brick_group(sets, stats, screen):
    """创建砖块组"""
    level = stats.level % (len(sets.brick_level_group) + 1)
    level = level if level != 0 else 1

    brick_level = sets.brick_level_group['level_' + str(level)]
    brick_rows =len(brick_level)
    for brick_row in range(brick_rows):
        for brick_x_num in range(brick_level[brick_row]):
            create_brick(sets, screen, brick_x_num, brick_row)


def create_brick(sets, screen, brick_x_num, brick_row):
    # 创建砖块并设置初始位置
    new_brick = Brick(sets, screen)

    x = 5 * new_brick.rect.width + new_brick.rect.width * brick_x_num
    new_brick.rect.x = x
    y = 5 * new_brick.rect.height + new_brick.rect.height * brick_row
    new_brick.rect.y = y

    sets.brick_list.append(new_brick)
