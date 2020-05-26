#pip install pygame
#pip install pygame_gui

import pygame
import pygame_gui

pygame.init()

(width, height) = (500, 500)
popup = pygame.display.set_mode((width, height)) #Wielkość okienka
pygame.display.set_caption('mp3 Player') #Tytuł okienka

background = pygame.Surface((500, 500))
background.fill(pygame.Color('#000000')) #Kolor tła

manager = pygame_gui.UIManager((500, 500)) 
playButtonOne = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50), (400, 50)), text='"She Wants" by Metronomy', manager=manager)
playButtonTwo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 125), (400, 50)), text='"Ain\'t No Sunshine" by Bill Withers', manager=manager)
playButtonThree = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200), (400, 50)), text='"Lone Digger" by Caravan Palace', manager=manager)
stopButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 400), (400, 50)), text='Pause the music', manager=manager)
#Tutaj o są przyciski do odtwarzania muzyki

pygame.display.flip() 

program = True
while program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Wyłączenie okienka
            program = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == playButtonOne:
                    print('"She Wants" by Metronomy is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("shewants.mp3")
                    pygame.mixer.music.play()
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == playButtonTwo:
                    print('"Ain\'t No Sunshine" by Bill Withers is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("nosunshine.mp3")
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == playButtonThree:
                    print('"Lone Digger" by Caravan Palace is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("lonedigger.mp3")
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stopButton:
                    print('The music has stopped.')
                    pygame.mixer.init()
                    pygame.mixer.music.stop()

        manager.process_events(event)
    popup.blit(background,(0, 0))
    manager.draw_ui(popup) #To tutaj pokazuje przyciski
    pygame.display.update()
