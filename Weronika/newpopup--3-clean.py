import pygame
import pygame_gui
import os
import tkinter
from tkinter.filedialog import askdirectory

path = ""
while path == "":
    path = askdirectory(title = "Select your music folder") #otwiera okno dialogowe z wyborem sciezki
print("Your music folder location: ", path)

playlist = []
for (path, subdirs, files) in os.walk(path): #tutorialspoint.com/python/os_walk.htm, tutorialspoint.com/python_network_programming/python_directory_listing.htm
    for f in files:
        if '.mp3' in f:
            playlist.append(path + "/" + f)
playlist.sort()
m = 0
print("Your playlist:")
while m < len(playlist):
    print(playlist[m])
    m += 1

pygame.init()
pygame.mixer.init()
pygame.display.init()

pygame.display.set_caption('mp3 Player')

window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 100), (500, 50)), text='Press the button to listen to the first song.', manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 150), (500, 50)), text='Press the button to pause music..', manager=manager)
unpause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 200), (500, 50)), text='Press the button to unpause music.', manager=manager)
next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (500, 50)), text='Press the button to listen to next song.', manager=manager)
previous_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 300), (500, 50)), text='Press the button to listen to previous song.', manager=manager)
infinite_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (500, 50)), text='Press the button to listen to current song infinitely.', manager=manager)

clock = pygame.time.Clock()
is_running = True

n = 0

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print("first song is playing")
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pause_button:
                    print('paused')
                    pygame.mixer.music.pause()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == unpause_button:
                    print('unpaused')
                    pygame.mixer.music.unpause()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == next_button:
                    print('Next song is playing.')
                    n += 1
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == previous_button:
                    print('Previous song is playing.')
                    n -= 1
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == infinite_button:
                    print('Cureent song is playing infinitely.')
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play(-1)

        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
