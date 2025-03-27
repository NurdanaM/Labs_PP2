import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving red ball")

ball_r = 25
ball_x = 800 // 2
ball_y = 600 // 2
ball_color = (255, 0, 0)
ball_speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_r)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_r - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_r + ball_speed <= 600:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_r - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_r + ball_speed <= 800:
                    ball_x += ball_speed

pygame.quit()