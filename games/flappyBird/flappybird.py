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
sprites["floor"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/floor.png")

class Player:
    def __init__(self, image, x, y, screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen
        self.falling = True
        self.fallingFPS = 0

    def jump(self,event,fps):
      if event.key == pygame.K_SPACE:
        self.falling = False
        self.fallingFPS = fps + 15
        if self.fallingFPS >60:
          self.fallingFPS -= 60


    def fall(self,fps):
      if self.falling == True:
        self.rect.y += 4
      else:
        self.rect.y -= 4
      if self.fallingFPS == fps:
        self.fallingFPS = 0
        self.falling = True
      

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Background:

    def __init__(self, image,x,y,screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))




def createWindow():
  (width, height) = (500, 500)
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption('Flappy bird')

  return screen
def calculateFPS(fps):
    fps+=1
    if(fps == 61):
      return 1
    return fps
def main():
  pygame.init()
  screen = createWindow() 
  running = True
  
  background = Background(sprites["backgound_01"] if random.randint(0,1) else sprites["backgound_02"],0,0,screen)
  floor = Background(sprites["floor"],-2,400,screen)
  background2 = Background(sprites["backgound_01"] if random.randint(0,1) else sprites["backgound_02"],250,0,screen)
  floor2 = Background(sprites["floor"],248,400,screen)
  player = Player(sprites["bird_01"],100,200,screen)
  
  fps = 0
  while running:
    pygame.display.update()
    time.sleep(1/60)
    fps = calculateFPS(fps)
    print(fps)
    background.draw()
    floor.draw()
    background2.draw()
    floor2.draw()
    player.draw()
    player.fall(fps)


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        player.jump(event,fps)
main()