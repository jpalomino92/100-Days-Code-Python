import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.cars:
            car.backward(self.speed)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.goto(x=300,y=random.randint(-250,250))
            self.cars.append(car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
