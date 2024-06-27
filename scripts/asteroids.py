import pygame
import random
import math
import os

from scripts.settings import *

# THE ASTEROID CLASS THAT GENERATES THE ASTEROIDS 
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()

        self.size = size  # 'small', 'medium', 'large'
        
        self.small_asteroid_images = {
            'sa1': SMALL_A_SPRITES + 'Asteroid_1.png',
            'sa2': SMALL_A_SPRITES + 'Asteroid_2.png',
            'sa3': SMALL_A_SPRITES + 'Asteroid_3.png',
        }
        self.medium_asteroid_images = {
            'ma1': MEDIUM_A_SPRITES + 'Asteroid_1.png',
            'ma2': MEDIUM_A_SPRITES + 'Asteroid_2.png',
            'ma3': MEDIUM_A_SPRITES + 'Asteroid_3.png',
            'ma4': MEDIUM_A_SPRITES + 'Asteroid_4.png',
            'ma5': MEDIUM_A_SPRITES + 'Asteroid_5.png',
        }
        self.large_asteroid_images = {
            'la1': LARGE_A_SPRITES + 'Asteroid_1.png',
            'la2': LARGE_A_SPRITES + 'Asteroid_2.png',
            'la3': LARGE_A_SPRITES + 'Asteroid_3.png',
            'la4': LARGE_A_SPRITES + 'Asteroid_4.png',
            'la5': LARGE_A_SPRITES + 'Asteroid_5.png',
            'la6': LARGE_A_SPRITES + 'Asteroid_6.png',
        }

        # Select a random asteroid image based on size
        if self.size == 'small':
            self.asteroid_images = self.small_asteroid_images
            self.size_value = 30  # Fixed size for small asteroids
        elif self.size == 'medium':
            self.asteroid_images = self.medium_asteroid_images
            self.size_value = 60  # Fixed size for medium asteroids
        elif self.size == 'large':
            self.asteroid_images = self.large_asteroid_images
            self.size_value = 120  # Fixed size for large asteroids

        image_name = random.choice(list(self.asteroid_images.keys()))
        self.image = pygame.image.load(self.asteroid_images[image_name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size_value, self.size_value))

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)
        self.angle = random.uniform(0, 360)
        self.speed = random.uniform(1, 3)

    def update(self):
        # Move the asteroid
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
