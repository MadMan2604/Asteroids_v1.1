import pygame
import random
import math
import os 

from scripts.settings import *

# THE ASTEROID CLASS THAT GENERATES THE ASTEROIDS 
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.asteroid_images = {
            'a1': SPRITES + 'Asteroid_1.png',
            'a2': SPRITES + 'Asteroid_2.png',
            'a3': SPRITES + 'Asteroid_3.png',
            'a4': SPRITES + 'Asteroid_4.png',
            'a5': SPRITES + 'Asteroid_5.png',
            'a6': SPRITES + 'Asteroid_6.png',
            'a7': SPRITES + 'Asteroid_7.png',
        }
        # Select a random asteroid image
        self.size = 64
        image_name = random.choice(list(self.asteroid_images.keys()))
        self.image = pygame.image.load(self.asteroid_images[image_name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size *2, self.size *2))
   
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