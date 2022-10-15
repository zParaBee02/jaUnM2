from dino_runner.utils.constants import SHIELD, POWER1_TYPE
from dino_runner.components.power_ups.power_up import  PowerUp

class Shield(PowerUp):

    def __init__(self):
        super().__init__(SHIELD, POWER1_TYPE)
        