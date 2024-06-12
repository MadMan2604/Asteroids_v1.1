import pygame
import random
from scripts.settings import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (25, 25), 25)
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.math.Vector2(velocity)

    def update(self):
        self.rect.center += self.velocity
        self.wrap_around_screen()

    def wrap_around_screen(self):
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
