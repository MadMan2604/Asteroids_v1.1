
# Enemy class 
import pygame 
import math
import random

from scripts.settings import *
from scripts.player import * 

class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Red bullet
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)  # Position of bullet
        self.vel = dir * 10  # Velocity of bullet

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ship_image = 'assets/sprites/spaceship.png'
        self.image = pygame.image.load(self.ship_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Spawn at the right corner
        self.rect.y = 0  # Spawn at the top
        self.direction = -1  # Move to the left
        self.speed = 5  # Speed of movement
        self.shoot_timer = 0  # Timer for shooting

    def shoot(self, target_pos):
        dir = pygame.math.Vector2(target_pos) - pygame.math.Vector2(self.rect.center)
        dir.normalize_ip()
        return Enemy_bullet(self.rect.center, dir)

    def update(self, player_pos):
        # Movement logic
        self.rect.x += self.direction * self.speed

        if self.rect.x <= 80:
            self.rect.x = 80
            self.rect.y += self.speed

        if self.rect.y >= 200:
            self.direction = 1

        if self.rect.x >= 1200:
            self.rect.x = 1200
            self.rect.y += self.speed

        if self.rect.x <= 70:
            self.rect.x = 70
            self.rect.x += self.speed

        # Shooting logic
        self.shoot_timer += 1
        if self.shoot_timer >= 100:  # Shoot every 100 frames
            self.shoot_timer = 0
            return self.shoot(player_pos)  # Shoot towards the player's position
        return None  # Return None if not shooting this frame
