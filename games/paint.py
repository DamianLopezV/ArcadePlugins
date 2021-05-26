import pygame
import random

colors = dict()
colors["white"] = (255,255,255)
colors["red"] = (255, 42, 55)
colors["blue"] = (0, 135, 255)
colors["gray"] = (204, 204, 204)
colors["black"] = (0, 0, 0)
colors["yellow"] = (255, 233, 0)
colors["purple"] = (163, 73, 164)
colors["green"] = (66, 255, 51)

size = 10

class Rect:
    def __init__(self,screen,i,j):
        self.screen = screen
        self.rect = pygame.Rect(j*size, i*size, size, size)
        self.color = colors["white"]
        self.value = 0
    
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,colors["white"],self.rect,2)
    
    def colision(self,turn,brush):
        if turn:
            if(self.rect.collidepoint(pygame.mouse.get_pos())):
                self.color = brush.color

class Map:
    def __init__(self):
        self.map = [[""]*100 for i in range(100)]
        self.mapColums = len(self.map)
        self.mapRows = len(self.map[0])

    def createMap(self,screen):
        for i in range(0,self.mapColums):
            for j in range(0,self.mapRows):
                self.map[i][j] = Rect(screen,i,j)

    def draw(self):
        for i in range(0,self.mapColums):
            for j in range(0,self.mapRows):
                self.map[i][j].draw()
    
    def playTurn(self,turn,brush):
        for i in range(0,self.mapColums):
            for j in range(0,self.mapRows):
                self.map[i][j].colision(turn,brush)

    def createWindow(self):
            (width, height) = (size*self.mapColums+1, size*self.mapRows+1)
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption('paint')
            pygame.display.flip()
            return screen

class Brush:
    def __init__(self):
        self.color = colors["blue"]
        
    def controls(self,event):
        if event.key == pygame.K_1:
            self.color = colors["blue"]
        if event.key == pygame.K_2:
            self.color = colors["red"]
        if event.key == pygame.K_3:
            self.color = colors["yellow"]
        if event.key == pygame.K_4:
            self.color = colors["purple"]
        if event.key == pygame.K_5:
            self.color = colors["green"]
        if event.key == pygame.K_6:
            self.color = colors["white"]
        if event.key == pygame.K_7:
            self.color = colors["black"]
        if event.key == pygame.K_8:
            self.color = colors["gray"]
        


def main():
    pygame.init()
    map = Map()
    screen = map.createWindow()
    map.createMap(screen)
    brush = Brush()
    running = True
    paint = False
    while running:
        pygame.display.update()
        map.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                paint = True
            if event.type == pygame.MOUSEBUTTONUP:
                paint = False
            if event.type == pygame.KEYDOWN:
                brush.controls(event)
            
            map.playTurn(paint,brush)

main()