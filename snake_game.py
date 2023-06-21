import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
width = 640
height = 480

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.segments = [(width // 2, height // 2)]
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        x, y = self.segments[0]

        if self.direction == "up":
            y -= 10
        elif self.direction == "down":
            y += 10
        elif self.direction == "left":
            x -= 10
        elif self.direction == "right":
            x += 10

        self.segments.insert(0, (x, y))
        if len(self.segments) > self.size:
            self.segments.pop()

    def change_direction(self, direction):
        if direction == "up" and self.direction != "down":
            self.direction = direction
        elif direction == "down" and self.direction != "up":
            self.direction = direction
        elif direction == "left" and self.direction != "right":
            self.direction = direction
        elif direction == "right" and self.direction != "left":
            self.direction = direction

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window, white, (segment[0], segment[1], 10, 10))

# Apple class
class Apple:
    def __init__(self):
        self.x = random.randint(0, width - 10) // 10 * 10
        self.y = random.randint(0, height - 10) // 10 * 10

    def draw(self):
        pygame.draw.rect(window, red, (self.x, self.y, 10, 10))

# Game variables
snake = Snake()
apple = Apple()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("right")

    snake.move()

    # Check for collision with apple
    if snake.segments[0] == (apple.x, apple.y):
        snake.size += 1
        apple = Apple()

    # Check for collision with walls
    if (
        snake.segments[0][0] < 0
        or snake.segments[0][0] >= width
        or snake.segments[0][1] < 0
        or snake.segments[0][1] >= height
    ):
        running = False

    # Check for collision with self
    if len(snake.segments) > 1 and snake.segments[0] in snake.segments[1:]:
        running = False

    # Clear the window
    window.fill(black)

    # Draw snake and apple
    snake.draw()
    apple.draw()

    # Update the display
    pygame.display.update()

    # Delay to control the frame rate
    clock.tick(20)

# Quit the game
pygame.quit()
