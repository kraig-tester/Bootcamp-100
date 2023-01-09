from turtle import Turtle, colormode
import random
# import turtle as t
# from turtle import *

tim = Turtle()
colors = ["cyan", "sienna", "salmon", "dark magenta", "plum"]
angles = [0, 90, 180, 270]
colormode(255)
# tim.shape("turtle")
# tim.color("red")

# # Draw square
# for num in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Draw dotted line
# for num in range(50):
#     tim.forward(5)
#     if tim.pen()["pendown"]:
#         tim.penup()
#     else:
#         tim.pendown()

# # Draw 3-angle to 10-angle
# for num in range(3,11):
#     angle = 360/num
#     tim.color(choice(colors))
#     for _ in range(num):
#         tim.forward(100)
#         tim.right(angle)

# # draw random lines
# tim.pensize(15)
# tim.speed("fast")
# for _ in range(200):
#     tim.setheading(random.choice(angles))
#     tim.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     tim.forward(30)  

# Draw a spirograph
tim.speed("fastest")
num_of_circles = random.randint(10, 100)
angle = 360 / num_of_circles
for _ in range(num_of_circles):
    tim.circle(100)
    tim.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    tim.setheading(tim.heading() + angle)


screen = tim.screen
screen.exitonclick()