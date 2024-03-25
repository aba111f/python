import pygame,sys 
import numpy as np
pygame.init()
screen = pygame.display.set_mode((500,400))

play_img = pygame.image.load('C:/Users/karat/Рабочий стол/pp2/Lab_7/images/play.png')
play_img = pygame.transform.scale(play_img,(50,50))

stop_img = pygame.image.load('C:/Users/karat/Рабочий стол/pp2/Lab_7/images/stop-button.png')
stop_img = pygame.transform.scale(stop_img,(50,50))

next_img = pygame.image.load('C:/Users/karat/Рабочий стол/pp2/Lab_7/images/next-button.png')
next_img = pygame.transform.scale(next_img,(50,50))

previous_img = pygame.image.load('C:/Users/karat/Рабочий стол/pp2/Lab_7/images/previous.png')
previous_img = pygame.transform.scale(previous_img,(50,50))

sound1 = pygame.mixer.Sound('C:/Users/karat/Рабочий стол/pp2/Lab_7/sounds/bouncing-joy-126495.mp3')
sound2 = pygame.mixer.Sound('C:/Users/karat/Рабочий стол/pp2/Lab_7/sounds/hammond_party_30sec-8471.mp3')
sound3 = pygame.mixer.Sound('C:/Users/karat/Рабочий стол/pp2/Lab_7/sounds/jungle-vibes-153242.mp3')


current_sound = sound1
current_img = play_img
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        

    

   
  
    keys = pygame.key.get_pressed()
    pressed = False
    if keys[pygame.K_SPACE]:
        current_sound.play()
        
        if current_img == play_img:
            current_img = stop_img


    if keys[pygame.K_s]:
        current_sound.stop()
        if current_img == stop_img:
            current_img = play_img

  
    if keys[pygame.K_RIGHT]:
        current_sound = sound2
        

    if keys[pygame.K_LEFT]:
            current_sound = sound3
            
                    
    
    
       
       
    
    



    pos = pygame.mouse.get_pos()
    
    
    screen.blit(current_img,(225,300))
    screen.blit(next_img,(300,300))
    screen.blit(previous_img,(150,300))
    pygame.display.flip()
    