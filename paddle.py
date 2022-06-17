from turtle import Turtle
UP = 20
DOWN = 20


class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=5)
        self.goto(x_cor,y_cor)
        self.color("white")

    def up(self):
        self.fd(20)

    def down(self):
        self.back(20)



2