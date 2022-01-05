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
        x_space = WIDTH / self.plato.x
        y_space = HEIGHT / self.plato.y
        self.turtle.speed(0)

        for i in range(self.plato.x + 1):
            self.turtle.pu()
            self.turtle.goto(self.x0 + 1/5 * x_space, self.y0 - y_space)
            self.turtle.pd()
            self.turtle.write(i, font=("arial", int(x_space / 1.5), "normal"))

            self.x0 += x_space
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(self.x0, -HEIGHT / 2 - x_space)


        for i in range(self.plato.y + 1):
            if i == 0:
                pass
            else:
                self.turtle.pu()
                self.turtle.goto( - self.x0 + x_space,  self.y0 - y_space)
                self.turtle.pd()
                self.turtle.write(i, font=("arial", int(x_space / 1.5), "normal"))


            self.y0 -= y_space
            self.turtle.pu()
            self.turtle.goto(self.x0, self.y0)
            self.turtle.pd()
            self.turtle.goto(-WIDTH / 2, self.y0)


    def draw_number(self):



        turtle.done()



zeg = Plateau(10, 10)
dd = Game_window(screen, stuck1, zeg)
Game_window.draw_plato_window(dd)