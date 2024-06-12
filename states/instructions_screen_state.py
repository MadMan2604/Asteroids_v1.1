""""script for the instructions screen"""
import pygame
import sys

from scripts.settings import *
from states.base_state import BaseState
from scripts.buttons import Button

class InstructionsScreen(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.clock = pygame.time.Clock()
        self.button = Button()

        """initialise tick counter"""
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.time_passed = (self.current_time - self.start_time) / 1000.0
        
        """initialise font"""
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)

        """text to be displayed"""
        self.text = ["The aim of the game is to avoid all the asteroids and shoot down any space ships.",
                    "Shooting any asteroids and UFO's will earn the player points.",
                    "If you collide with an asteroids you loose."]
        
        """typewriter effect (text speed)"""
        self.text_speed = 50 # characters per second

    
    
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.collidepoint(event.pos):
                    print("returned to title screen")
                    self.game.state_manager.change_state("title_screen")

        """clear the screen"""
        self.screen.fill(BLACK)

        """load the instructions title"""
        instructions_txt = self.font2.render("Instructions", True, WHITE)
        self.screen.blit(instructions_txt, (0, 0))


        """load the buttons"""
        self.back_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Back", WHITE, self.font1, BLACK)

        """update the display window"""
        pygame.display.flip()