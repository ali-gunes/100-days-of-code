# On day 20, we are: Making the Infamous Snake Game
import time
# Project 20 - Snake Game Part 1
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ali G - Snake Game")
screen.tracer(0)  # Animations off, need to update for every scene

snake = Snake()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
