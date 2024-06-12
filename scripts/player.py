import pygame
import random
import math
import os
import time

from scripts.settings import *
from pygame.locals import *


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 30
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(BLACK)
        # Draw triangle using lines
        pygame.draw.line(self.image, WHITE, (self.size // 2, 0), (self.size, self.size), 2)
        pygame.draw.line(self.image, WHITE, (self.size // 2, 0), (0, self.size), 2)
        pygame.draw.line(self.image, WHITE, (0, self.size), (self.size, self.size), 2)
        self.original_image = self.image  # Store the original image for rotation
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.angle = 0
        self.speed = 2  # Adjust player speed as needed
        self.bullet_group = pygame.sprite.Group()  # Group to hold bullets

    def update(self):
        # Player movement keys
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        # Update player angle
        if dx != 0 or dy != 0:  # Only update angle if moving
            self.angle = math.degrees(math.atan2(dy, dx)) - 90
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        # Update player position
        self.rect.x += dx
        self.rect.y += dy

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
