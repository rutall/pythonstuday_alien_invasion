import sys

from time import sleep
import pygame as pg
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

#定义一个类，用于初始化游戏窗口和监听键盘鼠标的事件
class AlienInvasion:
    def __init__(self):
        pg.init()

        #游戏启动后处于活动状态
        self.game_active = True
        #实例化Settings类
        self.settings = Settings()
        #创建一个长1200，宽800的窗口
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        #初始化时钟属性
        # 实例化Ship类
        self.ship = Ship(self)
        #实例化game_stats类
        self.stats = GameStats(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        self.clock = pg.time.Clock()
        #设置背景颜色
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Alien Invasion")
    def run_game(self):
        while True:
            #调用辅助方法，侦听键盘和鼠标事件
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    #记录按下键盘
    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_UP:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pg.K_UP:
            self.ship.moving_up = False
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        #创建一颗子弹，并将其加入编组bullets
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        #更新屏幕上的图像并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pg.display.flip()

    def _update_bullets(self):
        #更新子弹位置并删除已消失的子弹
        # 更新子弹的位置
        self.bullets.update()
        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self):
        #检查是否有外星人到达了屏幕的下边缘
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #想飞船被撞到一样处理
                break

    def _update_aliens(self):
        #更新外星舰队中所有外星人的位置
        self._check_fleet_edges()
        self.aliens.update()

        #检测外星人和飞船之间的碰撞
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #检查是否有外星人到达屏幕的下边缘
        self._check_aliens_bottom()

    def _create_fleet(self):
        #创建一个外星舰队
        #创建一个外星人,再不断添加，知道没有空间再添加外星人位置
        #外新人的间距为外星人的宽度和外星人的高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y <(self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height
    def _create_alien(self, x_position, y_position):
        #创建一个外星人并将其放在当前行中
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        #在有外星人到达边缘时采取相应的措施
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #将整个外星舰队向下移动，并改变它们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        #响应飞船和外星人的碰撞

        if self.stats.ships_left >0:
        # 将ships_left减1
            self.stats.ships_left -= 1

            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            #创建一个新的外星舰队，并将飞船放在屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()