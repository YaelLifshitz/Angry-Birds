import pygame


class BlueBird(pygame.sprite.Sprite):
    # the constructor
    def __init__(self, x, y):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load('angry bird blue.png').convert()
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
        self.image = pygame.image.load('angry bird black.png').convert()
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
        self.image = pygame.image.load('bullet.png').convert()
        PINK_BACKGROUND = (255, 20, 147)
        self.image.set_colorkey(PINK_BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = 10
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
