from turtle import Turtle

SCREEN_HEIGHT = 600
CENTER_LINE = 30


class Scoreboard(Turtle):
    PLAYER_ONE_SCORE = 0
    PLAYER_TWO_SCORE = 0
    WINNER_SCORE = 10

    def __init__(self):
        super().__init__()

        self.color("white")
        self.pensize(5)
        self.penup()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.goto(-60, 250)
        self.write(self.PLAYER_ONE_SCORE, move=False, align="center", font=("Arial", 28, "bold"))
        self.goto(60, 250)
        self.write(self.PLAYER_TWO_SCORE, move=False, align="center", font=("Arial", 28, "bold"))

        # Check if one of the players reach to score 10
        if self.PLAYER_ONE_SCORE == self.WINNER_SCORE:
            self.game_over("Left Player")
            return False
        elif self.PLAYER_TWO_SCORE == self.WINNER_SCORE:
            self.game_over("Right Player")
            return False

        return True

    def draw_center_line(self):
        self.goto(0, 300)
        self.setheading(270)
        for i in range(600 // (2 * CENTER_LINE)):
            self.pendown()
            self.forward(CENTER_LINE)
            self.penup()
            self.forward(CENTER_LINE)

    def game_over(self, winner):
        self.goto(0, 10)
        self.write("Game Over", move=False, align="center", font=("Arial", 28, "bold"))
        self.goto(0, -30)
        self.write(f"{winner} won!", move=False, align="center", font=("Arial", 12, "bold"))
