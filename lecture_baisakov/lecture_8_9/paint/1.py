import pygame
from check_posiotion import isIcon, isPalitre
from get_shapes import getCircle, getRectangle
 
class icon:
    def __init__(self, place: pygame.Surface, img: pygame.image.load, size: tuple):
        self.place = place
        self.img = pygame.transform.scale(img, size)
        self.size = size
    
    def create_icon(self, coord = (0, 0)):
        pygame.draw.rect(self.place, (255, 255, 255), pygame.Rect(coord[0], coord[1], self.size[0], self.size[1]))
        self.place.blit(self.img, coord)

def change_scale(mode: bool):
    global list_x, list_y, another_list, white_list
    
    if mode:
        list_x = min(list_x + 10, 1200)
        list_y = min(list_y + 10, 650)
    else:
        list_x = max(list_x - 10, 800)
        list_y = max(list_y - 10, 500)
        screen.fill((58, 59, 60))
    
    another_list.blit(white_list, (0, 0))
    white_list = pygame.Surface((list_x, list_y))
    white_list.fill((255, 255, 255))
    white_list.blit(another_list, (0, 0))
    another_list = pygame.Surface((list_x, list_y))


def draw_interface() -> None:
    global red_color, green_color, blue_color
    global rect_img, circle_img, pen_img
    
    screen.blit(white_list, (5, 155))
    pygame.draw.rect(screen, (33, 40, 45), pygame.Rect(0, 0, 1200, 150))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1200, 150), 2)
    pygame.draw.rect(screen, mode, pygame.Rect(180, 25, 100, 100))
    pygame.draw.line(screen, (0, 0, 0), (325, 0), (325, 149), 2)
    
    rect_icon = icon(screen, rect_img, (30, 30))
    rect_icon.create_icon((350, 20))
    
    circle_icon = icon(screen, circle_img, (30, 30))
    circle_icon.create_icon((350, 70))
    
    pen_icon = icon(screen, pen_img, (30, 30))
    pen_icon.create_icon((400, 20))
    
    
    eraser_icon = icon(screen, rect_img, (30, 30))
    eraser_icon.create_icon((400, 70))
    
    blue_color = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(25, 25, 20, 20))
    green_color = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(75, 25, 20, 20))
    red_color = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(125, 25, 20, 20))
    black_color = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(25, 65, 20, 20))
    white_color = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(75, 65, 20, 20))
    yellow_color = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(125, 65, 20, 20))
    pink_color = pygame.draw.rect(screen, (255, 192, 203), pygame.Rect(25, 105, 20, 20))
    purple_color = pygame.draw.rect(screen, (128, 0, 128), pygame.Rect(75, 105, 20, 20))
    brown_color = pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(125, 105, 20, 20))
     
def drawLineBetween(screen, start, end, width, color_mode) -> None:
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1] - 150)
        pygame.draw.circle(screen, color_mode, (x, y), width)
        

def main():
    global screen, check, mode, white_list, list_x, list_y, active_item, another_list
    global rect_img, circle_img, pen_img
    
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    screen.fill((58, 59, 60))
    clock = pygame.time.Clock()
    size = 1
    
    list_x, list_y = 800, 500
    white_list = pygame.Surface((list_x, list_y))
    white_list.fill((255, 255, 255))
    
    another_list = pygame.Surface((list_x, list_y))
    another_list.fill((255, 255, 255))
    
    cursor = pygame.transform.scale(pygame.image.load('hand.png'), (30, 30))
    rect_img = pygame.transform.scale(pygame.image.load('rectangle.png'), (30, 30))
    circle_img = pygame.transform.scale(pygame.image.load('dry-clean.png'), (30, 30))
    pen_img = pygame.transform.scale(pygame.image.load('pen.png'), (30, 30))
      
    check = False
    mode = 'black'
    points = []
    active_item = 'pen'
    
    while True:
        screen.fill((58, 59, 60))
        coord = pygame.mouse.get_pos()
        
        if ((0 <= coord[0] <= list_x and 150 <= coord[1] <= list_y) or
            (0 <= coord[0] <= 1200 and 0 <= coord[1] <= 150)): 
            pygame.mouse.set_visible(True)
        else:   
            pygame.mouse.set_visible(False)
            screen.blit(cursor, coord)
            

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_p]: size = min(30, size + 1)
        if pressed[pygame.K_m]: size = max(1, size - 1)
    
        if pressed[pygame.K_q]: change_scale(True)
        if pressed[pygame.K_e]: change_scale(False)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if isPalitre(event.pos):                     
                        mode = isPalitre(event.pos)
                    elif isIcon(event.pos):
                        active_item = isIcon(event.pos)
                    else:
                        check = True
                        points = [(event.pos[0], event.pos[1])]
                    
                    if active_item == 'rect':
                        check = True
                        x1 = event.pos[0]
                        y1 = event.pos[1] - 150
                    
                    if active_item == 'circle':
                        check = True
                        x1 = event.pos[0]
                        y1 = event.pos[1] - 150
                        
            if event.type == pygame.MOUSEBUTTONUP:
                check = False
                points = points[-256:]
                         
                if active_item == 'rect' and event.button == 1:
                    another_list.blit(white_list, (0, 0))
                
                if active_item == 'circle' and event.button == 1:
                    another_list.blit(white_list, (0, 0))
            
            if event.type == pygame.MOUSEMOTION:
                if check and active_item == 'pen':                    
                    position = event.pos
                    points = points + [position]
                    i = 0
                    while i < len(points) - 1:
                        drawLineBetween(white_list, points[i], points[i + 1], size, mode)
                        i += 1
                        
                if check and active_item == 'rect':
                    x2 = event.pos[0]
                    y2 = event.pos[1] - 150
                    white_list.blit(another_list, (0, 0))
                    pygame.draw.rect(white_list, mode, pygame.Rect(getRectangle(x1, y1, x2, y2)), size)
                    
                    
                if check and active_item == 'circle':
                    x2 = event.pos[0]
                    y2 = event.pos[1] - 150
                    white_list.blit(another_list, (0, 0))
                    pygame.draw.circle(white_list, mode, (x1 + (x1 - x2), y1 + (y1 - y2)), getCircle(x1, y1, x2, y2), size)
                    
                if check and active_item == 'eraser':                    
                    position = event.pos
                    points = points + [position]
                    
                    i = 0
                    while i < len(points) - 1:
                        drawLineBetween(white_list, points[i], points[i + 1], size, (255, 255, 255))
                        i += 1

        draw_interface()
        pygame.display.flip()
        
        clock.tick(60)
        
main()
