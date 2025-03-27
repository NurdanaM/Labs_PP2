import pygame
import random

pygame.init()

# Window size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Initial variables
score = 0
fruit_eaten = False
level = 1
speed = 200  
fruits_needed_for_level_up = 3 

# Initial snake parameters
head_square = [100, 100]
squares = [
    [30, 100], [40, 100], [50, 100], [60, 100], [70, 100],
    [80, 100], [90, 100], [100, 100]
]

# Function to generate fruit 
def generate_fruit():
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        fruit_coor = [fr_x, fr_y]

        # Ensure the fruit does not appear on the snake
        if fruit_coor not in squares:
            return fruit_coor

fruit_coor = generate_fruit()

direction = "right"
next_dir = "right"
done = False

# Function to handle game over
def game_over():
    global done
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("times new roman", 45)
    text_surface = font.render(f"Game Over! Score: {score}", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()
    exit()

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    # Prevent movement in opposite direction
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    # Update snake head position
    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    # Check collision with walls
    if head_square[0] < 0 or head_square[0] >= width or head_square[1] < 0 or head_square[1] >= height:
        game_over()

    # Check collision with itself
    if head_square in squares[:-1]:
        game_over()

    # Update snake body
    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    
    # Check if fruit is eaten
    if head_square == fruit_coor:
        fruit_eaten = True
        score += 10

        # Level up
        if score % (fruits_needed_for_level_up * 10) == 0:
            level += 1
            speed = max(50, speed - 20)  
    else:
        squares.pop(0)  # remove tail if fruit is not eaten
    if fruit_eaten:
        fruit_coor = generate_fruit()
        fruit_eaten = False

   
    screen.fill((170, 207, 104))

    # Display score and level
    font = pygame.font.SysFont("Courier New", 20)
    score_surface = font.render(f"Счет: {score}", True, (0, 0, 0))
    level_surface = font.render(f"Уровень: {level}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))
    screen.blit(level_surface, (10, 30))

    # Draw fruit
    pygame.draw.circle(screen, (255, 0, 0), (fruit_coor[0] + 5, fruit_coor[1] + 5), 5)

    # Draw snake
    for el in squares:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()