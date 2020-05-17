#pip install pygame
#pip install pygame_gui

import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('mp3 Player')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600)) 

playButtonOne = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 50), (400, 50)), text='"She Wants" by Metronomy', manager=manager)
playButtonTwo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 125), (400, 50)), text='"Ain\'t No Sunshine" by Bill Withers', manager=manager)
playButtonThree = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (400, 50)), text='"Lone Digger" by Caravan Palace', manager=manager)
stopButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 400), (400, 50)), text='Pause the music', manager=manager)


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        #1
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == playButtonOne:
                    print('"She Wants" by Metronomy is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("shewants.mp3")
                    pygame.mixer.music.play()

        #2
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == playButtonTwo:
                    print('"Ain\'t No Sunshine" by Bill Withers is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("nosunshine.mp3")
                    pygame.mixer.music.play()

        #3
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
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
