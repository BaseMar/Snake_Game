import time
import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('times new roman', 30)
        self.color = "white"

    def show_score(self, surface):
        score_surface = self.font.render(f'Score: {self.score}', True, self.color)
        score_rect = score_surface.get_rect(center=(600 // 2, 30))
        surface.blit(score_surface, score_rect)

    def game_over(self, surface):
        game_over_surface = self.font.render('GAME OVER', True, "red")
        game_over_rect = game_over_surface.get_rect(center=(600 // 2, 600 // 3))
        surface.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()
