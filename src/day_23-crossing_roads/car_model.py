from turtle import Turtle, colormode
import random

colormode(255)

ALLOWED_LANES = [180, 140, 100, 60, 20, -20, -60, -100, -140, -180]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random_color())
        self.spawn_random()

    def spawn_random(self):
        x_cor = -520
        y_cor = random.choice(ALLOWED_LANES)

        self.goto(x_cor, y_cor)

    def move(self, car_pace=10):
        if self.xcor() < 520:
            self.forward(car_pace)
