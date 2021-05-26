import os, sys
import pygame
import pygame_menu

def start_snake():
    os.system(f'cmd /c "python ArcadePlugins/games/viborita.py"')

def start_flappyBird():
    os.system(f'cmd /c "python ArcadePlugins/games/flappyBird/flappybird.py"')

def start_ticTacToe():
    os.system(f'cmd /c "python ArcadePlugins/games/gato.py"')

def start_paint():
    os.system(f'cmd /c "python ArcadePlugins/games/paint.py"')

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

            