import pygame              
import random              

pygame.init() 

SW, SH = 600, 600 # screen size(playing area)
WW, WH = 600, 700 # window size

BLOCK_SIZE = 40
FONT = pygame.font.SysFont('Comic Sans MS', BLOCK_SIZE)    

screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("snake")
clock = pygame.time.Clock() # to controlling the game's speed
all_ship = []

for i in range(10):
    all_ship.append((random.randint(1, 16) * 40, random.randint(1, 16) * 40))
    
def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (60, 60, 60), rect, 1)
            
            if (x, y) in all_ship:
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (60, 60, 60), rect)
                
            

    
drawGrid()
 
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos
            pygame.draw.rect(screen, (0, 0, 0), (x, y, x + 40, y + 40))
    

    screen.fill("white")
    drawGrid()


    pygame.display.update() # updating the screen
    clock.tick(30) # using fps to control game speed
