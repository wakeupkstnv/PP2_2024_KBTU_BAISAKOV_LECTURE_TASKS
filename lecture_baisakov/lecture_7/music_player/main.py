import pygame
import os

pygame.init()

window_width = 800
window_height = 600
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

pygame.display.set_caption('SportikFy')
bg_image = pygame.image.load(os.path.normpath('img/icon/bg.png'))
pygame_icon = pygame.image.load(os.path.normpath('img/icon/icon.png'))
pygame.display.set_icon(pygame_icon)

button_size = 60
play_button = pygame.transform.scale(pygame.image.load(os.path.normpath('img/icon/play.png')), (button_size, button_size))
pause_button = pygame.transform.scale(pygame.image.load(os.path.normpath('img/icon/pause.png')), (button_size, button_size))

current_song_index = 0
songs = ['sound/Billie Jean.mp3', 'sound/Yesterday.mp3', 'sound/Sky.mp3', 'sound/1993.mp3', 'sound/New Tank.mp3']
pygame.mixer.music.load(os.path.normpath(songs[current_song_index]))
pygame.mixer.music.play()

covers = ['img/cover/billie_jean.jpg', 'img/cover/yesterday_cover.jpg', 'img/cover/wlr_cover.jpeg', 'img/cover/1993_cover.jpeg', 'img/cover/wlr_cover.jpeg']
album_cover_size = 275
album_cover = pygame.transform.scale(pygame.image.load(os.path.normpath(covers[current_song_index])), (album_cover_size, album_cover_size))

play = True
x = 0
font = pygame.font.SysFont('arialполужирный', 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play
        if play:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    
    if pressed[pygame.K_LEFT]: 
        current_song_index = (current_song_index - 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load(covers[current_song_index]), (album_cover_size, album_cover_size))
            
    if pressed[pygame.K_RIGHT]: 
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load(covers[current_song_index]), (album_cover_size, album_cover_size))
        

    game_display.fill((255, 255, 255))    
    game_display.blit(bg_image, (0, 0))
    text = font.render(songs[current_song_index][6:-4], True, (0, 0, 0))
    game_display.blit(text, (425 - text.get_width() // 2, 420 - text.get_height() // 2))
    game_display.blit(album_cover, (290, 65))
    
    pygame.draw.rect(game_display, (225, 225, 225), (290, 342, 275, 11))
    if play:
        x += 0.1
        if x > 275:
            x = 0
    pygame.draw.rect(game_display, (100, 150, 200), (290, 342, x, 11))
    
    
    if play:
        game_display.blit(pause_button, (400, 465))
    else:
        game_display.blit(play_button, (400, 465))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
