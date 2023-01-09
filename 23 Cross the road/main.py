import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if player.ycor() > FINISH_LINE_Y:
        car_manager.level_up()
        scoreboard.level_passed()
        player.to_start()

    if car_manager.check_collusion(player):
        game_is_on = False
        scoreboard.game_over()
        break

    if randint(1,6) == 1:
        car_manager.add_car()

    car_manager.move_cars()

screen.exitonclick()
