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
    pygame.draw.rect(screen, (255, 0, 0), [x, y, 100, 100])
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    keys = pygame.key.get_pressed() 
      
    if keys[K_LEFT] and x>10: x -= speed
    elif keys[K_RIGHT] and x<690: x += speed
    elif keys[K_UP] and y>10: y -= speed  
    elif keys[K_DOWN] and y<490: y += speed
    elif keys[K_ESCAPE]: running = False
    else: pass
                
pygame.quit()