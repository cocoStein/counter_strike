from plato import *
from case import *
from gui import *

plato = Plateau(int(input("Largeur du plateau: ")),int(input("Hauteur du plateau: ")))
plato.matrice()
plato.crBombe(int((plato.x * plato.y)*25/100))
plato.bombinator()
plato.showTerminal()
k = Case(1000,1000,valeur=False)

dd = Game_window(screen, stuck1, plato)
Game_window.draw_plato_window(dd)

while k.valeur == False and plato.checkwin() != 0:
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
if plato.checkwin() == 0:
    print("BRAVO!!!!! Vous êtes le meilleur démineur!")
else:
    print("BOUUM !!", x, ",", y, "est une bombe, vous avez perdu...")