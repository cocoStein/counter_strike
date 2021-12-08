from case import *
from random import *

class Plateau:
    def __init__(self, x , y, list = []):
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

    def bombinator(self):
        for y in range(self.y):
            for x in range(self.x):
                self.list[y][x].checkbomb(self.list)
    
    


zeg = Plateau(10,10)
zeg.matrice()
zeg.crBombe(42)
zeg.bombinator()
print(zeg)

