from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level(speed=10)

    def update_level(self, speed):
        self.clear()
        self.goto(-450, 250)
        self.write(f"Level: {self.level}", move=False, align="left", font=("Arial", 16, "bold"))
        self.goto(-450, 235)
        self.write(f"Current Speed: {speed * 5} km/s", move=False, align="left", font=("Arial", 10, "bold"))

    def game_over(self, level):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(0, -30)
        self.write(f"You've reached level {level}", move=False, align="center", font=("Arial", 14, "bold"))
        return False