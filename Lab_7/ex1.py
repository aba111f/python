import pygame
from sys import exit  
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Micky Mouse clock")

background = pygame.image.load("C:/Users/karat/Рабочий стол/pp2/Lab_7/images/main-clock.png")
background = pygame.transform.scale(background, (600, 500))

left = pygame.image.load("C:/Users/karat/Рабочий стол\pp2/Lab_7/images/left-hand.png")
left = pygame.transform.scale(left, (400, 100))

right = pygame.image.load("C:/Users/karat/Рабочий стол\pp2/Lab_7/images/right-hand.png")
right = pygame.transform.scale(right, (300, 100))

left = pygame.transform.rotate(left, 90)
left_rect = left.get_rect()
left_rect.center = (300, 250)

right = pygame.transform.rotate(right, 90)
right_rect = right.get_rect()
right_rect.center = (300, 250)

Fps = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    current_time = datetime.datetime.now().time()

    sec_angle = -(current_time.second * 6)
    min_angle = -((current_time.minute + current_time.second/60) * 6)

    rotate_left = pygame.transform.rotate(left, sec_angle)
    rotate_right = pygame.transform.rotate(right, min_angle)

    left_rect = rotate_left.get_rect(center=(300, 250)) 
    right_rect = rotate_right.get_rect(center=(300, 250))
    
    screen.blit(rotate_left, left_rect.topleft)
    screen.blit(rotate_right, right_rect.topleft)

    pygame.display.flip()
    Fps.tick(1)
