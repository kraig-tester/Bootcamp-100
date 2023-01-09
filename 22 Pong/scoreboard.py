from re import L
from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 80
FONT = ("courier", FONT_SIZE, "normal")
class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    
    def print_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    
    def score_left(self):
        self.l_score += 1
        self.print_score()


    def score_right(self):
        self.r_score += 1
        self.print_score()
