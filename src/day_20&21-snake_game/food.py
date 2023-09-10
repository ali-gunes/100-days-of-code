# Everything related to food functionality is refactored into this class

from turtle import Turtle
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Food(Turtle):  # We inherited because we want to use every function of Turtle class
    def __init__(self):
        super().__init__()  # Inherit from the Turtle class
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.collision()  # Initialize with a position

    @staticmethod  # Pycharm convinced me to change this method to static bc I didn't use anything with self()
    def spawn_random():
        x_pos = randint(0, (SCREEN_WIDTH // 2) - 30)
        y_pos = randint(0, (SCREEN_HEIGHT // 2) - 30)
        return x_pos, y_pos

    def collision(self):
        self.location = self.spawn_random()
        self.goto(self.location)
