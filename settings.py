class Settings:
    #存储游戏中所有设置的类

    def __init__(self):
        #初始化游戏的设置
        #屏幕设置
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.5
        #子弹设置
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20
        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3