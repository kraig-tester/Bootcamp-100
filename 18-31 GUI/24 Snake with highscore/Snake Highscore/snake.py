from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(3):
            self.add_segment((i*-MOVE_DISTANCE, 0))    


    def move(self):
        for part in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[part-1].xcor()
            new_y = self.segments[part-1].ycor()
            self.segments[part].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)


    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        new_segment.showturtle()


    def restart_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)