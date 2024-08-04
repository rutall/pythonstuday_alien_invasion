import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        # 初始化外星人并设置起始位置
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # 添加这行以获取设置

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确水平位置
        self.x = float(self.rect.x)

    def update(self):
        # 向右或向左移动外星人
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # 如果外星人位于屏幕边缘，就返回True
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
