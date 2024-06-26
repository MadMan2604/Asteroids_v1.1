import pygame
import math
from scripts.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        # Calculate points for an equilateral triangle
        side_length = 50
        height = side_length * (math.sqrt(3) / 2)
        half_base = side_length / 2
        pygame.draw.polygon(self.image, WHITE, [(25, 0), (0, height), (50, height)])
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.position = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.rotation_speed = 5
        self.acceleration = 0.2
        self.friction = 0.99
        self.colliding = False # collision attribute
        self.invincibility_timer = 0 # the invincibility timer
        self.last_shot_time = pygame.time.get_ticks()  # Initialize the last shot time
        self.shoot_delay = 100  # Set delay to 5 seconds (5000 milliseconds)

    def update(self):
        self.velocity *= self.friction
        self.position += self.velocity
        self.rect.center = self.position

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.wrap_around_screen()

        # decrease the invincibility timer if active
        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1

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
    
    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            self.last_shot_time = current_time
            return True
        return False