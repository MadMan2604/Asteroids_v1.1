import pygame
import random
import math
import os 
import sys 

from scripts.settings import *
from scripts.asteroids import Asteroid
from scripts.player import Player
from scripts.buttons import Button
from states.game_over_state import GameOver
from states.base_state import BaseState
from scripts.bullet import Bullet
from scripts.enemy import Enemy

# THE MAIN GAME CLASS 
class InGame(BaseState):

    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.clock = pygame.time.Clock()
        self.button = Button()

        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.spaceships = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()  # Add group for enemy bullets
        self.player = Player()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.spaceships)

        # spawning counters
        self.spawn_rate_asteroids = 100  # Adjust spawn rate as needed
        self.spawn_rate_spaceships = random.randint(1000, 5000)
        self.spawn_counter_asteroids = 0
        self.spawn_counter_spaceships = 0
        self.paused = False 
        
        # Other game logic
        self.points = 0
        self.lives = 5
        self.heart_img = pygame.image.load(SPRITES + 'heart.png')
        self.heart_width, self.heart_height = self.heart_img.get_size()
        self.hearts = [self.heart_img for _ in range(self.lives)]

        # Initialize fonts
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)
        self.font5 = pygame.font.Font(FONT1, 50)

    # draw the hearts 
    def draw_hearts(self, screen):
        for i in range(self.lives):
            screen.blit(self.hearts[i], (10 + i * (self.heart_width + 10), 50))
    
    # draw the points metre at the topleft of the screen
    def draw_points(self, screen):
        font = pygame.font.SysFont(FONT1, 50)
        points_txt = font.render(str(self.points), True, WHITE)
        screen.blit(points_txt, (10, 10))

    def check_collisions(self, player, asteroids, bullets, spaceships, enemy_bullets):
        for asteroid in asteroids:
            if player.rect.colliderect(asteroid.rect):
                if player.invincibility_timer == 0:
                    self.lives -= 1
                    player.invincibility_timer = 60
                    player.colliding = True # set the collisions to true
                    if self.lives == 0: 
                        self.game.state_manager.change_state("game_over")
                break # exit the loop after processing the first collision

        for spaceship in spaceships:
            if player.rect.colliderect(spaceship.rect):
                if player.invincibility_timer == 0:
                    self.lives -= 1
                    player.invincibility_timer = 60
                    player.colliding = True # set the collisions to true
                    if self.lives == 0: 
                        self.game.state_manager.change_state("game_over")
                break # exit the loop after processing the first collision
        
        # Check for bullet-asteroid collisions
        collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)
        for bullet, asteroid_list in collisions.items():
            for asteroid in asteroid_list:
                if asteroid.size == 'small':
                    self.points += 100
                if asteroid.size == 'medium':
                    self.points += 50
                if asteroid.size == 'large':
                    self.points += 20
        
        # check for bullet-spaceship collisions
        collisions = pygame.sprite.groupcollide(bullets, spaceships, True, True)
        for bullet, collided_spaceships in collisions.items():
            # add logic here
            print("shot spaceship")
            self.points += 1000

        # Check for enemy bullet collisions with player
        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            if player.invincibility_timer == 0:
                    self.lives -= 1
                    player.invincibility_timer = 60
                    player.colliding = True # set the collisions to true
                    if self.lives == 0: 
                        self.game.state_manager.change_state("game_over")                        

    def update(self, events):
        # Process input/events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused


        if not self.paused:
            # Update all sprites except spaceships (Enemy)
            for sprite in self.all_sprites:
                if isinstance(sprite, Enemy):
                    bullet = sprite.update(self.player.rect.center)
                    if bullet:
                        self.all_sprites.add(bullet)
                        self.enemy_bullets.add(bullet)
                else:
                    sprite.update()

            # Spawn asteroids
            self.spawn_counter_asteroids += 1 
            if self.spawn_counter_asteroids >= self.spawn_rate_asteroids:
                size = random.choice(['small', 'medium', 'large'])  # Randomly choose a size
                asteroid = Asteroid(size)
                self.all_sprites.add(asteroid)
                self.asteroids.add(asteroid)
                self.spawn_counter_asteroids = 0

            
            # Spawn the Spaceship
            self.spawn_counter_spaceships += 1
            if self.spawn_counter_spaceships >= self.spawn_rate_spaceships:
                spaceship = Enemy()
                self.all_sprites.add(spaceship)
                self.spaceships.add(spaceship)
                self.spawn_counter_spaceships = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.rotate_left()
            if keys[pygame.K_d]:
                self.player.rotate_right()
            if keys[pygame.K_w]:
                self.player.accelerate()
            if keys[pygame.K_s]:
                self.player.decelerate()
            if keys[pygame.K_SPACE] and self.player.can_shoot():
                bullet = Bullet(self.player.rect.center, -self.player.angle)
                self.all_sprites.add(bullet)
                self.bullets.add(bullet)

            # Draw / render
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.check_collisions(self.player, self.asteroids, self.bullets, self.spaceships, self.enemy_bullets)
            self.draw_points(self.screen)
            self.draw_hearts(self.screen)

        else: 
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.resume_button.collidepoint(event.pos):
                        self.paused = False 
                    if self.restart_button.collidepoint(event.pos):
                        self.game.state_manager.restart_state("game")
                    if self.options_button.collidepoint(event.pos):
                        print("Options Screen")
                    if self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # DRAW THE TITLE SCREEN NAME
            pause_screen_text = self.font2.render("PAUSED", True, WHITE)
            self.screen.blit(pause_screen_text, (375, 200))
            self.resume_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Resume", WHITE, self.font1, BLACK)
            self.restart_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Restart", WHITE, self.font1, BLACK)
            self.options_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
            self.quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)

        pygame.display.update()
        self.clock.tick(FPS)
