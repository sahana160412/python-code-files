import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))


x, y = 100, 100  
static_x, static_y = 400, 200 

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]:    y -= 5
    if keys[pygame.K_DOWN]:  y += 5

    
    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))       # Blue square
    pygame.draw.rect(screen, (255, 0, 0), (static_x, static_y, 50, 50)) # Red square
    
    pygame.display.flip()
    pygame.time.Clock().tick(60) # Limits speed

pygame.quit()
