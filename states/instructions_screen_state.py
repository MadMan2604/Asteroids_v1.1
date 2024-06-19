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

        """initialise font"""
        self.font = pygame.font.Font(FONT1, 150)
        self.font1 = pygame.font.Font(FONT2, 80)
        self.font2 = pygame.font.Font(FONT3, 80)
        self.font3 = pygame.font.Font(FONT4, 80)
        self.font4 = pygame.font.Font(FONT4, 40)

        """text to be displayed"""
        self.text = ("The aim of the game is to avoid all the asteroids and shoot down any space ships.",
                     "Shooting any asteroids and UFO's will earn the player points.",
                     "If you collide with an asteroid you lose.", 
                     "Use W A S D to move and SPACE to shoot.")
    
    def render_text_paragraph(self, surface, text, font, color, max_width, start_pos):
        words = text.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            # Check if adding the word exceeds the max width
            test_line = current_line + word + ' '
            if font.size(test_line)[0] > max_width:
                lines.append(current_line)
                current_line = word + ' '
            else:
                current_line = test_line
        
        lines.append(current_line)  # Add the last line
        
        # Render each line onto the surface
        x, y = start_pos
        for line in lines:
            line_surface = font.render(line, True, color)
            surface.blit(line_surface, (x, y))
            y += font.get_height()

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
        instructions_txt = self.font3.render("Instructions", True, WHITE)
        self.screen.blit(instructions_txt, (10, 10))

        """render the text paragraphs"""
        y_offset = 100  # Starting Y position for the text
        for paragraph in self.text:
            self.render_text_paragraph(self.screen, paragraph, self.font4, WHITE, 780, (10, y_offset))
            y_offset += self.font4.get_height() * (paragraph.count(' ') // 10 + 2)  # Adjust y_offset based on text length

        """load the buttons"""
        self.back_button = self.button.draw_button(self.screen, 100, 700, BUTTON_WIDTH, BUTTON_HEIGHT, "Back", WHITE, self.font1, BLACK)

        """update the display window"""
        pygame.display.flip()

# Assuming you have a Pygame game instance and StateManager properly set up
# Example usage:
# game_instance = YourGameClass()
# instructions_screen = InstructionsScreen(game_instance)
# while True:
#     events = pygame.event.get()
#     instructions_screen.update(events)
