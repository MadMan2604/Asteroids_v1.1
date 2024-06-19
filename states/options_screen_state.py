"""the script of the options screen"""
import pygame
import sys

from scripts.settings import *
from states.base_state import BaseState
from scripts.buttons import Button


class OptionsScreen(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.clock = pygame.time.Clock()
        self.button = Button()
    
        """initialise + define the fonts"""
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.collidepoint(event.pos):
                    print("changed bacl to title screen")
                    self.game.state_manager.change_state("title_screen")
                if self.fullscreen_button.collidepoint(event.pos):
                    self.game.toggle_fullscreen()
        
        """clear the screen"""
        self.screen.fill(BLACK)

        """load the background"""
        options_screen_bg = pygame.image.load(BACKGROUND_PATH + "title_screen_bg.png")
        options_screen_bg = pygame.transform.scale(options_screen_bg, (WIDTH, HEIGHT))
        self.screen.blit(options_screen_bg, (0, 0))

        """options screen title"""
        options_title = self.font1.render("Options", True, WHITE)
        self.screen.blit(options_title, (0, 0))

        """load the buttons"""
        self.back_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Back", WHITE, self.font1, BLACK) # the back button
        self.fullscreen_button = self.button.draw_button(self.screen, 100, 100, BUTTON_WIDTH, BUTTON_HEIGHT, "Fullscreen", WHITE, self.font1, BLACK) # the fullscreen button
        self.windowed_button = self.button.draw_button(self.screen, 100, 300, BUTTON_WIDTH, BUTTON_HEIGHT, "Windowed", WHITE, self.font1, BLACK)
        
        """update the display"""
        pygame.display.flip()
        self.clock.tick(FPS)
