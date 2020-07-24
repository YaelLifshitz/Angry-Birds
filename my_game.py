import pygame
from random import randint
from shapes import BlackBird
from shapes import BlueBird
from shapes import Plain
from shapes import Bullet
from shapes import Button
import sys
import os
from game_loop import my_function


pygame.init()
# Set up an assets folders, so the game could run on any computer
Angry_Birds_Game_folder = os.path.dirname(__file__)
img_folder = os.path.join(Angry_Birds_Game_folder, "img")
sound_folder = os.path.join(Angry_Birds_Game_folder, "sound")

# Some constant var
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 466
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
PINK_BACKGROUND = (255, 20, 147)
LIGHT_PINK = (255, 174, 201)
LIFES = 0
FPS = 60 # frames per sec
SOUND_FILE = "Angry Birds Theme Song.mp3"


# setting of mouse movement:
LEFT = 1
SCROLL = 2
RIGHT = 3

## initialzing pygame and creating a window

# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Angry Birds Game")
img_background = pygame.image.load(os.path.join(img_folder, 'clouds background.jpg')).convert()
screen.blit(img_background, (0, 0)) # loading the image to coordinates (0,0)
# if we load to (150,0) the image will move more to the right on the screen
# so the bottom rightest pixel on the screen will be (801, 465)

# init player- the plain
pygame.mouse.set_visible(False) # in order to not see the mouse arrow

player_image = pygame.image.load(os.path.join(img_folder, 'plain.png')).convert()
player_image.set_colorkey(PINK_BACKGROUND)
screen.blit(player_image, [220, 300]) #the size of the plain
pygame.display.flip()

# refreshing screen rate for moving objects
clock = pygame.time.Clock()

# init music
pygame.mixer.init()
pygame.mixer.music.load('sound\Angry Birds Theme Song.mp3')
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound("sound\Bomb Explosion 1-SoundBible.com-980698079.wav")
winning_sound = pygame.mixer.Sound("sound\Ta Da-SoundBible.com-1884170640.wav")
loser_sound = pygame.mixer.Sound("sound\Smashing-Yuri_Santana-1233262689.wav")
gunshot_sound = pygame.mixer.Sound("sound\gunshot_single-mike-koenig.wav")
#pygame.mixer.music.load(os.path.join(sound_folder, "Angry Birds Theme Song.mp3"))
#pygame.mixer.music.play(loops=-1)


all_bullets = pygame.sprite.Group()
all_birds = pygame.sprite.Group()
player = Plain()
pygame.time.set_timer(pygame.USEREVENT, 500)

score = 0 # player score
life_score = 0 # How many times the player can touch the birds before loosing
myfont = pygame.font.SysFont("monospace", 16)

# to play I need to call the game_loop function
# I need to do the start over button

life_score = my_function(clock, FPS, screen, all_birds, player, all_bullets, LEFT, score, life_score, myfont, gunshot_sound, crash_sound,  img_background, loser_sound)
if life_score < 0:
    # img_background = pygame.image.load(os.path.join(img_folder, 'the game you just lost it.jpg')).convert()
    # screen.blit(img_background, (0, 0))
    finish = False
    while not finish and life_score < 0:
        clock.tick(FPS)
        pygame.display.update()
        img_background = pygame.image.load(os.path.join(img_folder, 'the game you just lost it.jpg')).convert()
        screen.blit(img_background, (100, 50))
        pygame.mouse.set_visible(True)  # in order to see the mouse arrow
        # making the button
        start_over_button = Button(LIGHT_PINK, 335, 401, 150, 50, 'Start Over :)')
        # drawing and adding a frame in the color specified
        start_over_button.draw(screen, (0, 0, 0))
        for event in pygame.event.get():
            mouse_point = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEMOTION:
                if start_over_button.isOver(mouse_point):
                    start_over_button.color = (255, 34, 106)
                else:
                    start_over_button.color = LIGHT_PINK

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_over_button.isOver(mouse_point):
                    score = 0
                    life_score = 0

                    # Init screen
                    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("Angry Birds Game")
                    img_background = pygame.image.load(os.path.join(img_folder, 'clouds background.jpg')).convert()
                    screen.blit(img_background, (0, 0))  # loading the image to coordinates (0,0)
                    # if we load to (150,0) the image will move more to the right on the screen
                    # so the bottom rightest pixel on the screen will be (801, 465)

                    #init the birds and bullets and the player
                    all_bullets = pygame.sprite.Group()
                    all_birds = pygame.sprite.Group()
                    player = Plain()

                    life_score = my_function(clock, FPS, screen, all_birds, player, all_bullets, LEFT, score,
                                             life_score, myfont, gunshot_sound, crash_sound, img_background,
                                             loser_sound)

pygame.quit()

# just checking hf
