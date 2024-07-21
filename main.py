import pygame
from food import Food
from snake import Snake
from scoreboard import Scoreboard

pygame.init()
pygame.display.set_caption('Snake Game')
WINDOW_SIZE = (600, 600)
game_window = pygame.display.set_mode(WINDOW_SIZE)
fps = pygame.time.Clock()

snake_speed = 30
direction = 'RIGHT'
change_to = direction

snake = Snake()
food = Food()
score = Scoreboard()

game_is_on = True

while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            snake.change_direction(event)
        elif event.type == pygame.QUIT:
            game_is_on = False

    snake.move()
    game_window.fill("black")
    snake.draw(game_window)
    food.draw(game_window)
    score.show_score(game_window)

    # Game over conditions
    if snake.starting_position[0] < 0 or snake.starting_position[0] >= WINDOW_SIZE[0] or snake.starting_position[1] < 0 or snake.starting_position[1] >= WINDOW_SIZE[1]:
        score.game_over(game_window, snake, food)

    for block in snake.body[1:]:
        if snake.starting_position[0] == block[0] and snake.starting_position[1] == block[1]:
            score.game_over(game_window, snake, food)

    # Detect collision with food
    if snake.starting_position[0] == food.position[0] and snake.starting_position[1] == food.position[1]:
        snake.body.insert(0, list(snake.starting_position))
        score.score += 1
        food = Food()
    else:
        snake.body.pop()
        snake.body.insert(0, list(snake.starting_position))

    pygame.display.update()
    fps.tick(snake_speed)

pygame.quit()
