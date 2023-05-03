import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter


class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud_one = 330
        self.y_pos_cloud = 130
        self.x_pos_cloud_two = 700
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen, "Please press any key to start...")
        self.running = False
        self.score = Counter()
        self.death_menu = Menu(self.screen, "-GAME OVER-")


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                if self.obstacle_manager.deaths == 0:
                    self.show_menu()
                else:
                    self.death_show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user = pygame.key.get_pressed()
        self.player.update(user)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(CLOUD, (self.x_pos_cloud_one, self.y_pos_cloud))
        self.screen.blit(CLOUD, (self.x_pos_cloud_two, self.y_pos_cloud))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(CLOUD, (self.x_pos_cloud_one, self.y_pos_cloud))
            self.screen.blit(CLOUD, (self.x_pos_cloud_two, self.y_pos_cloud))            
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.screen.blit(ICON, (half_screen_width-50, half_screen_height-140))
        self.menu.draw(self.screen)
        self.menu.update(self)
    
    def death_show_menu(self):
        self.death_menu.reset_screen_color(self.screen)
        if  self.score.max_score:
            max_score = max(self.score.max_score)
        else:
            max_score = 0
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score.count}", True, (0,0,0))
        text2 = font.render(f"Deaths: {self.obstacle_manager.deaths}", True, (0,0,0))
        text3 = font.render(f"Max Score: {max_score}", True, (0,0,0))
        text4 = font.render("Please press any key to start...", True, (0,0,0))
        text_rect = text.get_rect()
        text2_rect = text2.get_rect()
        text3_rect = text3.get_rect()
        text4_rect = text4.get_rect()
        text2_rect.center = (550, 400)
        text_rect.center = (550, 350)
        text3_rect.center = (550, 450)
        text4_rect.center = (550, 550)
        self.screen.blit(ICON, (half_screen_width-50, half_screen_height-140))
        self.screen.blit(text, text_rect)
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)
        self.screen.blit(text4, text4_rect)
        self.death_menu.draw(self.screen)
        self.death_menu.update(self)
        
    def update_score(self):
        self.score.update()
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5

#        print(f"Score: {self.score}, Speed: {self.game_speed}")
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score.reset()
        self.player.reset()