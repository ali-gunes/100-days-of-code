# On day 20, we are: Making the Infamous Snake Game
# On day 21, we are: Learning Inheritance, Slicing and Continuing Making the Infamous Snake Game
# In OOP, Classes can inherit from other classes, they can inherit attributes and methods.

# Project 20 - Snake Game Part 1
# Project 21 - Snake Game Part 2
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

ALLOWED_MODS = ["wall", "space"]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ali G - Snake Game")
screen.tracer(0)  # Animations off, need to update for every scene

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scoreboard.write_scoreboard()

# Input the game mode and validate
title = "Game Mode"
while True:
    snake.GAME_MOD = screen.textinput(title, "Please choose a game mode: (Wall / Space)").lower()
    if snake.GAME_MOD not in ALLOWED_MODS:
        print("Invalid input, try again")
        title = "Invalid Input"
    else:
        break

screen.listen()
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.up, key="w")

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_is_on = snake.move()  # Returns False if snake hit to a wall, else True

    # Detect Collision with food using Distance method from Turtle
    if snake.head.distance(food) <= 15:
        food.collision()
        snake.SNAKE_LENGTH += 1
        snake.MOVE_PACE += .2
        scoreboard.SCORE += 1
        scoreboard.write_scoreboard()

    for segment in snake.snake_body[1::]:  # I sliced the snake body list to start from 1 to avoid head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over(reason="You ate yourself")

screen.exitonclick()
