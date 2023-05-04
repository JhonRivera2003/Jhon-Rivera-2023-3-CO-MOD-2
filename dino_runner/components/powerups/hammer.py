from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE, HAMMER, HAMMER_TYPE

class Hammer(Powerup):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        
