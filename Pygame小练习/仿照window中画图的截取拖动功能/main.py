"""
功能：
仿制 window 中画图的截取图片的功能，不过很简陋

程序是基于上一层目录中的 单个弹性变化的矩形.py 写的

1、按住左键，然后拖动鼠标，画出一个矩形，边框为红色
    点击在矩形范围内，则可以拖动矩形框内的背景图
    如果是点击在矩形范围外，则初始化
2、拖动了子截图后，松开了鼠标左键
    此时的状态相当于刚画完一个矩形
        点击在矩形范围内，则可以拖动矩形框内的背景图
        如果是点击在矩形范围外，则初始化

# 目前存在的缺陷：
#    只能从左上往右下画矩形，不然会内存溢出保存
#    用来画矩形的外边框，在获取子截图后，会一直跟随着子截图，作为子截图的边框一直存在着
#    拖动的子截图的中心坐标跟鼠标坐标保持一致，子截图的中心点会出现瞬移到鼠标下方的情况
"""

import sys
import pygame


class SubImage():
    """子截图相关的类"""

    def __init__(self, screen):
        self.screen = screen
        self.img = ''
        self.rect = (0, 0, 0, 0)

    def blit_img(self):
        self.screen.blit(self.img, self.rect)


class Rectangle():
    """矩形相关的类"""

    def __init__(self, screen):
        self.screen = screen

        self.start = (0, 0)
        self.end = (0, 0)
        self.size = (0, 0)

        self.drawing = False
        self.rect_color = (255, 0, 0)
        self.border_width = 1

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.rect_color, (self.start, self.size), self.border_width)


class Configuration():
    """配置相关的类"""

    def __init__(self):
        self.size = (480, 700)
        self.caption = 'Strip background image'

        self.click_time = 0
        self.can_drag = False

        self.rects = []
        self.sub_images = []

        # 背景图
        self.bg_img = pygame.image.load('images/background.png')
        self.bg_img_rect = self.bg_img.get_rect()


def mouse_down(event, screen, configs):
    if configs.click_time == 0:
        # 确定矩形的起点
        flex_rect = Rectangle(screen)
        flex_rect.start = event.pos
        flex_rect.size = 0, 0
        flex_rect.drawing = True
        configs.rects.append(flex_rect)

    elif configs.click_time == 1:
        # 是否点击在矩形框范围内
        if (configs.sub_images[-1].rect.x < event.pos[0] and event.pos[0] < (
                configs.sub_images[-1].rect.x + configs.sub_images[-1].rect.width)) and (
                configs.sub_images[-1].rect.y < event.pos[1] and event.pos[1] < (
                configs.sub_images[-1].rect.y + configs.sub_images[-1].rect.height)):
            # 点在焦点范围内，可以拖动
            configs.can_drag = True
        else:
            # 不是点击在矩形框范围内，将所有配置项初始化
            configs.click_time = 2
            # 将原来的矩形框剔除
            configs.rects.pop()


def mouse_up(event, screen, configs):
    if configs.click_time == 0 and configs.rects:
        if configs.rects[-1].start == event.pos:
            # 点击了左键后立即松开，则判断为未画出矩形，则返回初始化
            configs.rects.pop()
            return
        else:
            # 确定矩形的尺寸大小
            configs.rects[-1].end = event.pos
            configs.rects[-1].size = configs.rects[-1].end[0] - configs.rects[-1].start[0], configs.rects[-1].end[1] - \
                                     configs.rects[-1].start[1]
            configs.rects[-1].drawing = False

            # 现在屏蔽画矩形框，改为拖拽判断
            configs.click_time = 1

            # 获取裁剪的图片
            sub_img = SubImage(screen)
            sub_img.img = screen.subsurface(pygame.Rect(configs.rects[-1].start, configs.rects[-1].size)).copy()
            # 通过 get_rect 获取到的 x 和 y 的坐标为 0， 0
            sub_img.rect = sub_img.img.get_rect()
            sub_img.rect.x = configs.rects[-1].start[0]
            sub_img.rect.y = configs.rects[-1].start[1]
            configs.sub_images.append(sub_img)

    elif configs.click_time == 1 and configs.can_drag:
        # 移动后，在其他位置松开左键,依然还可以再次拖动
        configs.can_drag = False
        # 获取移动后的子截图的坐标？

    elif configs.click_time == 2:
        configs.can_drag = False
        configs.click_time = 0


def mouse_motion(event, configs):
    if configs.click_time == 0 and configs.rects:
        if configs.rects[-1].drawing:
            # 不断变化中的矩形形状
            configs.rects[-1].end = event.pos
            configs.rects[-1].size = configs.rects[-1].end[0] - configs.rects[-1].start[0], configs.rects[-1].end[1] - \
                                     configs.rects[-1].start[1]
    elif configs.can_drag:
        # 获取拖动中的子截图的坐标
        configs.sub_images[-1].rect.center = event.pos


def event_listener(screen, configs):
    for event in pygame.event.get():
        # 关闭游戏窗口
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down(event, screen, configs)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_up(event, screen, configs)

        elif event.type == pygame.MOUSEMOTION:
            mouse_motion(event, configs)


def main():
    # 游戏配置项
    configs = Configuration()

    # 游戏的初始化、游戏窗口的设置、游戏窗口标题的设置
    pygame.init()
    screen = pygame.display.set_mode(configs.size)
    pygame.display.set_caption(configs.caption)

    while True:
        screen.blit(configs.bg_img, configs.bg_img_rect)

        # 只要存在子截图，就将其绘画出来
        if configs.sub_images:
            for temp_img in configs.sub_images:
                temp_img.blit_img()

        # 在允许绘画矩形以及拖拉子截图时，绘制矩形
        if configs.rects and configs.click_time != 2:
            configs.rects[-1].draw_rect()

        event_listener(screen, configs)

        pygame.display.update()


if __name__ == '__main__':
    main()