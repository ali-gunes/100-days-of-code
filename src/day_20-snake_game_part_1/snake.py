from turtle import Turtle, Screen

MOVE_PACE = 20
SNAKE_START_LENGTH = 3

RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270


class Snake:
    def __init__(self, snake_body=None, x_pos=0):
        if snake_body is None:  # Pycharm suggested this
            snake_body = []
        self.snake_body = snake_body
        self.x_pos = x_pos
        self.initialize_snake()  # Called this here because to initialize head, snake_body[] shouldn't be empty
        self.head = self.snake_body[0]
        self.screen = Screen()

    def initialize_snake(self):
        for _ in range(SNAKE_START_LENGTH):
            _ = Turtle("square")
            _.penup()
            _.color("white")
            _.setx(self.x_pos)
            self.snake_body.append(_)
            self.x_pos -= 20

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def controls(self):
        self.screen.listen()
        self.screen.onkey(fun=self.right, key="d")
        self.screen.onkey(fun=self.left, key="a")
        self.screen.onkey(fun=self.down, key="s")
        self.screen.onkey(fun=self.up, key="w")

    def move(self):
        # Check if the snake exceeds the screen borders
        if self.head.xcor() > 270 or self.head.xcor() < -270 or self.head.ycor() > 270 or self.head.ycor() < -270:
            print("Game over! You lose.")
            exit()

        for i in range(len(self.snake_body) - 1, 0, -1):  # Think about this!
            x_cor = self.snake_body[i - 1].xcor()
            y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x_cor, y_cor)

        self.head.forward(MOVE_PACE)

        self.controls()
