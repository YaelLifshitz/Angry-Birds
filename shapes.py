import pygame
from random import randint
import os
Angry_Birds_Game_folder = os.path.dirname(__file__)
img_folder = os.path.join(Angry_Birds_Game_folder, "img")
#player_image = pygame.image.load(os.path.join(img_folder, 'plain.png')).convert()
PINK_BACKGROUND = (255, 20, 147)
LIGHT_PINK = (255, 174, 201)

class Plain(pygame.sprite.Sprite):
    # the constructor/ sprite for the Plain
    def __init__(self):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'plain.png')).convert()
        self.image.set_colorkey(PINK_BACKGROUND)
        # Every image has a rectangle around it- the image size - the get_rect function gives us that
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (0, 0)
        self.speedx = 0
        self.speedy = 0


    # the next few methodes role is to find the plain locations each time we want
    def update_loc_mouse(self, mouse_point):
            self.rect.x, self.rect.y = mouse_point
            '''
            if self.rect.x < 600:
                self.rect.x = 600
            elif self.rect.x > 790:
                self.rect.x = 790
            '''

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



class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
