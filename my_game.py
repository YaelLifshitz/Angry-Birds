import pygame
import random
from shapes import BlackBird
from shapes import BlueBird
from shapes import Bullet

WINDOW_WIDTH = 802
WINDOW_HEIGHT = 466
PINK_BACKGROUND = (255, 20, 147)
FPS = 60 # frames per sec
SOUND_FILE = "Angry Birds Theme Song.mp3"
IMAGE_BACKGROUND = 'clouds background.jpg' # background game image

## initialzing pygame and creating a window

# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Angry Birds Game")
img_background = pygame.image.load(IMAGE_BACKGROUND)
screen.blit(img_background, (0, 0))  # loading the image to coordinates (0,0)
# if we load to (150,0) the image will move more to the right on the screen
# so the bottom rightest pixel on the screen will be (801, 465)

# init player- the plain
pygame.mouse.set_visible(False) # in order to not see the mouse arrow

player_image = pygame.image.load('plain.png').convert()
player_image.set_colorkey(PINK_BACKGROUND)
screen.blit(player_image, [220, 300]) #the size of the plain
pygame.display.flip()

# refreshing screen rate for moving objects
clock = pygame.time.Clock()

# setting of mouse movement:
LEFT = 1
SCROLL = 2
RIGHT = 3

# init music
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.play(loops=-1)


all_bullets = pygame.sprite.Group()
all_birds = pygame.sprite.Group()
## Game loop:
finish = False
while not finish:
    # Keep loop running at the same speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check if user closed the window
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            mouse_point = pygame.mouse.get_pos()
            screen.blit(player_image, mouse_point)
            bullet = Bullet(x, y)
            all_bullets.add(bullet)
        else:
            x, y = pygame.mouse.get_pos()

    # Updates:


    black_bird1 = BlackBird(0, 100)
    black_bird1.update_loc()
    screen.blit(black_bird1.image, black_bird1.get_pos())
    pygame.display.flip()

    blue_bird1 = BlueBird(0, 100)
    blue_bird1.update_loc()
    screen.blit(blue_bird1.image, blue_bird1.get_pos())
    pygame.display.flip()


    for bullet in all_bullets:
        bullet.update_loc()
        screen.blit(bullet.image, bullet.get_pos())
        pygame.display.flip()

    screen.blit(img_background, (0, 0)) # prevents from leaving plain residue on the screen
    # putting the birds:
    # black_bird1 = BlackBird(100, 100)

    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    pygame.display.flip()

pygame.quit()

