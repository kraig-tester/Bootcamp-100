from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1
        self.reset_scoreboard()
        
    
    def reset_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-290,260)
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",align=ALIGNMENT,font=(FONT))

    
    def level_passed(self):
        self.level += 1
        self.reset_scoreboard()

    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=(FONT))
