import pygame
import sys
from time import sleep

from brick import Brick


def check_events(baffle, ball):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, baffle, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, baffle)


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


def update_screen(sets, screen, baffle, ball):
    """更新屏幕上的图像，并切换到新的屏幕"""
    blit_bg_img(sets, screen)

    # 绘制挡板
    baffle.blit_img()

    # 绘制弹球
    ball.blit_img()

    # 绘制砖块
    for brick in sets.brick_list:
        brick.blit_img()

    # 重绘屏幕对象
    pygame.display.update()


def blit_bg_img(sets, screen):
    # 绘制背景图片
    screen.blit(sets.bg_img, sets.bg_img_rect)


def update_ball(sets, stats, screen, baffle, ball):
    # 更新弹球的坐标
    ball.update()

    # 检测弹球碰到左右墙壁以及顶上的墙壁
    if ball.rect.left < 0 or ball.rect.right > sets.screen_width:
        sets.ball_speed_factor[0] *= sets.reverse_direction
    if ball.rect.top < 0:
        sets.ball_speed_factor[1] *= sets.reverse_direction

    # 弹球出界后，重置游戏
    ball_out_of_game(sets, stats, screen, baffle, ball)

    # 检测弹球与挡板的碰撞
    if collided(ball, baffle):
        sets.ball_speed_factor[1] *= sets.reverse_direction

    # 检测弹球与砖块的碰撞
    collisions = check_ball_brick_collide(sets, ball)
    if collisions:
        sets.ball_speed_factor[1] *= sets.reverse_direction
        pass

    if len(sets.brick_list) == 0:
        # 初始化砖块和挡板的位置
        # 创建新的砖块组
        pass


def ball_out_of_game(sets, stats, screen, baffle, ball):
    """弹球出界后，重置游戏"""
    #  检测弹球触碰到屏幕底部
    if ball.rect.bottom > sets.screen_height:
        # 游戏可用的生命数减一
        stats.life_left -= 1

        # 清空砖块列表
        for brick in sets.brick_list.copy():
            sets.brick_list.remove(brick)

        # 创建新的砖块组
        create_brick_group(sets, screen)

        # 初始化挡板和弹球的位置
        baffle.center_baffle()
        ball.reset_ball()

        # 暂停 0.5 秒
        sleep(0.5)


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


def create_brick_group(sets, screen):
    """创建砖块组"""
    brick_level_group = {
        'level_1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'level_2': [10, 8, 6, 4, 2, 4, 6, 8, 10],
        'level_3': [2, 4, 6, 8, 10, 8, 6, 4, 2],
    }

    brick_level = brick_level_group['level_1']
    brick_rows =len(brick_level)
    for brick_row in range(brick_rows):
        for brick_x_num in range(brick_level[brick_row]):
            create_brick(sets, screen, brick_x_num, brick_row)


# def create_brick_group(sets, screen, baffle):
#     """创建砖块组"""
#     brick_tool = Brick(sets, screen)
#     number_brick_x = get_number_brick_x(sets, brick_tool)
#     number_brick_rows = get_number_brick_y(sets, brick_tool, baffle)
# 
#     for brick_row in range(number_brick_rows):
#         for brick_x_num in range(number_brick_x):
#             create_brick(sets, screen, brick_x_num, brick_row)


def get_number_brick_x(sets, brick_tool):
    """每一行可容纳的砖块个数"""
    available_space_x = sets.screen_width - 10 * brick_tool.rect.width
    number_x = int(available_space_x / brick_tool.rect.width)

    return number_x


def get_number_brick_y(sets, brick_tool, baffle_tool):
    """计算屏幕可容纳多少行砖块"""
    available_space_y = sets.screen_height - 5 * brick_tool.rect.height - 10 * baffle_tool.rect.height
    number_brick_rows = int(available_space_y / brick_tool.rect.height)

    return number_brick_rows


def create_brick(sets, screen, brick_x_num, brick_row):
    # 创建砖块并设置初始位置
    new_brick = Brick(sets, screen)

    x = 5 * new_brick.rect.width + new_brick.rect.width * brick_x_num
    new_brick.rect.x = x
    y = 5 * new_brick.rect.height + new_brick.rect.height * brick_row
    new_brick.rect.y = y

    sets.brick_list.append(new_brick)
