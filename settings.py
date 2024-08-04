class Settings:
    def __init__(self):
        # 初始化游戏的设置
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1表示向右移动，-1表示向左移动
        self.ship_limit = 3

        # 游戏的速度缩放因子
        self.speed_scale = 1.1
        self.score_scale = 1.5

        # 最高分数的设置
        self.high_score = 0

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 定义子弹的颜色
        self.bullets_allowed = 30

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50  # 外星人的积分

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
