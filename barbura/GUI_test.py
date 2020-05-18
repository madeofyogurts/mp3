### TODO >> check if possible to transfer everything connected with styling to .json file
### TODO >> check the logic for toggle buttons

import pygame
import pygame_gui

# initiation of pygame module
pygame.init()

# window creation:
pygame.display.set_caption('MP3 Player')
window_surface = pygame.display.set_mode((800, 300))
background = pygame.Surface((800, 600))

# bg styling
background.fill(pygame.Color('#ffffff'))

# pygame_gui Manager
manager = pygame_gui.UIManager((800, 600), 'theme.json')


### UI ###

# label_1: Now playing from:
label_1 = pygame_gui.elements.UILabel(text="NOW PLAYING FROM", relative_rect=pygame.Rect((100, 55), (200, 13)), manager = manager)

# label_2: User's whereabouts
user_whereabouts = pygame_gui.elements.UILabel(text="My Music in Desktop", relative_rect=pygame.Rect((100, 80), (200, 13)), manager = manager, object_id="label_dolny")


### MUSIC CONTROLS

# note to self: buttons are styled as follows:
# pygameRect (the area taken by the button) - ((x, y), (w, h)) where:
                                              # x - horizontal position, y - vertical position
                                              # l - width, w - height

# previous
backward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((480, 155), (60, 60)), text = '<', manager = manager)
# play
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 130), (100, 100)), text = 'Play', manager = manager)
# next
forward_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 155), (60, 60)), text = '>',manager = manager)

# creates an object which tracks time
clock = pygame.time.Clock()
is_running = True

# IGNORE THIS PART LOL

# while is_running:
#     # time delta apparently expresses the difference between two dates, and here, combined with tick() it apparently
#     # ensures that the program doesn't run at more than 60 FPS, dunno what the 1000.0 stands for tho
#     time_delta = clock.tick(60) / 1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False
#
#         manager.process_events(event)
#
#     manager.update(time_delta)
#
#     window_surface.blit(background, (0, 0))
#     manager.draw_ui(window_surface)
#
#     pygame.display.update()

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    pygame.mixer.init()
                    pygame.mixer.music.load("shewants.mp3")
                    pygame.mixer.music.play()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == forward_button:
                    print('"She Wants" by Metronomy has stopped.')
                    pygame.mixer.init()
                    pygame.mixer.music.stop()

        manager.process_events(event)
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()