import sys

import pygame
import pygame as pg
from settings import Settings
from ship import Ship

#定义一个类，用于初始化游戏窗口和监听键盘鼠标的事件
class AlienInvasion:
    def __init__(self):
        pg.init()

        #实例化Settings类
        self.settings = Settings()
        #创建一个长1200，宽800的窗口
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #初始化时钟属性
        # 实例化Ship类
        self.ship = Ship(self)
        self.clock = pg.time.Clock()
        #设置背景颜色
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Alien Invasion")
    def run_game(self):
        while True:
            #调用辅助方法，侦听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
            # 重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 显示最近绘制的屏幕
            pg.display.flip()


    #定义一个辅助方法（辅助方法一般只在类中调用）
    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                 sys.exit()

            #记录键盘按下实现左右移动
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True

            #记录键盘谈起实现停止移动
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()