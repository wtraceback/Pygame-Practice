import pygame
import sys


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

    # 重绘屏幕对象
    pygame.display.update()


def blit_bg_img(sets, screen):
    # 绘制背景图片
    screen.blit(sets.bg_img, sets.bg_img_rect)


def update_ball(sets, baffle, ball):
    # 更新弹球的坐标
    ball.update()

    # 检测弹球碰到左右墙壁以及顶上的墙壁
    if ball.rect.left < 0 or ball.rect.right > sets.screen_width:
        sets.ball_speed_factor[0] *= -1
    # if ball.rect.top < 0 or ball.rect.bottom > sets.screen_height:
    if ball.rect.top < 0:
        sets.ball_speed_factor[1] *= -1

    #  检测弹球触碰到屏幕底部
    if ball.rect.bottom > sets.screen_height:
        pass

    # 检测弹球的碰撞
    if collided(ball, baffle):
        sets.ball_speed_factor[1] *= -1


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
