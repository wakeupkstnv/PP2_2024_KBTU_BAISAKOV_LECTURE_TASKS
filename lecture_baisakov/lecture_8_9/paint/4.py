import pygame

queue = []

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    return (x, y, w, h)

def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0 or x > 400 or y > 300:
        return False
    if screen.get_at((x, y)) != origin_color:
        return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)
    return True

pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))
done = False
clock = pygame.time.Clock()

origin_color = (0, 0, 0)
fill_color = (255, 0, 0)
tools_count = 3
tool = 0  # 0 - pencil, 1 - rectangle, 2 - fill

x1 = y1 = x2 = y2 = 10
color = (0, 128, 255)
isMouseDown = False

screen.fill((0, 0, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                if tool == 0:
                    x1, y1 = event.pos
                    x2, y2 = x1, y1
                elif tool == 1:
                    x1, y1 = event.pos
                elif tool == 2:
                    x1, y1 = event.pos
                    origin_color = screen.get_at((x1, y1))
                    queue.append((x1, y1))
                    screen.set_at((x1, y1), fill_color)
                    while queue:
                        cur_pos = queue.pop(0)
                        x, y = cur_pos
                        step(screen, x + 1, y, origin_color, fill_color)
                        step(screen, x - 1, y, origin_color, fill_color)
                        step(screen, x, y + 1, origin_color, fill_color)
                        step(screen, x, y - 1, origin_color, fill_color)
            elif event.button == 3:  # Right click
                tool = (tool + 1) % tools_count
            isMouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                another_layer.blit(screen, (0, 0))
            isMouseDown = False
        elif event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                if tool == 0:
                    x1, y1 = x2, y2
                    x2, y2 = event.pos
                    pygame.draw.line(screen, color, (x1, y1), (x2, y2))
                elif tool == 1:
                    screen.blit(another_layer, (0, 0))
                    x2, y2 = event.pos
                    pygame.draw.rect(screen, color, pygame.Rect(*getRectangle(x1, y1, x2, y2)), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
