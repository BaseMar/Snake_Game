import random
import pygame

class Food:
    def __init__(self):
        self.position = [random.randrange(1, (600 // 10)) * 10, random.randrange(1, (600 // 10)) * 10]

    def draw(self, surface):
        pygame.draw.rect(surface, "red", pygame.Rect(self.position[0], self.position[1], 10, 10))

    def reset(self):
        self.position = [random.randrange(1, (600 // 10)) * 10, random.randrange(1, (600 // 10)) * 10]
