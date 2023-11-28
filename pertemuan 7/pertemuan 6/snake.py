import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Colors
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (255, 255, 255)
APPLE_COLOR = (255, 0, 0)

# Window size
WIDTH = 640
HEIGHT = 480

# Snake size
SNAKE_SIZE = 20

# Snake speed
SNAKE_SPEED = 5

# Directions
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Create the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Create the snake and apple objects
snake = [(200, 200), (220, 200), (240, 200)]
apple = (100, 100)

direction = RIGHT
clock = pygame.time.Clock()

score = 0

# Function to draw the snake on the screen
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(WIN, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

# Function to draw the apple on the screen
def draw_apple(apple):
    pygame.draw.rect(WIN, APPLE_COLOR, pygame.Rect(apple[0], apple[1], SNAKE_SIZE, SNAKE_SIZE))

# Function to handle user input
def change_direction(direction):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
            elif event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN

    return direction
    

# Main game loop
while True:
    clock.tick(SNAKE_SPEED)
    WIN.fill(BACKGROUND_COLOR)

    draw_snake(snake)
    draw_apple(apple)

    # Handling user input
    direction = change_direction(direction)

    # Checking for collisions with apple
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        score += 1
        apple = (random.randint(0, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE, random.randint(0, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)
    else:
        snake.pop()

    # Checking for collisions with the walls or itself
    if (direction == LEFT and snake[0][0] < 0) or (direction == RIGHT and snake[0][0] >= WIDTH) or (direction == UP and snake[0][1] < 0) or (direction == DOWN and snake[0][1] >= HEIGHT) or (snake[0] in snake[1:]):
        break

    # Moving the snake in the current direction
    if direction == LEFT:
        snake.insert(0, (snake[0][0] - SNAKE_SIZE, snake[0][1]))
    elif direction == RIGHT:
        snake.insert(0, (snake[0][0] + SNAKE_SIZE, snake[0][1]))
    elif direction == UP:
        snake.insert(0, (snake[0][0], snake[0][1] - SNAKE_SIZE))
    elif direction == DOWN:
        snake.insert(0, (snake[0][0], snake[0][1] + SNAKE_SIZE))

    pygame.display.update()

# Game over message
pygame.font.init()
font = pygame.font.Font(None, 36)
win_surface = font.render('You lost! Your score is: %s' % (score), True, (255, 255, 255))
win_rect = win_surface.get_rect()
win_rect.midtop = (WIDTH / 2, 10)
WIN.blit(win_surface, win_rect)
pygame.display.flip()
pygame.time.wait(5000)

pygame.quit()
quit()
