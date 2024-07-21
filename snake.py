import pygame

STARTING_POSITION = [100, 50]
MOVE_DISTANCE = 10
class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.starting_position = STARTING_POSITION
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def move(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.starting_position[1] -= MOVE_DISTANCE
        if self.direction == 'DOWN':
            self.starting_position[1] += MOVE_DISTANCE
        if self.direction == 'LEFT':
            self.starting_position[0] -= MOVE_DISTANCE
        if self.direction == 'RIGHT':
            self.starting_position[0] += MOVE_DISTANCE

    def change_direction(self, event):
        if event.key == pygame.K_UP and self.direction != 'DOWN':
            self.change_to = 'UP'
        if event.key == pygame.K_DOWN and self.direction != 'UP':
            self.change_to = 'DOWN'
        if event.key == pygame.K_LEFT and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if event.key == pygame.K_RIGHT and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def draw(self, surface):
        for pos in self.body:
            pygame.draw.rect(surface, "white", pygame.Rect(pos[0], pos[1], MOVE_DISTANCE, MOVE_DISTANCE))

    def reset(self):
        self.__init__()
