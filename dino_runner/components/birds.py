import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH
import random
class BirdDown(Obstacle):
    def __init__(self, image):
        self.step_index = 0
        self.image = image
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 280
        
    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1
class BirdMid(Obstacle):
    def __init__(self, image):
        self.step_index = 0
        self.image = image
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220
        
    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1
class BirdUp(Obstacle):
    def __init__(self, image):
        self.step_index = 0
        self.image = image
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 170
        self.rect.x = SCREEN_WIDTH
    
    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1