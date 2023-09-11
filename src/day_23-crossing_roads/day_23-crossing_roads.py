# On day 23, we are: Building our second capstone project: Crossing Roads Game

# Project 23 - Crossing Roads Game

# ---------------------------------------------------------------------------------
# TODO-1: Create a screen
# TODO-2: Create the player turtle and allow it to move with space bar
# TODO-3: Create the randomly generated cars moving from left edge to write edge
# TODO-4: Create road lines in between cars
# TODO-5: Detect collision with turtle and cars
# TODO-6: Create a scoreboard and keep score
# TODO-7: Create levels, each level increase the car speed
# TODO-8: Allow infinite levels
# ---------------------------------------------------------------------------------
# Mistakes to learn: I tried to create and delete cars in the same class, tried to manage
# game loop in the car_model class, this was a mistake, it should've been in the main game loop

from turtle import Screen
import time
from draw_lanes import Lanes
from player import Player
from scoreboard import Scoreboard
from car_model import Car

screen = Screen()
screen.title("Ali G - Crossing Road")
screen.tracer(0)
screen.setup(1000, 600)

lanes = Lanes()
lanes.draw_lanes()

scoreboard = Scoreboard()

player = Player()

car = Car()

screen.listen()
screen.onkeypress(fun=player.move, key="space")

screen.update()
car_wave = []
game_loop = 1
TIME_SPEED = 0.1
game_on = True
while game_on:
    time.sleep(TIME_SPEED)
    screen.update()

    # Game Over condition
    for car in car_wave:
        if player.distance(car) < 3:
            game_on = scoreboard.game_over(scoreboard.level)

    # Create another car object every third game loop and add it to car wave list
    if game_loop == 3:
        car = Car()
        car_wave.append(car)
        game_loop = 0
    else:
        game_loop += 1

    # Move the car
    for car in car_wave:
        car.move(10 + (scoreboard.level * 1.5))
        if car.xcor() >= 510:
            car.hideturtle()
            car_wave.pop(car_wave.index(car))

    # If player reaches finish line
    if player.ycor() > 230:
        player.goto(0, -250)

        # Increase the level
        scoreboard.level += 1
        scoreboard.update_level(10 + (scoreboard.level * 3))

        # Increase the refresh rate
        TIME_SPEED /= 1.15

screen.exitonclick()
