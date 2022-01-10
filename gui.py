import turtle
from plato import *

WIDTH = 500
HEIGHT = 500

screen = turtle.Screen()
#screen.screensize(WIDTH, HEIGHT, "gray")
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

    def draw_plato_window(self):
        """
        dessine le plateau en fonction de sa taille
        """

        x_space = WIDTH / self.plato.x
        y_space = HEIGHT / self.plato.y
        self.turtle.speed(0)

        for i in range(self.plato.x + 1):
            if i-1 == -1:
                pass
            else:
                self.turtle.pu()
                self.turtle.goto(self.x0 + 1/5 * x_space, self.y0 - y_space)
                self.turtle.pd()
                self.turtle.write(i - 1, font=("arial", int(x_space / 1.5), "normal"))

            self.x0 += x_space
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(self.x0, -HEIGHT / 2 - x_space)


        for i in range(self.plato.y + 1):
            if i-1 == -1:
                pass
            else:
                self.turtle.pu()
                self.turtle.goto(- self.x0 + x_space,  self.y0 - y_space)
                self.turtle.pd()
                self.turtle.write(i - 1, font=("arial", int(x_space / 1.5), "normal"))


            self.y0 -= y_space
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(-WIDTH / 2, self.y0)

        #turtle.done()

def draw_number(platard, x, y):
    """
    Dessine les numéros une fois décovert
    :param platard: plateau
    :param x: int
    :param y: int
    """

    x_space = WIDTH / platard.x
    y_space = HEIGHT / platard.y

    x0 = - WIDTH / 2
    y0 = HEIGHT / 2

    stuck1.penup()
    stuck1.goto(x_space, y_space)
    stuck1.pd()


    stuck1.pu()
    stuck1.goto((x0 + x * x_space + x_space + 1/5 * x_space), (y0 - y * y_space - 2 * y_space))
    stuck1.pd()
    stuck1.write(platard.list[y][x].numero, font=("arial", int(x_space / 1.5), "normal"))

def draw_evidence(platard, x, y):
    """
    Dessine les numéros une fois mis en évidence
    :param platard: plateau
    :param x: int
    :param y: int
    """

    x_space = WIDTH / platard.x
    y_space = HEIGHT / platard.y

    x0 = - WIDTH / 2
    y0 = HEIGHT / 2

    stuck1.penup()
    stuck1.goto(x_space, y_space)
    stuck1.pd()

    stuck1.pu()
    stuck1.goto((x0 + x * x_space + x_space + 1/5 * x_space), (y0 - y * y_space - 2 * y_space))
    stuck1.pd()
    stuck1.write("!", font=("arial", int(x_space / 1.5), "normal"))

