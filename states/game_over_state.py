import pygame 
import sys 

from states.base_state import BaseState
from scripts.settings import *
from scripts.buttons import Button

class GameOver(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.clock = pygame.time.Clock()
        self.button = Button()
    
        """initialise the fonts"""
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)
    
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if self.restart_button.collidepoint(event.pos):
                    self.game.state_manager.change_state("game")
        
        """load the text for the gameover"""
        gameover_text = self.font.render("GAME OVER", True, WHITE)
        self.screen.blit(gameover_text, (300, 100))
        
        """load the buttons for the game"""
        self.quit_button = self.button.draw_button(self.screen, 600, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)
        self.restart_button = self.button.draw_button(self.screen, 600, 500, BUTTON_WIDTH, BUTTON_HEIGHT,"Restart", WHITE, self.font1, BLACK)
