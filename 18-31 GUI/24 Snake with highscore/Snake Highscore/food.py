from turtle import Turtle
import random

SCREEN_SIZE = 300
SCREEN_PADDING = 20
SCOREBOARD_PADDING = 50
POS_RANGE = SCREEN_SIZE - SCREEN_PADDING

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-POS_RANGE, POS_RANGE)
        random_y = random.randint(-POS_RANGE, POS_RANGE-SCOREBOARD_PADDING)
        self.goto(random_x, random_y)