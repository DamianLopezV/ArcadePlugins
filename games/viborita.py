import pygame
import random
import time
import sys 
#colors
colors = dict()
colors["white"] = (255,255,255)
colors["red"] = (224, 59, 47)
colors["darkRed"] = (173, 47, 38)
colors["black"] = (0,0,0)
colors["green"] =  (16, 235, 115)
colors["darkGreen"] = (13, 186, 91)
#map
map = [["0"]*20 for i in range(0,20)]
mapColums = len(map)
mapRows = len(map[0])
#square size
size = 30

class Body:

  bodyCordinates = list()
  def __init__(self,column,row):
    self.column = column
    self.row = row
    self.child = None
    self.parent = None

  def addChild(self,body,direction):
    if(body.child):
      return self.addChild(body.child,direction)
    if(not body.child):
      childColumn,childRow = self.caculateChildPositon(body.column,body.row,direction)
      child = Body(childColumn,childRow)
      body.child = child
      child.parent = body
      map[childColumn][childRow] = "2"

  def caculateChildPositon(self,parentColumn,parentRow,direction):
    if(direction == "R"):
      return (parentColumn,parentRow-1)
    elif(direction == "L"):
      return (parentColumn,parentRow+1)
    elif(direction == "U"):
      return (parentColumn+1,parentRow)
    elif(direction == "D"):
      return (parentColumn-1,parentRow)
    
  def getParentOldCordiantes(self,oldColumn,oldRow,body):
    currentColumn = body.column
    currentRow = body.row
    map[currentColumn][currentRow] = 0
    body.column = oldColumn
    body.row = oldRow
    map[oldColumn][oldRow]
    if(body.child):
      self.getParentOldCordiantes(currentColumn,currentRow,body.child)
  

class Player:
  movement = ""
  def __init__(self):
    self.score = 0
    self.column = int(mapColums/2)
    self.row = int(mapRows/2)
    self.head = Body(self.column,self.row)
    map[self.column][self.row] = "2"

  def controls(self,event):
      if event.key == pygame.K_RIGHT and not self.movement == "L":
        self.movement ="R"
      if event.key == pygame.K_LEFT and not self.movement == "R":
        self.movement ="L"
      if event.key == pygame.K_UP and not self.movement == "D":
        self.movement ="U"
      if event.key == pygame.K_DOWN and not self.movement == "U":
        self.movement = "D"

  def constantMovement(self,body):
    if(self.movement == "R"):
      self.movePlayer(0,1,body)
    elif(self.movement == "L"):
      self.movePlayer(0,-1,body)
    elif(self.movement == "U"):
      self.movePlayer(-1,0,body)
    elif(self.movement == "D"):
       self.movePlayer(1,0,body)


  def movePlayer(self,column,row,body):
    #set las cordinate to space
    map[body.column][body.row] = "0"
    oldColumn = body.column
    oldRow = body.row
    body.column += column
    body.row += row
    #set the player new codinates
    map[body.column][body.row] = "2"
    #set head cordinates
    if(not body.parent):
      self.head.row = body.row
      self.head.column = body.column
    if(body.child):
      body.getParentOldCordiantes(oldColumn,oldRow,body.child)

    
  def drawPlayer(self,screen,body):
    column = body.column 
    row = body.row
    pygame.draw.rect(screen,colors["black"],pygame.Rect(row*size, column*size, size, size))
    if(body.child):
      self.drawPlayer(screen,body.child)
  
  def addScore(self,points):
    self.head.addChild(self.head,self.movement)
    self.score+=points
  
  def checkColisions(self,body):
    if(body.parent):
      if(self.head.column == body.column and self.head.row == body.row):
        sys.exit("Nooooooo perdiste ahhhhh :(")
    if(body.child):
      self.checkColisions(body.child)
  
  def checkPlayerInMap(self):
    if(self.head.column<0 or self.head.column>= mapColums):
      sys.exit("Nooooooo te salisteee ahhh ahhhhh :(")
    if(self.head.row<0 or self.head.row>= mapRows):
      sys.exit("Nooooooo te salisteee ahhh ahhhhh :(")


  def printScore(self,screen):
    fuente = pygame.font.Font(None, 20)
    text = f"Score: {self.score}"
    mensaje = fuente.render(text, 1, (255, 255, 255))
    screen.blit(mensaje, (15, 15))

    

class Food:

  def __init__(self):
    self.exists = False

  def createFood(self,screen):
    if(self.exists):
      pygame.draw.rect(screen,colors["red"],pygame.Rect(self.row*size, self.column*size, size, size))
      pygame.draw.rect(screen,colors["darkRed"],pygame.Rect(self.row*size, self.column*size, size, size),3)
      map[self.column][self.row] = "1"
      return ""
    else:
      self.column = random.randint(0,mapColums-1)
      self.row = random.randint(0,mapRows-1) 
      pygame.draw.rect(screen,colors["red"],pygame.Rect(self.row*size, self.column*size, size, size))
      pygame.draw.rect(screen,colors["darkRed"],pygame.Rect(self.row*size, self.column*size, size, size),3)
      map[self.column][self.row] = "1"
      self.exists = True 
    
  def destroyFood(self,columnPlayer,rowPlayer):
    if(columnPlayer == self.column and rowPlayer == self.row):
      self.exists = False
      map[self.column][self.row] = "0"
      return True
    return False

def createWindow():
  (width, height) = (size*mapColums+1, size*mapRows+1)
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption('viborita')
  screen.fill(colors["white"])
  pygame.display.flip()
  return screen

def createMap(screen):
  i=-1
  for column in map:
    i+=1
    for j in range(0,len(column)):
      pygame.draw.rect(screen,colors["green"],pygame.Rect(j*size, i*size, size, size))
      pygame.draw.rect(screen,colors["darkGreen"],pygame.Rect(j*size, i*size, size, size),2)

def main():
  pygame.init()
  screen = createWindow() 
  running = True
  food = Food()
  player = Player()
  while running:
    pygame.display.update()
    time.sleep(0.08)
    createMap(screen)
    player.printScore(screen)
    player.constantMovement(player.head)
    player.drawPlayer(screen,player.head)
    player.checkColisions(player.head)
    player.checkPlayerInMap()
    food.createFood(screen)
    if(food.destroyFood(player.head.column,player.head.row)):
      player.addScore(1)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        player.controls(event)

main()
