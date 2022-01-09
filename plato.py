from case import *
from random import *
from gui import *


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
        # crée une matrice pour le plateau
        for i in range(self.y):
            k = []
            for n in range(self.x):
                
                k.append(Case(n,i))
            self.list.append(k)
    
    def crBombe(self, difficulty=3):
        # crée les bombes dans la matrice
        for i in range(difficulty):
            x = randrange(self.x) 
            y = randrange(self.y)
            self.list[y][x].valeur = True

    def bombinator(self):
        for y in range(self.y):
            for x in range(self.x):
                self.list[y][x].checkbomb(self.list)

    def showTerminal(self):
        # Affiche dans le terminal les différents éléments
        terminal = "/   "
        for i in range(self.x):
            terminal += str(i) + "   "
        terminal += "\n"
        for line in self.list:
            terminal += str(self.list.index(line)) + "|| "
            for case in line:

               if case.open == False and case.evidence == False:
                    terminal += "■" + " | "
               elif case.evidence == True and case.open == False:
                   terminal += "!" + " | "
               else:
                    terminal += "" + str(case) + " | "
            
            
            terminal +="\n"       
        print(terminal)

    def discovered(self, x , y):
        # affiche dans le terminal une fois découverte
        self.list[y][x].open = True

        draw_number(self, x, y)

        if self.list[y][x].numero == "X":
            print("BOUUM !!", x, ",", y, "est une bombe, vous avez perdu...")
            

        if self.list[y][x].numero == 0:
            vs = self.list[y][x].voisins(self.list)
            for case in vs:
                if self.list[case[1]][case[0]].valeur == False and self.list[case[1]][case[0]].open == False :
                    self.discovered(case[0],case[1])

    def evidence(self, x, y):
        self.list[y][x].evidence = True
        draw_evidence(self, x, y)


    def checkwin(self):
        # regarde si toute les bombes ont été découverte
        n = 0  # nombre de case restant

        for line in self.list:
            for case in line:
                if case.valeur == False and case.open == False:
                    n += 1
        return n


if __name__ == "__main__":
    print("璽■○□")
    zeg = Plateau(10,10)
    zeg.matrice()
    zeg.crBombe(20)
    zeg.bombinator()
    print(zeg)
    zeg.showTerminal()
    for i in range(100):
        x = int(input("Nombre en x : "))
        y = int(input("Nombre en y : "))
        zeg.discovered(x, y)
        zeg.showTerminal()

