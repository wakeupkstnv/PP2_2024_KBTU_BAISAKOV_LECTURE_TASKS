            if random.randint(0, 100) == 3:
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (255, 255, 255), rect)