# THE SCRIPT FOR THE BUTTONS USED IN THE TITLE SCREEN, PAUSE MENU, AND THE GAME OVER SCREEN
import pygame
import sys 

from scripts.settings import * 

# CLASS FOR THE BUTTONS
class Button: 
    # CREATES FUNCTION TO LOAD THE BUTTONS
    def draw_button(self, surface, x, y, width, height, text, text_colour, font, hover_colour=None):
        # Calculate the dimensions for the outline button
        outline_width = width + 10  # Adding 10 pixels to the width
        outline_height = height + 10  # Adding 10 pixels to the height

        # Draw the outline button
        pygame.draw.rect(surface, pygame.Color(WHITE), (x - 5, y - 5, outline_width, outline_height))

        # Draw semi-circles on each end of the outline button
        pygame.draw.circle(surface, pygame.Color(WHITE), (x - 5, y + height // 2), height// 2)
        pygame.draw.circle(surface, pygame.Color(WHITE), (x + outline_width - 5, y + height // 2), height // 2)

        # Draw the current button (text-filled)
        button_rect = pygame.Rect(x, y, width, height)
        is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())
        default_colour = pygame.Color('black')  # Default button color is black
        hover_colour = hover_colour if is_hovered else default_colour
        pygame.draw.rect(surface, hover_colour, button_rect)

        # Draw semi-circles on each end of the current button
        pygame.draw.circle(surface, hover_colour, (x, y + height // 2), height // 2)
        pygame.draw.circle(surface, hover_colour, (x + width, y + height // 2), height // 2)

        # Render and center the text
        font_size = 36
        if is_hovered:
            font_size = 40
        button_font = pygame.font.Font(None, font_size)
        button_text = button_font.render(text, True, text_colour)
        text_rect = button_text.get_rect(center=button_rect.center)

        # Blit the text onto the current button
        surface.blit(button_text, text_rect.topleft)

        return button_rect