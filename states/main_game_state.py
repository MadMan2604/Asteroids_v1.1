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
        self.player = Player()
        self.all_sprites.add(self.player)
        self.spawn_rate = 100  # Adjust spawn rate as needed
        self.spawn_counter = 0
        self.paused = False 
        # Bullet variables

        """initialise the fonts"""
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)



       
    
    def check_collisions(self, player, asteroids):
        for asteroid in asteroids:
            if player.rect.colliderect(asteroid.rect):
                self.game.state_manager.change_state("game_over")

    def update(self, events):
        # Main game loop
        

            # Process input/events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    
            
                
            if not self.paused:
                # Update
                self.all_sprites.update()
                # Spawn asteroids
                self.spawn_counter += 1
                if self.spawn_counter >= self.spawn_rate:
                    asteroid = Asteroid()
                    self.all_sprites.add(asteroid)
                    self.asteroids.add(asteroid)
                    self.spawn_counter = 0
                
            
                # Draw / render
                self.screen.fill(BLACK)
                self.all_sprites.draw(self.screen)
                self.all_sprites.update()
                self.check_collisions(self.player, self.asteroids)

                pygame.display.update()
            
            else: 
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

                # DRAW THE TITLE SCREEN NAME
                pause_screen_text = self.font2.render("PAUSED", True, WHITE)
                self.screen.blit(pause_screen_text, (375, 200))
                self.resume_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Resume", WHITE, self.font1, BLACK)
                self.restart_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Restart", WHITE, self.font1, BLACK)
                self.options_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
                self.quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)
                
            pygame.display.update()
            self.clock.tick(FPS)
        
        
            

