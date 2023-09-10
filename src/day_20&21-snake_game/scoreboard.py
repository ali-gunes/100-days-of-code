# Everything related to scoreboard functionality is refactored into this class
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.SCORE}", move=False, align="center", font=("Arial", 12, "bold"))

    def game_over(self, reason):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 16, "bold"))
        self.goto(0, -20)
        self.write(reason, move=False, align="center", font=("Arial", 10, "bold"))
