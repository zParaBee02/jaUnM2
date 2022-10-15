
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(220, 275)
        self.step_index = 0

    def draw(self, screen):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.step_index >= 10:
            self.step_index = 0

        self.step_index += 1



# import random
# import pygame
# from dino_runner.components.obstacles.obstacle import Obstacle
# from dino_runner.utils.constants import BIRD

# class Bird(Obstacle):

#     def __init__(self, image):
#         self.type = random.randint(0, 1)
#         super().__init__(image, self.type)
#         self.rect.y = random.randint(200, 300)
#         self.step.index = 0


#     def update(self, screen):
#         self.image = BIRD[0] if self.step_index < 5 else Bird[1]
#         screen.blit(self.image, (self.rect.x, self.rect.y))

#         if self.step_indexx >= 10:
#             self.step_index = 0 
#         self.step_index += 1






        

    # def __init__(self, image):
    #     self.type = 0
    #     super().__init__(image, self.pos)
    #     self.rect.y = random.randint(200, 300)    #implementar un random de la pos Y

    # def update(self, game_speed, obstacles):
    #     self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
    #     self.step_index += 1
    #     self.rect.x -= game_speed
    #     if self.step_index >= 10: 
    #         self.step_index = 0
    #     if self.rect.x < -self.rect.width:
    #         obstacles.pop()

