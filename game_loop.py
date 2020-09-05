import pygame
from random import randint
from shapes import BlackBird
from shapes import BlueBird
from shapes import Plain
from shapes import Bullet
from shapes import Button
import sys
import os



def my_function(clock, FPS, screen, all_birds, player, all_bullets, LEFT, score, life_score, myfont, gunshot_sound, crash_sound,  img_background, loser_sound):

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

        # In order to not leave marks on the background from moving objects
        screen.blit(img_background, (0, 0))



        # Updates:

        for bird in all_birds:
            bird.update_loc()
            screen.blit(bird.image, bird.get_pos())


        for bullet in all_bullets:
            bullet.update_loc()
            screen.blit(bullet.image, bullet.get_pos())
            # Checking if a bullet hits a bird and if so it will make a crushing sound and raise the player score
            # and delete the bird and the bullet
            for bird in all_birds:
                if (bullet.rect.colliderect(bird.rect)):
                    # deleting the bird from the screen
                    bullet_hits_birds_list = pygame.sprite.spritecollide(bullet, all_birds, True)
                    # deleting the bullet from th screen
                    bullet_hits_birds_list = pygame.sprite.spritecollide(bird, all_bullets, True)
                    pygame.mixer.Sound.play(crash_sound)
                    score += 1


        # Checking if a bird hits a player and if so it will make the loser sound and reduce life
        for bird in all_birds:
            if (player.rect.colliderect(bird.rect)):
                birds_hits_player_list = pygame.sprite.spritecollide(player, all_birds, True)
                pygame.mixer.Sound.play(loser_sound)
                life_score -= 1

        # Draw / render
        screen.blit(player.image, player.get_pos())

        # Score board:
        scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
        screen.blit(scoretext, (5, 10))
        # life score bord
        lifetext = myfont.render("life {0}".format(life_score), 1, (0, 0, 0))
        screen.blit(lifetext, (5, 30))

        if life_score < 0:
            return life_score


