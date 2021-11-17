from case import *


class Plateau:
    def __init__(self, list = []):
        self.list = list

    def matrice(self, x, y):
        for i in range(y):
            k = []
            for n in range(x):
                k.append(Case(n,i))
            self.list.append(k)
            

if __name__== "main":
    zeg = Plateau()
    zeg.matrice(8,3)
    print(zeg.list[2][2].y)