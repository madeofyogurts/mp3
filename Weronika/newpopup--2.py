import pygame
import pygame_gui

from os import listdir
from os.path import isfile, join
music_folder = r"C:\Users\Dell\Desktop\MP3"
music_list = [f for f in listdir(music_folder) if isfile(join(music_folder, f))]
print(music_list)


pygame.init()

pygame.display.set_caption('mp3 Player')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 100), (500, 50)), text='Press the button to listen to "She Wants" by Metronomy', manager=manager)
stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 150), (500, 50)), text='Press the button to stop listening', manager=manager)
next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 200), (500, 50)), text='Press the button to listen to next song', manager=manager)
previous_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (500, 50)), text='Press the button to listen to previous song', manager=manager)
infinte_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 300), (500, 50)), text='Press the button to listen to current song infinitely', manager=manager)

clock = pygame.time.Clock()
is_running = True

n=0
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print(music_list[n],"is playing")
                    pygame.mixer.init()
                    pygame.mixer.music.load(music_list[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stop_button:
                    print('"She Wants" by Metronomy has stopped.')
                    pygame.mixer.init()
                    pygame.mixer.music.stop()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == next_button:
                    print('Next song is playing.')
                    n += 1
                    pygame.mixer.music.load(music_list[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == previous_button:
                    print('Previous song is playing.')
                    n -= 1
                    pygame.mixer.music.load(music_list[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == infinite_button:
                    print('Cureent song is playing infinitely.')
                    pygame.mixer.music.load(music_list[n])
                    pygame.mixer.music.play(-1)

        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
