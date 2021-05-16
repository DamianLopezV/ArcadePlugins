import pygame;
import time;

#colors
colors = dict()
colors["white"] = (255,255,255)
colors["red"] = (224, 59, 47)
colors["darkRed"] = (173, 47, 38)
colors["black"] = (0,0,0)
colors["green"] =  (16, 235, 115)
colors["darkGreen"] = (13, 186, 91)
#images

def createWindow():
  (width, height) = (100, 200)
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption('viborita')
  screen.fill(colors["white"])
  pygame.display.flip()
  return screen

def main():
  pygame.init()
  screen = createWindow() 
  running = True

  while running:
    pygame.display.update()
    time.sleep(0.08)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

main()