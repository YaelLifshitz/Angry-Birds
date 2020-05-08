import pygame
from random import randint
import os
Angry_Birds_Game_folder = os.path.dirname(__file__)
img_folder = os.path.join(Angry_Birds_Game_folder, "img")
#player_image = pygame.image.load(os.path.join(img_folder, 'plain.png')).convert()


class Plain(pygame.sprite.Sprite):
    # the constructor/ sprite for the Plain
    def __init__(self):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'plain.png')).convert()
        PINK_BACKGROUND = (255, 20, 147)
        self.image.set_colorkey(PINK_BACKGROUND)
        # Every image has a rectangle around it- the image size - the get_rect function gives us that
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (0, 0)
        self.speedx = 0
        self.speedy = 0


    # the next few methodes rule is to find the birds locations each time we want
    def update_loc_mouse(self, mouse_point):
        self.rect.x, self.rect.y = mouse_point
        if self.rect.x < 600:
            self.rect.x = 600
        elif self.rect.x > 790:
            self.rect.x = 790

    # def update_loc_k(self):
    #     self.speedx = 0
    #     self.speedy = 0
    #     keystate = pygame.key.get_pressed()
    #     if keystate[pygame.K_LEFT]:
    #         self.speedx = -5
    #     if keystate[pygame.K_RIGHT]:
    #         self.speedx = 5
    #     self.rect.x += self.speedx
    #     if keystate[pygame.K_UP]:
    #         self.speedy = -5
    #     if keystate[pygame.K_DOWN]:
    #         self.speedy = +5
    #     self.rect.y += self.speedy

    def get_pos(self):
        return self.rect.x, self.rect.y


class BlueBird(pygame.sprite.Sprite):
    # the constructor/ sprite for the blue bird
    def __init__(self, x, y):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'angry bird blue.png')).convert()
        PINK_BACKGROUND = (255, 20, 147)
        self.image.set_colorkey(PINK_BACKGROUND)
        # Every image has a rectangle around it- the image size - the get_rect function gives us that
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = randint(1, 10)
        self.__vy = randint (-10, 10)

    # the next few methodes rule is to find the birds locations each time we want
    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.vx, self.vy


class BlackBird(pygame.sprite.Sprite):
    # the constructor
    def __init__(self, x, y):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'angry bird black.png')).convert()
        PINK_BACKGROUND = (255, 20, 147)
        self.image.set_colorkey(PINK_BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = randint(1, 10)
        self.__vy = randint(-10, 10)

    # the next few methodes rule is to find the birds locations each time we want
    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    # the next few methodes rule is to find the birds locations each time we want
    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.vx, self.vy


class Bullet(pygame.sprite.Sprite):
    # the constructor
    def __init__(self, x, y):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'bullet.png')).convert()
        PINK_BACKGROUND = (255, 20, 147)
        self.image.set_colorkey(PINK_BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = 20
        self.__vy = 0

    # the next few methodes rule is to find the birds locations each time we want
    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x -= self.__vx
        #self.rect.y -= self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy
