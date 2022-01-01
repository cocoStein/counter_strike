import turtle
from plato import *

WIDTH = 500
HEIGHT = 500

screen = turtle.Screen()
screen.screensize(WIDTH, HEIGHT)

screen.bgcolor("light blue")
screen.title("Démineur")
stuck1 = turtle.Turtle()


class Game_window:
    def __init__(self, screen, turtle, plato):
        self.screen = screen
        self.turtle = turtle
        self.plato = plato
        self.x0 = - WIDTH / 2
        self.y0 = HEIGHT / 2

    def main_window(self):
        x_space = WIDTH / self.plato.x
        y_space = HEIGHT / self.plato.y
        self.turtle.speed(0)

        for i in range(self.plato.x + 1):
            self.x0 += x_space
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(self.x0, -HEIGHT)


        for i in range(self.plato.y + 1):
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(-WIDTH, self.y0)
            self.y0 -= y_space







        turtle.done()


zeg = Plateau(100, 100)
dd = Game_window(screen, stuck1, zeg)
Game_window.main_window(dd)