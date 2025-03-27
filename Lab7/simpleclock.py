#Mickey Mouse clock
import pygame 
import time

pygame.init()

#создание окна 800х600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey clock")

clock = pygame.time.Clock()

#загрузка изображений 
theclock = pygame.transform.scale(pygame.image.load("/Users/nurdanam/Downloads/images/clock.png"), (800, 600))
rightarm = pygame.image.load("/Users/nurdanam/Downloads/images/rightarm.png")
leftarm = pygame.image.load("/Users/nurdanam/Downloads/images/leftarm.png")

running = False

while not running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    #текущее локальное время (minute and second)
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    #углы поворота стрелок
    minute_angle =(minute * 6 + (second / 60) * 6) - 150
    second_angle = second * 6  
    
    #отображение циферблата на экране
    screen.blit(theclock, (0, 0))
    
    #right hand
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -(minute_angle - 150))
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    #left hand
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (50, 580)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60)
    
pygame.quit()