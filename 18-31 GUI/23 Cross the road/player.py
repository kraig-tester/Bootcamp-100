from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    

    def __init__(self):
        super().__init__()
        self.to_start()


    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    
    def to_start(self):
        self.penup() 
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.goto(STARTING_POSITION)

