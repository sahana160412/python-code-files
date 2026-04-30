import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("Arial", 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))
    text = font.render("Basic Screen", True, (0, 0, 0))
    screen.blit(text, (220, 50))
    pygame.display.flip()

pygame.quit()
