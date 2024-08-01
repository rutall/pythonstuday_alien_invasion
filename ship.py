import pygame

class Ship:
    #管理飞船类
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.moving_right = False
        self.moving_left = False


        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/spider.bmp')
        self.rect = self.image.get_rect()
        #每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    #定义飞船左右移动距离
    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)