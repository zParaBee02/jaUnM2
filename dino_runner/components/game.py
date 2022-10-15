import pygame
import random

from dino_runner.utils.constants import (BG, CLOUD, ICON,
                                         SCREEN_HEIGHT, SCREEN_WIDTH, 
                                         TITLE, FPS, FONT_STYLE, 
                                         DEFAULT_TYPE, POWER1_TYPE,
                                         POWER2_TYPE, POWER3_TYPE
                                         )

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.message import draw_message
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = random.randint(1000, 1200)
        self.y_pos_cloud = random.randint(50, 150)
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.best_score = 0


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        self.game_speed = 20
        self.score = 0
        self.power_up_manager.reset_power_ups()


    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.score = 0


    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.draw_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1200
        self.x_pos_cloud -= self.game_speed


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)


    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message(f'Power up enable for {time_to_show} seconds', 
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 50
                )
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def update_score(self):
        self.score += 2
        if self.score % 100 == 0:
            self.game_speed += 2.5

        if self.score > self.best_score:
            self.best_score = self.score

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()


    def show_menu(self):

        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message('Press any key to start', self.screen)


        else:
            draw_message('Press any key to restart', self.screen)
            draw_message(f'your score: {self.score}', self.screen, 
                            pos_x_center = half_screen_width + 425, 
                            pos_y_center = half_screen_height -275)

                                            
            draw_message(f'Death count: {self.death_count}', self.screen, 
                                pos_y_center = half_screen_height + 150)


            draw_message(f'Your best: {self.best_score}', self.screen, 
                                                pos_x_center = + 125, 
                                pos_y_center = half_screen_height -275)


        self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))

        
        pygame.display.update()
        self.handle_events_on_menu()