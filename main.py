from turtle import Screen
from car_manager import CarManager
from score_board import ScoreBoard
from player import Player
import time

player = Player()
score_board = ScoreBoard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.move_cars()

    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

    if int(time.time()) % 4 == 0:
        car_manager.create_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.goto(0, 0)
            score_board.write("Game Over", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()