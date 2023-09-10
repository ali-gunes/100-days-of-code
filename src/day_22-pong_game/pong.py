from turtle import Turtle

MOVE_PACE = 20


class Pong(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()

        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.goto(x_cor, y_cor)

    def up(self):
        if self.ycor() < 280:
            self.forward(MOVE_PACE)

    def down(self):
        if self.ycor() > -280:
            self.backward(MOVE_PACE)
