import pygame
import random
import sys

from scripts.settings import *
from scripts.asteroids import Asteroid
from scripts.player import Player
from scripts.buttons import Button
from states.game_over_state import GameOver
from states.base_state import BaseState

class InGame(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.clock = pygame.time.Clock()
        self.button = Button()

        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.spawn_rate = 100  # Adjust spawn rate as needed
        self.spawn_counter = 0
        self.paused = False 

        # Initialise fonts
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)

    def check_collisions(self, player, asteroids):
        for asteroid in asteroids:
            if player.rect.colliderect(asteroid.rect):
                self.game.state_manager.change_state("game_over")

    def spawn_asteroid(self):
        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            position = (0, random.randint(0, HEIGHT))
            velocity = pygame.math.Vector2(random.uniform(1, 3), random.uniform(-1, 1))
        elif side == 'right':
            position = (WIDTH, random.randint(0, HEIGHT))
            velocity = pygame.math.Vector2(random.uniform(-1, -3), random.uniform(-1, 1))
        elif side == 'top':
            position = (random.randint(0, WIDTH), 0)
            velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(1, 3))
        else:
            position = (random.randint(0, WIDTH), HEIGHT)
            velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, -3))
        
        asteroid = Asteroid(position, velocity)
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)

    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                if event.key == pygame.K_LEFT:
                    self.player.rotate_left()
                if event.key == pygame.K_RIGHT:
                    self.player.rotate_right()
                if event.key == pygame.K_UP:
                    self.player.accelerate()
                if event.key == pygame.K_DOWN:
                    self.player.decelerate()

        if not self.paused:
            self.all_sprites.update()
            self.spawn_counter += 1
            if self.spawn_counter >= self.spawn_rate:
                self.spawn_asteroid()
                self.spawn_counter = 0

            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.check_collisions(self.player, self.asteroids)
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resume_button.collidepoint(event.pos):
                        self.paused = False
                    if self.restart_button.collidepoint(event.pos):
                        self.game.state_manager.change_state("game")
                    if self.options_button.collidepoint(event.pos):
                        print("Options Screen")
                    if self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            pause_screen_text = self.font2.render("PAUSED", True, WHITE)
            self.screen.blit(pause_screen_text, (375, 200))
            self.resume_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Resume", WHITE, self.font1, BLACK)
            self.restart_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Restart", WHITE, self.font1, BLACK)
            self.options_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
            self.quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)
        
        pygame.display.update()
        self.clock.tick(FPS)
