import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 40, 40))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 0, 40, 40))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 40, 40, 40))
        pygame.draw.rect(screen, (255, 128, 255), pygame.Rect(40, 40, 40, 40))

        pygame.display.flip()
