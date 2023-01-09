from turtle import Turtle, colormode, pendown
import random

#Getting main colors of image
#import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

colors = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
    (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

painting = Turtle()
painting.penup()
painting.speed("fastest")
painting.pensize(10)
colormode(255)

screen = painting.screen
screen.setup(1000, 1000)

width = screen.window_height()
print(f"Screen width: {width}")
height = screen.window_width()
print(f"Screen height: {height}")

num_of_steps = 10
print(f"Number of steps: {num_of_steps}")
padding = 50
print(f"Padding: {padding}")

starting_point_x = -width/2 + padding
starting_point_y = -height/2 + padding

print(f"Starting point: x[{starting_point_x}], y[{starting_point_y}]")

step_x = (width - padding*2)/(num_of_steps)
step_y = (height - padding*2)/(num_of_steps-1)

print(f"Steps: x[{step_x}], y[{step_y}]")

for step in range(num_of_steps):
    painting.setx(starting_point_x)
    painting.sety(starting_point_y + step*step_y)
    painting.dot()
    for _ in range(num_of_steps):
        painting.pencolor(random.choice(colors))
        painting.forward(step_x)
        painting.dot()

screen.exitonclick()
