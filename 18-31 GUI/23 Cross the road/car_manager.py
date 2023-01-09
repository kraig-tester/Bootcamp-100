from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:


    def __init__(self):
        self.cars = []
        self.current_move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(320, random.randint(-250, 250))
        self.cars.append(new_car)

    
    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor()-self.current_move_distance, car.ycor())


    def check_collusion(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False        


    def level_up(self):
        self.current_move_distance += MOVE_INCREMENT
