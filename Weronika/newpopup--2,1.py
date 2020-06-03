import pygame
import pygame_gui
import os
import glob

from os import listdir
from os.path import isfile, join
music_folder = r"C:\Users\Dell\Desktop\MP3\music"
playlist = [f for f in listdir(music_folder) if isfile(join(f))]
print("Twoja playlista to:", playlist)


import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


pygame.init()
pygame.mixer.init()
pygame.display.init()

pygame.display.set_caption('mp3 Player')

window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 100), (500, 50)), text='Press the button to listen to "She Wants" by Metronomy', manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 150), (500, 50)), text='Press the button to pause listening', manager=manager)
unpause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 200), (500, 50)), text='Press the button to unpause listening', manager=manager)
next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (500, 50)), text='Press the button to listen to next song', manager=manager)
previous_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 300), (500, 50)), text='Press the button to listen to previous song', manager=manager)
infinite_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (500, 50)), text='Press the button to listen to current song infinitely', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print("first song is playing")
                    pygame.mixer.music.queue(playlist.pop())
                    pygame.mixer.music.load(playlist.pop())
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pause_button:
                    print('paused')
                    pygame.mixer.init()
                    pygame.mixer.music.pause()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == unpause_button:
                    print('unpaused')
                    pygame.mixer.init()
                    pygame.mixer.music.unpause()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == next_button:
                    print('Next song is playing.')
                    pygame.mixer.music.load(playlist.pop())
                    pygame.mixer.music.queue(playlist.pop())
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == previous_button:
                    print('Previous song is playing.')
                    pygame.mixer.music.load(playlist.pop())
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == infinite_button:
                    print('Cureent song is playing infinitely.')
                    pygame.mixer.music.load(playlist.pop())
                    pygame.mixer.music.play(-1)

        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
