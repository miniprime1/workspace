import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT
)

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Moving Circle")
running = True
x,y = 400,300
speed = 1

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    keys = pygame.key.get_pressed() 
      
    if keys[K_LEFT] and x>60: x -= speed
    elif keys[K_RIGHT] and x<740: x += speed
    elif keys[K_UP] and y>60: y -= speed  
    elif keys[K_DOWN] and y<540: y += speed
    elif keys[K_ESCAPE]: running = False
    else: pass
                
pygame.quit()