import os, sys
import pygame
import pygame_menu

def start_snake():
    pygame.QUIT
    appFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
    # os.system(f'cmd /k "{appFolder}"')
    print(appFolder)
    os.system(f'cmd /k "python games/viborita.py"')

def start_flappyBird():
    pass

def start_ticTacToe():
    pass

def start_paint():
    pass

pygame.init()
pantalla = pygame.display.set_mode((600,400))
menu = pygame_menu.Menu('Pygame Mini Arcade', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Snake', start_snake)
menu.add.button('Flappy Bird', start_flappyBird)
menu.add.button('TicTacToe', start_ticTacToe)
menu.add.button('Paint', start_paint)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

            