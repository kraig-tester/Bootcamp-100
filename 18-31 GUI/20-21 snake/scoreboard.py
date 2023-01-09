from ctypes import alignment
from turtle import Turtle

ALIGNMENT = "center"
SCREEN_SIZE = 300
FONT_SIZE = 20
FONT = ("Comic Sans MS", FONT_SIZE, "normal")


class Scoreboard(Turtle):

    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0,SCREEN_SIZE-FONT_SIZE*2)
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align=ALIGNMENT, font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()      