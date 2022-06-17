from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",23)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.l_score = 0
        self.r_score = 0
        self.points()

    def points(self):
        self.clear()
        self.write(f"P1:{self.l_score}        P2:{self.r_score}", align=ALIGN, font=FONT)


