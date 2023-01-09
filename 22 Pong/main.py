from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# screen.onkey(quit, "esc")

running = True
while running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -283:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.xcor() < 340 and ball.distance(r_paddle) < 70 or ball.xcor() < -320 and ball.xcor() > -340 and ball.distance(l_paddle) < 70:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.restart()
        scoreboard.score_left()
         
    if ball.xcor() < -370:
        ball.restart() 
        scoreboard.score_right()

screen.exitonclick()