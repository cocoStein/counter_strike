from case import *


class Plateau:
    def __init__(self, list = []):
        self.list = list

    def matrice(self, x, y):
        for i in range(y):
            k = []
            for n in range(x):
                k.append(case(n,i))
            list.append(k)
            k.clear()


zeg = Plateau()
zeg.matrice(8,3)
print(zeg.list)