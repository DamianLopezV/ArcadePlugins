import pygame
import random

colors = dict()
colors["white"] = (255,255,255)
colors["red"] = (255, 42, 55)
colors["blue"] = (0, 135, 255)
colors["gray"] = (204, 204, 204)

size = 5

class Rect:
    def __init__(self,screen,i,j):
        self.screen = screen
        self.rect = pygame.Rect(j*size, i*size, size, size)
        self.color = colors["white"]
        self.value = 0
    
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,colors["gray"],self.rect,2)
    
    def colision(self,turn):
        if turn:
            if(self.rect.collidepoint(pygame.mouse.get_pos())):
                self.color = colors["red"]

class Map:
    def __init__(self):
        self.map = [[""]*100 for i in range(0,100)]
        for i in range(len(map)):
            self.map.append
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
    
    def playTurn(self,turn):
        for i in range(0,self.mapColums):
            for j in range(0,self.mapRows):
                self.map[i][j].colision(turn)

    def createWindow(self):
            (width, height) = (size*self.mapColums+1, size*self.mapRows+1)
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption('paint')
            pygame.display.flip()
            return screen

class Brush:
    def __init__(self):
        self.color = colors["white"]

class paintura:
    def __init__(self, screen, i, j, color):
        self.screen = screen
        self.rect = pygame.Rect(j*size, i*size, size, size)
        self.color = color


    def colision(self,turn):
        if(self.rect.collidepoint(pygame.mouse.get_pos())):
            return self.color
        

def main():
    pygame.init()
    map = Map()
    screen = map.createWindow()
    map.createMap(screen)
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
            map.playTurn(paint)

main()