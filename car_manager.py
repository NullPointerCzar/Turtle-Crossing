from turtle import Turtle
import random
import time
car_colors = ["red", "blue", "green", "white"]
class CarManager(Turtle):
    movedistance = 10
    cars = []
    
    def __init__(self):
        self.create_cars()

    def create_cars(self):
        car = Turtle("square")
        car.color(random.choice(car_colors))
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)
            
    def move_cars(self):
        for car in self.cars:
            car.forward(self.movedistance)
            
    def level_up(self):
        self.movedistance+=3