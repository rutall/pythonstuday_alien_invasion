import sys

import pygame as pg

#定义一个类，用于初始化游戏窗口和监听键盘鼠标的事件
class AlienInvasion:
    def __init__(self):
        pg.init()

        #创建一个长1200，宽800的窗口
        self.screen = pg.display.set_mode((1200, 800))
        #初始化时钟属性
        self.clock = pg.time.Clock()
        #设置背景颜色
        self.bg_color = (230, 230, 230)
    def run_game(self):
        while True:
            #侦听键盘和鼠标事件
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            #重新绘制屏幕
            self.screen.fill(self.bg_color)
            #显示最近绘制的屏幕
            pg.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()