import pygame
import math
from scripts.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, WHITE, [(0, 50), (25, 0), (50, 50)])
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.position = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.rotation_speed = 5
        self.acceleration = 0.2
        self.friction = 0.99

    def update(self):
        self.velocity *= self.friction
        self.position += self.velocity
        self.rect.center = self.position

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

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

    def rotate_left(self):
        self.angle += self.rotation_speed

    def rotate_right(self):
        self.angle -= self.rotation_speed

    def accelerate(self):
        self.velocity += pygame.math.Vector2(self.acceleration, 0).rotate(-self.angle)

    def decelerate(self):
        self.velocity -= pygame.math.Vector2(self.acceleration, 0).rotate(-self.angle)