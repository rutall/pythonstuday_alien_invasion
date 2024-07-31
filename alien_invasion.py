import sys

import pygame as pg

#定义一个类，用于初始化游戏窗口和监听键盘鼠标的事件
class AlienInvasion:
    def __init__(self):
        pg.init()

        #创建一个长1200，宽800的窗口
        self.screen = pg.display.set_mode((1200, 800))

    def run_game(self):
        while True:
            #侦听键盘和鼠标事件
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            #显示最近绘制的屏幕
            pg.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()