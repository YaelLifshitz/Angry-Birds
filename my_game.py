import pygame
from random import randint
from shapes import BlackBird
from shapes import BlueBird
from shapes import Plain
from shapes import Bullet
import os
pygame.init()
# Set up an assets folders, so the game could run on any computer
Angry_Birds_Game_folder = os.path.dirname(__file__)
img_folder = os.path.join(Angry_Birds_Game_folder, "img")
sound_folder = os.path.join(Angry_Birds_Game_folder, "sound")

# Some constant var
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 466
PINK_BACKGROUND = (255, 20, 147)
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
screen.blit(img_background, (0, 0))  # loading the image to coordinates (0,0)
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
loser_sound = pygame.mixer.Sound("sound\Smashing-Yuri_Santana-1233262689.wav")
gunshot_sound = pygame.mixer.Sound("sound\gunshot_single-mike-koenig.wav")
#pygame.mixer.music.load(os.path.join(sound_folder, "Angry Birds Theme Song.mp3"))
#pygame.mixer.music.play(loops=-1)


all_bullets = pygame.sprite.Group()
all_birds = pygame.sprite.Group()
player = Plain()
pygame.time.set_timer(pygame.USEREVENT, 500)
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
        # timing the birds creation
        if event.type == pygame.USEREVENT:
            random_choose = randint(1, 2)
            y = randint(0, 400)
            if random_choose == 1:
                bird = BlackBird(-5, y)
            else:
                bird = BlueBird(-5, y)
            all_birds.add(bird)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = player.get_pos()
            # Creating the bullets
            bullet = Bullet(x, y)
            all_bullets.add(bullet)
            screen.blit(bullet.image, bullet.get_pos())
            pygame.display.flip()
            pygame.mixer.Sound.play(gunshot_sound)
            #pygame.mixer.music.play()

        else:
            mouse_point = pygame.mouse.get_pos()
            player.update_loc_mouse(mouse_point)

    # In order to not leaving marks on background from moving objects
    screen.blit(img_background, (0, 0))



    # Updates:

    for bird in all_birds:
        bird.update_loc()
        screen.blit(bird.image, bird.get_pos())


    for bullet in all_bullets:
        bullet.update_loc()
        screen.blit(bullet.image, bullet.get_pos())
        # Checking if a bullet hits a bird and if so it will delete the bird
        for bird in all_birds:
            if (bullet.rect.colliderect(bird.rect)):
                bullet_hits_birds_list = pygame.sprite.spritecollide(bullet, all_birds, True)
                pygame.mixer.Sound.play(crash_sound)


    # Checking if a bullet hits a bird and if so it will delete the bird
    for bird in all_birds:
        if (player.rect.colliderect(bird.rect)):
            birds_hits_player_list = pygame.sprite.spritecollide(player, all_birds, True)
            pygame.mixer.Sound.play(loser_sound)


    # Draw / render
    screen.blit(player.image, player.get_pos())


    # bullet_hits_birds_list = pygame.sprite.spritecollide(all_bullets, all_birds, True)

    # mouse_point = pygame.mouse.get_pos()
    # screen.blit(player_image, mouse_point)  # In order to show the plain


pygame.quit()

