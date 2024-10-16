#Imports
import pygame
import sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 500))

FPS = pygame.time.Clock()
FPS.tick(30)

#Player
player = pygame.Rect(100, 200, 25, 25)
#Box

while True:
    
    #Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:         #Left
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:       #Right
        player.move_ip(1, 0)
    elif key[pygame.K_w]:       #Up
        player.move_ip(0, -1)
    elif key[pygame.K_s]:       #Down
        player.move_ip(0, 1)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    window.fill((200, 100, 50))
    
    pygame.draw.rect(window, (0, 0, 0), player)     #Player
    
    pygame.display.update()