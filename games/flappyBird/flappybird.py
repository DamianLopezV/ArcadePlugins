import pygame
import time
import random

#variables
size = 2
#sprites
sprites = dict()
yellowbird_01 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_01.png")
yellowbird_02 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_02.png")
yellowbird_03 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_03.png")
sprites["yellowbird"] =  [yellowbird_01,yellowbird_02,yellowbird_03]
sprites["backgound_01"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_01.png")
sprites["backgound_02"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_02.png")
sprites["floor"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/floor.png")

class Player:
    def __init__(self, images, x, y, screen):
        #setting images
        for i in range(0,len(images)):
          images[i] = pygame.transform.scale(images[i], (images[i].get_width()*size, images[i].get_height()*size))
        #animations
        self.animations = images
        self.image = images[0]
        #sprites
        self.width = images[0].get_width()
        self.height = images[0].get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen
        #falling
        self.falling = True
        self.fallingFPS = 1
        #animation  fps
        self.animationFPS = 3
        self.animationcont = 0
        #rotating 
        self.rotaringfps = 10
        self.angle = 0

    def jump(self,event,fps):
      if event.key == pygame.K_SPACE:
        self.falling = False
        self.fallingFPS = fps + 15
        if (self.fallingFPS > 60):
          self.fallingFPS -= 60


    def fall(self,fps):
      if (self.falling == True):
        self.rect.y += 5
      else:
        self.rect.y -= 4
      if (self.fallingFPS == fps):
        self.fallingFPS = 1
        self.falling = True
      

    def draw(self,fps):
      if (self.animationFPS == fps):
        self.animationFPS = fps + 3
        self.animationcont+=1

      if (self.animationcont > 2):
        self.animationcont = 0

      if (self.animationFPS > 60):
        self.animationFPS -= 60

      if(self.falling == False):
        self.angle +=15
        if(self.angle>30):
          self.angle=30
        rotatedImage,rotatedRect = self.rotatePlayer(self.animations[self.animationcont],self.rect,self.angle)
        self.screen.blit(rotatedImage, rotatedRect)
        return None

      self.angle -= 7.5
      if(self.angle<-90):
        self.angle =-90
      rotatedImage,rotatedRect = self.rotatePlayer(self.animations[self.animationcont],self.rect,self.angle)
      # self.screen.blit(self.animations[self.animationcont], (self.rect.x, self.rect.y))
      self.screen.blit(rotatedImage, rotatedRect)

    def rotatePlayer(self,image, rect, angle):
      rotatedImage = pygame.transform.rotate(image, angle)
      rotatedRect = rotatedImage.get_rect(center=rect.center)
      return rotatedImage,rotatedRect

class Background:

    def __init__(self, image,x,y,screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        self.image = image
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
  player = Player(sprites["yellowbird"],100,200,screen)
  fps = 0

  while running:
    pygame.display.update()
    time.sleep(1/60)
    fps = calculateFPS(fps)
    background.draw()
    floor.draw()
    background2.draw()
    floor2.draw()
    player.draw(fps)
    player.fall(fps)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        player.jump(event,fps)
main()