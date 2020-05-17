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

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 100), (500, 50)), text='Press the button to listen to "She Wants" by Metronomy', manager=manager)
stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 200), (500, 50)), text='Press the button to stop listening', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print('"She Wants" by Metronomy is playing.')
                    pygame.mixer.init()
                    pygame.mixer.music.load("shewants.mp3")
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stop_button:
                    print('"She Wants" by Metronomy has stopped.')
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                


        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()