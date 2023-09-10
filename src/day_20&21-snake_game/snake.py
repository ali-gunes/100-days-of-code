# Everything related to Snake functionality is refactored into this class

from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()


class Snake:
    MOVE_PACE = 10
    SNAKE_LENGTH = 3
    GAME_MOD = None
    RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

    def __init__(self, snake_body=None, x_pos=0):
        if snake_body is None:  # Pycharm suggested this
            snake_body = []
        self.snake_body = snake_body
        self.x_pos = x_pos
        self.initialize_snake()  # Called this here because to initialize head, snake_body[] shouldn't be empty
        self.head = self.snake_body[0]

    def initialize_snake(self):
        if len(self.snake_body) <= self.SNAKE_LENGTH:
            for _ in range(self.SNAKE_LENGTH - len(self.snake_body)):
                _ = Turtle("square")
                _.penup()
                _.color("white")
                _.setx(self.x_pos)
                self.snake_body.append(_)
                self.x_pos -= 20

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(270)

    def move(self):
        self.initialize_snake()

        # Check if the snake exceeds the screen borders and do stuff according to game mode
        if self.GAME_MOD == "wall":
            if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
                print("Game over! You lose.")
                scoreboard.game_over(reason="You hit a wall")
                return False
                # exit()
        else:
            if self.head.xcor() > 280:
                self.head.goto(-280, self.head.ycor())
            elif self.head.xcor() < -280:
                self.head.goto(280, self.head.ycor())
            elif self.head.ycor() > 280:
                self.head.goto(self.head.xcor(), -280)
            elif self.head.ycor() < -280:
                self.head.goto(self.head.xcor(), 280)

        # Move the snake's body with snake's head
        for i in range(len(self.snake_body) - 1, 0, -1):  # Think about this!
            x_cor = self.snake_body[i - 1].xcor()
            y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x_cor, y_cor)

        self.head.forward(self.MOVE_PACE)
        return True
