import pygame
import random
import psycopg2

# PostgreSQL connection
con = psycopg2.connect(
    host="localhost",
    database="snake_db",  
    user="postgres",
    password="nurdana205!" 
)
cur = con.cursor()

# get or create user
def get_user():
    username = input("Enter your username: ")
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        print(f"Welcome back, {username}!")

        # get the latest level from scores
        cur.execute("SELECT level FROM scores WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
        row = cur.fetchone()
        if row:
            level = row[0]
            print(f"Your current level: {level}")
        else:
            level = 1
            print("No previous games found. Starting from level 1.")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        con.commit()
        level = 1
        print(f"New user {username} created. Starting from level 1.")
    return user_id, level

# save score and level
def save_score(user_id, level, score):
    cur.execute("INSERT INTO scores (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    con.commit()
    print("Progress saved.")

# walls for different levels
walls = {
    2: [[300, 100], [310, 100], [320, 100], [330, 100]],
    3: [[400, 300], [400, 310], [400, 320], [400, 330], [400, 340]],
    4: [[150, 150], [160, 150], [170, 150], [180, 150],
        [150, 160], [150, 170], [150, 180]]
}

def generate_fruit():
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        fruit_coor = [fr_x, fr_y]
        if fruit_coor not in squares and fruit_coor not in current_walls:
            return fruit_coor

def game_over():
    global done
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("times new roman", 45)
    text_surface = font.render(f"Game Over! Score: {score}", True, (255, 0, 0))
    screen.blit(text_surface, text_surface.get_rect(center=(width // 2, height // 2)))
    pygame.display.update()
    pygame.time.delay(3000)
    save_score(user_id, level, score)
    pygame.quit()
    cur.close()
    con.close()
    exit()

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

score = 0
fruit_eaten = False
fruits_needed_for_level_up = 3

# get player and initial level
user_id, level = get_user()
speed = max(50, 200 - (level - 1) * 20)
current_walls = walls.get(level, [])

head_square = [100, 100]
squares = [[30 + 10 * i, 100] for i in range(8)]
fruit_coor = generate_fruit()

direction = "right"
next_dir = "right"
done = False

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            elif event.key == pygame.K_UP:
                next_dir = "up"
            elif event.key == pygame.K_LEFT:
                next_dir = "left"
            elif event.key == pygame.K_RIGHT:
                next_dir = "right"
            elif event.key == pygame.K_p:
                save_score(user_id, level, score)
                done = True

    if next_dir == "right" and direction != "left":
        direction = "right"
    elif next_dir == "left" and direction != "right":
        direction = "left"
    elif next_dir == "up" and direction != "down":
        direction = "up"
    elif next_dir == "down" and direction != "up":
        direction = "down"

    if direction == "right":
        head_square[0] += 10
    elif direction == "left":
        head_square[0] -= 10
    elif direction == "up":
        head_square[1] -= 10
    elif direction == "down":
        head_square[1] += 10

    if (head_square[0] < 0 or head_square[0] >= width or
        head_square[1] < 0 or head_square[1] >= height or
        head_square in squares[:-1] or head_square in current_walls):
        game_over()

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)

    if head_square == fruit_coor:
        fruit_eaten = True
        score += 10
        if score % (fruits_needed_for_level_up * 10) == 0:
            level += 1
            speed = max(50, speed - 20)
            current_walls = walls.get(level, [])
    else:
        squares.pop(0)

    if fruit_eaten:
        fruit_coor = generate_fruit()
        fruit_eaten = False

    screen.fill((170, 207, 104))
    font = pygame.font.SysFont("Courier New", 20)
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (10, 30))

    pygame.draw.circle(screen, (255, 0, 0), (fruit_coor[0] + 5, fruit_coor[1] + 5), 5)
    for wall in current_walls:
        pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(wall[0], wall[1], 10, 10))
    for el in squares:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()
cur.close()
con.close()