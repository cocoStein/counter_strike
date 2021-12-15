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
            affiche+="\n" + ""
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

    def showTerminal(self):
        terminal = ""
        for line in self.list:
            for case in line:
                if case.open == False:
                    terminal += "■" + " "
                      
                else:
                    terminal += "" + str(case) + " "
            terminal +="\n"       
        print(terminal)

    def discovered(self,x ,y):
        self.list[y][x].open = True

        if self.list[y][x].numero == 0:
            if self.x == 0:
                    pass
            else:
                  
                try:    # Check millieu gauche
                    if self.list[self.y][self.x - 1].valeur == True:
                        self.discovered(self.x, self.y)
                except IndexError:
                    pass

                try:    # Check bas gauche
                    if self.list[self.y + 1][self.x - 1].valeur == True:
                        self.discovered(self.x, self.y)
                except IndexError:
                    pass
            
            if self.y == 0:
                pass
            else:
                try:    # Check haut millieu
                    if self.list[self.y - 1][self.x].valeur == True:
                        self.discovered(self.x, self.y)
                except IndexError:
                    pass
                try:   # Check haut gauche
                    if self.list[self.y - 1][self.x + 1].valeur == True:
                        self.discovered(self.x, self.y)
                except IndexError:
                    pass
            
            if self.y == 0 or self.x == 0:
                pass
            else:
                try:    # Check haut gauche
                    if self.list[self.y - 1][self.x - 1].valeur == True:
                        self.discovered(self.x, self.y)
                except IndexError:
                    pass

            try:    # Check millieu droite
                if self.list[self.y][self.x + 1].valeur == True:
                    self.discovered(self.x, self.y)
            except IndexError:
                pass

            

            try:    # Check bas millieu
                if self.list[self.y + 1][self.x].valeur == True:
                    self.discovered(self.x, self.y)
            except IndexError:
                pass

            try:    # Check bas droite
                if self.list[self.y + 1][self.x + 1].valeur == True:
                    self.sdiscovered(self.x, self.y)
            except IndexError:
                pass
        else:
            self.discovered(self.x, self.y)

        
        
if __name__==  "__main__":
    print("璽■○□")
    zeg = Plateau(10,10)
    zeg.matrice()
    zeg.crBombe(42)
    zeg.bombinator()
    print(zeg)
    zeg.showTerminal()
    for i in range(100):
        x = int(input("Nombre en x : "))
        y = int(input("Nombre en y : "))
        zeg.discovered(x, y)
        zeg.showTerminal()
