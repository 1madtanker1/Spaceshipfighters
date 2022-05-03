import pygame, sys
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Laser")
clock = pygame.time.Clock()
enemy_yellow = pygame.image.load("yellow.png")
player = pygame.image.load('player.png')
#enemy x pos for animations
enemy_yellow_y_pos = 50
while True:
    #if the person presses the "X" button, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #attaching display surface
    screen.blit(player,(80,300))
    enemy_yellow_y_pos += 1
    screen.blit(enemy_yellow, (400, enemy_yellow_y_pos))

    #draw all elements
    pygame.display.update()
    clock.tick(60)

