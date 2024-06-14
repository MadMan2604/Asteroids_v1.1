# PROJECTILE SCRIPT
import pygame, sys, os
import math

from scripts.settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle
        self.speed = 5

    def update(self):
        # Move the bullet in the direction of the angle
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

        # Remove the bullet if it goes off-screen
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)