from turtle import Turtle, Screen
from random import randint

colors = ["red", "blue", "yellow", "green", "purple", "coral", "orange", "magenta", "cyan", "lime"]
MAX_TURTLES = 10
num_of_turtles = 5
turtles = []

screen = Screen()
screen.setup(width=500, height=400)
height = screen.canvheight
width = screen.canvwidth
side_padding = 20
top_padding = 20
turtle_range = (height-top_padding*2) / (num_of_turtles-1)

def set_turtle_start(turtle_start_x, turtle_start_y):

    for turtle_num in range(num_of_turtles):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[turtle_num])
        new_turtle.penup()
        new_turtle.goto(x=turtle_start_x,y=turtle_start_y-turtle_range*(turtle_num))
        new_turtle.pendown()
        turtles.append(new_turtle)

def start_race():
    finish_x = width/2 - side_padding
    turtle_finished = False
    while not turtle_finished:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > finish_x:
                turtle_finished = True
                return turtle.pencolor()


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

set_turtle_start(-width/2+side_padding, height/2-top_padding)

winning_turtle_color = start_race()
print(winning_turtle_color)
if winning_turtle_color == user_bet.lower():
    print(f"You won! {winning_turtle_color.capitalize()} turtle has won!")
else:
    print(f"You lost! {winning_turtle_color.capitalize()} turtle has won!")

screen.exitonclick()