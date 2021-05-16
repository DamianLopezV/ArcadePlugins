import pygame
import time
import random

#variables
size = 2
#sprites
sprites = dict()
sprites["bird_01"] =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/bird_01.png")
sprites["backgound_01"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_01.png")
sprites["backgound_02"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_02.png")

class Player:
    def __init__(self, image, x, y, screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Background:

    def __init__(self, image,screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

def createWindow():
  (width, height) = (250, 400)
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption('Flappy bird')

  pygame.display.flip()
  return screen

def main():
  pygame.init()
  screen = createWindow() 
  running = True
  
  background = Background(sprites["backgound_01"] if random.randint(0,1) else sprites["backgound_02"],screen)
  player = Player(sprites["bird_01"],50,50,screen);

  while running:
    pygame.display.update()
    time.sleep(0.08)
    background.draw()
    player.draw()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

main()