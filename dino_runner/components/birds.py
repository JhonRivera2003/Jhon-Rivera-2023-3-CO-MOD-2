import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
import random
class BirdDown(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 280
class BirdMid(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 220
class BirdUp(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 170