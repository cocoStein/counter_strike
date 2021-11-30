from case import *
from random import *

class Plateau:
    def __init__(self, x , y, list = [],):
        self.list = list
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.list)
    def matrice(self):
        for i in range(self.y):
            k = []
            for n in range(self.x):
                
                k.append(Case(n,i))
            self.list.append(k)
    
    def crBombe(self, difficulty=3):
        for i in range(difficulty):
            x = randrange(self.x)
            y = randrange(self.y)
            self.list[y][x].valeur = True
    
    def showTerminal(self):
        for i in range(self.y):
            for l in range(self.x):
                print(self.list[self.y][self.x].valeur,"  |   ")


zeg = Plateau(4,4)
zeg.matrice()
zeg.crBombe(7)
print(zeg)
#zeg.showTerminal()