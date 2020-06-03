#nowe, potrzebne importy
import os
import tkinter
from tkinter.filedialog import askdirectory

#popup z wyborem ścieżki
path = ""
while path == "": #ścieżka poczeka na decyzję użytkownika
    path = askdirectory(title = "Select your music folder")
print("Your music folder location: ", path)

#dodawanie utworów do playlisty na podstawie ścieżki
playlist = []
for (path, subdirs, files) in os.walk(path):
    for f in files:
        if '.mp3' in f: #dodajemy do playlisty tylko utwory mp3, mp4 jest poszkodowane; dajcie znać to appendujemy inne formaty też
            playlist.append(path + "/" + f)
playlist.sort()
m = 0
print("Your playlist:")
while m < len(playlist):
    print(playlist[m]) #przez linijkę 17-tą to tak źle wygląda, ale tak musi być, żeby się odtwarzało
    m += 1

#wyciągnięte z poszczególnych buttonów, żeby było tylko raz
#po: pygame.init()
pygame.mixer.init()
pygame.display.init()

#pozmieniane nazwy buttonów, żeby lepiej oddawały co robią
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 100), (500, 50)), text='Press the button to listen to the first song.', manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 150), (500, 50)), text='Press the button to pause music..', manager=manager)
unpause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 200), (500, 50)), text='Press the button to unpause music.', manager=manager)
next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (500, 50)), text='Press the button to listen to next song.', manager=manager)
previous_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 300), (500, 50)), text='Press the button to listen to previous song.', manager=manager)
infinite_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (500, 50)), text='Press the button to listen to current song infinitely.', manager=manager)

#odliczanie numeru na playliście
n = 0

#i.. samo serce odtwarzania muzyki!
#dla: play_button
                #po: if event.ui_element == play_button:
                    print("First song is playing.")
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

#dla: pause_button:
                #po: if event.ui_element == pause_button:
                    print('Paused.')
                    pygame.mixer.music.pause()

#dla: unpause_button:
                #po: if event.ui_element == unpause_button:
                    print('Unpaused.')
                    pygame.mixer.music.unpause()

#dla: next_button:
                #po: if event.ui_element == next_button:
                    print('Next song is playing.')
                    n += 1
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

#dla: play_button:
                #po: if event.ui_element == previous_button:
                    print('Previous song is playing.')
                    n -= 1
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play()

#dla: infinite_button:
                #po: if event.ui_element == infinite_button:
                    print('Cureent song is playing infinitely.')
                    pygame.mixer.music.load(playlist[n])
                    pygame.mixer.music.play(-1)
