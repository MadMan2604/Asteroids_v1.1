# script for the title screen game state 
import pygame, sys 

from scripts.settings import * 
from states.base_state import BaseState
from scripts.buttons import Button

class TitleScreen(BaseState):
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

        """"initialise music"""
        pygame.mixer.init()
        # tts_music = "assets/music/asteroids.wav"
        # pygame.mixer.music.load(tts_music)
    
    def update(self, events):
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                """click the play button"""
                if self.play_button.collidepoint(event.pos):
                    """transitions the state"""
                    self.game.state_manager.change_state("game")
                elif self.options_button.collidepoint(event.pos):
                    print("Options screen")
                    self.game.state_manager.change_state("options_screen")
                elif self.instructions_button.collidepoint(event.pos):
                    print("Instructions")
                    self.game.state_manager.change_state("information_screen")
                elif self.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        """clear the screen"""
        self.screen.fill(BLACK)
        
        """title screen background"""
        title_screen_bg = pygame.image.load(BACKGROUND_PATH + 'title_screen_bg.png')
        title_screen_bg = pygame.transform.scale(title_screen_bg, (WIDTH, HEIGHT))
        self.screen.blit(title_screen_bg, (0, 0))

        """draw the title screen text"""
        title_screen_text = self.font.render("ASTEROIDS", True, WHITE)
        self.screen.blit(title_screen_text, (300, 200))

        """draw the buttons onto the screen"""
        self.play_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Play", WHITE, self.font1, BLACK)
        self.options_button = self.button.draw_button(self.screen, 400, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Options", WHITE, self.font1, BLACK)
        self.instructions_button = self.button.draw_button(self.screen, 800, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Instructions", WHITE, self.font1, BLACK)
        self.quit_button = self.button.draw_button(self.screen, 1100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", WHITE, self.font1, BLACK)

        """update the display"""
        pygame.display.flip()
        self.clock.tick(FPS)







