import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
clock = pygame.time.Clock()

x, y = 400, 400
delta = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 27: y -= 20
    if pressed[pygame.K_DOWN] and y <= 765.5: y += 20
    if pressed[pygame.K_LEFT] and x >= 27: x -= 20
    if pressed[pygame.K_RIGHT] and x <= 765.5: x += 20      
    
    if y <= 765.6:
        y += 10
        if y > 765.5: y = 765.5
    
    screen.fill((255, 255, 255))
    
    if y < 765.5 and not pressed[pygame.K_UP]:
        delta -= 0.5
        if delta < -10: delta = -10
        if delta > 0: delta = 0
        pygame.draw.circle(screen, (200, 200, 200), (x, y + delta * 3), 25)
        pygame.draw.circle(screen, (100, 100, 100), (x, y + delta * 2), 25)
        pygame.draw.circle(screen, (0, 0, 0), (x, y + delta), 25)
    if pressed[pygame.K_UP] and y <= 765.5:
        delta += 0.5
        if delta > 10: delta = 10
        if delta < 0: delta = 0
        pygame.draw.circle(screen, (200, 200, 200), (x, y + delta * 3), 25)
        pygame.draw.circle(screen, (100, 100, 100), (x, y + delta * 2), 25)
        pygame.draw.circle(screen, (0, 0, 0), (x, y + delta), 25)
        
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    
    pygame.display.update()  
    clock.tick(60)
    
pygame.quit()