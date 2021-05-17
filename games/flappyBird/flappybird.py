import pygame
import time
import random
import threading

from pygame.time import delay

#variables
size = 2
#sprites
sprites = dict()
#player yellow bird
yellowbird_01 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_01.png")
yellowbird_02 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_02.png")
yellowbird_03 =  pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/yellowbird_03.png")
sprites["yellowbird"] =  [yellowbird_01,yellowbird_02,yellowbird_03]
#background 
sprites["backgound_01"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_01.png")
sprites["backgound_02"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/background_02.png")
sprites["floor"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/floor.png")
#tubes
sprites["greenTube"] = pygame.image.load("C:/Users/PC/OneDrive/Documentos/Up/Up cuarto semestre/desarrolo de plugins/arcade/games/flappyBird/sprites/greentube_01.png")

class Player:
    def __init__(self, images, x, y, screen,playerNumber):
        self.animations = list()
        #setting images
        for i in range(0,len(images)):
          self.animations.append( pygame.transform.scale(images[i], (images[i].get_width()*size, images[i].get_height()*size)))
        #animations

        self.image = images[0]
        #sprites 
        self.width = images[0].get_width()
        self.height = images[0].get_height()
        self.rect = pygame.Rect(x, y, self.width-10, self.height+10)
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
        #alive
        self.alive = True
        #multiplayer
        self.playerNumber = playerNumber

    def jump(self,event,fps):
      if event.key == pygame.K_SPACE and self.alive and self.playerNumber ==1:
        self.falling = False
        self.fallingFPS = fps + 15
        if (self.fallingFPS > 60):
          self.fallingFPS -= 60
      if event.key == pygame.K_UP and self.alive and self.playerNumber ==2:
        self.falling = False
        self.fallingFPS = fps + 15
        if (self.fallingFPS > 60):
          self.fallingFPS -= 60


    def fall(self,fps):
      if (self.falling == True):
        self.rect.y += 5
      else:
        self.rect.y -= 3.5
      if (self.fallingFPS == fps):
        self.fallingFPS = 1
        self.falling = True

      if self.rect.y < -10:
        self.rect.y =- 10
      if self.rect.y >=370:
        self.rect.y=370
      

    def draw(self,fps):

      if (self.animationFPS == fps):
        self.animationFPS = fps + 3
        self.animationcont+=1

      if (self.animationcont > 2):
        self.animationcont = 0

      if (self.animationFPS > 60): 
        self.animationFPS -= 60

      if(self.falling == False):
        self.angle +=20
        if(self.angle>30):
          self.angle=30
        if(self.alive):
          rotatedImage,rotatedRect = self.rotatePlayer(self.animations[self.animationcont],self.rect,self.angle)
        else:
          rotatedImage,rotatedRect = self.rotatePlayer(self.animations[0],self.rect,self.angle)
        self.screen.blit(rotatedImage, rotatedRect)
        self.rect = rotatedRect
        return None

      self.angle -= 5
      if(self.angle<-90):
        self.angle =-90
      if(self.alive):
        rotatedImage,rotatedRect = self.rotatePlayer(self.animations[self.animationcont],self.rect,self.angle)
      else:
        rotatedImage,rotatedRect = self.rotatePlayer(self.animations[0],self.rect,self.angle)
      self.rect = rotatedRect
      self.screen.blit(rotatedImage, rotatedRect)

    def rotatePlayer(self,image, rect, angle):
      rotatedImage = pygame.transform.rotate(image, angle)
      rotatedRect = rotatedImage.get_rect(center=rect.center)
      return rotatedImage,rotatedRect

    def die(self,colision):
      if(self.rect.colliderect(colision)):
        self.alive = False



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

    

class Tubes:
    #seconds
    def __init__(self, image,x,separation,screen):
        image = pygame.transform.scale(image, (image.get_width()*size, image.get_height()*size))
        y = random.randint(200,350)
        self.originalX = x
        self.screen = screen
        #separation 
        self.separation = separation
        #upwars
        self.UPimage = image
        self.UPwidth = image.get_width()
        self.UPheight = image.get_height()
        self.UPrect = pygame.Rect(x, y, self.UPwidth, self.UPheight)
        self.UPmoveFPS = 10
        #downwars
        self.Dimage = self.rotateTube(image,180)
        self.Dwidth = image.get_width()
        self.Dheight = image.get_height()
        self.Drect = pygame.Rect(x+2, y-318 - self.separation, self.UPwidth, self.UPheight)
        self.DmoveFPS = 40
        #delay to move
        self.delaySeconds = 1
        self.delayTimer = 0
        self.startMoving = False
        #spawn fps 


    def draw(self):
        self.screen.blit(self.UPimage, (self.UPrect.x, self.UPrect.y))
        self.screen.blit(self.Dimage, (self.Drect.x, self.Drect.y))

    def move(self,speed,fps):
      if(not self.startMoving):
        if(fps == 60):
          self.delayTimer+=1
        if(self.delaySeconds == self.delayTimer):
          self.startMoving = True
        if(not self.startMoving):
          return None

      self.UPrect.x-=speed
      self.Drect.x-=speed
      if(self.UPrect.x == -60):
        print(fps)
        y = random.randint(200,350)
        self.UPrect.y = y 
        self.Drect.y = y -318 - self.separation
        self.UPrect.x = self.originalX
        self.Drect.x = self.originalX+2
        self.startMoving = False
        self.delayTimer = 0
        
    def rotateTube(self,image, angle):
      rotatedImage = pygame.transform.rotate(image, angle)
      return rotatedImage


def createWindow():
  (width, height) = (500, 500)
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption('Flappy bird')
  pygame.display.set_icon(yellowbird_01)
  return screen

def calculateFPS(fps):
    fps+=1
    if(fps == 61):
      return 1
    return fps

def onePlayer():
  pygame.init()
  screen = createWindow() 
  running = True
  
  background = Background(sprites["backgound_01"] if random.randint(0,1) else sprites["backgound_02"],0,0,screen)
  floor = Background(sprites["floor"],-2,400,screen)
  background2 = Background(sprites["backgound_01"] if random.randint(0,1) else sprites["backgound_02"],250,0,screen)
  floor2 = Background(sprites["floor"],248,400,screen)
  player1 = Player(sprites["yellowbird"],100,200,screen,1)
  tube = Tubes(sprites["greenTube"],500,150,screen)
  tube2 = Tubes(sprites["greenTube"],700,150,screen)
  tube3 = Tubes(sprites["greenTube"],900,150,screen)

  fps = 0

  while running:
    pygame.display.update()
    time.sleep(1/60)
    #draw
    fps = calculateFPS(fps)
    background.draw()
    floor.draw()
    background2.draw()
    floor2.draw()
    tube.move(2,fps)
    tube.draw()
    tube2.move(2,fps)
    tube2.draw()
    tube3.move(2,fps)
    tube3.draw()
    player1.draw(fps)
    player1.fall(fps)
    #colisions
    player1.die(floor.rect)
    player1.die(tube.Drect)
    player1.die(tube.UPrect)
    player1.die(tube2.Drect)
    player1.die(tube2.UPrect)
    player1.die(tube3.Drect)
    player1.die(tube3.UPrect)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        player1.jump(event,fps)

onePlayer()
