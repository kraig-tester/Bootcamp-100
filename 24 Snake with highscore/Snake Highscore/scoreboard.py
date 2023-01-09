from ctypes import alignment
from turtle import Turtle

ALIGNMENT = "center"
SCREEN_SIZE = 300
FONT_SIZE = 20
FONT = ("Comic Sans MS", FONT_SIZE, "normal")


class Scoreboard(Turtle):

    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0,SCREEN_SIZE-FONT_SIZE*2)
        self.update_scoreboard()

    
    def restart_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER",align=ALIGNMENT, font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} ---- High score: {self.high_score}",align=ALIGNMENT, font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()      