import pygame
from config import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed = -8, screen_height = SCREEN_HEIGHT):
        super().__init__()
        self.length = 20
        self.power = 3
        self.image = pygame.Surface((self.power, self.length))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.range = 100
        if self.range > screen_height:
            self.height_y_constraint = self.range
        else:
            self.height_y_constraint = screen_height + 50
    
    def destroy(self):
        if self.rect.y <= 50 or self.rect.y >= self.height_y_constraint:
            self.kill()
        
    def update(self):
        self.rect.y += self.speed
        self.destroy()