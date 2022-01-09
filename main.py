from plato import *
from case import *
from gui import *

plato = Plateau(10,10)
plato.matrice()
plato.crBombe(20)
plato.bombinator()
plato.showTerminal()
k = Case(1000,1000,valeur=False)

dd = Game_window(screen, stuck1, plato)
Game_window.draw_plato_window(dd)

while k.valeur == False:
    print("Il reste ", plato.checkwin(), " case(s) à trouver.")
    x = int(input("Nombre en x : "))
    y = int(input("Nombre en y : "))
    question = input("Voulez-vous découvrire cette case (d), ou la mettre eb évidence (e)")
    if question == "d":
        plato.discovered(x, y)
        k = plato.list[y][x]
        plato.showTerminal()

    elif question == "e":
        plato.evidence(x , y)
        plato.showTerminal()
print("BOUUM !!", x, ",", y, "est une bombe, vous avez perdu...")