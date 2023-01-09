from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

WALL_PADDING = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def restart():
        scoreboard.restart_game()
        snake.restart_snake()


running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > WALL_PADDING or snake.head.xcor() < -WALL_PADDING or snake.head.ycor() > WALL_PADDING or snake.head.ycor() < -WALL_PADDING:
        restart()

    # Tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            restart()

screen.exitonclick()