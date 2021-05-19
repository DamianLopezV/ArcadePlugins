import pygame
import random
#TODO: UI
#colors
colors = dict()
colors["white"] = (255,255,255)
colors["red"] = (255, 42, 55)
colors["blue"] = (0, 135, 255)
colors["gray"] = (204, 204, 204)
#screen size
size = 120


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
        if(self.rect.collidepoint(pygame.mouse.get_pos()) and turn and self.value!=2):
            self.color = colors["red"]
            self.value = 1
        if(self.rect.collidepoint(pygame.mouse.get_pos()) and not turn and self.value!=1):
            self.color = colors["blue"]
            self.value = 2

class Map:
    def __init__(self):
        self.map = [[""]*3 for i in range(0,3)]
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
    
    def checkWin(self):

        for i in range(0,self.mapColums):
            contBlue = 0
            contRed = 0
            for j in range(0,self.mapRows):
                if(self.map[i][j].value == 1):
                    contRed +=1
                if(self.map[i][j].value == 2):
                    contBlue +=1
                if(contRed>=3):
                    print("rojo gana")
                if(contBlue>=3):
                    print("axul gana")

        for i in range(0,self.mapColums):
            contBlue = 0
            contRed = 0
            for j in range(0,self.mapRows):
                if(self.map[j][i].value == 1):
                    contRed +=1
                if(self.map[j][i].value == 2):
                    contBlue +=1
                if(contRed>=3):
                    print("rojo gana")
                if(contBlue>=3):
                    print("axul gana")
        
        contBlue = 0    
        contRed = 0
        for i in range(0,self.mapColums):
            if(self.map[i][i].value == 1):
                contRed +=1
            if(self.map[i][i].value == 2):
                contBlue +=1
            if(contRed>=3):
                print("rojo gana")
            if(contBlue>=3):
                print("axul gana")
                
        contBlue = 0    
        contRed = 0
        for i in range(0,self.mapColums):
            j = self.mapColums-i-1
            if(self.map[j][i].value == 1):
                contRed +=1
            if(self.map[j][i].value == 2):
                contBlue +=1
            if(contRed>=3):
                print("rojo gana")
            if(contBlue>=3):
                print("axul gana")
        contTie = 0
        for i in range(0,self.mapColums):
            for j in range(0,self.mapRows):
                if(self.map[i][j].value != 0):
                    contTie +=1
                if(contTie>=9):
                    print("empate")

    def createWindow(self):
        (width, height) = (size*self.mapColums+1, size*self.mapRows+1)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('gato')
        pygame.display.flip()
        return screen

def main():
    pygame.init()
    map = Map()
    screen = map.createWindow()
    map.createMap(screen)
    running = True
    turn = True if random.randint(0,1) else False
    while running:
        pygame.display.update()
        map.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                map.playTurn(turn)
                if(turn):
                    turn = False
                else:
                    turn = True
        map.checkWin()

main()