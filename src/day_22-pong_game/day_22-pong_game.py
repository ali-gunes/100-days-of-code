# On day 22, we are: Making the Pong Game

# Project 22 - Pong Game

import time
from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard

TIME_SPEED = 0.1

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ali G - Pong")
screen.tracer(0)

# Initializing players and setting the starting position
player_one = Pong(-380, 0)
player_two = Pong(380, 0)

# Initializing scoreboard and center line
scoreboard = Scoreboard()
center_line = Scoreboard()
center_line.draw_center_line()
scoreboard.WINNER_SCORE = screen.numinput("Winner Score", "Please determine a winner score: [1, 100]", minval=1,
                                          maxval=100, default=10)
scoreboard.write_score()

# Initializing ball
ball = Ball()

screen.update()

screen.listen()
# Player One key presses
screen.onkeypress(fun=player_one.up, key="w")
screen.onkeypress(fun=player_one.down, key="s")

# Player Two key presses
screen.onkeypress(fun=player_two.up, key="Up")
screen.onkeypress(fun=player_two.down, key="Down")

game_on = True
while game_on:
    time.sleep(TIME_SPEED)
    screen.update()
    game_on = scoreboard.write_score()
    ball.move()

    # Detect collision with y-axis
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(player_two) < 50) or (ball.xcor() < -320 and ball.distance(player_one) < 50):
        ball.change_direction()
        TIME_SPEED /= 1.15

    # Check collision with x-axis
    if ball.xcor() >= 400:
        scoreboard.PLAYER_ONE_SCORE += 1
        ball.x_move *= -1
        ball.goto(0, 0)
        time.sleep(0.5)
        TIME_SPEED = 0.1

    elif ball.xcor() <= -400:
        scoreboard.PLAYER_TWO_SCORE += 1
        ball.x_move *= -1
        ball.goto(0, 0)
        time.sleep(0.5)
        TIME_SPEED = 0.1



center_line.clear()

screen.exitonclick()
