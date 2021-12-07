from case import *
from random import *

class Plateau:
    def __init__(self, x , y, list = [],):
        self.list = list
        self.x = x
        self.y = y

    def __str__(self):
        affiche = ""
        for line in self.list:
            for case in line:
                affiche+=str(case) + " | "
            affiche+="\n"
        return affiche

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
    
    


zeg = Plateau(9,9)
zeg.matrice()
zeg.crBombe(16)
print(zeg)
#zeg.showTerminal()