from dino_runner.utils.constants import HAMMER, POWER3_TYPE
from dino_runner.components.power_ups.power_up import  PowerUp

class Hammer(PowerUp):

    def __init__(self):
        super().__init__(HAMMER, POWER3_TYPE)
