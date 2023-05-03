import pygame 
from dino_runner.components.cactus import Cactus
from dino_runner.components.birds import BirdDown, BirdMid, BirdUp
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            cactus_large = Cactus(LARGE_CACTUS)
            bird_down = BirdDown(BIRD)
            bird_mid = BirdMid(BIRD)
            bird_up = BirdUp(BIRD)
            obstacle_type = random.choice(["small", "large", "bird_down", "bird_mid", "bird_up"])
            if obstacle_type == "small":
                self.obstacles.append(cactus)
            elif obstacle_type == "large": 
                self.obstacles.append(cactus_large)
            elif obstacle_type == "bird_down":
                self.obstacles.append(bird_down)
            elif obstacle_type == "bird_mid":
                self.obstacles.append(bird_mid)
            elif obstacle_type == "bird_up":
                self.obstacles.append(bird_up)
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []