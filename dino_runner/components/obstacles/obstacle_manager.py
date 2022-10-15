import random

import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, POWER1_TYPE, POWER2_TYPE, POWER3_TYPE


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.deathsound = pygame.mixer.Sound('dino_runner/assets/GameSounds/minecraft-death-sound-effect.mp3')
        


    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
                cactus = Cactus(cactus_type)
                self.obstacles.append(cactus)
            else:
                bird = Bird(BIRD)
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                

            #salida del escudo
                if game.player.type ==POWER1_TYPE:
                    game.playing = True
                    break
                else:
                    game.playing = False
                    
            #salida del martillo
                if game.player.type == POWER3_TYPE:
                    game.playing = True
                    self.obstacles.remove(obstacle)
                    break
                else:
                    game.playing = False
                    
            #salida del corazon
                if game.player.type == POWER2_TYPE:
                    game.playing = True
                    self.obstacles.remove(obstacle)
                    break
                elif game.playing: False
                    
                else:
                    game.playing = False
                    game.death_count += 1
                    self.deathsound.play()



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []


# import pygame
# import random

# from dino_runner.utils.constants import SMALL_CACTUS, SHIELD_TYPE
# from dino_runner.components.obstacles.cactus import Cactus

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []

#     def update(self, game):
#         if len(self.obstacles) == 0:
#             cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
#             cactus = Cactus(cactus_type)
#             self.obstacles.append(cactus)

#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)

#             if game.player.dino_rect.colliderect(obstacle):
#                 if game.player.type != SHIELD_TYPE:
#                     pygame.time.delay(1000)
#                     game.playing = False
#                     game.death_count += 1
#                     break
#                 else:
#                     self.obstacles.remove(obstacle)

#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

#     def reset_obstacles(self):
#         self.obstacles = []










# import pygame
# import random
# from dino_runner.utils.constants import SHIELD_TYPE, SMALL_CACTUS
# from dino_runner.components.obstacles.cactus import Cactus
# from dino_runner.components.obstacles.bird import Bird

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []

#     def update(self, game):

#         if len(self.obstacles) == 0:
#             cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
#             cactus = Cactus(cactus_type)
#             self.obstacles.append(cactus)
#         # else:
#         #     bird = Bird(BIRD)
#         #     self.obstacles.append(bird)

#             #aqui se actualiza para los pajaros

#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 # if game.player.type != SHIELD_TYPE:
#                     Print('There was a collision')
#                     pygame.time.delay(1000)
#                     game.death_count += 1
#                     game.playing = False
#                     break
#             else:
#                 self.obstacles.remove(obstacle)


#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

#     def reset_obstacles(self):
#         self.obstacles = []