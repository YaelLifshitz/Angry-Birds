import pygame
from random import randint
from shapes import BlackBird
from shapes import BlueBird
from shapes import Bullet

WINDOW_WIDTH = 802
WINDOW_HEIGHT = 466
PINK_BACKGROUND = (255, 20, 147)
FPS = 60 # frames per sec
SOUND_FILE = "Angry Birds Theme Song.mp3"
IMAGE_BACKGROUND = 'clouds background.jpg' # background game image

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
    pygame.display.flip()
    # Process input (events)
    for event in pygame.event.get():
        # Check if user closed the window
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            mouse_point = pygame.mouse.get_pos()
            screen.blit(player_image, mouse_point)

            # Creating the bullets
            bullet = Bullet(x, y)
            all_bullets.add(bullet)
            screen.blit(bullet.image, bullet.get_pos())
            pygame.display.flip()

        else:
            x, y = pygame.mouse.get_pos()

    # In order to not leaving marks on background from moving objects
    screen.blit(img_background, (0, 0))


    y1 = randint(0, 400)
    y2 = randint(0, 400)
    bird = BlackBird(0, y1)
    all_birds.add(bird)
    bird = BlueBird(0, y2)
    all_birds.add(bird)


    all_birds.draw(screen)



    # Updates:

    for bird in all_birds:
        bird.update_loc()
        screen.blit(bird.image, bird.get_pos())
        #pygame.display.flip()


    for bullet in all_bullets:
        bullet.update_loc()
        screen.blit(bullet.image, bullet.get_pos())


    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    pygame.display.flip()

pygame.quit()

