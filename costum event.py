import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
COLOR_CHANGE = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE, 1000) # Trigger every 1 second

sprite1 = pygame.Rect(100, 100, 50, 50)
sprite2 = pygame.Rect(250, 100, 50, 50)
color1, color2 = "red", "blue"

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == COLOR_CHANGE:
            color1 = random.choices(range(256), k=3)
            color2 = random.choices(range(256), k=3)

    screen.fill("white")
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.flip()

pygame.quit()
