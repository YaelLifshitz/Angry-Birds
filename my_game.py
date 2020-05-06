import pygame
from shapes import BlackBird
from shapes import BlueBird
from shapes import Bullet
import random

# Constants
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 466

# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

# in order to not see the mouse arrow
pygame.mouse.set_visible(False)

# Fill screen and show
IMAGE_BACKGROUND = 'clouds background.jpg'
img_background = pygame.image.load(IMAGE_BACKGROUND)
screen.blit(img_background, (0, 0))  # loading the image to coordinates (0,0)
# if we load to (150,0) the image will move more to the right on the screen
# so the bottom rightest pixel on the screen will be (801, 465)
PINK_PLAYER = (255, 20, 147)
player_image = pygame.image.load('plain.png').convert()
player_image.set_colorkey(PINK_PLAYER)
#the size of the plain
screen.blit(player_image, [220, 300])
pygame.display.flip()

# refreshing screen rate for moving objects
clock = pygame.time.Clock()
REFRESH_RATE = 200  # the screen updates itself 60 times per secound.

# setting of mouse movement:
LEFT = 1
SCROLL = 2
RIGHT = 3

# putting music
SOUND_FILE = "Angry Birds Theme Song.mp3"
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.play(loops=-1)

vx_blue = 0
vy_blue = 0
vx_black = 0
vy_black = 100


bullet_list = pygame.sprite.Group()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            mouse_point = pygame.mouse.get_pos()
            screen.blit(player_image, mouse_point)
            bullet = Bullet(x, y)
            #vx_bullet = x + 10
            #vy_bullet = x + 10
            #bullet.update_v(vx_bullet, vy_bullet)
            bullet_list.add(bullet)

        else:
            x, y = pygame.mouse.get_pos()


    black_bird1 = BlackBird(0, 100)
    vx_black = vx_black + 1
    black_bird1.update_v(vx_black, 0)
    black_bird1.update_loc()
    screen.blit(black_bird1.image, black_bird1.get_pos())
    pygame.display.flip()

    blue_bird1 = BlueBird(0, 100)
    vx_blue = vx_blue + 2
    blue_bird1.update_v(vx_blue, 0)
    blue_bird1.update_loc()
    screen.blit(blue_bird1.image, blue_bird1.get_pos())
    pygame.display.flip()

    for bullet in bullet_list:
        #vx_bullet = x - 10
        #vy_bullet = x
        bullet.update_loc()
        screen.blit(bullet.image, bullet.get_pos())
        pygame.display.flip()










    screen.blit(img_background, (0, 0))
    # putting the birds:
    # black_bird1 = BlackBird(100, 100)


    clock.tick(REFRESH_RATE)

    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    pygame.display.flip()

pygame.quit()

