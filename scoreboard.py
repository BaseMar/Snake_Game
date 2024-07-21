import time
import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('times new roman', 30)
        self.color = "white"
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def show_score(self, surface):
        score_surface = self.font.render(f"Score: {self.score}", True, self.color)
        score_rect = score_surface.get_rect(topleft=(10, 10))
        surface.blit(score_surface, score_rect)

        high_score_surface = self.font.render(f"High Score: {self.high_score}", True, self.color)
        high_score_rect = high_score_surface.get_rect(topright=(590, 10))
        surface.blit(high_score_surface, high_score_rect)

    def game_over(self, surface, snake, food):
        game_over_surface = self.font.render('GAME OVER', True, "red")
        game_over_rect = game_over_surface.get_rect(center=(600 // 2, 600 // 3))
        surface.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        self.reset_game(snake, food)

    def reset_game(self, snake, food):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        snake.reset()
        food.reset()
