from case import *
from random import *

class Plateau:
    def __init__(self, x , y, list = [],):
        self.list = list
        self.x = x
        self.y = y
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


zeg = Plateau(4,4)
zeg.matrice()
zeg.crBombe(7)
for i in range(zeg.y):
    for n in range(zeg.x):
        print(zeg.list[i][n].valeur)