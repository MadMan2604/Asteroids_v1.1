# PROJECTILE SCRIPT 
import pygame, sys, os 

class Projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 8 * facing 
    
    def draw(self, screen):
        self.colour = (255, 255, 255)
        self.x = self.player.rect.x 
        self.y = self.player.rect.y
        self.radius = 6 
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)