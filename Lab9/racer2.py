# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0 # (1) Added variable to store the number of collected coins

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading background image
background = pygame.image.load("/Users/nurdanam/Downloads/PygameTutorial_3_0/AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer Game")

# (2) Added background music 
pygame.mixer.music.load("/Users/nurdanam/Downloads/PygameTutorial_3_0/background.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/nurdanam/Downloads/PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/nurdanam/Downloads/PygameTutorial_3_0/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# (3) Added Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/nurdanam/Downloads/SimRacer-500px.png")
        self.image = pygame.transform.scale(self.image, (50,50)) # resized the coin 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # random appearance of the coin
        self.weight = random.randint(1, 5)  # Random weight for each coin
    
    def move(self):
        self.rect.move_ip(0, SPEED) # coin moves down
        if self.rect.top > SCREEN_HEIGHT:  # If the coin moves off the screen, reposition it at the top
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin() # (4) Added Coin instance

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1) # (5) Added coin to the sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    # (6) Added score and coin count display in the top rigth corner
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # (7) Check if the player collects a coin
    if pygame.sprite.spritecollideany(P1, coins):
        coin = pygame.sprite.spritecollideany(P1, coins)
        COINS_COLLECTED += coin.weight  # Increase score by the coin's weight
        C1.rect.top = 0 # reset the coin's position
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/nurdanam/Downloads/PygameTutorial_3_0/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        pygame.mixer.music.stop()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check if the player has collected 10 or more coins, then increase enemy speed
    if COINS_COLLECTED >= 20:
        SPEED += 0.5 
        COINS_COLLECTED = 0 # Reset coin count after increase

    pygame.display.update()
    FramePerSec.tick(FPS)